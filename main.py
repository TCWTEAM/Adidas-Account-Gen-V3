import requests
import json
import time
import threading
import random
from classes import tools
proxyarr = []

def gen(threadnum, catchall, useproxies, num):
    threadnum = str(threadnum)
    print('[Thread {}] Starting Thread...'.format(threadnum))
    for i in range(int(num)):
        if useproxies == True:
            proxy = random.choice(proxyarr)
            try:
                proxytest = proxy.split(":")[2]
                userpass = True
            except IndexError:
                userpass = False
            if userpass == True:
                ip = proxy.split(":")[0]
                port = proxy.split(":")[1]
                userpassproxy = ip + ":" + port
                proxyuser = proxy.split(":")[2].rstrip()
                proxypass = proxy.split(":")[3].rstrip()
            if userpass == True:
                proxies = {'http': 'http://' + proxyuser + ':' + proxypass + '@' + userpassproxy, 'https': 'http://' + proxyuser + ':' + proxypass + '@' + userpassproxy}
            if userpass == False:
                proxies = {'http': 'http://' + proxy, 'https': 'http://' + proxy}
        
        fullname = tools.genName()
        password = tools.password()
        aemail = tools.email(fullname.split(" ")[0], catchall)


        s = requests.session()
        doby = str(random.randint(1960, 1997))
        dobm = random.randint(1, 12)
        if dobm < 10:
            dobm = "0{}".format(str(dobm))
        else:
            dobm = str(dobm)
        
        dobd = random.randint(1, 28)
        if dobd < 10:
            dobd = "0{}".format(str(dobd))
        else:
            dobd = str(dobd)
        
        dob = "{}-{}-{}".format(doby, dobm, dobd)
        json1 = {
            "clientId": "1ffec5bb4e72a74b23844f7a9cd52b3d",
            "actionType": "REGISTRATION",
            "email": aemail,
            "password": password,
            "countryOfSite": "US",
            "dateOfBirth": dob,
            "minAgeConfirmation": "Y",
            "firstName": fullname.split(" ")[0],
            "lastName": fullname.split(" ")[1]
        }
        if useproxies == True:
            r1 = s.post("https://apim.scv.3stripes.net/scvRESTServices/account/createAccount", json=json1, proxies=proxies)
        else:
            r1 = s.post("https://apim.scv.3stripes.net/scvRESTServices/account/createAccount", json=json1)
        if "iCCD_CRT_ACCT_0001" in r1.text:
            with open("accs.txt", "a+") as f:
                f.write("{}:{}".format(aemail, password))
            print('[Thread {}] Successfully Created Account!'.format(threadnum))
        else:
            print("[Thread {}] There was an error creating your account {}".format(threadnum, r1.text))


if __name__ == '__main__':
    print("_____       .___.__    .___                 ________")              
    print("/  _  \    __| _/|__| __| _/____    ______  /  _____/  ____   ____") 
    print("/  /_\  \  / __ | |  |/ __ |\__  \  /  ___/ /   \  ____/ __ \ /    /") 
    print("/    |    \/ /_/ | |  / /_/ | / __ \_\___ \  \    \_\  \  ___/|   |  /")
    print("\____|__  /\____ | |__\____ |(____  /____  >  \______  /\___  >___|  /")
    print("        \/      \/         \/     \/     \/          \/     \/     \/")
    print("")
    print("By XO | xodev.io | @ehxohd | TCWTEAM")
    print("Yes I'm using Euph's endpoint")
    print("")
    catchall = input("Catch-All Domain: ")
    num = input("# Of Entries Per Thread: ")
    threadn = input("# Of Threads: ")
    with open("proxies.txt", "r") as file:
        if len(file.read().splitlines()) < 1:
            useproxies = False
        else:
            useproxies = True
            for prox in file.read().splitlines():
                proxyarr.append(prox)
            print("USING PROXIES")
    
    tc = 0
    for x in range(int(threadn)):
        tc += 1
        t = threading.Thread(target=gen, args=(tc, catchall, useproxies, num))
        t.start()
        time.sleep(random.randint(1, 3))
