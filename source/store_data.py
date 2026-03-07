import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import urllib.parse
import json

try:
    #Database Configuration & Connection Parameters
    name_0f_sever = r"njabulo\SQLEXPRESS"
    name_of_db = 'ARMNWAREHOUSE'
    name_of_driver = r'ODBC Driver 17 for SQL Server'

    #Constructing the connection string for Windows Authentication
    connection_string = (
        f"DRIVER={{{name_of_driver}}};"
        f"SERVER={name_0f_sever};"
        f"DATABASE={name_of_db};"
        f"Trusted_Connection=yes;"
    )

    #Create SQLAlchemy engine
    refined_connection = urllib.parse.quote_plus(connection_string)
    the_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={refined_connection}")

    #Load JSON data and convert to DataFrame
    with open(r"data\Cleaned_data.json",'r') as jsondata:
        dict_data = json.load(jsondata)
    dict_data = [dict_data]
    df = pd.DataFrame(dict_data)

    #Final Loading to data warehouse on SSMS
    df.to_sql(name='ARMN_Statistics',con=the_engine,if_exists='replace',index=False)

except OSError:
    print(f"Error occured:\n\tFile not found!")
except (json.JSONDecodeError,SQLAlchemyError,Exception) as e:
    print(f"Error Occured:\n\t{e}")