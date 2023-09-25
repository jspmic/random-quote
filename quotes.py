import sys
import json
import requests

def quote_API(api_key:str, category:str) -> None:
    #Setting up the parameters and headers
    header = {"X-Api-Key": api_key} #Use your api-key
    addr = "https://api.api-ninjas.com/v1/quotes" #Default address
    params = {"category":category}

    #Making the GET request
    resp = requests.get(addr,params=params,headers=header)

    #Response is str so, unpack it using json
    quote_resp = json.loads(resp.text)

    #Response form [{...}]
    if resp.status_code == requests.codes.ok:
        print("\n",quote_resp[0]["quote"])
        print(f"\n- {quote_resp[0]['author']}\n")
    else:
        print("Bad things happened! try again")

if __name__== "__main__":
    api_key = open("api_key").read().strip()
    category = input("Category(leave empty if needed): ").lower()
    quote_API(api_key,category)
    sys.exit(0)
