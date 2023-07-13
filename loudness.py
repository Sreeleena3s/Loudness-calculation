import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def calculate_loudness(data):
    # Compute the RMS (root mean square) of the audio signal
    rms = np.sqrt(np.mean(data ** 2))

    # Convert RMS to decibels (dB)
    loudness_db = 20 * np.log10(rms)
    return np.abs(loudness_db)


# Define the callback function for real-time audio processing
def audio_callback(indata, frames, time, status):
    # Calculate the loudness of the audio signal
    loudness_db = calculate_loudness(indata)

    # Print the loudness in decibels
    print("Loudness (dB):", loudness_db)


# Set the audio parameters
sample_rate = 44100  # Sample rate in Hz
duration = 1.0  # Duration of each audio frame in seconds

# Start the audio stream with the specified parameters
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate,
                        blocksize=int(sample_rate * duration))
stream.start()

# Display the live spectrogram (optional)
fig, ax = plt.subplots()
image = ax.imshow([[]], cmap='hot', aspect='auto')
plt.title('Live Spectrogram')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.tight_layout()


# Update the live spectrogram with the incoming audio data
def update_spectrogram(indata):
    image.set_array(np.abs(np.fft.fftshift(np.fft.fft(indata, axis=0)) ** 2))
    plt.draw()


ani = animation.FuncAnimation(fig, update_spectrogram, interval=10, blit=False)

# Show the live spectrogram plot
plt.show()

# Keep the program running until interrupted
while True:
    pass

# Stop the audio stream
stream.stop()
stream.close()
