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
        if self._start_tick is not None and self._end_tick is not None:
            endval = self._end_tick - self._start_tick
            self._end_tick = None
            self._start_tick = None
            return endval

    def cancel(self):
        self._callback.cancel()

