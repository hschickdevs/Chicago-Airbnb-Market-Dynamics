import streamlit as st

from util import handle_env

handle_env()

st.set_page_config(
   page_title="Overview",
   page_icon="🏠",
)

st.sidebar.success("☝️ Select an analysis theme above to explore.")

st.markdown(
"""
# 🌎 Data Management Final Project - Chicago Airbnb Market Analysis 📊
"""
)

st.image("https://miro.medium.com/v2/resize:fit:1358/0*NChTo-XqLOxLabIW")

st.markdown(
"""
> 👈📊 _**Please see the page selection on the left-hand navbar for our analysis results.**_

## Group Members

- **William Dang** - [LinkedIn](https://www.linkedin.com/in/williampdang/)
- **Harrison Schick** - [LinkedIn](https://www.linkedin.com/in/harrison-schick/)
- **Poonnawit Suwatanapongched** - [LinkedIn](https://www.linkedin.com/in/poonnawit-s/)
- **Suhas Yogish** - [LinkedIn](https://www.linkedin.com/in/suhasy/)
- **Srishti Gupta** - [LinkedIn](https://www.linkedin.com/in/srishti-gupta-ut/)

## Project Selection & Motivations

Welcome to our comprehensive analysis of the Airbnb market in Chicago. This project was chosen due to the dynamic and diverse nature of the Chicago Airbnb landscape, which presents a unique opportunity to explore various aspects of urban hospitality and economics. Chicago, known for its rich cultural heritage and vibrant neighborhoods, offers a plethora of data that can yield insights into both the short-term rental market and the city's socioeconomic dynamics.

The motivation behind this project stems from a desire to understand:

1. **The impact of external factors** such as local events and crime rates on the short-term rental market.
2. **Host behavior and strategies**, which can influence guest experiences and rental success.
3. **Neighborhood dynamics**, exploring how different areas of the city compare in terms of pricing, popularity, and guest satisfaction.
4. **Economic implications** for both hosts and renters in the context of the larger Chicago economy.

By dissecting these elements, we aim to provide valuable insights for hosts, guests, and local policymakers.

## Questions We Are Trying to Answer

Our analysis is structured around several key questions, each designed to unravel a different facet of the Airbnb experience in Chicago:

1. **Market Dynamics:** How do listing prices and review frequencies change over time? What external factors, like crime rates, influence these dynamics?
2. **Host Insights:** What characterizes successful hosts in terms of number of listings, profile completeness, and status as a superhost?
3. **Neighborhood Analysis:** Which neighborhoods are most and least expensive? How do safety and local amenities influence pricing?
4. **Price and Reviews Correlation:** How do guest reviews relate to pricing strategies? Does a higher price correlate with better ratings?
5. **Listing Characteristics:** What impact do room types and amenities have on listing prices?
6. **Host Experience and Pricing:** Is there a relationship between a host's tenure on the platform and the pricing of their listings?

Through these questions, we aim to paint a comprehensive picture of the Airbnb market in Chicago, offering insights that can benefit hosts, guests, and analysts alike.

## Data Acquisition

We obtained the data for our project from 2 sources, http://insideairbnb.com/get-the-data/ and https://data.cityofchicago.org/. From the airbnb dataset, we downloaded the detailed listings csv (listings.csv) for airbnbs in Chicago, the associated reviews csv for those listings (reviews.csv), and the calendar csv containing pricing data for listings over time (calendar.csv). From the Chicago dataset we downloaded the crime reports csv data for Chicago for the entire year of 2020 (crimes_2020.csv), and the geospatial boundary data for every unique Chicago neighborhood (boundaries_neighborhoods.geojson).

The largest challenge we faced from getting acquiring the data was loading the calendars.csv file from the airbnb database because the zip file would not unzip on MacOS. To remedy this, we used Windows to unzip the data and process the data.

## Data Sampling
"""
)

st.image("https://drive.google.com/uc?export=view&id=16Tm2h1oRQ_Ug_bcpiAfnZrDpgh903U0h")
st.image("https://drive.google.com/uc?export=view&id=17BhfI-VJ7UTP8itunPIbfsBNHGpE1dtG")
st.image("https://drive.google.com/uc?export=view&id=14LE_tnSKHNl5knflnPeV_-TgKHEKNqca")
st.image("https://drive.google.com/uc?export=view&id=1n6A46KB2hXGSt9AykqHWozDQlXNy5U6q")
st.image("https://drive.google.com/uc?export=view&id=1zfKZYPrVtE-j7ksvTsxIGbjeM4pJawiI")

st.markdown(
   """
   ## Data Cleaning

   The main ETL tools we used were Python Jupyter notebooks for data extraction and transformation and the Snowflake console wizard for data loading.

   Our cleaning startegy began with extracting only the relevant columns from the listings.csv (columns that pertained to data collection, unnecessary web links, and columns that lacked any data). Then we cleaned up columns with false but relevant data pertaining to information on bed, bedrooms, and bathrooms counts. We were able to ressed these columns with values that were extracted from another column that contained the listing name which had the actual value counts for these columns. We also encoded columns with categorical variables by creating new columns with numerical values that mapped to those categories; these columns included. The next thing we did to clean this data was fix NaN values in numerical columns by imputing those values with the columnar mean.

   After working on the listings.csv we moved onto the reviews.csv and calendars.csv of which we removed columns that were not relevant such as reviewer first names since those names did not have a context and could be repeated for different people. Then, since the reviews, calendar, and listings data all contained primary and foreign key values that mapped to each other but were extremely large, we decided to map those values and reset their sequences to start from 1 - this would help us drastically reduce the data size of our tables.

   The next piece of work was to process the Chicago crime data by mapping a json list of Chicago neighborhoods to the their neighborhood numbers in the crime dataset. We then grouped by the communities in the crime data to compute a relative crime rate to produce a new communities.csv that contained the community number, community name, relative crime rate, and geospatial boundaries. After we mapped community names to community numbers, we went back to the listings.csv to impute a column to hold community numbers that corresponded to the communities where the listings were hosted.

   The last piece of transformation was to break down the reviews.csv and calendars.csv files into smaller chunks since they exceeded the 50MB loading capacity of the Snowflake Console Wizard.

   Once those CSVs were broken down, we used the Snowflake Console Wizard to create tables within a database instance and schema inside of Snowflake and automatically generate a table schema for those listings, reviews, calendar, and communities tables.

   To complete loading, we then loaded any CSV files that were broken into chunks into their corresponding tables, the Snowflake Console Wizard was able to resolve any row and column header conflicts for us.
   """
)

st.image("https://drive.google.com/uc?export=view&id=1hhI7bCGNpDuOr9DdfbnQM9H6iPZYkHN2", caption="Snowflake Data Import")

st.markdown(
   """
   # Tools and Technologies
   """
)

st.image("https://drive.google.com/uc?export=view&id=1u2aRkC_33ml5rPPzlm3QcN4tY_W_kDA1")

st.markdown(
   """
   ## Streamlit
   Streamlit provides interactive dashboard and visualizations that we used to bring our analysis to life. It allows us to continue to glean insights from our database with filtering even after we did reliminary quantitative analysis. It is also the way we're hosting this website for you to view!
   """
)

st.image("https://drive.google.com/uc?export=view&id=1050qyAZk51G-KNxDxtWup3FNyxa4_HB6")

st.markdown(
   """
   ## Python / Jupyter Notebooks
   Python and Jupyter Notebooks allowed us to perform data transformation of very messy and uncleaned data. Moreover, it allowed us to run analysis on the data after we imported the data to Snowflake by using the Snowpark package to query our Snowflake database.
   """
)

st.image("https://drive.google.com/uc?export=view&id=1U1wJeN37C6iJFyOlMIkR7FiAhFL9OzUP")
st.markdown("""
   ## Snowflake
   Snowflake enabled us to upload our data to the cloud and query it using SQL. Snowflake is very fast because of its "warehouse" capability (compute) that can scale out and up. Because of the power of a scaled up compute, we were able to load 3 million rows into the database in about 3 minutes.

   Snowflake allowed us to not worry too much about the loading process of our data since the Snowflake Console Wizard has the ability to automatically detect the schema of our tables we uploaded, there was limited manual work for us.

   The only specific requirements of Snowflake was that we needed to have tables with clean dataimported, we chose CSVs. Moreover, the requirement was that CSVs uploaded were limited to a file size of 50MB per upload.
  """)
            
st.markdown("""
   # Real-life Impact
   ## Neighborhood Analysis
   Understanding the relationship between geography-based pricing and crime rates for Airbnb listings is essential for hosts and guests. Hosts can optimize pricing and target marketing based on neighborhood safety, while guests can make informed decisions about safety and value. This knowledge also impacts investment choices, community engagement, and overall profitability and reputation of Airbnb properties.

   ## Price and Reviews
   The data suggests that Airbnb guests are inclined to pay more for better-located properties, as indicated by the positive correlation between price and location ratings. Cleanliness is consistently high across various price points, showing it's a standard expectation for guests. The number of reviews does not correlate strongly with price, implying other factors motivate guests to leave feedback. Additionally, the overall satisfaction is not strictly tied to price, with similar ratings across a broad price range. This indicates that guests weigh multiple factors, including location and cleanliness, more heavily than price in their overall assessment of an Airbnb experience.

   ## Host Dynamics
   Airbnb comprises hosts with fewer than 5 listings, highlighting the platform's individual and small-scale host focus. Superhost status correlates with more reviews, suggesting higher guest satisfaction and increased bookings. There's only a slight price increase with host experience, indicating other factors might be more influential in pricing. Guests seem to value Superhost status, implying a willingness to pay more for assured quality. Both hosts and guests should note the importance of reputation and perceived service quality on the platform.

   ## Market Dynamics
   The time series data on Airbnb listing prices and review frequencies indicate cyclical trends, likely tied to seasonal demand and weekly patterns, with higher prices and review volumes around weekends. Hosts can optimize earnings by adjusting rates in response to these trends, potentially increasing prices during peak demand. Review patterns suggest that guests actively leave feedback at the week's start and end, which could inform hosts when to encourage reviews. Understanding these temporal patterns can help hosts plan for high-demand periods and set dynamic pricing, while guests could book during dips for better deals. Overall, strategic timing based on these insights could benefit hosts' profitability and guests' cost savings.

   ## Listing Characteristics
   The data shows that Airbnb listings offering entire homes or apartments charge the highest prices, with a clear price gradient down to shared rooms. Amenities significantly influence pricing, with pools notably increasing listing prices. Hosts can optimize their earnings by offering sought-after amenities and considering the type of room they list. Guests should expect to pay more for privacy and premium features like pools. Both hosts and guests must consider these factors in the context of value for money and competitive pricing.
""")

