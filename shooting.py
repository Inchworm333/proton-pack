import threading
import time
import gpiozero
import colorzero
from pygame import mixer 
import helpers
import random

mixer.init(buffer=512)


class Shooting:

    def __init__(self, background):
        #self.cyclotron = cyclotron
        #self.vent = vent
        #self.status = status
        self.background = background

        self.can_fire_event = threading.Event()

        self.thread_arm_disarm = None
        self.thread_start_stop_fire = None

        self.on_event = threading.Event()

        self.armed_sound = mixer.Sound("sounds/ai_protongun_powerup.wav")
        self.disarm_sound = mixer.Sound("sounds/protongun_shutdown.wav")

        self.firing_start_sound = mixer.Sound("sounds/protongun_turbo_head.wav")
        self.firing_stop_sound = mixer.Sound("sounds/protongun_turbo_tail.wav")
        self.firing_loop_sound = mixer.Sound("sounds/protongun_turbo_loop.wav")

        self.firing_mode = gpiozero.Button(22, pull_up=True)

        self.fire_button = gpiozero.Button(27, pull_up=False)

        self.ison = gpiozero.Button(23, pull_up=False)
        
        self.ison.when_pressed = self.turned_on

        self.ison.when_released = self.turned_off

        self.firing_listeners()

    def firing_listeners(self):
        self.thread_arm_disarm = threading.Thread(target=self.arm_disarm)
        self.thread_start_stop_fire = threading.Thread(target=self.start_stop_fire)
        self.on_event.set()
        self.thread_arm_disarm.start()
        self.thread_start_stop_fire.start()

    def arm_disarm(self):
        while self.on_event.is_set():
            if (not self.can_fire_event.is_set()):
                self.firing_mode.wait_for_press()
                print('pressed')
                if (not self.on_event.is_set()):
                    print('killed')
                    return
                self.armed_sound.play()
                time.sleep(3)
                self.can_fire_event.set()

            if self.can_fire_event.is_set():
                self.firing_mode.wait_for_release()
                print('released')
                if (not self.on_event.is_set()):
                    print('killed')
                    return
                self.can_fire_event.clear()
                self.disarm_sound.play()
                time.sleep(self.disarm_sound.get_length() - 0.1)
                self.background_default()
        else:
            self.on_event.wait()

    def start_stop_fire(self):
        while True:
            while self.can_fire_event.is_set():
                print('waiting for firing')
                self.fire_button.wait_for_press()
                self.firing_start_sound.play()
                time.sleep(self.firing_start_sound.get_length() - 0.25)
                self.firing_loop_sound.play(-1)

                print('waiting for stop firing')
                self.fire_button.wait_for_release()
                self.firing_loop_sound.stop()
                self.firing_stop_sound.play()
            else:
                self.can_fire_event.wait()

    def turned_on(self):
        print('setting on')
        self.on_event.set()

    def turned_off(self):
        print('setting off')
        self.on_event.clear()

    #def kill_all(self):
    #    print('trying to kill')
    #    self.stop.set()
    #    self.can_fire_event.clear()

    #    self.firing_loop_sound.stop()
    #    self.firing_stop_sound.stop()
    #    self.firing_start_sound.stop()

    def mode(self, mode):
        
        mode_decoded = helpers.mode_decode(mode)

        if mode_decoded == "proton":
            close = mixer.Sound("sounds/proton_pack_rail_close.wav")
            self.play_wait(close, 0.5)
            open = mixer.Sound("sounds/proton_pack_rail_open.wav")
            open.play()

            self.firing_start_sound = mixer.Sound("sounds/protongun_turbo_head.wav")
            self.firing_stop_sound = mixer.Sound("sounds/protongun_turbo_tail.wav")
            self.firing_loop_sound = mixer.Sound("sounds/protongun_turbo_loop.wav")

        elif mode_decoded == "slime":
            close = mixer.Sound("sounds/proton_pack_rail_close.wav")
            self.play_wait(close, 0.5)
            open = mixer.Sound("sounds/proton_pack_slime_open.wav")
            self.play_wait(open, 0.1)
            self.background.change_sound("sounds/slime_labs_glass_bubbles_loop_1.wav")

            self.firing_start_sound = mixer.Sound("sounds/slimegun_head.wav")
            self.firing_stop_sound = mixer.Sound("sounds/slimegun_tail.wav")
            self.firing_loop_sound = mixer.Sound("sounds/slimegun_loop.wav")

        elif mode_decoded == "stasis":
            close = mixer.Sound("sounds/proton_pack_slime_close.wav")
            self.play_wait(close, 0.5)
            open = mixer.Sound("sounds/proton_pack_ice_open.wav")
            self.play_wait(open, 0.1)
            self.background.change_sound("sounds/proton_ice_freezing_loop.wav")

            self.firing_start_sound = mixer.Sound("sounds/proton_stasis_head.wav")
            self.firing_stop_sound = mixer.Sound("sounds/proton_stasis_tail.wav")
            self.firing_loop_sound = mixer.Sound("sounds/proton_stasis_loop.wav")

        elif mode_decoded == "meson":
            close = mixer.Sound("sounds/proton_pack_ice_close.wav")
            self.play_wait(close, 0.5)
            open = mixer.Sound("sounds/proton_pack_rail_open.wav")
            self.play_wait(open, 0.1)
            self.background_default()

            #self.firing_start_sound = mixer.Sound("sounds/")
            #self.firing_stop_sound = mixer.Sound("sounds/")
            #self.firing_loop_sound = mixer.Sound("sounds/")

    def play_wait(self, sound, delay=0):
        sound.play()
        time.sleep(sound.get_length() + delay)

    def background_default(self):
        self.background.change_sound("sounds/protongun_amb_hum_loop.wav")

