# Text-to-Speech Module using Android's built-in TTS

import subprocess

class TextToSpeech:
    def __init__(self):
        # Android's built-in TTS doesn't need initialization
        pass

    def speak(self, text):
        """
        Use Android's built-in text-to-speech
        """
        try:
            # Use Android's TTS intent
            subprocess.run([
                'am', 'start', '-a', 'android.intent.action.TTS_SERVICE',
                '--es', 'android.speech.extra.TEXT', text
            ], capture_output=True)
            
            # Alternative: Use Android's speak command if available
            # subprocess.run(['tts', text], capture_output=True)
            
        except Exception as e:
            print(f"TTS Error: {e}")
            # Fallback: just print the text
            print(f"Speaking: {text}")

    def set_speed(self, speed=1.0):
        """
        Set TTS speed (0.5 to 2.0)
        """
        # This would configure Android's TTS settings
        pass

    def set_pitch(self, pitch=1.0):
        """
        Set TTS pitch (0.5 to 2.0)
        """
        # This would configure Android's TTS settings
        pass 