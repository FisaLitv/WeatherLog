import sqlite3 as sl


def initDb(name):
    con = sl.connect(name + '.db')
    # TODO save to file
    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS DATA (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                datetime INTEGER,
                temperature REAL,
                humidity, INTEGER,
                wind REAL,
                pressure INTEGER
            );
        """)
    return con


class WeatherDbHandle:
    def __init__(self, name):
        self.con = initDb(name)

    def insertData(self, temperature, humidity, wind_speed, pressure, now):
        ts = int(now.timestamp())
        sql = 'INSERT INTO DATA (datetime, temperature, humidity, wind, pressure) ' \
              'values(?, ?, ?, ?, ?)'
        data = [ts, temperature, humidity, wind_speed, pressure]
        with self.con:
            self.con.execute(sql, data)


