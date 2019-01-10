# STRAVA export fix
Simple Python script to unzip and convert strava `TCX` files to the unified `GPX` format (using `gpsbabel`)

## Requirements
- *GPSbabel*:
  - RHEL/Centos `sudo yum install gpsbabel`
  - Ubuntu `sudo apt-get install gpsbabel`
  - Windows: [download](https://www.gpsbabel.org/download.html) and mare sure the script can reach path or copy the `gpsbabel.exe' to the repo root
- *Python 3.4+* (tested on Windows / Linux)

## How to get all Strava tracks?
- Login to [strava.com](https://www.strava.com/)
- Go to your profile, click [My Account](https://www.strava.com/account), click [Download or Delete Your Data](https://www.strava.com/athlete/delete_your_account) then `Get Started` button. Don't worry nothing gets deleted.
- Under point 2 click button `Request Your Archive`.
- You should receive within an email within a few hours with a link to your ZIP archive
- Download the archive 

## How to use this tool
- Clone this repository
- Unzip thee strava zip file into `unzipped` folder
- run `./run.py`

 




