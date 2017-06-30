import os

os.getcwd()
os.chdir('.')

try:
    lines = open('sketch.txt')

    for line in lines:
        try:
            (role, spoken) = line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(spoken, end='')
        except ValueError:
            pass

    lines.close()
except IOError:
    print('The data file is missing!')
