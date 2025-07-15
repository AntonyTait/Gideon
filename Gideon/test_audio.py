#!/usr/bin/env python3
"""
Simple audio test for Gideon on LineageOS
Tests microphone input and speaker output
"""

import pyaudio
import wave
import time
import sys

def test_audio():
    """Test microphone input and speaker output"""
    
    # Audio settings
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 3
    
    p = pyaudio.PyAudio()
    
    print("Testing audio input/output...")
    print("Available audio devices:")
    
    # List available devices
    for i in range(p.get_device_count()):
        dev_info = p.get_device_info_by_index(i)
        print(f"  {i}: {dev_info['name']}")
    
    try:
        # Test recording
        print(f"\nRecording {RECORD_SECONDS} seconds of audio...")
        stream = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)
        
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        
        print("Recording complete!")
        stream.stop_stream()
        stream.close()
        
        # Test playback
        print("Playing back recorded audio...")
        stream = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       output=True,
                       frames_per_buffer=CHUNK)
        
        for frame in frames:
            stream.write(frame)
        
        stream.stop_stream()
        stream.close()
        print("Playback complete!")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTrying alternative audio setup...")
        
        # Try with default devices
        try:
            stream = p.open(format=FORMAT,
                           channels=CHANNELS,
                           rate=RATE,
                           input=True)
            print("Default input device works!")
            stream.close()
        except Exception as e2:
            print(f"Default input also failed: {e2}")
    
    p.terminate()

if __name__ == "__main__":
    test_audio() 