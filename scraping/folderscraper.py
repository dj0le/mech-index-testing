
import os
import csv

# set path for image folder
path = '/home/djole/python-dev/mech-index/sql_app/static/mech_thumbnails/'


# use scandir to find all image names and write them to csv
with open('mech_images.csv', 'w') as output:
    writer = csv.writer(output)
    for file in os.scandir(path):
        writer.writerow([file.name])

# use listdir to change the name of all the files in a folder
# for filename in os.listdir(path):
#     new_filename = 'small_' + filename
#     os.rename(os.path.join(path, filename), os.path.join(path, new_filename))




        