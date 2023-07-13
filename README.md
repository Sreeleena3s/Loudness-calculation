# Loudness-calculation

tle: Real-time Audio Analysis and Live Spectrogram Display

Introduction:
This code provides a framework for real-time audio analysis using the SoundDevice library in Python. It calculates the loudness of the audio signal and displays a live spectrogram using Matplotlib's animation capabilities. The code sets up an audio stream, processes the incoming audio data, and continuously updates the spectrogram plot.

Libreries required:

sounddevice: A Python library for audio input and output.
numpy: A numerical computing library for efficient array operations.
matplotlib: A plotting library for creating visualizations.

Functions and Usage of the code:

calculate_loudness(data)

Input: 'data' - numpy array of audio samples
Output: 'loudness_db' - loudness in decibels (dB)
Description: Calculates the loudness of the audio signal using the root mean square (RMS) method and converts it to decibels (dB).
audio_callback(indata, frames, time, status)

Input: 'indata' - input audio samples
'frames' - number of frames
'time' - time elapsed
'status' - status of the audio stream
Description: The callback function for real-time audio processing. It calls the 'calculate_loudness' function to compute the loudness of the audio signal and prints it in decibels.
update_spectrogram(indata)

Input: 'indata' - input audio samples
Description: Updates the live spectrogram plot with the incoming audio data. It performs the Fast Fourier Transform (FFT) on the input data, computes the absolute values squared, and sets the resulting array as the data for the spectrogram plot.

Main Program:
Sets the audio parameters: sample rate and duration.
Starts the audio stream using the 'sd.InputStream' class with the specified parameters and the 'audio_callback' function as the callback.
Creates a figure and axes for the live spectrogram plot using Matplotlib.
Defines an animation that calls the 'update_spectrogram' function to update the spectrogram plot at a specified interval.
Displays the live spectrogram plot.
Keeps the program running until interrupted.
Stops and closes the audio stream.

Usage:
Ensure that the required dependencies (sounddevice, numpy, matplotlib) are installed.
Run the code.
The loudness of the incoming audio will be printed in decibels.
A live spectrogram plot will be displayed, showing the frequency content of the audio signal over time.
The program will continue running until interrupted (e.g., by pressing Ctrl+C).
The audio stream will be stopped and closed automatically.

Conclusion:
This code can be customized and extended for various real-time audio analysis applications by modifying the 'audio_callback' and 'update_spectrogram' functions. Additional processing, visualizations, or actions can be incorporated based on the specific requirements.
