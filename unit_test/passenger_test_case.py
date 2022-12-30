from unittest import TestCase
from project1.utilclass import validate_number


class TestPassengerDetails(TestCase):
    def test_input_contact(self):
        output = validate_number("8778417447")
        self.assertEqual(output, True)







