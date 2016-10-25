import sys

AuxiliaryDataDict = dict()

LatitudeFilePathAndName = dict()
LongitudeFilePathAndName = dict()
LandCoverFilePathAndName = dict()
LandSeaMaskFilePathAndName = dict()
DEMFilePathAndName = dict()
SeaCoastFilePathAndName = dict()
SensorZenithFilePathAndName = dict()
SensorAzimuthFilePathAndName = dict()
SolarZenithFilePathAndName = dict()
SolarAzimuthFilePathAndName = dict()

pixel_DataSetsFilePathAndName = dict()#8static datasets in the same file

#resolution = 500
#resolution = 1000
#resolution = 2000
resolution = int(sys.argv[3])


if resolution == 2000:
   # print(2000)
    LatitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/fygatNAV.Himawari08.xxxxxxx.000001(2000).hdf'
    LatitudeFilePathAndName['Name'] = 'Lat'
    AuxiliaryDataDict['Latitude'] = LatitudeFilePathAndName

    LongitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/fygatNAV.Himawari08.xxxxxxx.000002(2000).hdf'
    LongitudeFilePathAndName['Name'] = 'Lon'
    AuxiliaryDataDict['Longitude'] = LongitudeFilePathAndName   
    
    SensorZenithFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'#2016_10_13
    SensorZenithFilePathAndName['Name'] = 'pixel_satellite_zenith_angle'
    AuxiliaryDataDict['SensorZenith'] = SensorZenithFilePathAndName

    SensorAzimuthFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'#2016_10_13
    SensorAzimuthFilePathAndName['Name'] = 'pixel_satellite_azimuth_angle'
    AuxiliaryDataDict['SensorAzimuth'] = SensorAzimuthFilePathAndName
     
    #pixel_desert_maskFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
    pixel_DataSetsFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
    pixel_DataSetsFilePathAndName['Name_pixel_desert_mask'] = 'pixel_desert_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_ecosystem_type'] = 'pixel_ecosystem_type'
    pixel_DataSetsFilePathAndName['Name_pixel_snow_mask'] = 'pixel_snow_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_surface_elevation'] = 'pixel_surface_elevation'
    pixel_DataSetsFilePathAndName['Name_pixel_surface_type'] = 'pixel_surface_type'
    pixel_DataSetsFilePathAndName['Name_pixel_volcano_mask'] = 'pixel_volcano_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_land_mask'] = 'pixel_land_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_coast_mask'] = 'pixel_coast_mask'
    AuxiliaryDataDict['pixel_DataSets'] = pixel_DataSetsFilePathAndName
    
elif resolution == 4000:				#2016_10_21
    LatitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_4000M_NOM_LATLON.HDF'
    LatitudeFilePathAndName['Name'] = 'Lat'
    AuxiliaryDataDict['Latitude'] = LatitudeFilePathAndName

    LongitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_4000M_NOM_LATLON.HDF'
    LongitudeFilePathAndName['Name'] = 'Lon'
    AuxiliaryDataDict['Longitude'] = LongitudeFilePathAndName
    
    SensorZenithFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.4000m.hdf'
    SensorZenithFilePathAndName['Name'] = 'pixel_satellite_zenith_angle'
    AuxiliaryDataDict['SensorZenith'] = SensorZenithFilePathAndName

    SensorAzimuthFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.4000m.hdf'
    SensorAzimuthFilePathAndName['Name'] = 'pixel_satellite_azimuth_angle'
    AuxiliaryDataDict['SensorAzimuth'] = SensorAzimuthFilePathAndName
    
    pixel_DataSetsFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.4000m.hdf'
    pixel_DataSetsFilePathAndName['Name_pixel_desert_mask'] = 'pixel_desert_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_ecosystem_type'] = 'pixel_ecosystem_type'
    pixel_DataSetsFilePathAndName['Name_pixel_snow_mask'] = 'pixel_snow_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_surface_elevation'] = 'pixel_surface_elevation'
    pixel_DataSetsFilePathAndName['Name_pixel_surface_type'] = 'pixel_surface_type'
    pixel_DataSetsFilePathAndName['Name_pixel_volcano_mask'] = 'pixel_volcano_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_land_mask'] = 'pixel_land_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_coast_mask'] = 'pixel_coast_mask'
    AuxiliaryDataDict['pixel_DataSets'] = pixel_DataSetsFilePathAndName
    
elif resolution == 8000:				
   # print(8000)																																#2016_10_14
    LatitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_8000M_NOM_LATLON.HDF'
    LatitudeFilePathAndName['Name'] = 'Lat'
    AuxiliaryDataDict['Latitude'] = LatitudeFilePathAndName

    LongitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_8000M_NOM_LATLON.HDF'
    LongitudeFilePathAndName['Name'] = 'Lon'
    AuxiliaryDataDict['Longitude'] = LongitudeFilePathAndName
    
    SensorZenithFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.8000m.hdf'
    SensorZenithFilePathAndName['Name'] = 'pixel_satellite_zenith_angle'
    AuxiliaryDataDict['SensorZenith'] = SensorZenithFilePathAndName

    SensorAzimuthFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.8000m.hdf'
    SensorAzimuthFilePathAndName['Name'] = 'pixel_satellite_azimuth_angle'
    AuxiliaryDataDict['SensorAzimuth'] = SensorAzimuthFilePathAndName
    
    pixel_DataSetsFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.8000m.hdf'
    pixel_DataSetsFilePathAndName['Name_pixel_desert_mask'] = 'pixel_desert_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_ecosystem_type'] = 'pixel_ecosystem_type'
    pixel_DataSetsFilePathAndName['Name_pixel_snow_mask'] = 'pixel_snow_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_surface_elevation'] = 'pixel_surface_elevation'
    pixel_DataSetsFilePathAndName['Name_pixel_surface_type'] = 'pixel_surface_type'
    pixel_DataSetsFilePathAndName['Name_pixel_volcano_mask'] = 'pixel_volcano_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_land_mask'] = 'pixel_land_mask'
    pixel_DataSetsFilePathAndName['Name_pixel_coast_mask'] = 'pixel_coast_mask'
    AuxiliaryDataDict['pixel_DataSets'] = pixel_DataSetsFilePathAndName
    
elif resolution == 1000:
   # print(1000)
    LatitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_1000M_NOM_LAT.hdf'
    LatitudeFilePathAndName['Name'] = 'Lat'
    AuxiliaryDataDict['Latitude'] = LatitudeFilePathAndName

    LongitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_1000M_NOM_LON.hdf'
    LongitudeFilePathAndName['Name'] = 'Lon'
    AuxiliaryDataDict['Longitude'] = LongitudeFilePathAndName
    
    #pixel_desert_maskFilePathAndName['FilePath'] = 'NULL'
    #pixel_desert_maskFilePathAndName['Name'] = 'pixel_desert_mask'
    #AuxiliaryDataDict['pixel_desert_mask'] = pixel_desert_maskFilePathAndName
    AuxiliaryDataDict['pixel_DataSets'] = 'NULL'
    
    SensorZenithFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_'+str(resolution)+'M_NOM_SATZEN.HDF'#2016_10_13
    SensorZenithFilePathAndName['Name'] = 'SatZenith'
    AuxiliaryDataDict['SensorZenith'] = SensorZenithFilePathAndName

    SensorAzimuthFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_'+str(resolution)+'M_NOM_SATAZI.HDF'#2016_10_13
    SensorAzimuthFilePathAndName['Name'] = 'SatAzimuth'
    AuxiliaryDataDict['SensorAzimuth'] = SensorAzimuthFilePathAndName

elif resolution == 500:
   # print(500)
    LatitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_500M_NOM_LAT.HDF'
    LatitudeFilePathAndName['Name'] = 'Lat'
    AuxiliaryDataDict['Latitude'] = LatitudeFilePathAndName

    LongitudeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_500M_NOM_LON.HDF'
    LongitudeFilePathAndName['Name'] = 'Lon'
    AuxiliaryDataDict['Longitude'] = LongitudeFilePathAndName
    
    #pixel_desert_maskFilePathAndName['FilePath'] = 'NULL'
    #pixel_desert_maskFilePathAndName['Name'] = 'pixel_desert_mask'
    #AuxiliaryDataDict['pixel_desert_mask'] = pixel_desert_maskFilePathAndName
    AuxiliaryDataDict['pixel_DataSets'] = 'NULL'
    
    SensorZenithFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_'+str(resolution)+'M_NOM_SATZEN.HDF'
    SensorZenithFilePathAndName['Name'] = 'SatZenith'
    AuxiliaryDataDict['SensorZenith'] = SensorZenithFilePathAndName

    SensorAzimuthFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_'+str(resolution)+'M_NOM_SATAZI.HDF'
    SensorAzimuthFilePathAndName['Name'] = 'SatAzimuth'
    AuxiliaryDataDict['SensorAzimuth'] = SensorAzimuthFilePathAndName

LandCoverFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/IFL_FY4A_AGRIX_LND_'+str(resolution)+'M.HDF'
LandCoverFilePathAndName['Name'] = 'LandCover'
AuxiliaryDataDict['LandCover'] = LandCoverFilePathAndName

LandSeaMaskFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/IFL_FY4A_AGRIX_LMK_'+str(resolution)+'M.HDF'
LandSeaMaskFilePathAndName['Name'] = 'LandSeaMask'
AuxiliaryDataDict['LandSeaMask'] = LandSeaMaskFilePathAndName

DEMFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/IFL_FY4A_AGRIX_DEM_'+str(resolution)+'M.HDF'
DEMFilePathAndName['Name'] = 'DEM'
AuxiliaryDataDict['DEM'] = DEMFilePathAndName

SeaCoastFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/IFL_FY4A_AGRIX_COAST_'+str(resolution)+'M.HDF'
SeaCoastFilePathAndName['Name'] = 'SeaCoast'
AuxiliaryDataDict['SeaCoast'] = SeaCoastFilePathAndName

#SensorZenithFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_'+str(resolution)+'M_NOM_SATZEN.HDF' #2016_10_13
#SensorZenithFilePathAndName['Name'] = 'SensorZenith'
#AuxiliaryDataDict['SensorZenith'] = SensorZenithFilePathAndName

#SensorAzimuthFilePathAndName['FilePath'] = '/FY4COMM/FY4A/COM/AHI8_OBI_'+str(resolution)+'M_NOM_SATAZI.HDF' #2016_10_13
#SensorAzimuthFilePathAndName['Name'] = 'SensorAzimuth'
#AuxiliaryDataDict['SensorAzimuth'] = SensorAzimuthFilePathAndName

#SolarZenithFilePathAndName['FilePath'] = 'NULL'
#SolarZenithFilePathAndName['Name'] = 'NOMSunZenith'
#AuxiliaryDataDict['SolarZenith'] = SolarZenithFilePathAndName
AuxiliaryDataDict['SolarZenith'] = 'NULL'

#SolarAzimuthFilePathAndName['FilePath'] = 'NULL'
#SolarAzimuthFilePathAndName['Name'] = 'NOMSunAzimuth'
#AuxiliaryDataDict['SolarAzimuth'] = SolarAzimuthFilePathAndName
AuxiliaryDataDict['SolarAzimuth'] = 'NULL'

## 2016_9_30 add 8 DataSets
#pixel_desert_maskFilePathAndName = dict()
#pixel_ecosystem_typeFilePathAndName = dict()
#pixel_snow_maskFilePathAndName = dict()
#pixel_surface_elevationFilePathAndName = dict()
#pixel_surface_typeFilePathAndName = dict()
#pixel_volcano_maskFilePathAndName = dict()
#pixel_land_maskFilePathAndName = dict()
#pixel_coast_maskFilePathAndName = dict()

#pixel_desert_maskFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
#pixel_desert_maskFilePathAndName['Name'] = 'pixel_desert_mask'
#AuxiliaryDataDict['pixel_desert_mask'] = pixel_desert_maskFilePathAndName

#pixel_ecosystem_typeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
#pixel_ecosystem_typeFilePathAndName['Name'] = 'pixel_ecosystem_type'
#AuxiliaryDataDict['pixel_ecosystem_type'] = pixel_ecosystem_typeFilePathAndName

#pixel_snow_maskFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
#pixel_snow_maskFilePathAndName['Name'] = 'pixel_snow_mask'
#AuxiliaryDataDict['pixel_snow_mask'] = pixel_snow_maskFilePathAndName

#pixel_surface_elevationFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
#pixel_surface_elevationFilePathAndName['Name'] = 'pixel_surface_elevation'
#AuxiliaryDataDict['pixel_surface_elevation'] = pixel_surface_elevationFilePathAndName

#pixel_surface_typeFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
#pixel_surface_typeFilePathAndName['Name'] = 'pixel_surface_type'
#AuxiliaryDataDict['pixel_surface_type'] = pixel_surface_typeFilePathAndName

#pixel_volcano_maskFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
#pixel_volcano_maskFilePathAndName['Name'] = 'pixel_volcano_mask'
#AuxiliaryDataDict['pixel_volcano_mask'] = pixel_volcano_maskFilePathAndName

#pixel_land_maskFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
#pixel_land_maskFilePathAndName['Name'] = 'pixel_land_mask'
#AuxiliaryDataDict['pixel_land_mask'] = pixel_land_maskFilePathAndName

#pixel_coast_maskFilePathAndName['FilePath'] = '/FY4COMM/FY4A/PAR/AGRIX/ancillary_data/navigation/fygatNAV.Himawari08.xxxxxxx.2000m.hdf'
#pixel_coast_maskFilePathAndName['Name'] = 'pixel_coast_mask'
#AuxiliaryDataDict['pixel_coast_mask'] = pixel_coast_maskFilePathAndName

