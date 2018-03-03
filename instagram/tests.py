from django.test import TestCase
from .models import Image,tags
# Create your tests here.
def setUp(self):
    self.family = Image(image_name ='Family',image_caption = 'I love you daddy', comments='You two look amazing in blue')

# testing instance
def test_instance(self):
    self.assertTrue(isinstance(self.family,Image))