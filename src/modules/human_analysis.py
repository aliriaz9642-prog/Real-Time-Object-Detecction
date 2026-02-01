from deepface import DeepFace
import cv2
import logging

# Disable DeepFace's excessive logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)

class HumanAnalyzer:
    def __init__(self):
        """Pre-load models if necessary."""
        # Models will be downloaded on first use
        self.actions = ['age', 'gender', 'emotion']

    def analyze(self, frame, detections):
        """
        Analyze 'person' detections for age, gender, and emotion.
        """
        human_results = []
        for det in detections:
            if det['label'] == 'person':
                x1, y1, x2, y2 = det['bbox']
                # Crop and fix coordinates
                padding = 20
                h, w = frame.shape[:2]
                roi = frame[max(0, y1-padding):min(h, y2+padding), max(0, x1-padding):min(w, x2+padding)]
                
                try:
                    # Enforce detection = False because we already have the bbox from YOLO
                    result = DeepFace.analyze(roi, actions=self.actions, enforce_detection=False, silent=True)
                    if isinstance(result, list): result = result[0]
                    
                    human_results.append({
                        'bbox': [x1, y1, x2, y2],
                        'age': result['age'],
                        'gender': result['dominant_gender'],
                        'emotion': result['dominant_emotion']
                    })
                except Exception as e:
                    # ROI might be too small or blurry
                    continue
        
        return human_results
