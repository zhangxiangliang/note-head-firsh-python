import pickle

man = ['xiaoer', 'xiaosi']
other = ['xiaobo', 'heizi']

try:
    with open('man.txt', 'wb') as man_file, open('other.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error: ' + str(err))
except PickleError as perr:
    print('Pickling error: ' + str(perr))
