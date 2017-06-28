# format time string
def sanitize(time_string):
    if '-' in time_string: splitter = '-'
    elif ':' in time_string: splitter = ':'
    else: return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)


# get coach data list
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))

# get data
james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

# print
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
