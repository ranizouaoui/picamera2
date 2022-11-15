#!/usr/bin/python3

import time

from picamera2 import Picamera2, Preview

if len(Picamera2.global_camera_info()) <= 1:
    print("SKIPPED (one camera)")
    quit()

picam2a = Picamera2(0)
picam2a.configure(picam2a.create_preview_configuration())
picam2a.start_preview(Preview.QTGL)
picam2a.start()

time.sleep(2)
picam2a.capture_file("testa.jpg")

picam2b = Picamera2(1)
picam2b.configure(picam2b.create_preview_configuration())
picam2b.start()

time.sleep(2)
picam2a.stop()

picam2b.capture_file("testb.jpg")

picam2b.stop()
