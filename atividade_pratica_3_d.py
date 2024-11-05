import cv2

path1 = 'images-cme/CME_13_1.jpg'
path3 = 'images-cme/CME_13_3.jpg'

cme_img_1 = cv2.imread('images-cme/CME_13_1.jpg')
cme_img_3 = cv2.imread('images-cme/CME_13_3.jpg')

cme_img_1 = cv2.cvtColor(cme_img_1, cv2.COLOR_BGR2GRAY)
cme_img_3 = cv2.cvtColor(cme_img_3, cv2.COLOR_BGR2GRAY)

sobel_x_1 = cv2.Sobel(cme_img_1, cv2.CV_64F, 1, 0)
sobel_y_1 = cv2.Sobel(cme_img_1, cv2.CV_64F, 0, 1)

sobel_x_3 = cv2.Sobel(cme_img_3, cv2.CV_64F, 1, 0)
sobel_y_3 = cv2.Sobel(cme_img_3, cv2.CV_64F, 0, 1)

if sobel_x_1.mean() > sobel_y_1.mean():
    print(f'A ferramenta da imagem {path1} está na horizontal')

else:
    print(f'A ferramenta da imagem {path1} está na vertical')

if sobel_x_3.mean() > sobel_y_3.mean():
    print(f'A ferramenta da imagem {path3} está na horizontal')

else:
    print(f'A ferramenta da imagem {path3} está na vertical')


