man = []
other = []

try:
    with open('man.txt', 'w') as man_file, open('other.txt', 'w') as other_file:
        print(man, file=man_file)
        print(other, file=other_file)
except IOError as err:
    print('File error: ' + err)
