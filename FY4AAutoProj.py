from DataOuter.HdfDataOuter import *
from DataProvider.H8DataProvider import *
from DataProvider.FY3AVirrProvider import *
from ProjProcessor import *
import sys
from ParameterParser import *
import multiprocessing


L1FilePath = ''


def CreateStdProjProvider(resolution):
    provider = H8Dataprovider()

    Latfile = '/FY4COMM/FY4A/COM/fygatNAV.Himawari08.xxxxxxx.000001(2000).hdf'
    Lonfile = '/FY4COMM/FY4A/COM/fygatNAV.Himawari08.xxxxxxx.000002(2000).hdf'
    L1file = L1FilePath+'AHI8_OBI_2000M_NOM_' + sys.argv[1] + '.hdf'

    if resolution == 1000:
        Latfile = '/FY4COMM/FY4A/COM/AHI8_OBI_1000M_NOM_LAT.hdf'
        Lonfile = '/FY4COMM/FY4A/COM/AHI8_OBI_1000M_NOM_LON.hdf'
        L1file = L1FilePath+'AHI8_OBI_1000M_NOM_' + sys.argv[1] + '.hdf'

    elif resolution == 500:
        Latfile = '/FY4COMM/FY4A/COM/AHI8_OBI_500M_NOM_LAT.HDF'
        Lonfile = '/FY4COMM/FY4A/COM/AHI8_OBI_500M_NOM_LON.HDF'
        L1file = L1FilePath+'AHI8_OBI_0500M_NOM_' + sys.argv[1] + '.hdf'


    provider.SetLonLatFile(Latfile,Lonfile)

    print sys.argv[1]
    provider.SetL1File(L1file)
    provider.SetDataDescription('Himawari8_OBI_'+sys.argv[1])
    
    if resolution == 4000:
        provider.SetAuxiliaryDataFile('NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL',L1file,L1file, 'NULL')
    
    return  provider

def ProcessProj(param,resolution):

    provider = CreateStdProjProvider(resolution)

    dataouter = HdfDataOuter()

    processor = ProjProcessor(provider, dataouter, param)
    processor.PerformProj()
    processor.Dispose()

def ProcessAuxProj(resolution):
    paramparser = ParameterParser()
    auxparam = paramparser.parseXML(sys.argv[2])
   # auxparam.OutputPath = '/FY4COMM/FY4A/COM/PRJ/' #2016_10_12
    auxparam.OutputPath = sys.argv[5] #2016_10_12
    auxparam.ProjectResolution = resolution
##    auxparam.IsAuxiliaryFileMode = True
##    ProcessProj(auxparam, resolution, True)
    ProcessProj(auxparam, resolution)
if __name__ == '__main__':
	
    L1FilePath = sys.argv[4]
    paramparser = ParameterParser()
    param = paramparser.parseXML(sys.argv[2])
    #param.OutputPath = '/FY4COMM/FY4A/L2/AGRIX/PRJ/' #2016_10_12
    param.OutputPath = sys.argv[5]  #2016_10_12
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
    L1FilePath = sys.argv[4]
    ProcessProj(param, int(sys.argv[3]))


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