import requests


class RandomUser:
    def get_user(self):
        return requests.get("https://randomuser.me/api/").json()["results"][0]

    def get_users(self, number_of_users):
        if type(number_of_users) != int:
            raise TypeError("Number of users is not an integer!")
        return requests.get("https://randomuser.me/api/?results=" + str(number_of_users)).json()["results"]

    def get_user_by_gender(self, gender):
        if gender != "male" and gender != "female":
            raise ValueError("Gender is not male or female!")
        return requests.get("https://randomuser.me/api/?gender=" + gender).json()["results"][0]

    def get_user_by_seed(self, seed):
        response = requests.get("https://randomuser.me/api/?seed=" + seed)
        if not response.ok:
            raise ValueError("Seed doesn't exist!")
        return response.json()["results"][0]
