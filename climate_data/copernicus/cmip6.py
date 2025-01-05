'''
CMIP6 constants and enums for Copernicus Climate Data Service (CDS) requests.
'''
from enum import Enum, unique
from dataclasses import dataclass

DATASET = "projections-cmip6"

@unique
class Listable(Enum):
    '''Listable enum class.'''
    @classmethod
    def to_list(cls) -> list[str]:
        '''Returns a list of enum values.'''
        return [e.value for e in cls]

#region CMIP6 Enums
class Experiments(Listable):
    '''CMIP6 experiments.'''
    HISTORICAL = "historical"
    SSP1_26 = "ssp126"
    SSP2_45 = "ssp245"
    SSP3_70 = "ssp370"
    SSP4_60 = "ssp460"
    SSP5_85 = "ssp585"

class Models(Listable):
    '''CMIP6 models.'''
    ACCESS_CM2 = "access_cm2"
    ACCESS_ESM1_5 = "access_esm1_5"
    AWI_CM_1_1_MR = "awi_cm_1_1_mr"
    AWI_ESM_1_1_LR = "awi_esm_1_1_lr"
    BCC_CSM2_MR = "bcc_csm2_mr"
    BCC_ESM1 = "bcc_esm1"
    CAMS_CSM_1_0 = "cams_csm_1_0"
    CANESM5 = "canesm5"
    CANESM5_CANOE = "canesm5_canoe"
    CESM2 = "cesm2"
    CESM2_FV2 = "cesm2_fv2"
    CESM2_WACCM = "cesm2_waccm"
    CESM2_WACCM_FV2 = "cesm2_waccm_fv2"
    CIESM = "ciesm"
    CMCC_CM2_HR4 = "cmcc_cm2_hr4"
    CMCC_CM2_SR5 = "cmcc_cm2_sr5"
    CMCC_ESM2 = "cmcc_esm2"
    CNRM_CM6_1 = "cnrm_cm6_1"
    CNRM_CM6_1_HR = "cnrm_cm6_1_hr"
    CNRM_ESM2_1 = "cnrm_esm2_1"
    E3SM_1_0 = "e3sm_1_0"
    E3SM_1_1 = "e3sm_1_1"
    E3SM_1_1_ECA = "e3sm_1_1_eca"
    EC_EARTH3 = "ec_earth3"
    EC_EARTH3_AERCHEM = "ec_earth3_aerchem"
    EC_EARTH3_CC = "ec_earth3_cc"
    EC_EARTH3_VEG = "ec_earth3_veg"
    EC_EARTH3_VEG_LR = "ec_earth3_veg_lr"
    FGOALS_F3_L = "fgoals_f3_l"
    FGOALS_G3 = "fgoals_g3"
    FIO_ESM_2_0 = "fio_esm_2_0"
    GFDL_ESM4 = "gfdl_esm4"
    GISS_E2_1_G = "giss_e2_1_g"
    GISS_E2_1_H = "giss_e2_1_h"
    HADGEM3_GC31_LL = "hadgem3_gc31_ll"
    HADGEM3_GC31_MM = "hadgem3_gc31_mm"
    IITM_ESM = "iitm_esm"
    INM_CM4_8 = "inm_cm4_8"
    INM_CM5_0 = "inm_cm5_0"
    IPSL_CM5A2_INCA = "ipsl_cm5a2_inca"
    IPSL_CM6A_LR = "ipsl_cm6a_lr"
    KACE_1_0_G = "kace_1_0_g"
    KIOST_ESM = "kiost_esm"
    MCM_UA_1_0 = "mcm_ua_1_0"
    MIROC6 = "miroc6"
    MIROC_ES2H = "miroc_es2h"
    MIROC_ES2L = "miroc_es2l"
    MPI_ESM_1_2_HAM = "mpi_esm_1_2_ham"
    MPI_ESM1_2_HR = "mpi_esm1_2_hr"
    MPI_ESM1_2_LR = "mpi_esm1_2_lr"
    MRI_ESM2_0 = "mri_esm2_0"
    NESM3 = "nesm3"
    NORCPM1 = "norcpm1"
    NORESM2_LM = "noresm2_lm"
    NORESM2_MM = "noresm2_mm"
    SAM0_UNICON = "sam0_unicon"
    TAIESM1 = "taiesm1"
    UKESM1_0_LL = "ukesm1_0_ll"

@unique
class TemporalResolutions(Enum):
    '''CMIP6 temporal resolutions.'''
    MONTHLY = "monthly"
    DAILY = "daily"
    FIXED = "fixed"

@unique
class Variables(Enum):
    '''
    CMIP6 variables.
    
    Note: 
        This is a patial list,
            see: https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form
        The availability of these data across models, experiments, and resolutions varies.
    '''
    TEMP = "tas"        # near surface air temperature at 2m, daily, monthly [K]
    TMAX = "tasmax"     # near surface maximum air temperature at 2m, daily, monthly [K]
    TMIN = "tasmin"     # near surface minimum air temperature at 2m, daily, monthly [K]
    SKIN_TEMP = "ts"    # surface temperature, monthly [K]
    PSL = "psl"         # sea level pressure, daily, monthly [Pa]
    PS = "ps"           # surface air pressure, monthly [Pa]
    UWIND = "uas"       # 10 m component of E wind, monthly [m/s]
    VWIND = "vas"       # 10 m component of N wind, monthly [m/s]
    WIND_SPEED = "sfcWind" # surface 10 m wind speed, daily, monthly [m/s]
    RH = "hurs"         # near-surface 2m relative humidity, monthly
    SH = "huss"         # near-surface 2m specific humidity, daily, monthly
    PRECIP = "pr"       # precipitation, daily, monthly [kg m-2 s-1]
    SNOW = "prsn"       # snowfall, monthly [kg m-2 s-1]
    EVAP = "evspsbl"    # evaporation, monthly [kg m-2 s-1]
    # add more from https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form\

@unique
class FileFormats(Enum):
    '''File formats.'''
    NETCDF = '.nc'
    GRIB = '.grib'
    ZIP = '.zip'
#endregion

#region CMIP6 Time Variable Constants
DAYS: tuple[str,...] = tuple((f'{i:02d}' for i in range(1, 32)))
MONTHS: tuple[str,...] = tuple((f'{i:02d}' for i in range(1, 13)))
HISTORY_YEARS: tuple[str,...] = tuple((f'{i:04d}' for i in range(1850, 2015)))
PROJECTION_YEARS: tuple[str,...] = tuple((f'{i:04d}' for i in range(2015, 2101)))
#endregion

def default_years(experiment: Experiments) -> tuple[str,...]:
    '''Returns the default years for the given experiment.'''
    if experiment == Experiments.HISTORICAL:
        return HISTORY_YEARS
    return PROJECTION_YEARS

#region List Constansts
CMIP6_EXPERIMENTS: tuple[str,...] = ('historical', 'ssp126', 'ssp245', 'ssp370', 'ssp460', 'ssp585')
CMIP6_MODELS: tuple[str,...] = (
        'access_cm2', 'access_esm1_5',                          # Australia
        'awi_cm_1_1_mr', 'awi_esm_1_1_lr',                      # Germany
        'bcc_csm2_mr', 'bcc_esm1', 'cams_csm_1_0',              # China
        'canesm5', 'canesm5_canoe',                             # Canada
        'cesm2', 'cesm2_fv2', 'cesm2_waccm', 'cesm2_waccm_fv2', # USA
        'ciesm',                                                # China
        'cmcc_cm2_hr4', 'cmcc_cm2_sr5', 'cmcc_esm2',            # Italy
        'cnrm_cm6_1', 'cnrm_cm6_1_hr', 'cnrm_esm2_1',           # France
        'e3sm_1_0', 'e3sm_1_1', 'e3sm_1_1_eca',                 # USA
        'ec_earth3', 'ec_earth3_aerchem', 'ec_earth3_cc',
        'ec_earth3_veg', 'ec_earth3_veg_lr',                    # Europe
        'fgoals_f3_l', 'fgoals_g3','fio_esm_2_0',               # China
        'gfdl_esm4', 'giss_e2_1_g', 'giss_e2_1_h',              # USA
        'hadgem3_gc31_ll', 'hadgem3_gc31_mm',                   # UK
        'iitm_esm',                                             # India 
        'inm_cm4_8', 'inm_cm5_0',                               # Russia
        'ipsl_cm5a2_inca', 'ipsl_cm6a_lr',                      # France 
        'kace_1_0_g', 'kiost_esm',                              # South Korea 
        'mcm_ua_1_0',                                           # USA
        'miroc6', 'miroc_es2h', 'miroc_es2l',                   # Japan
        'mpi_esm_1_2_ham',                                      # Switzerland             
        'mpi_esm1_2_hr', 'mpi_esm1_2_lr',                       # Germany 
        'mri_esm2_0',                                           # Japan
        'nesm3',                                                # China
        'norcpm1', 'noresm2_lm', 'noresm2_mm',                  # Norway
        'sam0_unicon',                                          # South Korea
        'taiesm1',                                              # Taiwan?
        'ukesm1_0_ll')
CMIP6_RESOLUTIONS: tuple[str,...] = ('monthly', 'daily', 'fixed')
CMIP6_VARIABLES: tuple[str,...] = (
    "tas", "tasmax", "tasmin", # daily, monthly [K]
    "ts", # surface temperature, monthly [K]
    "psl", # sea level pressure, daily, monthly [Pa]
    "ps", # surface air pressure, monthly [Pa]
    "uas", "vas", # 10 m component of E, N wind, monthly [m/s]
    "sfcWind", # surface 10 m wind speed, daily, monthly [m/s]
    "hurs", # near-surface 2m relative humidity, monthly
    "huss", # near-surface 2m specific humidity, daily, monthly 
    "pr", # precipitation, daily, monthly [kg m-2 s-1]
    "prsn", # snowfall, monthly [kg m-2 s-1]
    "evspsbl", # evaporation, monthly [kg m-2 s-1]
    # add more from https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form
)

FILE_FORMATS: dict[str, str] = {
    '.nc': 'netcdf',
    '.grib': 'grib',
    '.zip': 'zip',
}
#endregion

@dataclass
class VariableData:
    '''Model variable data class.'''
    variable: str = Variables.TEMP
    '''CMIP6 Data variable.'''
    months: tuple[str,...] = MONTHS
    '''Months in yr to download.'''
    days: None|tuple[str,...] = None
    '''Days in month to download.'''
    time_step: str = TemporalResolutions.MONTHLY
    '''Temporal resolution of variable.'''
    location: tuple[int, int, int, int] = (1, 0, 0, 1) # [N, W, S, E]
    '''Bounding box location of data to download.'''

    def __post_init__(self):
        if self.days is not None and self.time_step != TemporalResolutions.DAILY:
            raise ValueError('Days are only valid for daily resolution.')
        if self.time_step == TemporalResolutions.FIXED:
            raise NotImplementedError('Fixed resolution not yet implemented.')
