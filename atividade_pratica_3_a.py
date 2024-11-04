import cv2
from matplotlib import pyplot as plt

cme_img_1 = cv2.imread('images-cme/CME_13_1.jpg')
cme_img_2 = cv2.imread('images-cme/CME_13_2.jpg')
cme_img_3 = cv2.imread('images-cme/CME_13_3.jpg')

cme_img_1 = cv2.cvtColor(cme_img_1, cv2.COLOR_BGR2RGB)
cme_img_2 = cv2.cvtColor(cme_img_2, cv2.COLOR_BGR2RGB)
cme_img_3 = cv2.cvtColor(cme_img_3, cv2.COLOR_BGR2RGB)

hsv_img_1 = cv2.cvtColor(cme_img_1, cv2.COLOR_RGB2HSV)
hsv_img_2 = cv2.cvtColor(cme_img_2, cv2.COLOR_RGB2HSV)
hsv_img_3 = cv2.cvtColor(cme_img_3, cv2.COLOR_RGB2HSV)

green_mask = (85, 50, 50)
green_mask_max = (105, 255, 255)

mask1 = cv2.inRange(hsv_img_1, green_mask, green_mask_max)
mask2 = cv2.inRange(hsv_img_2, green_mask, green_mask_max)
mask3 = cv2.inRange(hsv_img_3, green_mask, green_mask_max)

plt.subplot(1, 3, 1)
plt.imshow(mask1)
plt.subplot(1, 3, 2)
plt.imshow(mask2)
plt.subplot(1, 3, 3)
plt.imshow(mask3)
plt.show()
