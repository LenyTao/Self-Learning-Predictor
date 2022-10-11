from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster, ResultSet


def create_cassandra_connection(config: dict):
    cluster = Cluster(
        [f"{config['cassandra']['host']}"],
        auth_provider=PlainTextAuthProvider(
            username=config['cassandra']['username'],
            password=config['cassandra']['password']),
        port=config['cassandra']['port'])

    return cluster.connect(config['cassandra']['keystore'])


def get_all_record_from(config: dict) -> ResultSet:
    with create_cassandra_connection(config) as session:
        query_result: ResultSet = session.execute(
            f'''
                SELECT * 
                FROM {config['cassandra']['table_name']}''')
        return query_result


def get_form_for_result(config: dict) -> ResultSet:
    with create_cassandra_connection(config) as session:
        query_result: ResultSet = session.execute(
            f'''
                SELECT id_event,
                       entry_date,
                       age,
                       name,
                       regression_prediction,
                       classifier_prediction 
                FROM {config['cassandra']['table_name']}''')
        return query_result


def get_date_by_id(id_event: str, config: dict):
    with create_cassandra_connection(config) as session:
        query_result: ResultSet = session.execute(
            f'''
                SELECT *
                FROM {config['cassandra']['table_name']}
                WHERE id_event = \'{id_event}\'''')
        return query_result


def del_record_by_id(id_event: str, config: dict):
    with create_cassandra_connection(config) as session:
        session.execute(
            f'''
                DELETE
                FROM {config['cassandra']['table_name']}
                WHERE id_event = \'{id_event}\'''')
