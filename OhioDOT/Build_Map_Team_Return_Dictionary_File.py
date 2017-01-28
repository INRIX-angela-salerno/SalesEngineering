# -*- coding: utf-8 -*-
"""
Spyder Editor

This module reads the two foundational files used by the Ohio DOT
API: DeviceInrixSegTable.txt and OhioDeviceSpeedInfo.txt, merges them,
and outputs to CSV.  This CSV is then shared with the Map Team.

"""

import pandas as pd

def main():
    # Import, read, dataframe the two data files used by the Ohio DOT API:
    #    DeviceInrixSegTable.txt
    #    OhioDeviceSpeedInfo.txt
    d_input = input("Enter full path to DeviceInrixSegTable.txt: ")
    o_input = input("Enter full path to OhioDeviceSpeedInfo.txt: ")
    
    d_read = pd.read_table(d_input, header = 0)
    o_read = pd.read_table(o_input, header = 0)
    
    ohio_dataframe = pd.merge(d_read, o_read,
        left_on = ["SensorID", "Latitude", "Longitude", "RoadName"],
        right_on = ["ID", "Latitude", "Longitude", "RoadName"])

    # Construct the aggregate CSV to be shared with Map Team.
    ohio_output = input("Enter the full path and file for output: ")

    ohio_dataframe.to_csv(path_or_buf = ohio_output,
                          columns = ["SensorID",
                                  "XDSegID", 
                                  "Latitude", 
                                  "Longitude", 
                                  "RoadName", 
                                  "RoadDir"],
                          header = ["SensorID",
                                  "XDSegID", 
                                  "Latitude", 
                                  "Longitude", 
                                  "RoadName", 
                                  "Bearing"],
                          index = False)

if __name__ == '__main__':
    main()