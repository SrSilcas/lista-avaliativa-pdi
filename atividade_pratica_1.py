import cv2

img = cv2.imread('images/tools.bmp')

image_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
filter_min = (0, 0, 215)
filter_max = (150, 150, 255)

mask = cv2.inRange(image_hsv, filter_min, filter_max)
filter_morph = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

erode_image = cv2.erode(mask, filter_morph, iterations=1)
negative_image = ~ erode_image

erode_image_negative = cv2.erode(negative_image, filter_morph, iterations=2)

dilate_image = cv2.dilate(erode_image_negative, filter_morph, iterations=5)

number_labels, labels = cv2.connectedComponents(dilate_image)
print(f'O numero de ferramentas nessa imagem é de: {number_labels - 1}')

cv2.imwrite('resultado-atividade-pratica1/mask.png', mask)
cv2.imwrite('resultado-atividade-pratica1/erode_image.png', erode_image)
cv2.imwrite('resultado-atividade-pratica1/negative_image.png', negative_image)
cv2.imwrite('resultado-atividade-pratica1/erode_image_negative.png', erode_image_negative)
cv2.imwrite('resultado-atividade-pratica1/dilate_image.png', dilate_image)
