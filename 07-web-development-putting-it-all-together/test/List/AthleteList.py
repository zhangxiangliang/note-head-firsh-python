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
        else: return(float(timer))
        (mins, secs) = timer.split(splitter)
        return (float(mins + '.' + secs))
