import shutil 
import os.path

# Creating the ZIP file 
archived = shutil.make_archive('/results/', 'zip', '/results')

if os.path.exists('/results.zip'):
   print(archived) 
else: 
   print("ZIP file not created")