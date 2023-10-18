import requests
import urllib.parse
def req(id,passwd):
    requests.packages.urllib3.disable_warnings()
    url = 'https://192.168.2.190/userSense'
    data = {
        'user': f'{id}',
        'passwd': f'{(passwd)}',
        'submit': 'Login',
        'actualurl': 'https://192.168.2.190/userlogin/'
    }


    headers = {
        'Host': '192.168.2.190',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://192.168.2.190',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'autologer_v001',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://192.168.2.190/userlogin/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    response = requests.post(url, data=data, headers=headers,verify=False)

    print(response.status_code)
    if (response.status_code==200):
        if(response.text.find("Authentication Failed for  user")>0):
            print("Authentication Failed")
            return response.status_code,-1

        if(response.text.find("You have been successfully log in to IIT Bhubaneswar Network")>0):
            print("sucass")
            return response.status_code,0

        else :
            print("General failure:\n your data limit has been exhausted or multiple device are using your user_id")
            return response.status_code,-2
    else:
        return response.status_code,-69