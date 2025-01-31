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

**CMIP6Request**. The following code builds a *CMIP6Request* (named *small_request* in the code below). This request is used to download 2 years of monthly near-surface air temperture data from a CMIP6 experiment-model pair (i.e. historical- ACCESS_CM2) within a bounding box around 1N, 1W, 0S, 1E degrees latitude and longitude from the CDS API, using the **CMIP6Request.download(...)** function in the **climate-data.copernicus.request** module.

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

**climate-data.copernicus.cmip6**. The *climate-data.copernicus.cmip6* module provides acceptable values for the most of the CDS API request parameters (i.e. experiment, model, variable names, etc.).

**climate_data.countries**. The *climate_data.countries* module includes boundary boxes for nearly every country on the planet. The *get_country_boundary_box(...)* function is used to get a bounding box of latitude and longitude coordinates. A cartoon representation of the bounding box coordinates for the country of Laos is displayed below. 

```
 ,--23--,
 | L    |
 |  A  108
100  O  |
 |    S |
 '--13--'
```
The boundary box described above is represented in the program (through the **get_country_boundary_box(...)** function) as a tuple of N, W, S, E latitudes and longitudes: i.e., (23, 100, 13, 108).

**build_CMIP6Requests(...)** The *build_CMIP6Requests(...)* function, in the *climate-data.copernicus.request* module returns a list of *CMIP6Requests*. It is used to request multiple data variables, models, experiments, etc.

**download_requests(...)** The *build_CMIP6Requests* and *download_requests(...)* functions in the codeblock below expand on the *small_request* created in the previous example to include a second general circulation model (GCM), i.e. ACCESS_ESM1_5. The *get_country_boundary_box* also modifies the location of the previous *small_request* example (as described above). 

```python
from climate_data.countries import get_country_bounding_box

LAOS_BBOX = get_country_bounding_box("Laos") 
# returns (23, 100, 13, 108)

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

**dowload_requests(requests, base_directory, ...)**. The data cooresponding to each *CMIP6Request* in the *requests* list is downloaded as a seperate .zip file. Starting from the *base_directory* parameter the generic file heirarchy displayed below is built for the provided list of requests (provided that this file heirarchy does not already exist).

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
**Folder structure**. In this diagram <variable_i> refers to the name of a requested variable, <timestep_i> refers to the requested temporal resolution (i.e. monthly, daily). The downloaded .zip files for each request is stored in the corresponding .zip folder. 

**File structure**. During the download routine compressed netCDF files in each of the downloaded .zip files are extracted to the parent directory. These extracted files follow a **model_exp_end_date-start_date.nc** file naming convention (displayed in the diagram above). "model" and "exp" in this convention refer to the names of the requested model and CMIP6 experiment (i.e. historical, ssp585, etc.), respectively. The "end_date-start_date" parts refer to the latest and earliest years, months (and for daily request days) in the request, recorded in YYYYMMDD format.

## Planned Development
Future versions will expand the climate-data programs functionality to other datasets (i.e. ERA5 reanalysis data) and APIs.