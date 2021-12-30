from kivy.app import App
from time import strftime
from kivy.clock import Clock

class StopWatchApp(App):
    sw_seconds=0
    sw_started = False

    def update_time(self,nap):
        if self.sw_started:
            self.sw_seconds+=nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        part_seconds = seconds * 100 % 100
        self.root.ids.stopwatch.text = f'{int(minutes):02}:{int(seconds):02}.[size=40]{int(part_seconds):02}[/size]'
        self.root.ids.time.text=strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time,0)

    def start_stop(self):
        self.root.ids.start_stop = 'Start' if\
            self.sw_started else 'Stop'
        self.sw_started = not self.sw_started

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
        print(strftime('%H:%M:%S ') + self.root.ids.hr_monitor.text)
        print(strftime('%H:%M:%S ') + self.root.ids.bp_monitor.text)
        print(strftime('%H:%M:%S ') + self.root.ids.o2_monitor.text)
        print(strftime('%H:%M:%S ') + self.root.ids.rr_monitor.text)
        print(strftime('%H:%M:%S ') + self.root.ids.temp_monitor.text)



if __name__=="__main__":
    StopWatchApp().run()