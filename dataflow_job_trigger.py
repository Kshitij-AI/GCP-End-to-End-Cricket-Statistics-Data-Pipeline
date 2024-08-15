# This Cloud Function will trigger a Dataflow job upon receiving a create event from a GCS bucket.
from googleapiclient.discovery import build

def datafow_job_trigger(data, context):

    service = build('dataflow', 'v1b3')
    project = "solid-binder-431511-d6"
    region = "asia-south2"

    template_path = "gs://dataflow-templates-asia-south2/2024-08-06-00_RC00/GCS_CSV_to_BigQuery"

    template_body = {
        "jobName": "load_from_gcs_to_bq",
        "parameters": {
            "inputFilePattern":"gs://cricbuzz_stats/player_stats.csv",
            "schemaJSONPath": "gs://cricbuzz_stats_metadata/bq_schema.json",
            "outputTable":"solid-binder-431511-d6:cricbuzz_stats.icc_odi_batsman_ranking",
            "badRecordsOutputTable":"solid-binder-431511-d6:cricbuzz_stats.bad_records_temp",
            "csvFormat":"Default",
            "delimiter":",",
            "bigQueryLoadingTemporaryDirectory": "gs://cricbuzz_stats_metadata",
            "csvFileEncoding": "UTF-8"
        }
    }

    request = service.projects().locations().templates().launch(
        projectId=project,
        location=region,
        gcsPath=template_path,
        body=template_body
        )
    response = request.execute()
    print(response)
