from django.test import TestCase
from django.urls import resolve

from .views import post_list

# Create your tests here.
class SmokeTest(TestCase):

    def test_monkey_math(self):
        self.assertEqual(1 + 2, 3)

class BlogHomePageTest(TestCase):

    def test_blog_homepage_resolves(self):
        found = resolve('/blog/')
        self.assertEqual(found.func, post_list)
