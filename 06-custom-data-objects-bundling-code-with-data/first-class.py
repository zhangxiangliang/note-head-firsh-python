class Athlete:
    def __init__(self, name, dob=None, times=[]):
        self.name = name
        self.dob = dob
        self.times = times
    def top3(self):
        return(self.sortlist())
    def last3(self):
        return(self.sortlist(True))
    def sortlist(self, reverse=False):
        return(sorted(set([sanitize(t) for t in self.times]),reverse=reverse)[0:3])
    def add_time(self, time_value):
        self.add_times([time_value])
    def add_times(self, list_of_times):
        self.times.extend(list_of_times)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return Athlete(temp.pop(0), temp.pop(0), temp)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

def sanitize(time_string):
    if '-' in time_string: splitter = '-'
    elif ':' in time_string: splitter = ':'
    else: return(float(time_string))
    (mins, secs) = time_string.split(splitter)
    return(float(mins + '.' + secs))

# james = get_coach_data('james.txt')
# print(james.name + "'s fastest times are: " + str(james.top3()))

lyon = Athlete('Lyon Zhang')
lyon.add_time('1.31')
lyon.add_times(['1.33', '19.88', '5.11'])
print(lyon.top3())
print(lyon.last3())
