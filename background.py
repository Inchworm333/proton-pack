import time
import threading
#from sound_player import Sound, Playlist, SoundPlayer
from pygame import mixer

mixer.init(buffer=512)

class Background:

    def __init__(self):
        self.sound = mixer.Sound("sounds/protongun_amb_hum_loop.wav")
        self.thread = None
        self.playbg()


    def playbg(self):
        self.thread = threading.Thread(target=self.playbg_function)
        self.thread.start()

    def stopbg(self):
        self.sound.stop()

    def playbg_function(self):
        self.sound.play(-1)

