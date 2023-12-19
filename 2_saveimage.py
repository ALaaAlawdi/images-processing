# حفظ وعرض الصورة

import cv2

# قراءة الصورة من الملف باللون الرمادي
img = cv2.imread('./galaxy_leader.jpg', 0)

# عرض الصورة في نافذة باسم "image"
cv2.imshow('image', img)

# انتظار الضغط على مفتاح من لوحة المفاتيح
k = cv2.waitKey(0)

# إذا تم الضغط على 's' (تستقبل حرف وترجع الأسكي كود الخاص به)
if k == ord('s'):
    # حفظ الصورة بشكل جديد باسم "newImage.png"
    cv2.imwrite("newImage.png", img)

# إغلاق النافذة بعد الانتهاء
cv2.destroyAllWindows()
