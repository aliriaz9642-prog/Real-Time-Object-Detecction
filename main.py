import cv2
import time
import queue
import threading
from datetime import datetime

from src.modules.detector import ObjectDetector
from src.modules.voice import VoiceEngine
from src.modules.human_analysis import HumanAnalyzer
from src.utils.ui_utils import draw_hud

class HighLevelVisionAI:
    def __init__(self):
        print("\n" + "="*50)
        print("  OPEN VISION ENTERPRISE v2.0 - SOTA EDITION")
        print("="*50)
        
        self.detector = ObjectDetector() # Will download YOLO11x (Extra Large)
        self.voice = VoiceEngine()
        self.analyzer = HumanAnalyzer()
        
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        # Threading Components
        self.frame_queue = queue.Queue(maxsize=2)
        self.result_queue = queue.Queue(maxsize=2)
        self.running = True
        
        # Stats & Intelligence
        self.global_stats = {"count": 0, "last_seen": "None"}
        self.detections = []
        self.human_data = []

    def capture_thread(self):
        """High-speed capture thread."""
        while self.running:
            ret, frame = self.cap.read()
            if not ret: break
            if not self.frame_queue.full():
                self.frame_queue.put(frame)

    def inference_thread(self):
        """Dedicated AI heavy-lifting thread."""
        frame_count = 0
        while self.running:
            try:
                frame = self.frame_queue.get(timeout=1)
                
                # 1. Precise Detection
                current_detections = self.detector.detect(frame)
                
                # 2. Strategic Demographic Analysis (Every 60 frames for performance)
                current_humans = []
                if frame_count % 60 == 0:
                    current_humans = self.analyzer.analyze(frame, current_detections)
                
                # Update shared results
                self.detections = current_detections
                if current_humans: self.human_data = current_humans
                
                # 3. Smart Voice Dispatcher
                self.process_voice_intelligence(current_detections)
                
                frame_count += 1
            except queue.Empty:
                continue

    def process_voice_intelligence(self, detections):
        """CEO-Level Logic: Don't just list objects, describe the scene."""
        current_time = time.time()
        if not hasattr(self, 'last_voice_time'): self.last_voice_time = 0
        
        if current_time - self.last_voice_time > 8:
            if detections:
                main_obj = detections[0]
                desc = f"Intelligence report: {main_obj['attributes']['size']} {main_obj['attributes']['color']} {main_obj['label']} identified."
                self.voice.speak(desc)
                self.last_voice_time = current_time

    def run(self):
        # Start Parallel Engines
        threading.Thread(target=self.capture_thread, daemon=True).start()
        threading.Thread(target=self.inference_thread, daemon=True).start()
        
        print("[SYSTEM] Parallel AI Engines started. Max performance active.")
        
        last_time = time.time()
        while self.running:
            if not self.frame_queue.empty():
                frame = self.frame_queue.get()
                
                # Render HUD with data richness
                fps = 1 / (time.time() - last_time)
                last_time = time.time()
                
                processed_frame = draw_hud(frame, self.detections, self.human_data, status=f"AI XL ENGINE | {fps:.1f} FPS")
                
                cv2.imshow("OPEN VISION v2.0 - COMMAND CENTER", processed_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False
                break
        
        self.cleanup()

    def cleanup(self):
        print("[SHUTDOWN] Releasing SOTA models and hardware resources...")
        self.cap.release()
        cv2.destroyAllWindows()
        self.voice.stop()

if __name__ == "__main__":
    app = HighLevelVisionAI()
    app.run()
