



import urllib3
import json
import csv

def main():
    # Source for the file reading and parsing; down to #print(sensorids)
    # http://stackoverflow.com/questions/7605374/parsing-a-tab-delimited-file-into-separate-lists-or-strings

    sensorids=[]
    inrixsegids=[]
    latitudes=[]
    longitudes=[]
    routenames=[]
    directions=[]
    
    fInputFilePath = "C:\\Users\\jimw\\Documents\\Projects\\ArchiveXDCustomOHODOT\\ODOT_changeList.txt"
    fSensorMPFile = "OhioDeviceSpeedInfo_Test.txt"
    fSensorSegFile = "DeviceInrixSegTable_Test.txt"
    
    with open(fInputFilePath,'r') as s:
        
        reader=csv.reader(s,delimiter='\t')
        
        # Capture header values and prepare output file.
        head = [next(reader) for x in range(1)]
        for sensorid,inrixsegid,latitude,longitude,routename,direction in head:
            sensoridheader = sensorid
            inrixsegidheader = inrixsegid
            latitudeheader = latitude
            longitudeheader = longitude
            routenameheader = routename
            
            fSensorMP = open(fSensorMPFile,"w+")
            fSensorSeg = open(fSensorSegFile,"w+")
            
            # OhioDeviceSpeedInfo.xml file
            fSensorMP.write("ID")
            fSensorMP.write("\t")
            fSensorMP.write("RoadName")
            fSensorMP.write("\t")
            fSensorMP.write("RoadDir")
            fSensorMP.write("\t")
            fSensorMP.write(str(latitudeheader))
            fSensorMP.write("\t")
            fSensorMP.write(str(longitudeheader))
            fSensorMP.write("\t")
            fSensorMP.write("MilePost")
            fSensorMP.write("\r")
            
            # DeviceInrixSegTable.txt file
            fSensorSeg.write(str(sensoridheader))
            fSensorSeg.write("\t")
            fSensorSeg.write(str(inrixsegidheader))
            fSensorSeg.write("\t")
            fSensorSeg.write(str(latitudeheader))
            fSensorSeg.write("\t")
            fSensorSeg.write(str(longitudeheader))
            fSensorSeg.write("\t")
            fSensorSeg.write(str(routenameheader))
            fSensorSeg.write("\r")   

        # Capture data values, send Latitude and Longitude to the API, capture MilePost data from the API for each coordinate set, and build dataset
        for sensorid,inrixsegid,latitude,longitude,routename,direction in reader:
            sensorids.append(sensorid)
            inrixsegids.append(inrixsegid)
            latitudes.append(latitude)
            longitudes.append(longitude)
            routenames.append(routename)
            directions.append(direction)
            
            urlDataLoop = "http://odotloc.dot.state.oh.us/?lat=" + str(latitude) + "&lon=" + str(longitude)
            http = urllib3.PoolManager()
    
            rLoop = http.request('GET', urlDataLoop)
            # Use the JSON module (the loads method) to load the string data into a dictionary
            theJSONLoop = json.loads(rLoop.data.decode('utf-8'))
            # Now we can access the contents of the JSON like any other Python object
            if "LogpointStateNbr":
                # This right here, creates a good bit of the desired output.
                fSensorMP = open(fSensorMPFile,"a+")
                fSensorSeg = open(fSensorSegFile,"a+")
                
                # Update the OhioDeviceSpeedInfo.xml file
                fSensorMP.write(str(sensorid))
                fSensorMP.write("\t")
                fSensorMP.write(str(routename))
                fSensorMP.write("\t")
                fSensorMP.write(str(direction))
                fSensorMP.write("\t")
                fSensorMP.write(str(latitude))
                fSensorMP.write("\t")
                fSensorMP.write(str(longitude))
                fSensorMP.write("\t")
                fSensorMP.write(str(theJSONLoop["LogpointStateNbr"]))
                fSensorMP.write("\r")
                
                # Update the DeviceInrixSegTable.txt file
                fSensorSeg.write(str(sensorid))
                fSensorSeg.write("\t")
                fSensorSeg.write(str(inrixsegid))
                fSensorSeg.write("\t")
                fSensorSeg.write(str(latitude))
                fSensorSeg.write("\t")
                fSensorSeg.write(str(longitude))
                fSensorSeg.write("\t")
                fSensorSeg.write(str(routename))
                fSensorSeg.write("\r")
            
            fSensorMP.close
            fSensorSeg.close

if __name__ == '__main__':
    main()