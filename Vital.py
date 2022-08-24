from kivy.app import App
from time import strftime
from kivy.clock import Clock
import sqlite3


class VitalApp(App):
    # "'Vital'App" Will refer to name of .kv file (make sure they match)
    sw_seconds=0
    sw_started = False
    #stopwatch not started


    def update_time(self,nap):
        if self.sw_started:
            self.sw_seconds+=nap
        # if stopwatch is started (true), nap argument will increment time
        minutes, seconds = divmod(self.sw_seconds, 60)
        # to display minute and seconds appropriately. Since sw_seconds starts at 0 and increments +1 each seconds. if 125s. (125/60) tuple of (2,5) will display 2 minutes and 5 seconds.
        part_seconds = seconds * 100 % 100
        # hundreths of a second
        self.root.ids.stopwatch.text = f'{int(minutes):02}:{int(seconds):02}.[size=40]{int(part_seconds):02}[/size]'
        self.root.ids.time.text=strftime('[b]%H[/b]:%M:%S')
        # python documentation to display time (now)
        # Since function is looping every second, the time is updated every second

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)
        # starts clock
        # refers to function update_time, then updates self.root.ids.time.text=strftime('[b]%H[/b]:%M:%S')
        # 0 to start right away without delay

    def start_stop(self):
        self.sw_started = not self.sw_started
        self.root.ids.start_stop = 'Start' if \
            self.sw_started else 'Stop'

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text='Start'
            self.sw_started = False
        self.sw_seconds=0

    def progress_entry(self):
        print(strftime('%H:%M:%S ') + self.root.ids.progress.text)
        self.root.ids.progress.text=""

    def hr_entry(self):
        hr= 'HR: '
        if self.root.ids.hr.text != hr:
            print(strftime('%H:%M:%S ') + self.root.ids.hr.text)
            self.root.ids.hr_monitor.text = ('HR ' + self.root.ids.hr.text[4:])
        else:
            pass
        self.root.ids.hr.text = hr

    def bp_entry(self):
        bp= 'BP: '
        if self.root.ids.bp.text != bp:
            print(strftime('%H:%M:%S ') + self.root.ids.bp.text)
            self.root.ids.bp_monitor.text = ('BP ' + self.root.ids.bp.text[4:])
        else:
            pass
        self.root.ids.bp.text = bp

    def o2_entry(self):
        o2= 'O2: '
        if self.root.ids.o2.text != o2:
            print(strftime('%H:%M:%S ') + self.root.ids.o2.text)
            self.root.ids.o2_monitor.text = ('O2 ' + self.root.ids.o2.text[4:])
        else:
            pass
        self.root.ids.o2.text = o2

    def rr_entry(self):
        rr= 'RR: '
        if self.root.ids.rr.text != rr:
            print(strftime('%H:%M:%S ') + self.root.ids.rr.text)
            self.root.ids.rr_monitor.text = ('RR ' + self.root.ids.rr.text[4:])
        else:
            pass
        self.root.ids.rr.text = rr

    def temp_entry(self):
        temp= 'Temp: '
        if self.root.ids.temp.text != temp:
            print(strftime('%H:%M:%S ') + self.root.ids.temp.text)
            self.root.ids.temp_monitor.text = ('Temp ' + self.root.ids.temp.text[5:])
        else:
            pass
        self.root.ids.temp.text = temp


    def vital_entry(self):
        # button pressed, adds data entry to database

        connection = sqlite3.connect('data.db')
        # if database does not exist, it will be created

        cursor = connection.cursor()
        print("Database connection successful")
        # to create a table cursor object is used

        # id INTEGER Primary KEY ASC allows id to be created in ascending order. 1 -> 2 -> 3...
        # so when referring to any data we can refer to the id of that data entry
        cursor.execute('''CREATE TABLE IF NOT EXISTS data
                        (id INTEGER Primary KEY ASC, Time TEXT, HR TEXT, BP TEXT, O2 TEXT, RR TEXT, TEMP TEXT)''')
        # CREATE TABLE Query. This creates the table with column names and data types

        # connection.commit()
        # commits the data being sent to database



        #print(strftime('%H:%M:%S ') + self.root.ids.hr_monitor.text)
        #print(strftime('%H:%M:%S ') + self.root.ids.bp_monitor.text)
        #print(strftime('%H:%M:%S ') + self.root.ids.o2_monitor.text)
        #print(strftime('%H:%M:%S ') + self.root.ids.rr_monitor.text)
        #print(strftime('%H:%M:%S ') + self.root.ids.temp_monitor.text)

        # above prints out the vitals


        Time = strftime('%H:%M:%S')
        HR = self.root.ids.hr_monitor.text
        BP = self.root.ids.bp_monitor.text
        O2 = self.root.ids.o2_monitor.text
        RR = self.root.ids.rr_monitor.text
        Temp= self.root.ids.temp_monitor.text

        #vitals=(Time, HR, BP, O2, RR, Temp)

        cursor.execute('''INSERT INTO data (Time, HR, BP, O2, RR, TEMP)
                        VALUES(?,?,?,?,?,?)''', (Time, HR, BP, O2, RR, Temp))

        # cursor.execute(query_insert)

        connection.commit()
        connection.close()
        # commit and close are required to complete addition to database

    def recall(self):
        # to callback entries in database
        connection = sqlite3.connect('data.db')
        # if database does not exist, it will be created
        cursor = connection.cursor()

        cursor.execute('''SELECT Time,HR,BP FROM data''')
        # executes SQL line
        recall1= cursor.fetchall()

        for row in recall1:
            print('{0} : {1}, {2}'.format(row[0],row[1],row[2]))
        # for loop to display database info

        print(recall1)

        connection.commit()
        connection.close()

    def delete(self):
        # button is pressed deleted the latest entry
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # deletes the last entry into DB. using SQL, max ID would mark the newest entry
        cursor.execute('''DELETE FROM data WHERE id = (SELECT MAX(id) from data)''')

        # ? should you store the error data in another database for review of data entry; or if the latest data didn't mean to be deleted.


        connection.commit()
        connection.close()

    def last(self):
        # button is pressed the last
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT Time,HR,BP FROM data''')
        recall1= cursor.fetchall()
        id = cursor.lastrowid

        print(recall1[-1])

        connection.commit()
        connection.close()


if __name__=="__main__":
    VitalApp().run()


'''
class Database:
    def __init__(self, name):
        self.con = sqlite3.connect(name)
        self.cursor = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self.con

    @property
    def cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
'''


