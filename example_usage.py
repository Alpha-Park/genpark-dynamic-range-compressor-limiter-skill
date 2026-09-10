from client import DynamicRangeCompressor

def main():
    print("=== Testing Dynamic Range Compressor ===")
    comp = DynamicRangeCompressor(threshold_db=-6.0, ratio=4.0, makeup_gain_db=0.0)

    audio_signal = [1.0, 0.5, 0.1, 0.01]
    compressed = comp.process(audio_signal)

    print("Input audio samples:", audio_signal)
    print("Compressed audio samples:", [round(x, 4) for x in compressed])

    assert abs(compressed[0]) < 1.0
    assert abs(compressed[2] - 0.1) < 1e-4
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
