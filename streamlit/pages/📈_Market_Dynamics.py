import streamlit as st
import pandas as pd
import plotly.express as px

# Custom imports
from data import SnowflakeConnector
from util import handle_env

# Set up page configuration
st.set_page_config(page_title="📈 Chicago Airbnb Market Dynamics Analysis", page_icon="💵")

# Markdown for the page
st.markdown("# 📈 Chicago Airbnb Market Dynamics Analysis")
st.sidebar.header("📈 Chicago Airbnb Market Dynamics Analysis")

# Description
st.markdown(
    """
    In this section we aim to uncover the trends and patterns in listing prices and reviews over time in Chicago.
    
    ### 🗂️ Dataset Used:
    
    For this analysis, we are querying the `calendar.csv` dataset, stored in Snowflake due to its astronomical size. Each row of the data represents the airbnb price for each day each each listing on airbnb for the past year.
    
    The `calendar.csv` dataset contains the following columns (data head shown below): 
    
    | listing_id | date      | available | price   | adjusted_price | minimum_nights | maximum_nights |
    |------------|-----------|-----------|---------|----------------|----------------|----------------|
    | 2384       | 9/12/2023 | f         | $125.00 | $125.00        | 3              | 1125           |
    | 2384       | 9/13/2023 | f         | $125.00 | $125.00        | 3              | 1125           |
    | 2384       | 9/14/2023 | f         | $125.00 | $125.00        | 3              | 1125           |
    | 2384       | 9/15/2023 | f         | $100.00 | $100.00        | 3              | 1125           |
    | 2384       | 9/16/2023 | f         | $100.00 | $100.00        | 3              | 1125           |
    """
)

# Set up environment and database connection
handle_env()
snowflake_cxn = SnowflakeConnector()
df = snowflake_cxn.retrieve_price_over_time()

# Convert 'DATE' to datetime and create 'day' column
df['DATE'] = pd.to_datetime(df['DATE'])
df['day'] = df['DATE'].dt.day_name()

# Sidebar for date range selection
start_date, end_date = st.sidebar.date_input(
    "Select Date Range for Listing Timeseries",
    [df['DATE'].min(), df['DATE'].max()],
    min_value=df['DATE'].min(),
    max_value=df['DATE'].max()
)

# Convert start_date and end_date to pandas datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data based on the selected date range
filtered_df = df[(df['DATE'] >= start_date) & (df['DATE'] <= end_date)]


# ------------------------ ANALYIS 1 - AVERAGE LISTING PRICES OVER TIME ------------------------ #

st.markdown("## 1️⃣ Average Listing Prices Over Time")
st.markdown(
    """
    The chart below presents a visual representation of average listing prices over time.
    Explore how these prices have fluctuated, potentially influenced by factors like seasonality, local events, or market changes.
    """
)

# Create chart layout to update the chart title
def set_chart_title(fig, title):
    fig.update_layout(
        title={
            'text': title,
            'font': {
                'size': 24,
                'color': '#3B3B3B',
                'family': "Arial, sans-serif",
            }
        },
    )
    return fig


# Plotting the time series chart using Plotly
time_series_fig = px.line(
    filtered_df,
    x='DATE',
    y='AVG_PRICE',
    markers=True
)
time_series_fig = set_chart_title(time_series_fig, "Time Series of Average Listing Prices")
st.plotly_chart(time_series_fig)

st.markdown("Additionally we can study the average listing prices distributed by day of the week to understand weekly demand fluctuations and possibly recommend strategic pricing for hosts.")

# Group by 'day' and calculate the average price for the filtered data
avg_price_by_weekday = filtered_df.groupby('day')['AVG_PRICE'].mean().reset_index()

# Set the order of weekdays
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
avg_price_by_weekday['day'] = pd.Categorical(avg_price_by_weekday['day'], categories=weekday_order, ordered=True)
avg_price_by_weekday = avg_price_by_weekday.sort_values('day')

# st.markdown(
#     """
#     ## Average Listing Price by Weekday
#     The chart below illustrates how the average listing prices vary across different days of the week.
#     This can reveal patterns related to weekly booking trends and preferences.
#     """
# )

weekday_colors = {
    'Monday': 'blue',
    'Tuesday': 'green',
    'Wednesday': 'red',
    'Thursday': 'cyan',
    'Friday': 'magenta',
    'Saturday': 'yellow',
    'Sunday': 'purple'
}

# Create a list of colors for the bars in the order of the DataFrame
bar_colors = [weekday_colors[day] for day in avg_price_by_weekday['day']]

# Plotting the weekday chart using Plotly with specific colors for each day
weekday_fig = px.bar(
    avg_price_by_weekday,
    x='day',
    y='AVG_PRICE',
    labels={'day': 'Day of the Week', 'AVG_PRICE': 'Average Price'},
    color='day',
    color_discrete_map=weekday_colors  # Apply the color mapping
)
weekday_fig = set_chart_title(weekday_fig, "Average Listing Price by Weekday")
st.plotly_chart(weekday_fig)

# st.markdown("### Insights")
# st.markdown(
#     """
#     - **Trend Observation:** 
#         - The data indicates a steady increase in average listing prices since September 2023. This upward trend may reflect a growing demand for Airbnb accommodations in Chicago, potentially influenced by factors such as seasonal visitor influx, local events, or a general rise in the popularity of short-term rentals in the city.
#         - Analysis of the average listing prices by weekday reveals that the highest prices are typically observed from Friday to Sunday. This pattern suggests a higher demand for accommodations during the weekends, possibly due to an influx of weekend travelers, tourists, or local residents seeking leisure stays.

#     - **Implications for Hosts/Guests:** 
#         - For hosts: The observed trends indicate an opportunity to optimize pricing strategies. Considering the steady increase in prices, hosts might consider adjusting their rates upward, particularly in anticipation of high-demand periods. Additionally, the premium pricing on weekends could be leveraged to maximize revenue, while still maintaining competitive pricing during weekdays to attract guests.
#         - For guests: Those seeking value-for-money stays might find better deals by booking on weekdays, as the data shows a significant price drop compared to weekends. Planning trips outside peak seasons could also be more economical, considering the overall rising trend in prices since September 2023.
#     """
# )


# ------------------------ ANALYIS 2 - Time series analysis of the frequency of reviews for the listing ------------------------ #
st.markdown("## 2️⃣ Average Review Frequency Over Time")
st.markdown(
    """
    The charts below present a visual representation of average aggregate review frequency over time.
    Understanding the change in review frequency serves as a key indicator of market activity, reflecting trends in demand, guest satisfaction, and the health of the market, while also offering insights into the effectiveness of pricing strategies, competitive dynamics, and the impact of regulatory changes.
    """
)

# Pul data from Snowflake
reviews_df = snowflake_cxn.retrieve_reviews()
reviews_df['DATE'] = pd.to_datetime(reviews_df['DATE'])

# Sidebar for date range selection
review_start_date, review_end_date = st.sidebar.date_input(
    "Select Date Range for Reviews Timeseries",
    [reviews_df['DATE'].min(), reviews_df['DATE'].max()],
    min_value=reviews_df['DATE'].min(),
    max_value=reviews_df['DATE'].max()
)
st.sidebar.success("☝️ Select a date range for listings and reviews.")

# Convert start_date and end_date to pandas datetime
review_start_date = pd.to_datetime(review_start_date)
review_end_date = pd.to_datetime(review_end_date)

# Filter data based on the selected date range
filtered_reviews_df = reviews_df[(reviews_df['DATE'] >= review_start_date) & (reviews_df['DATE'] <= review_end_date)]

# Plotting the time series chart using Plotly
review_time_series_fig = px.line(
    filtered_reviews_df,
    x='DATE',
    y='NUMBER_OF_REVIEW',
    markers=True
)
review_time_series_fig = set_chart_title(review_time_series_fig, "Time Series of Review Frequency")
st.plotly_chart(review_time_series_fig)

# Creating 'day' column in the review DataFrame
filtered_reviews_df['day'] = filtered_reviews_df['DATE'].dt.day_name()

# Group by 'day' and calculate the average number of reviews
avg_reviews_by_weekday = filtered_reviews_df.groupby('day')['NUMBER_OF_REVIEW'].mean().reset_index()

# Set the order of weekdays for the review data
avg_reviews_by_weekday['day'] = pd.Categorical(avg_reviews_by_weekday['day'], categories=weekday_order, ordered=True)
avg_reviews_by_weekday = avg_reviews_by_weekday.sort_values('day')

# Plotting the weekly review frequency chart using Plotly
review_weekday_fig = px.bar(
    avg_reviews_by_weekday,
    x='day',
    y='NUMBER_OF_REVIEW',
    labels={'day': 'Day of the Week', 'NUMBER_OF_REVIEW': 'Average Number of Reviews'},
    color='day',
    color_discrete_map=weekday_colors  # Reuse the color mapping
)
review_weekday_fig = set_chart_title(review_weekday_fig, "Average Review Frequency by Weekday")
st.plotly_chart(review_weekday_fig)

# st.markdown("### Insights")
# st.markdown(
#     """
#     - **Trend Observation:** 
#         - From September 2022 to March 2023, the review frequency remained relatively stable, indicating a consistent level of guest activity and market engagement during this period. Post-March 2023, there has been a notable increase in review frequency, suggesting a surge in guest interactions, possibly due to seasonal factors, increased travel, or growing popularity of Airbnb listings in Chicago.
#         - A significant peak in reviews is observed on Sundays and Mondays, with the frequency more than doubling compared to other days of the week. This pattern might be indicative of guests concluding their stays and leaving reviews at the end of weekends or early in the week.

#     - **Implications for Market Dynamics:** 
#         - The increased review frequency, especially on Sundays and Mondays, highlights these days as key points for guest feedback and interaction. This trend could be leveraged by hosts for targeted marketing and improving guest experiences during and post-stay.
#         - For guests and hosts alike, understanding these patterns can aid in predicting busier times in the Airbnb market, potentially influencing booking decisions and pricing strategies.
#     """
# )

# Button to re-run the app (optional)
st.button("Re-run")
