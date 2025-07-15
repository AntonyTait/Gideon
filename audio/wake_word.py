# Wake Word Detection Module for Android

import time
import subprocess

class WakeWordDetector:
    def __init__(self):
        # For now, we'll use a simple approach
        # In a full implementation, we'd use Android's SpeechRecognizer API
        # or integrate with a wake word library that works on Android
        self.is_listening = False
        
    def listen(self):
        """
        Listen for wake word 'hey gideon'
        Returns True if wake word detected, False otherwise
        """
        # This is a simplified implementation
        # In practice, we'd need to:
        # 1. Use Android's SpeechRecognizer API for continuous listening
        # 2. Or use a wake word library like Porcupine (if it works on Android)
        # 3. Or implement a simple audio level detection + keyword spotting
        
        # For now, return False (no wake word detected)
        return False
    
    def start_listening(self):
        """
        Start listening for wake word
        """
        self.is_listening = True
        print("Started listening for 'Hey Gideon'...")
        
    def stop_listening(self):
        """
        Stop listening for wake word
        """
        self.is_listening = False
        print("Stopped listening for wake word.")
        
    def is_active(self):
        """
        Check if currently listening
        """
        return self.is_listening 