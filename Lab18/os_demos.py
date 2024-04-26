import os

# Get os name
# print( os.name )
# if os.name=='posix':
#     print('Linux')
# else:
#     print('Windows')

# --------------------------------- Get CWD: --------------------------------- #
# cwd = os.getcwd()
# print("Current Working Directory:", cwd)


# set CWD:
# os.chdir(script_dir)

# ------------------------- Working with directories ------------------------- #
### List entries:
# contents = os.listdir()
# # print(contents)
# for entry in contents:
#     if os.path.isfile(entry):
#         print(entry)

### Create directory
# os.mkdir('Data/Audio')
# os.makedirs('Data/Audio/mp3/')

### Delete directory
# os.rmdir('Data/Audio/mp3/')

# TODO: why not remove whole tree?
# import shutil
# shutil.rmtree('Data/Audio/mp3')


# ------------------------------ os.path module ------------------------------ #
# path1 = 'parent/file.ext'
# print(os.path.dirname(path1))

# path1 = 'parent'
# path2 = 'test.txt'
# print( os.path.join(path1, path2, 'file.mp3') )

# script_folder = os.path.dirname(__file__)
# print(f'script_dir: {script_folder}')

# audio_folder_path = 'Audio/np3'



# print(os.environ['PATH'])

