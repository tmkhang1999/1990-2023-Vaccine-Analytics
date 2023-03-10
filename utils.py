from sqlalchemy import create_engine, text
import pandas as pd


def load_data(database_path, table_name):
    """
    INPUT:
    database_path - The path to the database
    table_name - Name of the table containing the data to be extracted in the database
    OUTPUT:
    df - the saved dataframe
    """
    # Load data from database
    engine = create_engine('sqlite:///' + database_path)
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql_query(sql=text(query), con=engine.connect())

    # Custom 'SEX' feature
    df['SEX'].replace(['F', 'M'], ['Female', 'Male'], inplace=True)

    # Calculate the max_time and min_time for date picker
    df['RECVDATE'] = pd.to_datetime(df['RECVDATE'])

    return df
