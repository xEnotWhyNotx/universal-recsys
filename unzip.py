import zipfile
import os

zip_file = "test_dataset__.zip"

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall()
#os.remove(zip_file)