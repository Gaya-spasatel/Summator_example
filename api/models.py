from django.db import models


# Create your models here.
class Summator:
    def __init__(self, first_operand, second_operand, result):
        self.first_operand = first_operand
        self.second_operand = second_operand
        self.result = result
        self.operation = '+'


class ImageFromPillow:
    def __init__(self, image_base64, encoding):
        self.image_base64 = image_base64
        self.encoding = encoding
