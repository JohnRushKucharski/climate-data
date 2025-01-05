'''
CDS CMIP6
Laos Monthly Temperature
'''
from pathlib import Path
print(Path.cwd())

import climate_data.cds_request as cds
from climate_data.countries import get_country_bounding_box

# Laos bounding box
LAOS_BBOX = get_country_bounding_box("Laos")
directory = cds.cmip6_directory(
    base_directory='G:/My Drive/data/gcms',
    variable=cds.CMIP6Variables.TEMP.value,
    resolution=cds.CMIP6Resolutions.MONTHLY.value)
file_name = cds.name_cmip6_file(
    model=cds.CMIP6Models.ACCESS_CM2.value,
    yrs=cds.HISTORY_YEARS,
    mos=cds.MONTHS,
    ext=cds.FileFormats.NETCDF.value
)

cds.small_monthly_request(
    dataset=cds.CMIP6_DATASET,
    experiment=cds.CMIP6Experiments.HISTORICAL.value,
    model=cds.CMIP6Models.ACCESS_CM2.value,
    variable=cds.CMIP6Variables.TEMP.value,
    months=cds.MONTHS, years=cds.HISTORY_YEARS,
    area=LAOS_BBOX,
    file_path=f'{directory}/{file_name}',
    overwrite=True
)
