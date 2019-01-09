# STRAVA export fix
Simple Python script to convert strava `TCX` files to `GPX` (using `gpsbabel`)

## How to get all Strava tracks?
- Login to Strava
- Go to your profile, click `[My Account](https://www.strava.com/account)`, click `[Download or Delete Your Data](https://www.strava.com/athlete/delete_your_account)` then `Get Started` button. Don't worry nothing gets deleted.
- Under point 2 click button `Request Your Archive`.
- You should receive within an email within a few hours with a link to your ZIP archive
- Download it and unzip into `unzipped` folder
- *Voila* here are your files, but some of them may be Gzipped and in TCX file. 
- To convert all your activities to `GPX` format just run `run.py`
 
## Requirements
- *GPSbabel*:
  - RHEL/Centos `sudo yum install gpsbabel`
  - Ubuntu `sudo apt-get install gpsbabel`
  - Windows: [download](https://www.gpsbabel.org/download.html) and mare sure the script can reach path or copy the `gpsbabel.exe' to the repo root
- *Python 3.6+* (tested on Windows / Linux)



