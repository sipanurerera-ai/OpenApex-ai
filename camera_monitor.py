import cv2
import numpy as np
import time
import os
from datetime import datetime
import pyautogui

# Konfigurasi
OUTPUT_DIR = "camera_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def take_photo(camera_id=0, filename=None):
    """Ambil foto dari webcam"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"photo_{timestamp}.jpg"
    
    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        print(f"❌ Tidak bisa membuka kamera {camera_id}")
        return False
    
    # Tunggu kamera siap
    time.sleep(0.5)
    
    # Ambil beberapa frame untuk stabilisasi
    for _ in range(5):
        ret, frame = cap.read()
    
    # Ambil foto
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        filepath = os.path.join(OUTPUT_DIR, filename)
        cv2.imwrite(filepath, frame)
        print(f"✅ Foto berhasil diambil: {filepath}")
        return True
    else:
        print("❌ Gagal mengambil foto")
        return False

def take_screenshot(filename=None):
    """Ambil screenshot layar"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
    
    try:
        screenshot = pyautogui.screenshot()
        filepath = os.path.join(OUTPUT_DIR, filename)
        screenshot.save(filepath)
        print(f"✅ Screenshot berhasil: {filepath}")
        return True
    except Exception as e:
        print(f"❌ Gagal screenshot: {e}")
        return False

def monitor_loop(interval_minutes=5, photo=True, screenshot=True):
    """Loop monitoring setiap X menit"""
    print(f"🦍 OpenApeX Monitoring Started!")
    print(f"📸 Foto: {'ON' if photo else 'OFF'}")
    print(f"🖥️ Screenshot: {'ON' if screenshot else 'OFF'}")
    print(f"⏱️ Interval: {interval_minutes} menit")
    print(f"📁 Output: {os.path.abspath(OUTPUT_DIR)}")
    print("-" * 50)
    
    counter = 0
    while True:
        counter += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[{counter}] {timestamp}")
        
        if photo:
            take_photo()
        
        if screenshot:
            take_screenshot()
        
        print(f"⏳ Menunggu {interval_minutes} menit...")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    # Test mode: ambil 1 foto dan 1 screenshot
    print("[OpenApeX] Camera Test Mode")
    take_photo()
    take_screenshot()
    
    # Uncomment baris di bawah untuk menjalankan monitoring loop
    # monitor_loop(interval_minutes=5, photo=True, screenshot=True)
