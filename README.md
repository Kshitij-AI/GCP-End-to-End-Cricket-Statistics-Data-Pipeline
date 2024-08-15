# GCP-End-to-End: Cricket Stats Data Pipeline

## Overview

This project demonstrates a complete end-to-end data pipeline on Google Cloud Platform (GCP). It includes extracting data from an external API([RapidAPI](https://rapidapi.com/)), processing and loading the data into BigQuery, and visualizing it using Looker Studio. The pipeline leverages various GCP services such as Cloud Composer(Airflow), Cloud Functions, Dataflow, and BigQuery to automate and streamline the data processing workflow.

## Architecture
![Data Engineering Project Architecture](https://github.com/user-attachments/assets/9b168216-f9da-4704-a4fc-4852f4d9efc2)

The architecture of the data pipeline includes the following components:

1. **Data Extraction**:
   - **Cricbuzz API**: Extracts cricket statistics from the Cricbuzz API via [RapidAPI](https://rapidapi.com/) and automated data formatting using a Python script managed by a DAG.

2. **Data Storage**:
   - **Google Cloud Storage (GCS)**: Stores the extracted data in CSV format.

3. **Data Processing**:
   - **Dataflow**: Uses a Dataflow job to read the CSV data from GCS, transform it, and load it into BigQuery.

4. **Automation**:
   - **Cloud Composer**: Orchestrates the data extraction and loading process by scheduling and triggering the Python script that uploads data(CSV) to GCS.

5. **Event Trigger**:
   - **Cloud Functions**: Listens for new files uploaded to the GCS bucket and triggers the Dataflow job to process and load the data into BigQuery.

6. **Data Visualization**:
   - **BigQuery**: Stores and queries the processed data.
   - **Looker Studio**: Visualizes the data by creating dashboards and reports.

## Conclusion

This end-to-end data pipeline showcases how to integrate various GCP services to automate the data processing workflow and visualize results.
