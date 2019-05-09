from PIL import Image
import numpy
import io
from urllib.request import urlopen
from skimage.measure import compare_ssim as get_ssim

def fetch_image_data(image_url):
    fd = urlopen(image_url)
    return io.BytesIO(fd.read())

def fetch_similarity_score(image_1, image_2):
    '''
    parameters: image_1,image_2 are the urls of the images on cloudinary
    retuns: similarity_score between both the image
    '''
    # open the image from the url and resize them so the both the images have same dimensions
    img_1 = Image.open(fetch_image_data(image_1)).resize((300, 300), Image.ANTIALIAS)
    img_2 = Image.open(fetch_image_data(image_2)).resize((300, 300), Image.ANTIALIAS)
    # get the structural similarity index between both the images
    score = get_ssim(numpy.array(img_1), numpy.array(img_2), multichannel=True)# multi channel should be set to False if B/W image
    return score
    # pairs = zip(img_1.getdata(), img_2.getdata())
    # if len(img_1.getbands()) == 1:
    #     # for gray-scale jpegs
    #     dif = sum(abs(p1-p2) for p1,p2 in pairs)
    # else:
    #     dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    # ncomponents = img_1.size[0] * img_1.size[1] * 3
    # return (dif / 255.0 * 100) / ncomponents