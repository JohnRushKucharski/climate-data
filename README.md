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
climate-data is intended use is as a library. 

## Planned Development
Future versions will expand the climate-data programs functionality to other datasets (i.e. ERA5 reanalysis data) and APIs.