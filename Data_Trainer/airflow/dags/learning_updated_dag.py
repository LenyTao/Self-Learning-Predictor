import json
import os
import sys

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


os.environ['CONFIG_PATH'] = "/trainer_app"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 0,
    'schedule_interval': "00 13 * * *"
}

DAG_ID = 'Learning_Update'

TASK_LEARNING_UPDATE_ID = 'Learning_Run'

dag = DAG(
    dag_id=DAG_ID,
    default_args=default_args,
    tags=['LearningUpdate', 'COVID'],
    catchup=False,
    max_active_runs=1
)

learning_update_name = f'{DAG_ID}.{TASK_LEARNING_UPDATE_ID}'

dag.doc_md = __doc__

with dag:
    covid_learning_updated_task = BashOperator(
        task_id=learning_update_name,
        bash_command=f'python3 /trainer_app/data_trainer_app.py $CONFIG_PATH',
        dag=dag)
