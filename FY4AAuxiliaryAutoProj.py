from DataOuter.HdfDataOuter import *
from DataProvider.H8DataProvider import *
from DataProvider.FY3AVirrProvider import *
from ProjProcessor import *
import sys
from ParameterParser import *
import multiprocessing
import AuxiliaryDict

#L1FilePath = ''

def CreateAuxilaryProvider(resolution):
    provider = H8Dataprovider()

#    Latfile = '/FY4COMM/FY4A/COM/fygatNAV.Himawari08.xxxxxxx.000001(2000).hdf'
#    Lonfile = '/FY4COMM/FY4A/COM/fygatNAV.Himawari08.xxxxxxx.000002(2000).hdf'
#    if resolution == 1000:
#        Latfile = '/FY4COMM/FY4A/COM/AHI8_OBI_1000M_NOM_LAT.hdf'
#        Lonfile = '/FY4COMM/FY4A/COM/AHI8_OBI_1000M_NOM_LON.hdf'
#    elif resolution ==500:
#        Latfile = '/FY4COMM/FY4A/COM/AHI8_OBI_500M_NOM_LAT.HDF'
#        Lonfile = '/FY4COMM/FY4A/COM/AHI8_OBI_500M_NOM_LON.HDF'
#    LNDfile = '/FY4COMM/FY4A/COM/IFL_FY4A_AGRIX_LND_'+str(resolution)+'M.HDF'
#    LMKfile = '/FY4COMM/FY4A/COM/IFL_FY4A_AGRIX_LMK_'+str(resolution)+'M.HDF'
#    DEMfile = '/FY4COMM/FY4A/COM/IFL_FY4A_AGRIX_DEM_'+str(resolution)+'M.HDF'
#    COASTfile = '/FY4COMM/FY4A/COM/IFL_FY4A_AGRIX_COAST_'+str(resolution)+'M.HDF'
#    SATZENfile = '/FY4COMM/FY4A/COM/AHI8_OBI_'+str(resolution)+'M_NOM_SATZEN.HDF'
#    SATAZIfile = '/FY4COMM/FY4A/COM/AHI8_OBI_'+str(resolution)+'M_NOM_SATAZI.HDF'
#    SolarZenfile = 'NULL'
#    solarAZIfile = 'NULL'
    
    Latfile = AuxiliaryDict.AuxiliaryDataDict['Latitude']['FilePath']        # not static dataset
    Lonfile = AuxiliaryDict.AuxiliaryDataDict['Longitude']['FilePath']       # not static dataset
    SOLARZENfile = AuxiliaryDict.AuxiliaryDataDict['SolarZenith']# not static dataset
    SOLARZIfile = AuxiliaryDict.AuxiliaryDataDict['SolarAzimuth']# not static dataset
    
    LNDfile = AuxiliaryDict.AuxiliaryDataDict['LandCover']
    LMKfile = AuxiliaryDict.AuxiliaryDataDict['LandSeaMask']
    DEMfile = AuxiliaryDict.AuxiliaryDataDict['DEM']
    COASTfile = AuxiliaryDict.AuxiliaryDataDict['SeaCoast']
    SATZENfile = AuxiliaryDict.AuxiliaryDataDict['SensorZenith']
    SATAZIfile = AuxiliaryDict.AuxiliaryDataDict['SensorAzimuth']
    pixel_desert_mask = AuxiliaryDict.AuxiliaryDataDict['pixel_DataSets']
#    pixel_ecosystem_type = AuxiliaryDict.AuxiliaryDataDict['pixel_ecosystem_type']['FilePath']
#    pixel_snow_mask = AuxiliaryDict.AuxiliaryDataDict['pixel_snow_mask']['FilePath']
#    pixel_surface_elevation = AuxiliaryDict.AuxiliaryDataDict['pixel_surface_elevation']['FilePath']
#    pixel_surface_type = AuxiliaryDict.AuxiliaryDataDict['pixel_surface_type']['FilePath']
#    pixel_volcano_mask = AuxiliaryDict.AuxiliaryDataDict['pixel_volcano_mask']['FilePath']
#    pixel_land_mask = AuxiliaryDict.AuxiliaryDataDict['pixel_land_mask']['FilePath']
#    pixel_coast_mask = AuxiliaryDict.AuxiliaryDataDict['pixel_coast_mask']['FilePath']
##above 8 Datasets -> pixel_XXX_XXX filepaths are the same,chose one filepath:use pixel_desert_mask

    provider.SetLonLatFile(Latfile,Lonfile)
    provider.SetAuxiliaryDataFile(LNDfile,LMKfile,DEMfile,COASTfile,SATZENfile,SATAZIfile,Lonfile,Latfile,SOLARZENfile,SOLARZIfile,pixel_desert_mask)

    return  provider


def ProcessProj(param, resolution):

    provider = CreateAuxilaryProvider(resolution)

    dataouter = HdfDataOuter()

    processor = ProjProcessor(provider, dataouter, param)
    processor.PerformProj()
    processor.Dispose()

def ProcessAuxProj(resolution):
    paramparser = ParameterParser()
    auxparam = paramparser.parseXML(sys.argv[2])
    auxparam.OutputPath = '/FY4COMM/FY4A/COM/'
    auxparam.ProjectResolution = resolution
    auxparam.IsAuxiliaryFileMode = True
    ProcessProj(auxparam, resolution)
if __name__ == '__main__':

    paramparser = ParameterParser()
    param = paramparser.parseXML(sys.argv[2])
    #param.OutputPath = '/FY4COMM/FY4A/L2/AGRIX/PRJ/'		#2016_10_14
    # ProcessProj(param, 2000,False)
    #
    # p1 = multiprocessing.Process(target = ProcessProj, args = (param,2000,False,))
    # p1.start()
    #
    # p2 = multiprocessing.Process(target = ProcessProj, args = (param,1000,False,))
    # p2.start()
    #
    # p2 = multiprocessing.Process(target = ProcessProj, args = (param,500,False,))
    # p2.start()
#    L1FilePath = sys.argv[4]
#    ProcessProj(param, int(sys.argv[3]),False)
#    auxfile = '/FY4COMM/FY4A/COM/PRJ/'+ param.GetParamDescription() + '_'+sys.argv[3]+'_'+param.ProjectTaskName+'.HDF'		#2016_10_14
    auxfile = '/FY4COMM/FY4A/COM/PRJ/'+ param.GetParamDescription() + '_'+sys.argv[3]+'_'+param.ProjectTaskName+'.HDF'
    #auxfile ='/home/bozi/Downloads/TestData/'+ param.GetParamDescription() + '_'+'2000'+'_'+param.ProjectTaskName+'.HDF'
    if os.path.exists(auxfile) == False:
        ProcessAuxProj(int(sys.argv[3]))
        #ProcessAuxProj(2000)
    # auxfile = param.OutputPath + param.GetParamDescription() + '_1000_Proj.HDF'
    # if os.path.exists(auxfile) == False:
    #     ProcessAuxProj(1000)

    # auxfile = param.OutputPath + param.GetParamDescription() + '_500_Proj.HDF'
    # if os.path.exists(auxfile) == False:
    #     ProcessAuxProj(500)

    # p1 = multiprocessing.Process(target = ProcessProj, args = (param,2000,))
    # p1.start()
    #
    # p2 = multiprocessing.Process(target = ProcessProj, args = (param,1000,))
    # p2.start()
    #
    # p3 = multiprocessing.Process(target = ProcessProj, args = (param,500,))
    # p3.start()
    # ProcessProj(param,2000)
    # ProcessProj(param, 1000)
    # ProcessProj(param, 500)