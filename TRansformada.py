import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import filedialog
import os

# FFT recursiva
def fft_recursive(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft_recursive(x[0::2])
    odd = fft_recursive(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return np.array([even[k] + T[k] for k in range(N // 2)] +
                    [even[k] - T[k] for k in range(N // 2)])

# IFFT recursiva
def ifft_recursive(X):
    X_conj = np.conjugate(X)
    x = fft_recursive(X_conj)
    return np.real(np.conjugate(x) / len(X))

# Seleccionar archivo MP3
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Seleccionar archivo MP3", filetypes=[("MP3 files", "*.mp3")])

# Cargar audio MP3 con pydub
audio = AudioSegment.from_mp3(file_path)
audio = audio.set_channels(1)  # Convertir a mono

# Extraer datos como array numpy
samples = np.array(audio.get_array_of_samples())
sample_rate = audio.frame_rate

# Guardar longitud original
N_original = len(samples)

# Rellenar con ceros hasta siguiente potencia de 2
N = 2**int(np.ceil(np.log2(N_original)))
samples_padded = np.pad(samples, (0, N - N_original), mode='constant')

# Aplicar FFT
fft_data = fft_recursive(samples_padded)

# Calcular frecuencias
frequencies = np.fft.fftfreq(N, d=1/sample_rate)
magnitude = np.abs(fft_data)

# Filtro pasabajas
cutoff_freq = 2000  # Hz
fft_filtered = fft_data.copy()
fft_filtered[np.abs(frequencies) > cutoff_freq] = 0
magnitude_filtered = np.abs(fft_filtered)

# Mostrar ambas gráficas en una sola ventana
plt.figure(figsize=(12, 6))

# Espectro original
plt.subplot(2, 1, 1)
plt.plot(frequencies[:N//2], magnitude[:N//2], color='blue')
plt.title("Espectro Original")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid(True)

# Espectro filtrado
plt.subplot(2, 1, 2)
plt.plot(frequencies[:N//2], magnitude_filtered[:N//2], color='green')
plt.title("Espectro Después del Filtro Pasabajas (2000 Hz)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid(True)

plt.tight_layout()
plt.show()

# Transformada inversa (IFFT)
filtered_signal = ifft_recursive(fft_filtered)

# Recortar a tamaño original
filtered_signal = filtered_signal[:N_original]

# Normalizar y convertir a enteros
filtered_signal = np.int16(filtered_signal / np.max(np.abs(filtered_signal)) * 32767)

# Guardar archivo WAV de salida
output_path = os.path.join(os.path.dirname(file_path), "salida_filtrada.wav")
write(output_path, sample_rate, filtered_signal)

print(f"\nAudio filtrado guardado en: {output_path}")


