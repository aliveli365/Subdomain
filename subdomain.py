import requests


domain = input("domain gir:")
file = open ("common.txt","r")

content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"

    try :
        requests.get(url)

    except ConnectionError:
        pass

    else:
        print("(+) bulundu : ",url)
