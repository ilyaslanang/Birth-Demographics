from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator

sync_conn_id = '2163f478-3837-48df-bc90-8c74f4029168' # replace with airbyte connection id


with DAG (
    dag_id='extract-load',
    schedule=None,
    start_date=days_ago(1)
    ) as dag:
    
    trigger_sync = AirbyteTriggerSyncOperator(
        task_id='trigger_sync',
        airbyte_conn_id='airbyte_conn',
        connection_id=sync_conn_id,
        asynchronous=True
    )
