import requests
import json 

#Pulling the data from the API at Yahoo
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v4/get-statistics"

queryParameters = {"symbol":"AMRN","region":"US","lang":"en-US"}

headers = {
	"x-rapidapi-key": "API_KEY",
	"x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}
try:
    response =  requests.get(url, headers=headers, params=queryParameters)
    print("Status code:", response.status_code)
    response.raise_for_status()
    data = response.json()
    #print(data)
except requests.exceptions.HTTPError:
    print("Resonse: > 400")
except requests.exceptions.ConnectionError:
    print("Cant connect to Api")
except requests.exceptions.RequestException as e:
    print(f"Error occured: {e}")
except ValueError:
    print("Cant be converted to json")
#Making the pulled data readable 
#print(json.dumps(data,indent=2))
