from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeSqlApiOperator

default_args = {"owner": "airflow"}

with DAG(
    dag_id="install_sid",
    start_date=datetime.now() - timedelta(days=1),
    schedule="@once",  # Exécution manuelle uniquement
    catchup=False,
    default_args=default_args,
    description="Création des tables dans Snowflake via scripts SQL",
) as dag:
    create_db = SnowflakeSqlApiOperator(
        task_id="create_database",
        sql="scripts/create_database.sql",
        snowflake_conn_id="my_snowflake_conn",
    )

    create_soc = SnowflakeSqlApiOperator(
        task_id="create_SOC",
        sql="scripts/create_SOC.sql",
        snowflake_conn_id="my_snowflake_conn",
    )

    create_stg = SnowflakeSqlApiOperator(
        task_id="create_STG",
        sql="scripts/create_STG.sql",
        snowflake_conn_id="my_snowflake_conn",
    )

    create_wrk = SnowflakeSqlApiOperator(
        task_id="create_WRK",
        sql="scripts/create_WRK.sql",
        snowflake_conn_id="my_snowflake_conn",
    )

    create_db >> [create_soc, create_stg, create_wrk]
