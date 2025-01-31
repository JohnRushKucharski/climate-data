# climate-data

Facilitates downloading and analyzing CMIP6&dagger; data through the **Copernicus Climate Data Service** Application Programing Interface (CDS API). 

## Installation Instructions

**CDS API personal token set up:** Use of the CDS API requires a personal access token. Instructions can be found here: [https://cds.climate.copernicus.eu/how-to-api](https://cds.climate.copernicus.eu/how-to-api).

**Clone or fork climate-data code from GitHub:** The hydropattern source code is stored on the following GitHub repository: [https://github.com/JohnRushKucharski/climate-data](https://github.com/JohnRushKucharski/climate-data) is available under the GNU Version 3 General Public License.

It can be cloned or forked by following the normal cloning or forking instructions, which are available here: [cloning-a-repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) and here: [fork-a-repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

**Poetry installation:**
The climate-data program is developed using Poetry, which can simply the installation process.

To install Poetry, follow the instructions here: https://python-poetry.org/docs/.

Once Poetry is installed, use your favorite shell to go to the location of the local hydropattern repository,

```shell
cd <PATH_TO_LOCAL>\hydropattern
```

then run:

```shell
poetry install
```

This creates a python virtual environment containing climate-data dependencies, without affecting your system's global python environment.

## Basic Usage
climate-data is intended use is as a library within a python script (or jupyter notebook). 

The following code builds a *CMIP6Request* named *small_request*. This request is used to download (using the *CMIP6Request.download* function) 2 years of monthly near-surface air temperture data from a CMIP6 experiment-model pair (i.e. historical- ACCESS_CM2) within a bounding box around 1N, 1W, 0S, 1E degrees latitude and longitude from the CDS API.

```python
import climate_data.copernicus.cmip6 as cmip6
import climate_data.copernicus.request as cds

small_request = cds.CMIP6Request(
    model = cmip6.Models.ACCESS_CM2,
    experiment = cmip6.Experiments.HISTORICAL,
    years = cmip6.HISTORY_YEARS[0:2],
    location = (1, 0, 0, 1),
    variable = cmip6.Variables.TEMP,
    time_step = cmip6.TemporalResolutions.MONTHLY,
    months = cmip6.MONTHS
)

basedir = "C:/data/gcms/"
small_request.download(
    directory=small_request.create_directories(basedir)
)
```

The *climate-data.copernicus.cmip6* module provides acceptable values for the most of the possible CDS API request parameters (i.e. experiment, model, variable names, etc.).

The *climate_data.countries* module includes boundary boxes for nearly every country on the planet. The *get_country_boundary_box* function is used to get a bounding box of latitude and longitude coordinates. A cartoon representation of the bounding box coordinates for the country of Laos is displayed below. The *get_country_boundary_box* function in the program returns this boundary box as N, W, S, E latitue longitude tuple: i.e., (23, 100, 13, 108).

```
 ,--23--,
 | L    |
 |  A  108
100  O  |
 |    S |
 '--13--'
```

The *build_CMIP6Requests* function, in the *climate-data.copernicus.cmip6* module returns a list of *CMIP6Requests*. It is used to request multiple of data variables, models, experiments, etc.

In the codeblock below the *build_CMIP6Requests* and *download_requests* functions expands the *small_request* created in the previous example to include a second general circulation model (GCM). Meanwhile the *get_country_boundary_box* changes modifies the location of the request. 

```python
from climate_data.countries import get_country_bounding_box

LAOS_BBOX = get_country_bounding_box("Laos") # returns (23, 100, 13, 108)

laos2model_requests = cds.build_CMIP6Requests(
    location=LAOS_BBOX,
    variables=[cmip6.Variables.TEMP],
    timesteps=[cmip6.TemporalResolutions.MONTHLY],
    models=[cmip6.Models.ACCESS_CM2, cmip6.Models.ACCESS_ESM1_5],
    experiments=[cmip6.Experiments.HISTORICAL],
    years=cmip6.HISTORY_YEARS[0:2]
)

cds.download_requests(
    requests = small_requests2,
    base_directory = basedir
)
```

The data cooresponding to each *CMIP6Request* is downloaded as a seperate .zip file. From the *base_directory* parameter in the *download_requests* function the generic file heirarchy displayed below built for the list of requests (provided that it does not already exist). In this diagram <variable_*> refers to the name of a requested variable, <timestep_*> refers to the requested temporal resolution (i.e. monthly, daily). The downloaded .zip files for each request is stored in the appropriate .zip folder. 

```
base_directory
|
+--cmip6
|  |
|  +--<variable_1>
|  |   |
|  |   +--<timestep_1>
|  |   |   *<model>_<exp>_<end_date>-<start_date>.nc
|  |   |   * ...
|  |   |   \ zip
|  |   +--<timestep_2>
|  |   |   * ...
|  |   |   \ zip
|  |   +-- ...
|  +--<variable_2>
|  |    ...
|  +-- ...
|  |
|  \__<variable_n>
```
As part of the downloading routine the compressed netCDF files contained in each of the downloaded .zip files are extracted to the parent directory. These extracted files following the <model>_<exp>_<end_date>-<start_date>.nc file naming convention shown in the diagram above. In this convension <model> and <exp> refer to the names of the requested model and CMIP6 experiment (i.e. historical, ssp585, etc.) respectively. The <end_date>-<start_date> parts refer to the latest and earliest years, months (and for daily request days) in the request, recorded in YYYYMMDD format.


## Planned Development
Future versions will expand the climate-data programs functionality to other datasets (i.e. ERA5 reanalysis data) and APIs.