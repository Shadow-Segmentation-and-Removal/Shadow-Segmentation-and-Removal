import shutil 
import os.path

# Creating the ZIP file 
archived = shutil.make_archive('/teamspace/studios/this_studio/ShadowFormer/results', 'zip', '/teamspace/studios/this_studio/ShadowFormer/results')

if os.path.exists('/teamspace/studios/this_studio/ShadowFormer/results.zip'):
   print("Zipped!") 
else: 
   print("ZIP file not created")