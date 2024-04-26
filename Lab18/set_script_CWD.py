import os
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Get path of current file
# print(__file__)
script_name= os.path.basename(__file__)
script_dir= os.path.dirname(__file__)

print(f'Script name: {script_name}' )
print(f'Script dir: {script_dir}' )


# set CWD:
os.chdir(script_dir)

with open('./Data/example.txt') as f:
    content = f.read()

print(content)