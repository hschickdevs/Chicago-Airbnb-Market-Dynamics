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
    
    def retrieve_community_data(self) -> pd.DataFrame:
        query = """
            SELECT communities.COMMUNITY_ID, NAME, GEOMETRY, CRIME_RATE, avg_price
            FROM communities INNER JOIN 
                                    (SELECT COMMUNITY_ID, ROUND(AVG(price),1) AS avg_price
                                    FROM listings
                                    GROUP BY COMMUNITY_ID
                                    ) AS subquery
                                    ON communities.COMMUNITY_ID = subquery.COMMUNITY_ID
        """
        return pd.read_sql(query, self.connection)

    
    # ---------------------------- UNNAMED ---------------------------- #
    # Queries from Sristi's analysis
    
    def srishti_query_1(self) -> pd.DataFrame:
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
    
    def srishti_query_2(self) -> pd.DataFrame:
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
    
    def srishti_query_3(self) -> pd.DataFrame:
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
    
    def srishti_query_4(self) -> pd.DataFrame:
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
    
    def srishti_query_5(self) -> pd.DataFrame:
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
    
    def srishti_query_6(self) -> pd.DataFrame:
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
    
    def suhas_query_1(self) -> pd.DataFrame:
        query = """
            SELECT 
                host_neighbourhood AS neighbourhood, 
                AVG(price) AS average_price,
                MIN(price) AS min_price,
                MAX(price) AS max_price,
                STDDEV(price) AS std_deviation
            FROM 
                LISTINGS
            GROUP BY 
                neighbourhood, 
                room_type;
        """
        return pd.read_sql(query, self.connection)
    
    def suhas_query_2(self) -> pd.DataFrame:
        query = """
            SELECT 
                AVG(price) AS average_price, 
                AVG(number_of_reviews) AS average_reviews
            FROM 
                LISTINGS
            GROUP BY 
                host_neighbourhood;
        """
        return pd.read_sql(query, self.connection)
    
    def suhas_query_3(self) -> pd.DataFrame:
        query = """
            SELECT 
                room_type, 
                AVG(price) AS average_price,
                COUNT(*) AS number_of_listings
            FROM 
                LISTINGS
            GROUP BY 
                room_type
            ORDER BY 
                average_price DESC;
        """
        return pd.read_sql(query, self.connection)
    
    def suhas_query_4(self) -> pd.DataFrame:
        query = """
            SELECT 
                AVG(CASE WHEN amenities LIKE '%"Wifi"%' THEN price ELSE NULL END) AS wifi,
                AVG(CASE WHEN amenities LIKE '%"Air conditioning"%' THEN price ELSE NULL END) AS air_conditioning,
                AVG(CASE WHEN amenities LIKE '%"Pool"%' THEN price ELSE NULL END) AS pool,
                AVG(CASE WHEN amenities LIKE '%"Bathtub"%' THEN price ELSE NULL END) AS bathtub,
                AVG(CASE WHEN amenities LIKE '%"Central heating"%' THEN price ELSE NULL END) AS central_heating,
                AVG(CASE WHEN amenities LIKE '%"Free parking on premises"%' THEN price ELSE NULL END) AS free_parking,
                AVG(CASE WHEN amenities LIKE '%"Free street parking"%' THEN price ELSE NULL END) AS free_street_parking,
                AVG(price) AS overall_avg_price
            FROM 
                LISTINGS;
        """
        return pd.read_sql(query, self.connection)
    
    def suhas_query_5(self) -> pd.DataFrame:
        query = """
            SELECT
                AVG(price) AS average_price,
                AVG(review_scores_rating) AS average_overall_rating,
                AVG(review_scores_cleanliness) AS average_cleanliness_rating,
                AVG(review_scores_location) AS average_location_rating
            FROM 
                LISTINGS
            GROUP BY 
                host_neighbourhood;
        """
        return pd.read_sql(query, self.connection)
    
    def suhas_query_6(self) -> pd.DataFrame:
        query = """
            SELECT 
                DATEDIFF(day, host_since, CURRENT_DATE()) AS days_as_host,
                AVG(price) AS average_price
            FROM 
                LISTINGS
            GROUP BY 
                days_as_host;
        """
        return pd.read_sql(query, self.connection)