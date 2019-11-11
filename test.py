from shutil import make_archive
import os
source = os.path.join( os.getcwd() , 'myarchive')
target = os.path.join( os.getcwd() , 'categories')
print(make_archive(source , 'zip' , target))


