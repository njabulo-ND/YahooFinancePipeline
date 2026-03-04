import json
from datetime import datetime, UTC

# EXTRACTING FROM RAW JSON AND VALIDATING
try:
    with open(r'data/Raw_data.json', 'r') as data_pulled_from_json_file:
        data = json.load(data_pulled_from_json_file)
    if 'quoteSummary' not in data.keys():
        raise ValueError("Value 'quoteSummary' is missing")
    else:
        Qsummary = data['quoteSummary']
    if 'error' in Qsummary.keys() and Qsummary.get('error') is None:
        pass
    else:
        raise ValueError(f"Status Error:{Qsummary['error']}")
    if 'result' not in Qsummary:
        raise ValueError("Value 'result' is missing")
    else:
        results = Qsummary['result']
    if isinstance(results, list) and len(results) == 0:
        raise ValueError("No results found")
    if results[0].get('defaultKeyStatistics') is not None:
        YahooStats = results[0]['defaultKeyStatistics']
        print(f"Statistics found!!")
    else:
        raise ValueError('Statistics are missing')

except json.JSONDecodeError as e:
    print(f"Error found: {e}")
except FileNotFoundError:
    print("raw data not found")
except ValueError as e:
    print(f"'Error found: {e}")
except Exception as e:
    print(f"Error found: {e}")

# TRANSFORMING AND CLEANING
try:
    for key, value in YahooStats.items():
        if isinstance(value, dict) and value.get('raw') is not None:
            if any(trigger in key.lower() for trigger in ['date', 'end', 'quarter', 'inception', 'report', 'dividend']):
                raw_date = value.get('raw')
                date2_obj = datetime.fromtimestamp(raw_date, UTC)
                date2_str = date2_obj.strftime(r"%d-%m-%Y")
                YahooStats[key] = {'raw': date2_str}
            elif isinstance(value.get('raw'), float):
                data = round(value.get('raw'), 2)
                YahooStats[key] = {'raw': data}
            else:
                data = value.get('raw')
                YahooStats[key] = {'raw': data}
        elif isinstance(value, (dict, list, tuple, set)) and len(value) == 0:
            YahooStats[key] = None
    print('Processed Successfully!!\n')
    important_keys_for_analysis = [
        "enterpriseValue",
        "forwardPE",
        "priceToBook",
        "profitMargins",
        "beta",
        "sharesOutstanding",
        "lastFiscalYearEnd",
    ]
    yahoo_missing_keys = set([key.lower() for key in important_keys_for_analysis]).difference(
        set([key.lower() for key in list(YahooStats.keys())]))
    YahooStats_cleaned = {
        key: YahooStats[key].get('raw') if isinstance(
            YahooStats[key], dict) else YahooStats.get(key)
        for key, _ in YahooStats.items()
        if any(key.lower() == important_key.lower() for important_key in important_keys_for_analysis)
    }
    if len(yahoo_missing_keys) != 0:
        for key in list(yahoo_missing_keys):
            YahooStats_cleaned.update({key: None})
    print("FIltered Successfully!\nOnly important data left\n")
    snapshort = datetime.now()
    metadata = {"symbol": "AMRN",
                "extraction_date": snapshort.strftime(r"%Y-%m-%d  %H:%M"),
                "data_source": "Yahoo Finance API"}
    YahooStats_cleaned.update(metadata)
    print("Metadata updated Successfully!\n")
except json.JSONDecodeError as e:
    print(f"Error found: {e}")
except ValueError as e:
    print(f"'Error found: {e}")
except Exception as e:
    print(f"Error found: {e}")

# LOADING CLEAN DATA
try:
    with open(r"data/Cleaned_Data.json", 'w') as File_to_Load_to:
        json.dump(dict(sorted(YahooStats_cleaned.items())),File_to_Load_to, indent=2)
    print("Loaded Successfully to Cleaned_data.json file")
except FileNotFoundError:
    print("File not found!!")
except json.JSONDecodeError as e:
    print(f"Error ocurred: {e}")
