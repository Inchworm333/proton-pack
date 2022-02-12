import threading
import time
import gpiozero
import colorzero
from pygame import mixer 
import helpers
import random
import _thread

mixer.init(buffer=512)


class Shooting:

    def __init__(self):
        #self.cyclotron = cyclotron
        #self.vent = vent
        #self.status = status

        self.can_fire_event = threading.Event()

        self.thread_arm_disarm = None
        self.thread_start_stop_fire = None

        self.armed_sound = mixer.Sound("sounds/ai_protongun_powerup.wav")
        self.disarm_sound = mixer.Sound("sounds/protongun_shutdown.wav")

        self.firing_start_sound = mixer.Sound("sounds/protongun_turbo_head.wav")
        self.firing_stop_sound = mixer.Sound("sounds/protongun_turbo_tail.wav")
        self.firing_loop_sound = mixer.Sound("sounds/protongun_turbo_loop.wav")

        self.firing_mode = gpiozero.Button(22, pull_up=False)

        self.firing_mode.bounce_time = 3

        self.fire_button = gpiozero.Button(27, pull_up=False)

        self.firing_listeners()

    def firing_listeners(self):
        self.thread_arm_disarm = threading.Thread(target=self.arm_disarm)
        self.thread_start_stop_fire = threading.Thread(target=self.start_stop_fire)
        self.thread_arm_disarm.start()
        self.thread_start_stop_fire.start()

    def arm_disarm(self):
        if not self.can_fire_event.is_set():
            self.firing_mode.wait_for_press()
            self.armed_sound.play()
            self.can_fire_event.set()

        if self.can_fire_event.is_set():
            self.firing_mode.wait_for_release()
            self.disarm_sound.play()
            self.can_fire_event.clear()

    def start_stop_fire(self):
        while self.can_fire_event.is_set():
            self.fire_button.wait_for_press()
            self.firing_start_sound.play()
            time.sleep(self.firing_start_sound.get_length() - 0.25)
            self.firing_loop_sound.play(-1)

            self.fire_button.wait_for_release()
            self.firing_loop_sound.stop()
            self.firing_stop_sound.play()
        else:
            self.can_fire_event.wait()

    def kill_all(self):
        self.can_fire_event.clear()

        self.firing_loop_sound.stop()
        self.firing_stop_sound.stop()
        self.firing_start_sound.stop()

        self.firing_mode.close()
        self.fire_button.close()

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
