from DataProvider import *
from HdfOperator import *
import numpy as N

class H8Dataprovider(DataProvider):
    __HdfOperator = HdfOperator()
    __latFileHandle = None
    __lonFileHandle = None
    __DataFileHandle = None
    __fileName = None

    def __init__(self):
        super(H8Dataprovider,self).__init__()
        return

    def SetFile(self,file):
        self.__latFileHandle = self.__HdfOperator.Open(file[0])
        self.__lonFileHandle = self.__HdfOperator.Open(file[1])
        self.__DataFileHandle = self.__HdfOperator.Open(file[2])
        self.__fileName = file[2]


    def Longitude(self):
        lon= N.array(self.__HdfOperator.ReadHdfDataset(self.__lonFileHandle, '/', 'Lon'))
        self.__HdfOperator.Close(self.__lonFileHandle)
        return lon



    def Latitude(self):
        lat=N.array(self.__HdfOperator.ReadHdfDataset(self.__latFileHandle, '/', 'Lat'))

        self.__HdfOperator.Close(self.__latFileHandle)
        return lat

    def GetResolution(self):
        return 8000

    def RefData(self,band):
        bandname = ''
        if band == 0:
            bandname = 'NOMChannelVIS0064_4000'
        elif band == 1:
            bandname = 'NOMChannelVIS0086_4000'
        elif band == 2:
            bandname = 'NOMChannelVIS0160_4000'
        elif band == 3:
            bandname = 'NOMChannelVIS0230_4000'

        if bandname!='':
            return self.__HdfOperator.ReadHdfDataset(self.__DataFileHandle, '/', bandname)

        return None

    def EmissData(self,band):
        return

    def GetFile(self):
        return  self.__fileName