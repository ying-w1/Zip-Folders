import os
import zipfile

provideDir = input("Provide directory to zip: ")

path = provideDir
path = os.path.abspath(os.path.normpath(os.path.expanduser(path)))

# Zip each folder in the directory 
for folder in os.listdir(path):
    if os.path.isdir(folder):   
        zipf = zipfile.ZipFile('{0}.zip'.format(os.path.join(path, folder)), 'w', zipfile.ZIP_DEFLATED)
        
        for root, dirs, files in os.walk(os.path.join(path, folder)):
            for filename in files:
                zipf.write(os.path.abspath(os.path.join(root, filename)), arcname=filename)
        
        zipf.close()
