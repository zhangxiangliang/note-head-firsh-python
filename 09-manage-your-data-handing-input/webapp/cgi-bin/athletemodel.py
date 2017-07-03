
import pickle
import sqlite3

from athletelist import AthleteList

db_name = 'data/coachdata.sqlite'

def get_names_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("SELECT name FROM athletes")
    response = [row[0] for row in results.fetchall()]
    connection.close()
    return(response)

def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name,id FROM athletes""")
    response = results.fetchall()
    connection.close()
    return(response)

def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("SELECT name, dob FROM athletes WHERE id=?", (athlete_id,))
    (name, dob) = results.fetchone()

    results = cursor.execute("SELECT value FROM timing_data WHERE athlete_id=?", (athlete_id,))
    data = [row[0] for row in results.fetchall()]

    response = {
        'name': name,
        'dob': dob,
        'data': data,
        'top3': data[0:3]
    }

    connection.close()
    return (response)

def update_athlete_timing_from_id_and_timer(id, timer):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)", (id, timer))
    connection.commit()
    connection.close()
