from django.urls import reverse
from rest_framework.test import APITestCase


class SummatorTests(APITestCase):
    def test_summ_correct(self):
        """
        Ensure that summary operation with correct operands works
        """
        url = reverse('summator', args=[1, 2])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "first_operand": 1,
            "second_operand": 2,
            "result": 3,
            "operation": "+"
        })
