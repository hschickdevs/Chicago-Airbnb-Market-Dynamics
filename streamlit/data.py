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
    
    # ---------------------------- UNNAMED ---------------------------- #
    # Queries from Sristi's analysis
    
    def query_1(self) -> pd.DataFrame:
        query = """
            WITH HostListings AS (
                SELECT
                    host_id,
                    COUNT(DISTINCT listing_id) AS listing_count,
                    MAX(host_is_superhost) AS host_is_superhost_value
                FROM
                    listings
                GROUP BY
                    host_id
            )

            SELECT
                CASE
                    WHEN listing_count = 1 THEN 'One Listing'
                    ELSE 'Multiple Listings'
                END AS listing_count_category,
                COUNT(DISTINCT host_id) AS host_count,
                SUM(host_is_superhost_value) AS host_is_superhost_count
            FROM
                HostListings
            GROUP BY
                listing_count_category;
        """
        return pd.read_sql(query, self.connection)
    
    def query_2(self) -> pd.DataFrame:
        query="""
            SELECT
                listing_count,
                COUNT(host_id) AS host_count
            FROM (
                SELECT
                    host_id,
                    COUNT(listing_id) AS listing_count
                FROM
                    listings
                GROUP BY
                    host_id
            ) AS HostListings
            GROUP BY
                listing_count
            ORDER BY
                listing_count;
        """
        return pd.read_sql(query, self.connection)
    
    def query_3(self) -> pd.DataFrame:
        query="""
            SELECT
                HOST_HAS_PROFILE_PIC,
                host_is_superhost,
                COUNT(DISTINCT host_id) AS host_count
            FROM
                listings
            GROUP BY
                HOST_HAS_PROFILE_PIC, host_is_superhost;
        """
        return pd.read_sql(query, self.connection)
    
    def query_4(self) -> pd.DataFrame:
        query="""
            SELECT
                HOST_IDENTITY_VERIFIED,
                host_is_superhost,
                COUNT(DISTINCT host_id) AS host_count
            FROM
                listings
            GROUP BY
                HOST_IDENTITY_VERIFIED, host_is_superhost;
        """
        return pd.read_sql(query, self.connection)
    
    def query_5(self) -> pd.DataFrame:
        query="""
            SELECT
                INSTANT_BOOKABLE,
                host_is_superhost,
                COUNT(DISTINCT host_id) AS host_count
            FROM
                listings
            GROUP BY
                INSTANT_BOOKABLE, host_is_superhost;
        """
        return pd.read_sql(query, self.connection)
    
    def query_6(self) -> pd.DataFrame:
        query="""
            SELECT
                host_id,
                host_is_superhost,
                AVG(REVIEWS_PER_MONTH) AS avg_reviews_per_month
            FROM
                listings
            GROUP BY
                host_id, host_is_superhost;
        """
        return pd.read_sql(query, self.connection)