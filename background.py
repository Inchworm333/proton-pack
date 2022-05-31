import time
import threading
from pygame import mixer

mixer.init(buffer=512)

class Background:

    def __init__(self):
        self.sound = mixer.Sound("sounds/protongun_amb_hum_loop.wav")
        self.thread = None

    def playbg(self):
        self.thread = threading.Thread(target=self.playbg_function)
        self.thread.start()

    def stopbg(self):
        self.thread.join()
        self.thread = None
        self.sound.stop()

    def playbg_function(self):
        self.sound.play(-1)
    
    def change_sound(self, sound):
        self.stopbg()
        self.sound = mixer.Sound(sound)
        self.playbg()
        self.thread.join()
