import unittest
from unittest.mock import *

from src.zad01.main import RandomUser


class RandomUserTest(unittest.TestCase):
    def setUp(self):
        self.randomUser = RandomUser()

    def test_get_user(self):
        self.randomUser.get_user = MagicMock(return_value={})
        self.assertIsInstance(self.randomUser.get_user(), dict)

    def test_get_users(self):
        self.randomUser.get_users = MagicMock(side_effect=lambda number: [{} for _ in range(number)])
        self.assertEqual(10, len(self.randomUser.get_users(10)))

    def test_get_user_by_gender(self):
        self.randomUser.get_user_by_gender = MagicMock(side_effect=lambda gender: {"gender": gender})
        self.assertEqual("female", self.randomUser.get_user_by_gender("female")["gender"])

    def test_get_user_by_seed(self):
        self.randomUser.get_user_by_seed = MagicMock(return_value={"location": {"city": "Taupo"}})
        self.assertEqual("Taupo", self.randomUser.get_user_by_seed("5b49cdf1bea27daa")["location"]["city"])

    def test_get_users_exception(self):
        self.randomUser.get_users = MagicMock(
            side_effect=lambda number: exec("raise TypeError('Number of users is not an integer!')") if type(
                number) != int else [{} for _ in range(number)])
        with self.assertRaisesRegex(TypeError, "Number of users is not an integer!"):
            self.randomUser.get_users("10")

    def test_get_user_by_gender_exception(self):
        self.randomUser.get_user_by_gender = MagicMock(side_effect=lambda gender: exec(
            "raise ValueError('Gender is not male or female!')") if gender != "male" and gender != "female" else {
            "gender": gender})
        with self.assertRaisesRegex(ValueError, "Gender is not male or female!"):
            self.randomUser.get_user_by_gender("")

    def test_get_user_by_seed_exception(self):
        self.randomUser.get_user_by_seed = MagicMock(side_effect=ValueError("Seed doesn't exist!"))
        with self.assertRaisesRegex(ValueError, "Seed doesn't exist!"):
            self.randomUser.get_user_by_seed("seed")

    def tearDown(self):
        self.randomUser = None
