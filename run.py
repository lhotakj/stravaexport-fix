#!/usr/bin/python3

#TODO: convert Activity type :)

import os
import os.path
import re
import subprocess
import glob
import csv
import collections

# CONSTANTS ------------------------------------
import sys

UNZIPPED_FOLDER = "unzipped"
STRAVA_ACTIVITIES_SUBFOLDER = "activities"
STRAVA_ACTIVITIES_FILE = "activities.csv"
# ----------------------------------------------


def unzip(file):
    import gzip
    import shutil
    print(file)
    with gzip.open(file, 'rb') as f_in:
        with open(file.lower().replace('.gz', ''), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            os.remove(file)

def exec_cmd(command):
    result = subprocess.Popen(command, shell=True)
    text = result.communicate()[0]
    print(text)
    return_code = result.returncode
    if return_code != 0:
        return False
    return True

def die(error):
    print("Error: " + error)
    quit()

def main():
    global UNZIPPED_FOLDER
    global STRAVA_ACTIVITIES_SUBFOLDER
    global STRAVA_ACTIVITIES_FILE

    strava_unzipped_folder = os.path.join(".", UNZIPPED_FOLDER)
    strava_unzipped_activities_folder = os.path.join(".", UNZIPPED_FOLDER, STRAVA_ACTIVITIES_SUBFOLDER)
    strava_unzipped_activities_file = os.path.join(".", UNZIPPED_FOLDER, STRAVA_ACTIVITIES_FILE)
    gpsbabel_command = "gpsbabel -w -t -i gtrnctr -f {filename_tcx} -o gpx,gpxver=1.1 -F {filename_gpx}"

    #check ----------------
    if not os.path.exists(strava_unzipped_folder):
        die("Folder with expected unzipped Strava archive '{path}' doesn't exits.".format(path=strava_unzipped_folder))

    if not os.path.exists(strava_unzipped_activities_folder):
        die("Folder with activities in unzipped Strava archive '{path}' doesn't exits.".format(path=strava_unzipped_activities_folder))

    if not os.path.isfile(strava_unzipped_activities_file):
        die("File with activities in unzipped Strava archive '{path}' doesn't exits.".format(path=strava_unzipped_activities_file))

    print("Reading '{path}'".format(path=strava_unzipped_activities_file));
    try:
        with open(strava_unzipped_activities_file, newline='\n', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            cnt = 0
            for row in reader:
                cnt += 1
            print("Found {cnt} activities ".format(cnt=str(cnt)))

    except Exception as ex:
        die("Cannot read '{path}'. {err}".format(path=strava_unzipped_activities_file, err=str(ex)))

    print("Unzipping ...");
    #sys.stdout.write("Progress: ")
    ucnt = 0
    for gz in glob.glob(os.path.join(strava_unzipped_activities_folder, "*.gz")):
        ucnt += 1
        #sys.stdout.write("{:2.0%}".format(ucnt / cnt))
        #sys.stdout.flush()
        unzip(os.path.join(strava_unzipped_activities_folder, gz))
        #sys.stdout.write("\b\b\b\b")
        #sys.stdout.flush()
    #sys.stdout.write("\n")

    for root, dirs, files in os.walk(strava_unzipped_activities_folder):
        for filename in files:
            extension = os.path.splitext(filename)[1][1:].strip().lower()

            # strip spaces from gpx
            if extension == "gpx":
                with open(os.path.join(strava_unzipped_activities_folder, filename), encoding='utf-8') as file:
                    content = file.read()
                    fixed = re.sub(r'>\s\s+<', '><', content).strip()
                    with open(filename, "w", encoding='utf-8') as filew:
                        filew.write(fixed)

            # strip spaces from tcx
            if extension == "tcx":
                with open(os.path.join(strava_unzipped_activities_folder, filename), encoding='utf-8') as file:
                    content = file.read()
                    fixed = re.sub(r'>\s\s+<', '><', content).strip()
                    with open(filename, "w", encoding='utf-8') as filew:
                        filew.write(fixed)
                        print(re.findall(r'<[Aa][Cc][Tt][Ii][Vv][Ii][Tt][Yy][ ]{1,}[Ss][Pp][Oo][Rr][Tt]="([^"]*)">', fixed))
                        # TODO: save artivity type #read from .activitues!

                    filename_gpx = filename.replace(".tcx", ".gpx")
                    rc = exec_cmd(gpsbabel_command.format(
                        filename_gpx=os.path.join(strava_unzipped_activities_folder, filename_gpx),
                        filename_tcx=os.path.join(strava_unzipped_activities_folder, filename))
                    )
                    if not rc:
                        print('error')


if __name__ == "__main__":
    main()





