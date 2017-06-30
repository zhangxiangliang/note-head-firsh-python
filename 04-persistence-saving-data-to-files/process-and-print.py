import os

man = []
other = []

try:
    lines = open('../dealing-with-errors/sketch.txt')
    for line in lines:
        try:
            (role, spoken) = line.split(":", 1)
            if role == 'Man':
                man.append(spoken)
            elif role == 'Other Man':
                other.append(spoken)
        except ValueError:
            pass
    lines.close()
except IOError:
    print('The datafile is missing!')

print(man)
print(other)
