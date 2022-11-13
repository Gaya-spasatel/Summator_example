from django.db import models


# Create your models here.
class Summator:
    def __init__(self, first_operand, second_operand, result):
        self.first_operand = first_operand
        self.second_operand = second_operand
        self.result = result
        self.operation = '+'
