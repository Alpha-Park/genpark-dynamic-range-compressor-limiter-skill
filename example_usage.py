from client import DynamicRangeCompressorLimiter
import math

def main():
    comp = DynamicRangeCompressorLimiter(sample_rate=44100)
    sig = [1.2 * math.sin(2 * math.pi * 400 * i / 44100) for i in range(1000)]
    res = comp.process(sig, threshold_db=-6.0, ratio=4.0)
    print("Compressor & Limiter Verification:")
    print(f"Max Gain Reduction: {res['max_gain_reduction_db']:.2f} dB")
    print(f"Peak Output: {res['peak_output']:.4f}")

if __name__ == "__main__":
    main()
