import cv2


image = cv2.imread('images/alumgrns.bmp')

image_passa_alta = cv2.Canny(image, 30, 150)

numbers_labels, _ = cv2.connectedComponents(image_passa_alta)
print(f'A quantidade de tonalidade de cinza diferentes encontradas na foto foram {numbers_labels - 1} cores')

