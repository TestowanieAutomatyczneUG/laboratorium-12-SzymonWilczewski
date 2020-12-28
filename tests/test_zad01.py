import unittest

from src.zad01.main import RandomUser


class RandomUserTest(unittest.TestCase):
    def setUp(self):
        self.randomUser = RandomUser()

    def test_get_user(self):
        self.assertIsInstance(self.randomUser.get_user(), dict)

    def test_get_users(self):
        self.assertEqual(10, len(self.randomUser.get_users(10)))

    def test_get_user_by_gender(self):
        self.assertEqual("female", self.randomUser.get_user_by_gender("female")["gender"])

    def test_get_user_by_seed(self):
        self.assertEqual("Taupo", self.randomUser.get_user_by_seed("5b49cdf1bea27daa")["location"]["city"])

    def test_get_users_exception(self):
        with self.assertRaisesRegex(TypeError, "Number of users is not an integer!"):
            self.randomUser.get_users("10")

    def test_get_user_by_gender_exception(self):
        with self.assertRaisesRegex(ValueError, "Gender is not male or female!"):
            self.randomUser.get_user_by_gender("")

    def test_get_user_by_seed_exception(self):
        with self.assertRaisesRegex(ValueError, "Seed doesn't exist!"):
            self.randomUser.get_user_by_seed("seed")

    def tearDown(self):
        self.randomUser = None
