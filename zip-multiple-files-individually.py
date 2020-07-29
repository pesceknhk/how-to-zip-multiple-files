from zipfile import ZipFile
import sys
import io
import os
from os.path import basename

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


def zipfilesindir(dirname, zipfilename):
    # create a zipfile object
    zipobj = ZipFile(zipfilename, 'w')
    filepath = os.path.join(foldername, filename)
    # add file to zip
    try:
        print(f"Zipping {filepath}...")
        zipobj.write(filepath, basename(filepath))
        print(f"Done {filepath}...")
        zipobj.close()
    except UnicodeEncodeError:
        print(f"Failed zipping {filepath}...")
        zipobj.close()
    except:
        print(f"Failed zipping {filepath}...")


print('Calling zipfilesindir function ....')
# give the complete folder/subfolder path
l_dirname = 'C:\\Users\\hemanth.nanjundappa\\logs'
whats_the_count = 0
# loop each files in the l_dirname
for foldername, subfolders, filenames in os.walk(l_dirname):
    l_foldername = foldername
    for filename in filenames:
        whats_the_count += 1
        try:
            l_zipname = filename + '.zip'
        except UnicodeEncodeError:
            l_zipname = 'xxxxxxxxxxxxx'
        # call the zipfilesindir function for each file
        zipfilesindir(l_foldername, l_zipname)
        print(f"So far count is: {whats_the_count}")

print(f"Final count is: {whats_the_count}")
