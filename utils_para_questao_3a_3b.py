import cv2
from matplotlib import pyplot as plt
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
from sklearn.cluster import KMeans

def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_colors(image, number_of_colors, show_chart):

    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    # KMeans expects the input to be of two dimensions, so we use Numpy’s reshape function to reshape the image data.
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)

    clf = KMeans(n_clusters = number_of_colors)
    # We then fit and predict on the same image to extract the prediction into the variable labels.

    # fit_predict() is more relevant to unsupervised learning where we don't have labelled inputs
    labels = clf.fit_predict(modified_image)

    # conta a qtde de elementos presentes em cada cluster
    counts = Counter(labels)
    # print('counts before: ', counts)
    # sort to ensure correct color percentage
    counts = dict(sorted(counts.items()))
    # print('counts after: ', counts)

    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if (show_chart):
        plt.figure(figsize = (8, 6))
        plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)

    return rgb_colors
