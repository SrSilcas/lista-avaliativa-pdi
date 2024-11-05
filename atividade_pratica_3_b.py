import cv2
from utils_para_questao_3a_3b import get_colors

path1 = 'images-cme/CME_13_1.jpg'
path2 = 'images-cme/CME_13_2.jpg'
path3 = 'images-cme/CME_13_3.jpg'

cme_img_1 = cv2.imread('images-cme/CME_13_1.jpg')
cme_img_2 = cv2.imread('images-cme/CME_13_2.jpg')
cme_img_3 = cv2.imread('images-cme/CME_13_3.jpg')

cme_img_1 = cv2.cvtColor(cme_img_1, cv2.COLOR_BGR2RGB)
cme_img_2 = cv2.cvtColor(cme_img_2, cv2.COLOR_BGR2RGB)
cme_img_3 = cv2.cvtColor(cme_img_3, cv2.COLOR_BGR2RGB)

hsv_img_1 = cv2.cvtColor(cme_img_1, cv2.COLOR_RGB2HSV)
hsv_img_2 = cv2.cvtColor(cme_img_2, cv2.COLOR_RGB2HSV)
hsv_img_3 = cv2.cvtColor(cme_img_3, cv2.COLOR_RGB2HSV)

green_mask = (85, 30, 30)
green_mask_max = (180, 255, 240)

mask1 = cv2.inRange(hsv_img_1, green_mask, green_mask_max)
mask2 = cv2.inRange(hsv_img_2, green_mask, green_mask_max)
mask3 = cv2.inRange(hsv_img_3, green_mask, green_mask_max)

correct_area1 = cv2.bitwise_and(cme_img_1, cme_img_1, mask=mask1)
correct_area2 = cv2.bitwise_and(cme_img_2, cme_img_2, mask=mask2)
correct_area3 = cv2.bitwise_and(cme_img_3, cme_img_3, mask=mask3)

graphic_information1 = get_colors(correct_area1, 2, True)
graphic_information2 = get_colors(correct_area2, 2, True)
graphic_information3 = get_colors(correct_area3, 2, True)

if graphic_information1[0][0] < 6 and graphic_information1[1][0] < 6:
    print(f"Imagem {path1} não possui um instrumento medico")

if graphic_information2[0][0] < 6 and graphic_information2[1][0] < 6:
    print(f"Imagem {path2} não possui um instrumento medico")

if graphic_information3[0][0] < 6 and graphic_information3[1][0] < 6:
    print(f"Imagem {path3} não possui um instrumento medico")

