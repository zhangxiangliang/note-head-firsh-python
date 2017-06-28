import os

man = []
other = []

try:
    lines = open('../dealing-with-errors/sketch.txt')

    for line in lines:
        try:
            (role, spoken) = line.split(':', 1)
            if role == 'Man':
                man.append(spoken)
            elif role == 'Other Man':
                other.append(spoken)
        except ValueError:
            pass
    lines.close()
except IOError:
    print('The datafile is missing!')

try:
    man_file = open('man.txt', 'w')
    other_file = open('other.txt', 'w')
    print(man, file=man_file)
    print(other, file=other_file)
except IOError:
    print('File writing error.')
finally:
    man_file.close()
    other_file.close()
