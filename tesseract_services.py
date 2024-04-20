import pytesseract
from PIL import Image
from pillow_services import del_image


def get_phone():
    pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERSCT_PATH")
    phone = pytesseract.image_to_string(Image.open('cropped_image.png'))
    del_image('cropped_image.png')
    return phone[:-1]


if __name__ == '__main__':
    get_phone()
