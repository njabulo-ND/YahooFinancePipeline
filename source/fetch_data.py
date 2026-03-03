import os
import requests
import json
from dotenv import load_dotenv

# Fetch stock statistics from Yahoo Finance API
# Current progress: data fetching completed, ready for processing
try:
    load_dotenv()                                           #Load API key from .env
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
    data = response.json()                                   # Convert JSON response to Python dictionary
except requests.exceptions.HTTPError:
    print("HTTP error (>400) received from API")
except requests.exceptions.ConnectionError:
    print("Cannot connect to API. Check URL or network.")
except ValueError:
    print("Failed to convert API response to dictionary")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except EnvironmentError as e:
    print(f"Environment error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")                         

with open(r'data/Raw_data.json',"w") as newjson_file:
    json.dump(data,newjson_file,indent=2)                       # Convert JSON response to Python dictionary