import os

os.getcwd() # get current working directory
os.chdir('.') # change directory

lines = open('sketch.txt')

for line in lines:
    try:
        (role, spoken) = line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(spoken, end='')
    except:
        pass

lines.close()
