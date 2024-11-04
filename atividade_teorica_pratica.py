import cv2
import numpy as np


image_org = cv2.imread('images/cameraman.bmp')

horizontal_kernel = np.array(([1/3, 1/3, 1/3]))
vertical_kernel = np.array(([1/3], [1/3], [1/3]))

kernel_multiplicada = horizontal_kernel * vertical_kernel

image_horizontal = cv2.filter2D(src=image_org, ddepth=-1, kernel=horizontal_kernel)
image_vertical = cv2.filter2D(src=image_horizontal, ddepth=-1, kernel=vertical_kernel)
image_multiplicada = cv2.filter2D(src=image_org, ddepth=-1, kernel=kernel_multiplicada)

cv2.imwrite('resultado-atividade-teorica-pratica/image_horizontal.png', image_horizontal)
cv2.imwrite('resultado-atividade-teorica-pratica/image_vertical.png', image_vertical)
cv2.imwrite('resultado-atividade-teorica-pratica/image_multiplicada.png', image_multiplicada)



