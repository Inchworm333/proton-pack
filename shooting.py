import threading
import time
import gpiozero
import colorzero
from sound_player import Sound, Playlist, SoundPlayer
import helpers
import random


class Shooting:

    def __init__(self, spin_speed, heating, status, mode):
        self.spin_speed = spin_speed
        self.heating = heating
        self.status = status
        self.mode = mode

        self.thread_armed = None
        self.thread_disarmed = None

        self.armed_sound = Sound("sounds/ai_protongun_powerup.wav")
        self.disarmed_sound = Sound("sounds/protongun_shutdown.wav")

        self.firing_start_sound = Sound("sounds/protongun_turbo_head.wav")
        self.firing_stop_sound = Sound("sounds/protongun_turbo_tail.wav")
        self.firing_loop_sound = Sound("sounds/protongun_turbo_loop.wav")
        self.firing_loop_sound.set_loop(0)

        self.firing_mode = gpiozero.Button(22, False)

        self.can_fire = self.firing_mode.is_pressed

        #self.fire_button = gpiozero.Button(27, False)
        #self.fire_button.hold_time = 0.75

        self.firing_listeners()

    def firing_listeners(self):
        self.thread_armed = threading.Thread(target=self.armed)
        self.thread_disarmed = threading.Thread(target=self.disarmed)
        self.thread_armed.start()
        self.thread_disarmed.start()

    def test_in_thread_function(self):
        print("testing sounds")
        self.sound.play()

    def armed(self):
        while not self.can_fire:
            self.firing_mode.wait_for_press()
            print("armed")
            #if debug:
            #    print("firing on")

            sound1 = self.armed_sound
            sound1.play()
            self.can_fire = True


    def disarmed(self):
        while self.can_fire:
            self.firing_mode.wait_for_release()
            print("disarmed")
            #if  debug:
            #    print("firing off")

            sound2 = self.disarmed_sound
            sound2.play()
            self.can_fire = False


    def firing_loop(self):
        if debug:
            print("firing loop")
        

    def mode(self, mode):
        
        mode_decoded = helpers.mode_decode(mode)

        if mode_decoded == "proton":
            self.armed_sound = Sound("sounds/ai_protongun_powerup.wav")
            self.disarmed_sound = Sound("sounds/protongun_shutdown.wav")

            self.firing_start_sound = Sound("sounds/protongun_turbo_head.wav")
            self.firing_stop_sound = Sound("sounds/protongun_turbo_tail.wav")
            self.firing_loop_sound = Sound("sounds/protongun_turbo_loop.wav")

        elif mode_decoded == "slime":
            self.firing_start_sound = Sound("sounds/slimegun_head.wav")
            self.firing_stop_sound = Sound("sounds/slimegun_tail.wav")
            self.firing_loop_sound = Sound("sounds/slimegun_loop.wav")
        elif mode_decoded == "stasis":
            None
            #self.firing_start_sound = Sound("sounds/
        elif mode_decoded == "meson":
            #SOUNDS HERE
            self.stop_spin()
            self.color = (1, 0.27, 0)
            self.start_spin(self.spin_fade_out_function)
    
