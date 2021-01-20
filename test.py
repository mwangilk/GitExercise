import pandas as pd 
import numpy
data_frame= pd.read_fwf('4X64log.txt')
data_frame.to_csv('iostat.csv')
print(data_frame)