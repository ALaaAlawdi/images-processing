# رسم خطوط على الصورة

import numpy as np
import cv2
from matplotlib import pyplot as plt

# قراءة الصورة
img = cv2.imread('./galaxy_leader.jpg')

# عكس الألوان من BGR إلى RGB
b, g, r = cv2.split(img)  # الحصول على القنوات اللونية B, G, R
img = cv2.merge([r, g, b])  # تحويلها إلى ترتيب لون RGB

# رسم مستطيل أزرق قطري بسماكة 3 بكسل
cv2.rectangle(img, (400, 35), (570, 160), (0, 0, 255), 3)

# عرض الصورة
plt.imshow(img)
plt.show()

# أحداث الفأرة ليست مهمة في هذا السياق
# المهم هو فهم كيفية تغيير قيم البكسل
