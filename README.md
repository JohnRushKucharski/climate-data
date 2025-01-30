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

The following code builds a request (i.e. *small_request*) for 2 years of simulated monthly near-surface air temperture data from a single CMIP6 experiment-model pair in a box around 1N, 1W, 0S, 1E degrees latitude and longitude and downloads it from the CDS API.

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

The *climate-data.copernicus.cmip6* module provides constants of acceptible values for the many of the request parameters.

In the codeblock below the *get_country_boundary_box* function from the *climate_data.countries* module is used to get a bounding box of latitude and longitude coordinates for the country of Laos. This bounding box is used to modify the *small_request* from the previous example, using the *build_CMIP6Requests* function in the codeblock below.

The *build_CMIP6Requests* and *download_requests* functions used the codeblock below are used to expand *small_request* in the previous example to a second general circulation model (GCM). This function can also be use to request additional data variables, experiments, etc.

```python
from climate_data.countries import get_country_bounding_box

laos2model_requests = cds.build_CMIP6Requests(
    location=LAOS_BBOX,
    variables=[cmip6.Variables.TEMP],
    timesteps=[cmip6.TemporalResolutions.MONTHLY],
    models=[cmip6.Models.ACCESS_CM2, cmip6.Models.ACCESS_ESM1_5],
    experiments=[cmip6.Experiments.HISTORICAL],
    years=cmip6.HISTORY_YEARS[0:2]
)

cds.download_requests(
    small_requests2, basedir
)
```

## Planned Development
Future versions will expand the climate-data programs functionality to other datasets (i.e. ERA5 reanalysis data) and APIs.