import unittest
from resume_text_analizer.helpers.matchers import get_email, get_phone, get_name, get_collage


class MatcherTests(unittest.TestCase):

    def test_email_matcher(self):
        t1 = ["Email: deep@gmail.com"]
        t2 = ["Email: deep@gmail"]
        self.assertIsNotNone(get_email(t1))
        self.assertIsNone(get_email(t2))


    def test_phone_matcher(self):
        t1 = ["Phone:8001334960"]
        t2 = ["Phone:8001223"]
        self.assertIsNotNone(get_phone(t1))
        self.assertIsNone(get_phone(t2))

    def test_name_matcher(self):
        t1 = ["Name: Dev"]
        self.assertIsNotNone(get_name(t1))

    def test_collage_matcher(self):
        t1 = ["Collage: SKIT"]
        self.assertIsNotNone(get_collage(t1))


if __name__ =="__main__":
    unittest.main()