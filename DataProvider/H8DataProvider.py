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
    __dataRes = 4000
    __dataWidthAndHeight= 2750
    __obsDataCount = 4


    def __init__(self):
        super(H8Dataprovider,self).__init__()
        return

    def __InitOrbitInfo(self):
        self.OrbitInfo.Sat = 'Himawari 8'
        self.OrbitInfo.Sensor = 'H8'
        self.OrbitInfo.OrbitDirection= ''

        self.OrbitInfo.Width = self.__dataWidthAndHeight
        self.OrbitInfo.Height = self.__dataWidthAndHeight

        solarzenith = self.GetSolarZenith()
        if solarzenith[int(self.__dataWidthAndHeight/2),int(self.__dataWidthAndHeight/2)] <=85:
            self.OrbitInfo.DNFlag = 'D'
        else:
            self.OrbitInfo.DNFlag = 'N'

        self.OrbitInfo.Date=''
        self.OrbitInfo.Time=''

        self.CreateBandsInfo2KM()

    def SetFile(self,file):
        self.__latFileHandle = self.__HdfOperator.Open(file[0])
        self.__lonFileHandle = self.__HdfOperator.Open(file[1])
        self.__DataFileHandle = self.__HdfOperator.Open(file[2])
        self.__fileName = file[2]
        if '_2000M_' in self.__fileName:
            self.__dataRes = 2000
            self.__dataWidthAndHeight = 5500
            self.__obsDataCount = 16

        self.__InitOrbitInfo()

    def CreateBandsInfo2KM(self):
        self.OrbitInfo.BandsWavelength['EVB1'] = '0046'
        self.OrbitInfo.BandsWavelength['EVB2'] = '0051'
        self.OrbitInfo.BandsWavelength['EVB3'] = '0064'
        self.OrbitInfo.BandsWavelength['EVB4'] = '0086'
        self.OrbitInfo.BandsWavelength['EVB5'] = '0160'
        self.OrbitInfo.BandsWavelength['EVB6'] = '0230'
        self.OrbitInfo.BandsWavelength['EVB7'] = '0390'
        self.OrbitInfo.BandsWavelength['EVB8'] = '0620'
        self.OrbitInfo.BandsWavelength['EVB9'] = '0700'
        self.OrbitInfo.BandsWavelength['EVB10'] = '0730'
        self.OrbitInfo.BandsWavelength['EVB11'] = '0860'
        self.OrbitInfo.BandsWavelength['EVB12'] = '0960'
        self.OrbitInfo.BandsWavelength['EVB13'] = '1040'
        self.OrbitInfo.BandsWavelength['EVB14'] = '1120'
        self.OrbitInfo.BandsWavelength['EVB15'] = '1230'
        self.OrbitInfo.BandsWavelength['EVB16'] = '1330'

        self.OrbitInfo.BandsType['EVB1'] = 'REF'
        self.OrbitInfo.BandsType['EVB2'] = 'REF'
        self.OrbitInfo.BandsType['EVB3'] = 'REF'
        self.OrbitInfo.BandsType['EVB4'] = 'REF'
        self.OrbitInfo.BandsType['EVB5'] = 'REF'
        self.OrbitInfo.BandsType['EVB6'] = 'REF'
        self.OrbitInfo.BandsType['EVB7'] = 'EMIS'
        self.OrbitInfo.BandsType['EVB8'] = 'EMIS'
        self.OrbitInfo.BandsType['EVB9'] = 'EMIS'
        self.OrbitInfo.BandsType['EVB10'] = 'EMIS'
        self.OrbitInfo.BandsType['EVB11'] = 'EMIS'
        self.OrbitInfo.BandsType['EVB12'] = 'EMIS'
        self.OrbitInfo.BandsType['EVB13'] = 'EMIS'
        self.OrbitInfo.BandsType['EVB14'] = 'EMIS'
        self.OrbitInfo.BandsType['EVB15'] = 'EMIS'
        self.OrbitInfo.BandsType['EVB16'] = 'EMIS'


    def GetLongitude(self):

        return self.GetDataSet(self.__lonFileHandle, '/', 'Lon')


    def GetLatitude(self):

        return self.GetDataSet(self.__latFileHandle, '/', 'Lat')


    def GetResolution(self):
        return self.__dataRes

    def GetOBSData(self, band):
        bandname = ''

        if self.__dataRes == 2000:
            bandname = self.__GetOBSDatasetName2KM(band)
        else:
            bandname = self.__GetOBSDatasetName4KM(band)

        ret = None
        if bandname!='':

            ret=self.GetDataSet(self.__DataFileHandle,'/', bandname)

        return ret

    def __GetOBSDatasetName2KM(self,band):
        bandname = ''
        if band == 'EVB1':
            bandname = 'NOMChannelVIS0046_2000'
        elif band == 'EVB2':
            bandname = 'NOMChannelVIS0051_2000'
        elif band == 'EVB3':
            bandname = 'NOMChannelVIS0064_2000'
        elif band == 'EVB4':
            bandname = 'NOMChannelVIS0086_2000'
        elif band == 'EVB5':
            bandname = 'NOMChannelVIS0160_2000'
        elif band == 'EVB6':
            bandname = 'NOMChannelVIS0230_2000'
        elif band == 'EVB7':
            bandname = 'NOMChannelIRX0390_2000'
        elif band == 'EVB8':
            bandname = 'NOMChannelIRX0620_2000'
        elif band == 'EVB9':
            bandname = 'NOMChannelIRX0700_2000'
        elif band == 'EVB10':
            bandname = 'NOMChannelIRX0730_2000'
        elif band == 'EVB11':
            bandname = 'NOMChannelIRX0860_2000'
        elif band == 'EVB12':
            bandname = 'NOMChannelIRX0960_2000'
        elif band == 'EVB13':
            bandname = 'NOMChannelIRX1040_2000'
        elif band == 'EVB14':
            bandname = 'NOMChannelIRX1120_2000'
        elif band == 'EVB15':
            bandname = 'NOMChannelIRX1230_2000'
        elif band == 'EVB16':
            bandname = 'NOMChannelIRX1330_2000'

        return  bandname

    def __GetOBSDatasetName4KM(self, band):
        bandname = ''
        if band == 'EVB1':
            bandname = 'NOMChannelVIS0064_4000'
        elif band == 'EVB2':
            bandname = 'NOMChannelVIS0086_4000'
        elif band == 'EVB3':
            bandname = 'NOMChannelVIS0160_4000'
        elif band == 'EVB4':
            bandname = 'NOMChannelVIS0230_4000'

        return bandname

    def GetOBSDataCount(self):
        return self.__obsDataCount

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

    # def GetEmissData(self, band):
    #     return

    def GetFile(self):
        return  self.__fileName


