from random import Random
import csv

class PasswordGeneration:
    def __init__(self):
        self.strength = 'weak'


    def random_str(self, randomlength=8):
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            str += chars[random.randint(0, length)]
        return str


    def password_generation(self, length = 100000):
        random = Random()

        with open('strong.csv','wb') as csvfiles:
            csvwriter = csv.writer(csvfiles)
            for i in range(length):
                password = self.random_str(random.randint(8,12))
                csvwriter.writerow([password, 1])
        return 1


password_generation = PasswordGeneration()

password_generation.password_generation()

