class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return (sorted(set([self.sanitize(t) for t in self]))[0:3])

    def sanitize(self, timer):
        if '-' in timer: splitter = '-'
        elif ':' in timer: splitter = ':'
        else: return(timer)
        (mins, secs) = timer.split(splitter)
        return mins + '.' + secs

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return (AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print("File error:" + str(ioerr))
        return (None)

# lyon = AthleteList('Lyon Zhang')
# lyon.append('1.31')
# lyon.extend(['1.33', '9.99', '5.7'])
# print(lyon.top3())

james = get_coach_data('james.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))
