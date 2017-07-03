from google.appengine.ext import db

class Sighting(db.Model):
    data = db.DateProperty()
    time = db.TimeProperty()
    name = db.StringProperty()
    email = db.StringProperty()
    location = db.StringProperty()
    fin_type = db.StringProperty()
    wave_type = db.StringProperty()
    blow_type = db.StringProperty()
    whale_type = db.StringProperty()
