from DataProvider import *
from HdfOperator import *
import numpy as N
from Parameters import *



class H8Dataprovider(DataProvider):
    __HdfOperator = HdfOperator()
    __latFileHandle = None
    __lonFileHandle = None
    __DataFileHandle = None
    __fileName = None
    __longitude = None
    __latitude = None




    def __init__(self):
        super(H8Dataprovider,self).__init__()
        return

    def __InitOrbitInfo(self):
        self.OrbitInfo.Sat = 'Himawari 8'
        self.OrbitInfo.Sensor = 'H8'
        self.OrbitInfo.OrbitDirection= ''

        self.OrbitInfo.Width = 2750
        self.OrbitInfo.Height = 2750

        solarzenith = self.GetSolarZenith();
        if solarzenith[int(2750/2),int(2750/2)] <=85:
            self.OrbitInfo.DNFlag = 'D'
        else:
            self.OrbitInfo.DNFlag = 'N'

        self.OrbitInfo.Date=''
        self.OrbitInfo.Time=''
        self.OrbitInfo.BandsCount = 16
        self.OrbitInfo.Band_name=''
        self.OrbitInfo.RefSBBandsCount = 0

        self.OrbitInfo.RefSBBandsNames = ''
        self.OrbitInfo.EmissiveBandsCoun=0
        self.OrbitInfo.EmissiveBandsNames = ''


    def SetFile(self,file):
        self.__latFileHandle = self.__HdfOperator.Open(file[0])
        self.__lonFileHandle = self.__HdfOperator.Open(file[1])
        self.__DataFileHandle = self.__HdfOperator.Open(file[2])
        self.__fileName = file[2]
        self.__InitOrbitInfo()


    def GetLongitude(self):

        return self.GetDataSet(self.__lonFileHandle, '/', 'Lon')



    def GetLatitude(self):

        return self.GetDataSet(self.__latFileHandle, '/', 'Lat')


    def GetResolution(self):
        return 4000

    def GetRefData(self, band):
        bandname = ''
        ret = None
        if band == 0:
            bandname = 'NOMChannelVIS0064_4000'
        elif band == 1:
            bandname = 'NOMChannelVIS0086_4000'
        elif band == 2:
            bandname = 'NOMChannelVIS0160_4000'
        elif band == 3:
            bandname = 'NOMChannelVIS0230_4000'

        if bandname!='':

            ret=self.GetDataSet(self.__DataFileHandle,'/', bandname)

        return ret

    def GetSensorAzimuth(self):

        return self.GetDataSet(self.__DataFileHandle,'/','NOMSatelliteAzimuth')


    def GetDataSet(self,filehandle,group,ds):

        data = self.__HdfOperator.ReadHdfDataset(filehandle, group, ds)
        startLine = self.startLine
        endlLine = self.endLine
        ret = None
        if startLine!= -1 & endlLine!= -1:
            ret = data[startLine:endlLine, :]
        else:
            ret = data[:,:]
        return ret

    def GetSensorZenith(self):
        return self.GetDataSet(self.__DataFileHandle,'/','NOMSatelliteZenith')

    def GetSolarAzimuth(self):
        return self.GetDataSet(self.__DataFileHandle,'/','NOMSunAzimuth')

    def GetSolarZenith(self):
        return self.GetDataSet(self.__DataFileHandle,'/','NOMSunZenith')

    def GetEmissData(self, band):
        return

    def GetFile(self):
        return  self.__fileName


