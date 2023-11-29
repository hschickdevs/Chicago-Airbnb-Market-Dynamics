from snowflake import connector
import os 
import pandas as pd


class SnowflakeConnector:
    def __init__(self):
        self.user = os.getenv("SNOWFLAKE_USER")
        self.password = os.getenv("SNOWFLAKE_PASSWORD")
        self.account = os.getenv("SNOWFLAKE_ACCOUNT")
        self.database = os.getenv("SNOWFLAKE_DATABASE")
        self.schema = os.getenv("SNOWFLAKE_SCHEMA")
        
        self.connection = self.connect()
        
    def __dict__(self):
        return {
            "user": self.user,
            "password": self.password,
            "account": self.account,
            "database": self.database,
            "schema": self.schema
        }
        
    def connect(self):
        return connector.connect(**self.__dict__())
    
    def close(self):
        self.connection.close()
    
    # ---------------------------- RETRIEVAL METHODS ---------------------------- #
    
    def retrieve_price_over_time(self) -> pd.DataFrame:
        # Used to plot the price over time
        query = """
        SELECT date, AVG(price) AS avg_price
        FROM calendar
        GROUP BY date
        ORDER BY date;
        """
        return pd.read_sql(query, self.connection)
    
    def retrieve_reviews(self) -> pd.DataFrame:
        # Used to plot the review count over time
        query = """
        SELECT date, count(review_id) AS number_of_review
        FROM reviews
        WHERE date > TO_DATE('2022-09-10', 'YYYY-MM-DD') 
        GROUP BY date
        ORDER BY date;
        """
        return pd.read_sql(query, self.connection)