import sys
import librosa
import numpy as np
import time

def calculate_average_frequency(audio_file):
    try:
        # Load the audio file
        y, sr = librosa.load(audio_file)

        # Calculate the fundamental frequency (F0) using librosa
        f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

        # Filter out 'nan' values and calculate the average frequency in Hz
        valid_f0 = f0[~np.isnan(f0)]
        if len(valid_f0) > 0:
            average_frequency_hz = np.mean(valid_f0)
            print("Average Frequency (Hz):", average_frequency_hz)
        else:
            print("No valid pitch detected in the audio.")

        # Calculate and print processing time with two decimal places
        end_time = time.time()
        processing_time = end_time - start_time
        print("Processing time: {:.2f} seconds".format(processing_time))

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audio-script.py <audio_file>")
    else:
        audio_file = sys.argv[1]
        # Start measuring processing time
        start_time = time.time()
        calculate_average_frequency(audio_file)
