import math

class DynamicRangeCompressor:
    """
    Audio Dynamic Range Compressor & Limiter.
    Attenuates signal above threshold dB with specified ratio and makeup gain.
    """
    def __init__(self, threshold_db=-10.0, ratio=4.0, makeup_gain_db=2.0):
        self.threshold = threshold_db
        self.ratio = ratio
        self.makeup_gain = 10.0 ** (makeup_gain_db / 20.0)

    def process(self, signal):
        output = []
        for s in signal:
            abs_s = abs(s) + 1e-9
            s_db = 20.0 * math.log10(abs_s)
            if s_db > self.threshold:
                excess = s_db - self.threshold
                compressed_db = self.threshold + excess / self.ratio
                gain = 10.0 ** ((compressed_db - s_db) / 20.0)
            else:
                gain = 1.0
            output.append(s * gain * self.makeup_gain)
        return output
