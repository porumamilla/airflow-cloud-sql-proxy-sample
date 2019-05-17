from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.mysql_to_gcs import MySqlToGoogleCloudStorageOperator
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'cloud_sql_proxy_to_gcs',
    default_args=default_args,
    description='Cloud SQL Proxy to GCS',
    schedule_interval=timedelta(days=1),
)

SQL = 'select * from sundar.supplier'
t1 = MySqlToGoogleCloudStorageOperator(
            mysql_conn_id="sundar-sql-con",
            task_id="sample_test_conn",
            bucket="hackathon-demo-238019",
            filename="test.json",
            google_cloud_storage_conn_id="sundar-gcs-con",
            export_format="json",
            sql=SQL,
            dag=dag
        )
t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag
)

t1 >> t2
