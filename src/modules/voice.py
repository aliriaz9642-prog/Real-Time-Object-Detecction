import pyttsx3
import threading
import queue

class VoiceEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voice_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self._process_queue, daemon=True)
        self.thread.start()
        
        # Configure properties
        self.engine.setProperty('rate', 170)  # Speed of speech
        self.engine.setProperty('volume', 1.0) # Volume 0.0 to 1.0

    def _process_queue(self):
        while not self.stop_event.is_set():
            try:
                text = self.voice_queue.get(timeout=1)
                self.engine.say(text)
                self.engine.runAndWait()
                self.voice_queue.task_done()
            except queue.Empty:
                continue

    def speak(self, text):
        """Asynchronously add text to the speech queue."""
        if self.voice_queue.qsize() < 3:  # Prevent queue bloat
            self.voice_queue.put(text)

    def stop(self):
        self.stop_event.set()
        self.thread.join()
