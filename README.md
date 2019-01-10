# STRAVA export fix
Simple Python script to unzip any GZ archives and convert `tcx` activities to the unified `gpx` format. After the conversion the tool updates your `activities.csv` filenames accordingly, the tool can be safely executed on the already converted activities.

## Requirements
- *GPSbabel*:
  - RHEL/Centos `sudo yum install gpsbabel`
  - Ubuntu `sudo apt-get install gpsbabel`
  - Windows: [download](https://www.gpsbabel.org/download.html) and mare sure the script can reach path or copy the `gpsbabel.exe` to the repo root
- *Python 3.4+* (tested on Windows and Linux)
- Strava archive file containing folder `activites.csv` and folder `activities` with individual files.

## How to get all Strava tracks?
- Login to [strava.com](https://www.strava.com/)
- Go to your profile, click [My Account](https://www.strava.com/account), click [Download or Delete Your Data](https://www.strava.com/athlete/delete_your_account) then `Get Started` button. Don't worry nothing gets deleted.
- Under point 2 click button `Request Your Archive`.
- You should receive within an email within a few hours with a link to your ZIP archive
- Download the archive 

## How to use this tool
- Clone this repository
- Unzip thee strava zip file into `unzipped` folder
- You may see in the folder miscellaneous file extensions `.tcx`, `.tcx.gz` or `.gpx.gz` files, eg.
```
$ cd /home/jarda/WORKING/
$ clone https://github.com/lhotakj/stravaexport-fix.git
...
$ unzip <your-downloaded-archive -d ./unzipped
...
$ cd ./stravaexport-fix/unzipped/activities/
$ ls
1008247839.gpx  1019050643.gpx  1022095894.gpx.gz  1029478699.gpx.gz  1440081027.tcx.gz  1440081322.tcx.gz  1440081476.tcx.gz
```

- Run `./run.py` or eg. `C:\Python37\python run.py` under Windows
- You should be getting the following progress:
```
$ ./run.py
Reading './unzipped/activities.csv'
Found <number> activities
Unzipping ...
Progress:  100%
Normalizing ...
./unzipped/activities/1008247839.gpx    | Ride         | <activity name>
./unzipped/activities/1019050643.gpx    | Walk         | <activity name>
...
...
./unzipped/activities/1022095894.gpx    | Ride         | <activity name>
./unzipped/activities/1029478699.gpx    | Ride         | <activity name>
./unzipped/activities/1440081027.gpx    | Ride         | <activity name>
Backing up the original activities as './unzipped/activities.csv.original' ...
Saving new activities ...
```
- All your activities in `activities` folder are now in `.gpx` format

## Future development
- Adding name and activity type to converted `.tcx` files - coming soon
- Better error handling
- Export the activities to XLS(X) files
- Parametrized execution

## Known issues
- None :) If you encounter any issue, feel free to report it in the GitHub issues.

