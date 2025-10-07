# ===============================
# Project: Live Camera Flip & Gray View
# Author: Yaser Mahmoudian
# Description:
#   نمایش زنده تصویر وب‌کم با OpenCV به‌صورت رنگی و سیاه‌وسفید
#   خروج از برنامه با کلید ESC و بستن کامل پنجره‌ها
# ===============================

import cv2
import numpy as np

# فعال‌سازی دوربین (0 = وب‌کم پیش‌فرض)
cap = cv2.VideoCapture(0)

# تنظیم اندازه‌ی تصویر
cap.set(3, 640)  # عرض
cap.set(4, 480)  # ارتفاع

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ خطا در خواندن تصویر از دوربین.")
        break

    # برعکس کردن تصویر به‌صورت افقی (مثل آینه)
    frame = cv2.flip(frame, 1)

    # تبدیل تصویر رنگی به سیاه‌وسفید
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # نمایش هر دو تصویر
    cv2.imshow('Color Frame', frame)
    cv2.imshow('Gray Frame', gray)

    # بررسی کلید فشرده‌شده
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # کلید ESC برای خروج
        print("🟡 در حال بستن پنجره‌ها ...")
        break

# آزاد کردن منابع و بستن همه پنجره‌ها
cap.release()
cv2.destroyAllWindows()

# اطمینان از بسته شدن کامل (در بعضی سیستم‌ها لازم است)
for i in range(5):
    cv2.waitKey(1)
