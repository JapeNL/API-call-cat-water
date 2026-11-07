import requests, json, duckdb
from datetime import datetime, timedelta
    
# The API endpoint with datetime now -36 hrs
d = datetime.today() - timedelta(hours=36)
d = d.strftime("%Y-%m-%d")
url = f"https://analisi.transparenciacatalunya.cat/api/odata/v4/gn9e-3qhr?$filter=dia eq '{d}T00:00:00.000'"


response = requests.get(url)

if response.ok: 

    # Print the response
    print(response.json())
    print(response.url)

    # Write to file with date of filter parameter as filename
    with open(f'data-{d}.json', 'w') as f:
        json.dump(response.json(), f, ensure_ascii=True, indent=4, sort_keys=True)


    # Connect to the DB  
    con = duckdb.connect('catwaterlevel.duckdb')

    # Check if today(-36hrs) is already in the DB
    last_date_imported = con.execute(f"""SELECT strftime(MAX(dia), '%Y-%m-%d') FROM reservoirs_levels""").fetchone()
    print(last_date_imported[0])

    if last_date_imported != None and last_date_imported[0] != d:
        # Import the json data into local duckdb
        con.execute(f"""
        INSERT INTO reservoirs_levels
        SELECT r.* FROM (
            SELECT unnest(value) AS r
            FROM read_json('data-{d}.json', columns = {{
                value: 'STRUCT(__id VARCHAR, dia TIMESTAMP, estaci VARCHAR,
                                nivell_absolut DOUBLE, percentatge_volum_embassat DOUBLE,
                                volum_embassat DOUBLE)[]'
            }})
        )
        """)
    else:
        print(f"Data already imported for date: {d}")    

    # Close the DB connection
    con.close()

else:

    # Print error code and url
    print(f"Request error, response code: {response.status_code}")
    print(response.url)