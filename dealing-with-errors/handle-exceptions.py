import os

os.getcwd() # get current working directory
os.chdir('.') # change directory

lines = open('sketch.txt')

# split 分割字符串
# find  查找字符串

for line in lines:
    try:
        (role, spoken) = line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(spoken, end='')
    except:
        pass
