from PIL import Image
import base64


def summary(a, b):
    return a + b


def generate_img(image_path):
    img = Image.new('RGB', (200, 200), 'black')
    img.save(image_path)


def encode_image(image_path):
    with open(image_path, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')

        return base64_message
