"""Dynamic Range Compressor & Limiter Engine
100% Python Standard Library (math).
"""

import math

class DynamicRangeCompressorLimiter:
    """Audio dynamic range compressor and brickwall peak limiter."""
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def process(self, signal, threshold_db=-18.0, ratio=4.0, knee_db=3.0,
                attack_ms=5.0, release_ms=50.0, makeup_gain_db=0.0):
        att_coeff = math.exp(-1.0 / (attack_ms * 0.001 * self.sample_rate))
        rel_coeff = math.exp(-1.0 / (release_ms * 0.001 * self.sample_rate))
        makeup_linear = 10.0 ** (makeup_gain_db / 20.0)

        output = []
        envelope_state = 0.0
        gain_reductions = []

        for x in signal:
            x_abs = abs(x)
            x_db = 20.0 * math.log10(max(x_abs, 1e-6))

            # Soft-knee gain computer
            if 2 * (x_db - threshold_db) < -knee_db:
                y_db = x_db
            elif 2 * abs(x_db - threshold_db) <= knee_db:
                y_db = x_db + ((1.0 / ratio - 1.0) * (x_db - threshold_db + knee_db / 2.0) ** 2) / (2.0 * knee_db)
            else:
                y_db = threshold_db + (x_db - threshold_db) / ratio

            desired_gain_db = y_db - x_db

            # Ballistics smoother
            if desired_gain_db < envelope_state:
                envelope_state = att_coeff * envelope_state + (1.0 - att_coeff) * desired_gain_db
            else:
                envelope_state = rel_coeff * envelope_state + (1.0 - rel_coeff) * desired_gain_db

            gain_linear = 10.0 ** (envelope_state / 20.0)
            y_out = x * gain_linear * makeup_linear
            output.append(y_out)
            gain_reductions.append(-envelope_state)

        return {
            "processed_samples": len(output),
            "max_gain_reduction_db": max(gain_reductions) if gain_reductions else 0.0,
            "average_gain_reduction_db": sum(gain_reductions) / max(1, len(gain_reductions)),
            "peak_output": max(abs(s) for s in output) if output else 0.0
        }
