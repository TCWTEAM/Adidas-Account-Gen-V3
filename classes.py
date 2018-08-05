import random
import time
import string
import names
import requests

class tools():

    def email(firstname, catchall):
        #take notes ethan
        addon = ''
        for x in range(random.randint(3, 5)):
            addon = addon + random.choice(string.ascii_letters)
        addon2 = str(random.randint(111, 999))
        res = "{}{}{}@{}".format(firstname, addon, addon2, catchall.replace("@", ""))
        return res
    
    def genName():
        firstname = names.get_first_name()
        lastname = names.get_last_name()

        return firstname + " " + lastname

    def password():
        r = requests.get("https://passwordwolf.com/api/").json()[0]['password']
        return r