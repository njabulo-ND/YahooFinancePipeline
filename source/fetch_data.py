import requests
import json
from dotenv import load_dotenv
import os
# Pulling the data from the API at Yahoo

try:
    load_dotenv()  # loading the key i got from yahoo from the .env for privacy of the key
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
    data = response.json()
    print(json.dumps(data,indent=2))
except requests.exceptions.HTTPError:
    print("Response: > 400")
except requests.exceptions.ConnectionError:
    print("Cant connect to Api\nMake sure the url aligns")
except ValueError:
    print("Cant be converted to json format")
except requests.exceptions.RequestException as e:
    print(f"Error occured: {e}")
except EnvironmentError as e:
    print(f"Error occured: {e}")
except json.JSONDecodeError as e:
    print(f'Error occured: {e}')
except Exception as e:
    print(f"Error occured: {e}")
# Making the pulled data readable
# print(json.dumps(data,indent=2))
