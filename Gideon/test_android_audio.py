#!/usr/bin/env python3
"""
Test Android's built-in audio capabilities on LineageOS
"""

import subprocess
import time

def test_android_tts():
    """Test Android's built-in text-to-speech"""
    print("Testing Android TTS...")
    
    try:
        # Try to use Android's TTS
        result = subprocess.run([
            'am', 'start', '-a', 'android.intent.action.TTS_SERVICE',
            '--es', 'android.speech.extra.TEXT', 'Hello, this is Gideon testing text to speech'
        ], capture_output=True, text=True)
        
        print(f"TTS command result: {result.returncode}")
        if result.stdout:
            print(f"STDOUT: {result.stdout}")
        if result.stderr:
            print(f"STDERR: {result.stderr}")
            
    except Exception as e:
        print(f"TTS test failed: {e}")

def test_android_stt():
    """Test Android's built-in speech recognition"""
    print("\nTesting Android STT...")
    
    try:
        # Try to launch speech recognition
        result = subprocess.run([
            'am', 'start', '-a', 'android.speech.action.RECOGNIZE_SPEECH'
        ], capture_output=True, text=True)
        
        print(f"STT command result: {result.returncode}")
        if result.stdout:
            print(f"STDOUT: {result.stdout}")
        if result.stderr:
            print(f"STDERR: {result.stderr}")
            
    except Exception as e:
        print(f"STT test failed: {e}")

def test_android_commands():
    """Test basic Android commands"""
    print("\nTesting Android commands...")
    
    commands = [
        ['am', 'start', '-a', 'android.settings.SETTINGS'],
        ['dumpsys', 'audio'],
        ['getprop', 'ro.product.model']
    ]
    
    for cmd in commands:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            print(f"Command {' '.join(cmd)}: {result.returncode}")
            if result.stdout:
                print(f"  Output: {result.stdout[:100]}...")
        except Exception as e:
            print(f"Command {' '.join(cmd)} failed: {e}")

if __name__ == "__main__":
    print("Testing Android audio capabilities on LineageOS...")
    test_android_commands()
    test_android_tts()
    test_android_stt()
    print("\nTest complete!") 