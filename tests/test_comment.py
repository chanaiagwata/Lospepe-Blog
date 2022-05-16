import unittest
from app.models import Blogs, User, Comment

class TestBlog(unittest.TestCase):
    
    def setUp(self):
        self.user_Chanai = User(first_name = "Chanai",
                                last_name = "Agwata",
                                username = "ochot-odong",
                                password = "268231",
                                email = "chanaiagwata82@mail.com")
        self.new_blog = Blogs(post_title = "Blog Title",
                            blog_content = "Hallo World",
                            user_id = self.user_Chanai.id)
        self.new_comment = Comment(comment = "I like this",
                                    blog_id = self.new_blog.id,
                                    user_id = self.user_Chanai.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Chanai, User))
        self.assertTrue(isinstance(self.new_blog, Blogs))
        self.assertTrue(isinstance(self.new_comment, Comment))