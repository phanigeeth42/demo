import pandas as pd
df = pd.read_csv('gs://databricks-bigquery-mdlz/iris.csv')
from google.cloud import bigquery
import pytz
table_id="mdlz-mlops-17-gcd-2157.sample.iris"
# Construct a BigQuery client object.
client = bigquery.Client()
job_config = bigquery.LoadJobConfig(autodetect=True, write_disposition="WRITE_TRUNCATE")
job = client.load_table_from_dataframe(
    df, table_id, job_config=job_config
)  # Make an API request.
job.result() 

