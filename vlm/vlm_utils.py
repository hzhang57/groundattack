
from PIL import Image
from io import BytesIO
import requests


def load_image(image_file):
    ## 支持url和本地路径
    ## 读取单张图片
    if image_file.startswith("http") or image_file.startswith("https"):
        response = requests.get(image_file)
        image = Image.open(BytesIO(response.content)).convert("RGB")
    else:
        image = Image.open(image_file).convert("RGB")
    return image


