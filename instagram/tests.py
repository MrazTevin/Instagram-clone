from django.test import TestCase
from .models import Image,tag
# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.family = Image(image_name = 'Family',image_caption='hanging out with my two lovely kids',comments='awesome')

    def test_instance(self):
        self.assertTrue(isinstance(self.family,Image))
    
    # Testing Save Method
    def test_save_method(self):
        self.family.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0) 
    
    def test_delete_method(self):
        self.family = Image(image_name='family')
        self.family.save_image()
        self.family.delete_image()
        image = Image.objects.all() 
        self.assertFalse(image)
        
    # def test_update_caption(self):
    #     self.hilarious = Image.objects.create(image_caption='hilarious')
    #     self.gorgeous = Image.objects.create(image_caption='gorgeous')
    #     self.hilarious.save_image()
    #     self.gorgeous.delete_image()
    #     self.hilarious.update_caption()
    #     image = Image.objects.all()
    #     self.assertEqual(True,image)
    
    def get_image(self,id):
        image = Image.objects.all()
        return image[:1]
