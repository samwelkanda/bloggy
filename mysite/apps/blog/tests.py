from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):

    def test_monkey_math(self):
        self.assertEqual(1 + 2, 4)