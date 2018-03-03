from django.test import TestCase
from .models import Image,tags
# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.family = Image(image_name = 'Family',image_caption='hanging out with my two lovely kids',comments='awesome')

    def test_instance(self):
        self.assertTrue(isinstance(self.family,Image))
    