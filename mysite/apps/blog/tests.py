from django.http import HttpRequest
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

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>My Blog</title>', html)
        # self.assertTrue(html.endswith('</html>'))