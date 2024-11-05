import cv2

path1 = 'images-cme/CME_13_1.jpg'
path2 = 'images-cme/CME_13_2.jpg'
path3 = 'images-cme/CME_13_3.jpg'

cme_img_1 = cv2.imread('images-cme/CME_13_1.jpg')
cme_img_2 = cv2.imread('images-cme/CME_13_2.jpg')
cme_img_3 = cv2.imread('images-cme/CME_13_3.jpg')

cme_img_1 = cv2.cvtColor(cme_img_1, cv2.COLOR_BGR2RGB)
cme_img_2 = cv2.cvtColor(cme_img_2, cv2.COLOR_BGR2RGB)
cme_img_3 = cv2.cvtColor(cme_img_3, cv2.COLOR_BGR2RGB)

canny_image_1 = cv2.Canny(cme_img_1, 100, 200)
canny_image_2 = cv2.Canny(cme_img_2, 100, 200)
canny_image_3 = cv2.Canny(cme_img_3, 100, 200)

if canny_image_1.mean() < 1:
    print(f'A imagem {path1} está borrada')

if canny_image_2.mean() < 1:
    print(f'A imagem {path2} está borrada')

if canny_image_3.mean() < 1:
    print(f'A imagem {path3} está borrada')



