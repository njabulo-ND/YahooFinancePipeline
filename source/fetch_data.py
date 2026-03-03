import requests
import json
from dotenv import load_dotenv
import os

# Pulling the data from the API at Yahoo
try:
    load_dotenv()                                           # loading the key i got from yahoo from the .env for privacy of the key
    API_KEY = os.environ.get('API_KEY')
    if not API_KEY:
        raise EnvironmentError("Key was not found on the env file / variable assignment dont align")
    else:
        print("Key Found!!")
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v4/get-statistics"

    queryParameters = {"symbol": "AMRN", "region": "US", "lang": "en-US"}

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=queryParameters)
    print("Status code:", response.status_code)
    response.raise_for_status()
    data = response.json()                                   #Converting data to a dictionary from json
except requests.exceptions.HTTPError:
    print("Response: > 400")                                 #Handling the raise for status function
except requests.exceptions.ConnectionError:
    print("Cant connect to Api\nMake sure the url aligns")   #Handling the get function Error wil be triggered if the url is not reachable
except ValueError:
    print("Cant be converted to dictionary format")          #handling the converntion from raw json to dictionary
except requests.exceptions.RequestException as e:
    print(f"Error occured: {e}")                              #Any Error other than above errors
except EnvironmentError as e:
    print(f"Error occured: {e}")                              #Handling the fetching of the key from .env file if key is not found                            
except Exception as e:
    print(f"Error occured: {e}")                             #If there is any error at all other than the ones above

with open('Raw_data.json',"w") as newjson_file:
    json.dump(data,newjson_file,indent=2)                              #Sending data to a json file to be ready for processing 