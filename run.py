#!/usr/bin/python3

#TODO: convert Activity type :)

import os
import os.path
import re
import subprocess
import glob


def unzip(file):
    import gzip
    import shutil
    with gzip.open(file, 'rb') as f_in:
        with open(file.lower().replace('.gz',''), 'wb') as f_out:
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


def main():

    target = "."
    gpsbabel_command = "gpsbabel -w -t -i gtrnctr -f {filename_tcx} -o gpx,gpxver=1.1 -F {filename_gpx}"

    print("Unzipping ...");

    for gz in glob.glob(os.path.join(target, "*.gz")):
        unzip(gz)

    for root, dirs, files in os.walk(target):
        for filename in files:
            extension = os.path.splitext(filename)[1][1:].strip().lower()

            # strip spaces from gpx
            if extension == "gpx":
                with open(filename, encoding='utf-8') as file:
                    content = file.read()
                    fixed = re.sub(r'>\s\s+<', '><', content).strip()
                    with open(filename, "w", encoding='utf-8') as filew:
                        filew.write(fixed)

            # strip spaces from tcx
            if extension == "tcx":
                with open(filename, encoding='utf-8') as file:
                    content = file.read()
                    fixed = re.sub(r'>\s\s+<', '><', content).strip()
                    with open(filename, "w", encoding='utf-8') as filew:
                        filew.write(fixed)
                        print(re.findall(r'<[Aa][Cc][Tt][Ii][Vv][Ii][Tt][Yy][ ]{1,}[Ss][Pp][Oo][Rr][Tt]="([^"]*)">', fixed))
                        # TODO: save artiviyty type #read from .activitues!

                    filename_gpx = filename.replace(".tcx", ".gpx")
                    rc = exec_cmd(gpsbabel_command.format(filename_gpx=os.path.join(target, filename_gpx),\
                                                          filename_tcx=os.path.join(target, filename)))
                    if not rc:
                        print('error')


if __name__ == "__main__":
    main()





