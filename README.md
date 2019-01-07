# STRAVA export fix
Simple Python script to convert strava TCX files to GPX (using gpsbabel)

## How to get all Strava tracks?
- Go to your profile, click `My Account`, click `Download or Delete Your Data` then `Get Started` button. Don't worry nothing gets deleted! ;) 
- Under point 2 click button `Requesy Your Archive`.
- You'll receive within a few hours an email with a link to a ZIP file. 
- Download it and unzip
- Go to folder `activities`
- *voila* here are your files, but some of them may be Gzipped and in TCX file. 

This script will normalized all of them to GPX v1.1 which is compatible with Karita

 
## Requirements
- GPSbabel:

RHEL/Centos `sudo yum install gpsbabel`
Ubuntu `sudo apt-get install gpsbabel`

- Python 2.7+

