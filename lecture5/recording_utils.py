import pyaudio
import wave
import time

def record_wav_file(CHUNK = 1024,
                    FORMAT = pyaudio.paInt16,
                    CHANNELS = 2,
                    RATE = 44100,
                    RECORD_SECONDS = 5,
                    WAVE_OUTPUT_FILENAME = "voice.wav"):

    """
    Creates a wav audio file and saves it out

    Parameters
    ----------
    CHUNK: int
    numer of samples in each frame

    FORMAT: pyaudio format

    CHANNELS: int
    Number of audio channels

    RATE: float
    Sampling rate in Hz

    RECORD_SECONDS: float
    Number of seconds to record for

    WAVE_OUTPUT_FILENAME: str
    Name of the output wave file
    
    Returns
    ------
    None

    """
    
    print 'ready?'
    time.sleep(1)
    
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print "* recording"

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print "* done recording" 

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def record_multiple_wav_files(fname,record_seconds):
    # record the first file
    n = 0
    record_wav_file(CHUNK = 1024,
                    FORMAT = pyaudio.paInt16,
                    CHANNELS = 2,
                    RATE = 44100,
                    RECORD_SECONDS = record_seconds,
                    WAVE_OUTPUT_FILENAME = "%s%i.wav"%(fname,n))    
    
    # then record more if desired
    ans = 'y'
    while (ans == 'y'):
        ans = raw_input('Would you like to record another? y/n')
        if ans=='y':
            n = n+1
            record_wav_file(CHUNK = 1024,
                            FORMAT = pyaudio.paInt16,
                            CHANNELS = 2,
                            RATE = 44100,
                            RECORD_SECONDS = 5,
                            WAVE_OUTPUT_FILENAME = "%s%i.wav"%(fname,n))    
                    
        elif ans=='n':
            print 'kthxbai'
            break
        else:
            print 'please type y or n, you heathen!'
            continue

print 'first record snaps'
fname = 'audio/snaps'
record_seconds = 1
record_multiple_wav_files(fname,record_seconds)

print 'now record claps'
raw_input('press enter to continue')
fname = 'audio/claps'
record_multiple_wav_files(fname,record_seconds)

