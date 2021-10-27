import pigpio

class proton_reader:

    def __init__(self, pi, gpio):

        self.pi = pi
        self.gpio = gpio

        self._start_tick = None 
        self._end_tick = None

        self._callback  = pi.callback(gpio, pigpio.EITHER_EDGE, self._callback_func)

    #LEVEL
    #0 = change to low
    #1 = change to high
    #2 = no level change
    def _callback_func(self, gpio, level, tick):

        if level == 1: #low to high (start recording)

            self._start_tick = tick

        elif level == 0: #high to low (end recording)

            if self._start_tick is not None:
                self._end_tick = tick

    def pulse_width(self):
        if self._start_tick is not None:
            endval = self._end_tick - self._start_tick
            self._end_tick = None
            self._start_tick = None
            return endval

    def cancel(self):
        self._callback.cancel()


mode = 0 

def wand_read_loop(GPIO, total_time, sample_time):
    
    while True:

        pi = pigpio.pi()

        wand_PWM = proton_reader(pi, GPIO)

        start = time.time()

        global mode

        while (time.time() - start) < total_time:
            
            time.sleep(sample_time)

            wand_pulse_val = wand_PWM.pulse_width()

            if(wand_pulse_val is not None):
                wand_pulse = wand_pulse_val // 1000

                print(wand_pulse)

                if near(wand_pulse, 8):
                    #Power Up
                    print('power up')
                    break
                elif near(wand_pulse, 14):
                    #Power Down
                    print('power down')
                    mode = 0
                    break
                elif near(wand_pulse, 20):
                    #Overheat start
                    print('overheat started')
                    break
                elif near(wand_pulse, 26):
                    #Vent Start (manual or auto)
                    print('venting started')
                    break
                elif near(wand_pulse, 32):
                    #Mode Change
                    print('Mode Changed')
                    mode += 1
                    mode_decode(mode)
                    break
                elif near(wand_pulse, 38):
                    #Song Request
                    print('playing song')
                    break
                elif near(wand_pulse, 44):
                    #Intense Fire ON
                    print('intense fire on')
                    break
                elif near(wand_pulse, 50):
                    #Intense Fire OFF
                    print('Intense fire off')
                    break
                elif near(wand_pulse, 56):
                    #Power Down with sound
                    print('power down (with sound)')
                    break
                wand_pulse_val = None
            else:
                print('wand_pulse_val is None')

def near(number, ideal):
    return abs(number - ideal) <= 3

def mode_decode(modeID):
    inner_mode = modeID % 4
    print(inner_mode)
    
    if inner_mode == 0:
        #Proton
        print('Shooting Mode: Proton')
        None
    elif inner_mode == 1:
        #Slime
        print('Shooting Mode: Slime')
        None
    elif inner_mode == 2:
        #Stasis
        print('Shooting Mode: Stasis')
        None
    elif inner_mode == 3:
        #Meson
        print('Shooting Mode: Meson')
        None
