from kivy.app import App
from time import strftime
from kivy.clock import Clock

class CodeApp(App):
    sw_seconds=0
    sw_started = False

    def update_time1(self,nap):
        if self.sw_started:
            self.sw_seconds+=nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        part_seconds = seconds * 100 % 100
        self.root.ids.epi_time.text = f'{int(minutes):02}:{int(seconds):02}.[size=40]{int(part_seconds):02}[/size]'
        self.root.ids.time.text=strftime('[b]%H[/b]:%M:%S')

    def update_time(self,nap):
        if self.sw_started:
            self.sw_seconds+=nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        part_seconds = seconds * 100 % 100
        self.root.ids.stopwatch.text = f'{int(minutes):02}:{int(seconds):02}.[size=40]{int(part_seconds):02}[/size]'
        self.root.ids.time.text=strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time,0)

    def on_start1(self):
        Clock.schedule_interval(self.update_time1,0)


    def start_stop(self):
        self.root.ids.start_stop = 'Start'\
            if self.sw_started \
            else 'Stop'
        print (strftime('%H:%M:%S ') + "Timer started")
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text='Start'
            self.sw_started = False
        self.sw_seconds=0


    def start_stop1(self):
        self.root.ids.start_stop1 = 'Start'\
            if self.sw_started \
            else 'Stop'
        print (strftime('%H:%M:%S ') + "epi")
        self.sw_started = not self.sw_started

    def reset1(self):
        if self.sw_started:
            self.root.ids.start_stop1.text='Start'
            self.sw_started = False
        self.sw_seconds=0

    def progress_entry(self):
        print(strftime('%H:%M:%S ') + self.root.ids.progress.text)
        self.root.ids.progress.text=""


if __name__=="__main__":
    CodeApp().run()