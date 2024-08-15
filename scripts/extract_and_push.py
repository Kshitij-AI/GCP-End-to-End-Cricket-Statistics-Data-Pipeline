import sys
import json
import requests
import pandas as pd

# Fetch cricket statistics for cricbuzz API using https://rapidapi.com/
def get_data_from_api(format):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

    querystring = {"formatType":format}

    headers = {
        "x-rapidapi-key": "53b026a7fbmsh487e8f69a5c3732p15f695jsn9f32db55a494",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response

# Create DataFrame
def create_dataframe(df, data, format):
    data = data['rank']
    df_temp = []
    for item in data:
        record = {
            'rank': item.get('rank'),
            'name': item.get('name'),
            'country': item.get('country'),
            'rating': item.get('rating'),
            'avg': item.get('avg'),
            'format': format.upper()
        }
        df_temp.append(record)

    df_temp = pd.DataFrame(df_temp)
    df = pd.concat([df, df_temp], ignore_index=True)

    return df

# Push CSV file to GCS
def push_data_to_gcs(csv_file):
    from google.cloud import storage
    print('Pushing data to GCS bucket!!')
    project_id = 'solid-binder-431511-d6'
    bucket_name = 'cricbuzz_stats'
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(csv_file)
    blob.upload_from_filename(csv_file)

if __name__=='__main__':

    df = pd.DataFrame()
    formats = ['odi', 'test', 't20']

    for format in formats:
        # Fetching cricket statistics from Cricbuzz API
        response = get_data_from_api(format)

        # Check if the request was successful
        if response.status_code == 200:

            # Convert the JSON response to a Python dictionary
            data = response.json()
            csv_file = 'player_stats.csv'

            if data:
                print(f"{format} data fetched successfully!!")

                # Creating DataFrame
                df = create_dataframe(df, data, format)
            else:
                print("No data from API!!")
                sys.exit()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}, Message: {response.text}")
            sys.exit()

    # Write Data in CSV
    df.to_csv(csv_file, index=False, header=False)
    print(f"Data written to '{csv_file}'")

    # Pushing data to GCS
    push_data_to_gcs(csv_file)
    print(f"'{csv_file}' pushed to GCS bucket successfully!!'")