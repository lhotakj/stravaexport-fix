# STRAVA export fix
Simple Python script to convert strava `TCX` files to `GPX` (using `gpsbabel`)

## How to get all Strava tracks?
- Go to your profile, click `My Account`, click `Download or Delete Your Data` then `Get Started` button. Don't worry nothing gets deleted! ;) 
- Under point 2 click button `Request Your Archive`.
- You'll receive within a few hours an email with a link to a ZIP file. 
- Download it and unzip into `unzipped` folder
- *voila* here are your files, but some of them may be Gzipped and in TCX file. 
- To convert all your activities to `GPX` format just run `run.py`
 
## Requirements
- GPSbabel:
  - RHEL/Centos `sudo yum install gpsbabel`
  - Ubuntu `sudo apt-get install gpsbabel`
  - Windows: download [here|https://www.gpsbabel.org/download.html] and mare sure the script can reach path
- Python 3.6+



