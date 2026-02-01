import cv2
import numpy as np

def draw_hud(frame, detections, human_data, status="System Online"):
    """
    PREMIUM HUD v2.0 - COMMAND CENTER DESIGN
    Features: Scoped Bounding Boxes, Attribute Badges, Demographic sidebar.
    """
    h, w = frame.shape[:2]
    
    # 1. TOP BAR (Tactical Glass Theme)
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, 70), (20, 20, 20), -1)
    cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
    
    cv2.putText(frame, "OPEN VISION COMMAND", (25, 45), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255, 255, 255), 2)
    cv2.putText(frame, status, (w - 350, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 127), 2)

    # 2. DETECTIONS (High-Level Styling)
    for det in detections:
        x1, y1, x2, y2 = det['bbox']
        label = det['label'].upper()
        color_attr = det['attributes']['color']
        size_attr = det['attributes']['size']
        
        # Tactical corners instead of full box for 'cleaner' look
        length = 20
        c = (0, 255, 255) if label != 'PERSON' else (0, 165, 255) # Yellow/Orange
        
        # Draw Corners
        cv2.line(frame, (x1, y1), (x1 + length, y1), c, 3)
        cv2.line(frame, (x1, y1), (x1, y1 + length), c, 3)
        cv2.line(frame, (x2, y1), (x2 - length, y1), c, 3)
        cv2.line(frame, (x2, y1), (x2, y1 + length), c, 3)
        cv2.line(frame, (x1, y2), (x1 + length, y2), c, 3)
        cv2.line(frame, (x1, y2), (x1, y2 - length), c, 3)
        cv2.line(frame, (x2, y2), (x2 - length, y2), c, 3)
        cv2.line(frame, (x2, y2), (x2, y2 - length), c, 3)

        # Intelligence Badge
        badge_text = f"{label} | {color_attr} | {size_attr}"
        (tw, th), _ = cv2.getTextSize(badge_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(frame, (x1, y1 - 25), (x1 + tw + 10, y1), c, -1)
        cv2.putText(frame, badge_text, (x1 + 5, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    # 3. SIDEBAR (Demographic Analytics)
    if human_data:
        sidebar_w = 280
        cv2.rectangle(overlay, (w - sidebar_w, 80), (w - 20, 300), (30, 30, 30), -1)
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
        
        cv2.putText(frame, "HUMAN ANALYTICS", (w - sidebar_w + 10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        for i, h_info in enumerate(human_data[:4]): # Show up to 4 people
            y_off = 150 + (i * 40)
            txt = f"P{i+1}: {h_info['gender']} | {h_info['age']} y | {h_info['emotion']}"
            cv2.putText(frame, txt, (w - sidebar_w + 10, y_off), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    # 4. FOOTER STATS
    cv2.rectangle(frame, (0, h - 35), (w, h), (10, 10, 10), -1)
    footer_text = f"ACTIVE OBJECTS: {len(detections)} | MODEL: YOLO11-XL | ARCHITECTURE: ASYNC-PARALLEL"
    cv2.putText(frame, footer_text, (20, h - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)
    
    return frame
