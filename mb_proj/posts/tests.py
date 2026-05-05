from django.test import TestCase # testcase module -> let's us create sample db
from .models import Post

class PostModelTest(TestCase):
    def setUp(self): # method "setUp" to create a new db with 1 entry, a post with a textfield containing a string
        Post.objects.create(text='just a test')

    # first test -> test_text_content => check that the db field contains actually just a test
    def test_text_content(self):
        post = Post.objects.get(id=1) # var => represents 1st id on the Post model
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, 'just a test')