import time
import threading
from sound_player import Sound, Playlist, SoundPlayer

class Background:

    def __init__(self):
        self.sound = Sound("../sounds/protongun_amb_hum_loop.wav")
        self.thread = None
        self.sound.set_loop(0)
        self.playbg()


    def playbg(self):
        self.thread = threading.Thread(target=self.playbg_function)
        self.thread.start()

    def stopbg(self):
        self.sound.stop()

    def playbg_function(self):
        self.sound.play()
