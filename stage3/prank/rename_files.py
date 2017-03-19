import os
path = "/home/carl/Projects/udacity_projects/stage3/prank/prank/"
file_list = os.listdir("/home/carl/Projects/udacity_projects/stage3/prank/prank")

for file in file_list:
    os.rename(path+file, path+file.translate(None, "1234567890"))