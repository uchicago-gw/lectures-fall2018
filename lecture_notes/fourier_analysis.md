# Basics of (Discrete) Fourier Analysis

A handwritten set of notes with more detail (and math!) is available [here](https://github.com/uchicago-gw/lectures-fall2018/blob/master/lecture_notes/fourier_analysis-handwritten.pdf).

Mathematical Concepts

  * Fourier Series
  * Fourier Transform
    * linearity
  * Fast Fourier Transform (FFT) as an implementation of the Discrete Fourier Transform (DFT)
    * aliasing
  * frequency-domain filtering
    * convolution
    * window functions

  * EXTRA TOPICS
    * multi-scale analysis
      * Haar wavelet transform
      * short-time Fourier transform

Applications

  * bandpass freq-domain filtering
  * whitening/noise-suppression
  * image compression

Software Libraries

  * Numpy (numpy.fft)
  * Matplotlib (matplotlib.pyplot)

--------------------------------------------------

## Fourier Series and Transform

  * orthogonality of sine and cosine functions
  * representation of periodic data in terms of a Fourier series (in terms of a base period)
    * EXAMPLE: square pulse and accuracy as we truncate the Fourier series 

  * motivate Fourier Transform as a limit of the Fourier Series

  * basic symmetries and intuition
    * even vs odd parity
    * EXAMPLE: FT[tanh(x/xo)] behavior as a function of xo

## Discrete Fourier Transform

  * Basic properties of the DFT
    * srate, seglen -> Nyquist freq, freq spacing
  * aliasing
    * EXAMPLE: a sine-Gaussian at different frequencies
  * FFT as an implementation of the DFT

## Frequency-domain Filtering

  * Convolution theorem
  * sidebands and windowing functions
  * Filter design
    * sharp corners in f-space -> sidebands in t-space
    * EXAMPLE: low-pass (band-pass?) butterworth filter with audio captured during a live-demo

--------------------------------------------------

## Multi-scale analysis

  * time-freq uncertainty principle
  * "pixel" interpretation of time-freq plain and sparse signal representation
  * short-time Fourier Transform
    * EXAMPLE: make a spectrogram of audio captured ruing a live-demo
  * Haar transform
    * adaptive trade-off in time vs. freq precision
    * image compression
    * wavelet whitening
