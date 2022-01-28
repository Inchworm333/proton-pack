import threading
import time
import gpiozero
import colorzero
from pygame import mixer 
import helpers
import random

mixer.init(buffer=512)


class Shooting:

    def __init__(self, spin_speed, heating, status):
        self.spin_speed = spin_speed
        self.heating = heating
        self.status = status

        self.thread_armDisarmed = None
        self.thread_startStopFire = None

        self.armed_sound = mixer.Sound("sounds/ai_protongun_powerup.wav")
        self.disarmed_sound = mixer.Sound("sounds/protongun_shutdown.wav")

        self.firing_start_sound = mixer.Sound("sounds/protongun_turbo_head.wav")
        self.firing_stop_sound = mixer.Sound("sounds/protongun_turbo_tail.wav")
        self.firing_loop_sound = mixer.Sound("sounds/protongun_turbo_loop.wav")

        self.firing_mode = gpiozero.Button(22, None, False)

        self.can_fire = self.firing_mode.is_pressed

        self.fire_button = gpiozero.Button(27, None, False)
        #self.fire_button.hold_time = 0.05

        #self.fire_button.when_held = self.startFiring
        #self.fire_button.when_released = self.stopFiring

        self.firing_listeners()

    def firing_listeners(self):
        self.thread_armDisarmed = threading.Thread(target=self.armDisarm)
        self.thread_startStopFire = threading.Thread(target=self.startStopFire)
        self.thread_armDisarmed.start()
        self.thread_startStopFire.start()

    def armDisarm(self):
        while True:
            if (self.can_fire is False):
                self.firing_mode.wait_for_press()
                self.armed_sound.play()
                print("true")
                self.can_fire = True
            if (self.can_fire):
                self.firing_mode.wait_for_release()
                self.disarmed_sound.play()
                print("false")
                self.can_fire = False

    def startStopFire(self):
        while True:
            if (self.can_fire is True):
                self.fire_button.wait_for_press()
                self.firing_start_sound.play()
                time.sleep(self.firing_start_sound.get_length() - 0.25)
                self.firing_loop_sound.play(-1)

                self.fire_button.wait_for_release()
                self.firing_loop_sound.stop()
                self.firing_stop_sound.play()

    #def startFiring(self):
    #    if (self.can_fire):
    #        self.firing_start_sound.play()
    #        time.sleep(self.firing_start_sound.get_length() - 0.25)
    #        self.firing_loop_sound.play(-1)

    #def stopFiring(self):
    #    if (self.can_fire):
    #        self.firing_loop_sound.stop()
    #        self.firing_stop_sound.play()

    def mode(self, mode):
        
        mode_decoded = helpers.mode_decode(mode)

        if mode_decoded == "proton":
            shutdown = mixer.Sound("sounds/proton_pack_rail_close.wav")
            shutdown.play()
            time.sleep(shutdown.get_length() + 0.5)
            mixer.Sound("sounds/proton_pack_rail_open.wav").play()

            self.firing_start_sound = mixer.Sound("sounds/protongun_turbo_head.wav")
            self.firing_stop_sound = mixer.Sound("sounds/protongun_turbo_tail.wav")
            self.firing_loop_sound = mixer.Sound("sounds/protongun_turbo_loop.wav")

        elif mode_decoded == "slime":
            shutdown = mixer.Sound("sounds/proton_pack_rail_close.wav")
            shutdown.play()
            time.sleep(shutdown.get_length() + 0.5)
            mixer.Sound("sounds/proton_pack_slime_open.wav").play()

            self.firing_start_sound = mixer.Sound("sounds/slimegun_head.wav")
            self.firing_stop_sound = mixer.Sound("sounds/slimegun_tail.wav")
            self.firing_loop_sound = mixer.Sound("sounds/slimegun_loop.wav")

        elif mode_decoded == "stasis":
            shutdown = mixer.Sound("sounds/proton_pack_slime_close.wav")
            shutdown.play()
            time.sleep(shutdown.get_length() + 0.5)
            mixer.Sound("sounds/proton_pack_ice_open.wav")

            self.firing_start_sound = mixer.Sound("sounds/proton_stasis_head.wav")
            self.firing_stop_sound = mixer.Sound("sounds/proton_stasis_tail.wav")
            self.firing_loop_sound = mixer.Sound("sounds/proton_stasis_loop.wav")

        elif mode_decoded == "meson":
            shutdown = mixer.Sound("sounds/proton_pack_ice_close.wav")
            shutdown.play()
            time.sleep(shutdown.get_length() + 0.5)
            mixer.Sound("sounds/proton_pack_rail_open.wav").play()

            #self.firing_start_sound = mixer.Sound("sounds/")
            #self.firing_stop_sound = mixer.Sound("sounds/")
            #self.firing_loop_sound = mixer.Sound("sounds/")
