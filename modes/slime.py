from __future__ import annotations
from mode import State
from pygame import mixer
import gpiozero
import colorzero

class Slime(State):

    firingLoopSound = mixer.Sound("../sounds/slimegun_loop.wav")

    def __init__(self) -> None:
        self.cyclotron.color = colorzero.Color('green')
        self.cyclotron.slime_bubble_start()

        startSound = mixer.Sound("../sounds/proton_pack_slime_open.wav")
        helpers.play_wait(startSound, 0.1)
        self.background.change_sound("../sounds/slime_labs_glass_bubbles_loop_1.wav")

    def arm(self) -> None:
        pass

    def disarm(self) -> None:
        pass

    def fire(self) -> None:
        startFireSound = mixer.Sound("../sounds/slimegun_head.wav")
        helpers.play_wait(startFireSound, -0.25)

        firingLoopSound.play(-1)

    def ceasefire(self) -> None:
        firingLoopSound.stop()

        mixer.Sound("../sounds/slimegun_tail.wav").play()

    def exitState(self) -> None:

        c = self.cyclotron

        mixer.Sound("../sounds/splash.wav").play()

        # quick drain effect
        c.all_on()
        c.leds[0].pulse(0, 0.65, (0.05,1,0.08), (0,0,0), 1)
        c.leds[1].pulse(0, 0.65, (0.05,1,0.08), (0,0,0), 1)
        time.sleep(0.65)
        c.leds[0].off()
        c.leds[1].off()
        c.leds[2].pulse(0, 0.35, (0.05,1,0.08), (0,0,0), 1)
        c.leds[3].pulse(0, 0.35, (0.05,1,0.08), (0,0,0), 1)
        time.sleep(0.35)
        c.all_off()

        exitSound = mixer.Sound("../sounds/proton_pack_slime_close.wav")
        helpers.play_wait(exitSound)

    def packOff(self) -> None:
        self.background.stopbg()

        mixer.Sound("../sounds/los2_slime_sewer_drain_loop.wav").play()

        c = self.cyclotron

        # slime drain effect
        c.all_on()
        c.leds[0].pulse(0, 1.5, (0.05,1,0.08), (0,0,0), 1)
        c.leds[1].pulse(0, 1.5, (0.05,1,0.08), (0,0,0), 1)
        time.sleep(1.5)
        c.leds[0].off()
        c.leds[1].off()
        c.leds[2].pulse(0, 0.75, (0.05,1,0.08), (0,0,0), 1)
        c.leds[3].pulse(0, 0.75, (0.05,1,0.08), (0,0,0), 1)
        time.sleep(0.75)
        c.all_off()
