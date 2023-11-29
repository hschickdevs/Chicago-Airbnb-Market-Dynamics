"""
Relationship between average price vs average reviews grouped by neighborhood (Suhas's code)
Relationship between the average price of a listing and the overall rating (Suhas's code)
Relationship between the average price of a listing and the cleanliness rating (Suhas's code)
Relationship between the average price of a listing and the average location rating (Suhas's code)
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Custom imports
from data import SnowflakeConnector
from util import handle_env

# Set up environment and database connection
handle_env()
snowflake_cxn = SnowflakeConnector()

# Set up page configuration
st.set_page_config(page_title="🏷️ Price & Reviews", page_icon="🏷️")

# Markdown for the page
st.markdown(
    """
    # 🏷️ Chicago Airbnb Listing Price & Reviews Analysis 💬
    
    In this analysis we aim to answer the following questions:
    
    * What is the relationship between average price vs average reviews?
    * What is the relationship between average price vs average overall rating?
    * What is the relationship between average price vs average cleanliness rating?
    * What is the relationship between average price vs average location rating?
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

# ------------------------ ANALYIS 1 - AVERAGE PRICE VS AVERAGE REVIEWS ------------------------ #

st.markdown("## 1️⃣ Average Price vs. Average Reviews")
st.markdown(
    """
    In the following graph we investigate the relationship between average price vs average reviews grouped by neighborhood.
    """
)

q2_df = snowflake_cxn.suhas_query_2()

# Set the aesthetic style of the plots
sns.set_theme(style="ticks")

# Streamlit widget for interactivity
# For example, a slider to filter data based on a specific column
price_filter = st.slider("Select a range of Average Price", 
                         min_value=int(q2_df['AVERAGE_PRICE'].min()), 
                         max_value=int(q2_df['AVERAGE_PRICE'].max()), 
                         value=(int(q2_df['AVERAGE_PRICE'].min()), int(q2_df['AVERAGE_PRICE'].max())))

# Filter the dataframe based on the selected price range
filtered_data = q2_df[(q2_df['AVERAGE_PRICE'] >= price_filter[0]) & (q2_df['AVERAGE_PRICE'] <= price_filter[1])]

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='AVERAGE_PRICE', y='AVERAGE_REVIEWS', data=filtered_data)

# Add titles and labels
plt.title('Average Price vs. Average # of Reviews')
plt.xlabel('Average Price ($)')
plt.ylabel('Average Reviews')

# Use Streamlit to display the plot
st.pyplot(plt)

st.markdown("### Insights")
st.markdown(
    """
    - **Trend Observation:** 
        - There is no clear linear trend between average price and the number of reviews, indicating that price may not be a determining factor in the quantity of reviews a listing receives.
        - Most listings are priced under $200 and have a varying number of reviews, with a high density of points in the lower price and review count range.
        - Listings with higher prices do not consistently have more reviews, suggesting that guests do not necessarily review more expensive listings more often.

    - **Implications for Hosts/Guests:** 
        - **For hosts:** Understanding that pricing strategy may not affect the likelihood or number of reviews, hosts might consider focusing on other aspects such as guest experience or additional amenities to improve the attractiveness of their listings.
        - **For guests:** The data suggests that there is a wide range of options available at lower price points with varying levels of feedback, which may assist in making informed decisions based on personal budget and the importance of reviews.
    """
)


# ------------------------ ANALYIS 2 - AVERAGE PRICE VS ASPECTS OF EVALUATION ------------------------ #

st.markdown("## 2️⃣ Average Price vs. Aspects of Evaluation")
st.markdown(
    """
    In the following analyses we investigate the relationship between average price vs the different aspects of evaluation in a customer listing review.
    
    These aspects of evaluation are:
    * Overall Rating
    * Cleanliness Rating
    * Location Rating
    
    First we will investigate the relationship between average price and the overall rating.
    """
)

q5_df = snowflake_cxn.suhas_query_5()

# Streamlit sidebar widgets for interactivity
rating_filter = st.slider("Filter by average overall rating", 
                          min_value=float(q5_df['AVERAGE_OVERALL_RATING'].min()), 
                          max_value=float(q5_df['AVERAGE_OVERALL_RATING'].max()), 
                          value=(float(q5_df['AVERAGE_OVERALL_RATING'].min()), 
                                 float(q5_df['AVERAGE_OVERALL_RATING'].max())))

# Filter the dataframe based on the selected average overall rating range
filtered_data = q5_df[(q5_df['AVERAGE_OVERALL_RATING'] >= rating_filter[0]) & 
                      (q5_df['AVERAGE_OVERALL_RATING'] <= rating_filter[1])]

# Set the aesthetic style of the plots
sns.set_theme(style="ticks")

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='AVERAGE_PRICE', y='AVERAGE_OVERALL_RATING', data=filtered_data)

# Add titles and labels
plt.title('Average Price vs. Average Overall Rating')
plt.xlabel('Average Price ($)')
plt.ylabel('Average Overall Rating')

# Use Streamlit to display the plot
st.pyplot(plt)

st.markdown("Second, we will investigate the relationship between average price and the cleanliness rating.")

# Add a slider in the sidebar to filter the plot based on cleanliness rating
cleanliness_rating_filter = st.slider(
    'Filter by Average Cleanliness Rating', 
    min_value=float(q5_df['AVERAGE_CLEANLINESS_RATING'].min()), 
    max_value=float(q5_df['AVERAGE_CLEANLINESS_RATING'].max()), 
    value=(float(q5_df['AVERAGE_CLEANLINESS_RATING'].min()), 
           float(q5_df['AVERAGE_CLEANLINESS_RATING'].max()))
)

# Filter the dataframe based on the selected average cleanliness rating range
filtered_data = q5_df[(q5_df['AVERAGE_CLEANLINESS_RATING'] >= cleanliness_rating_filter[0]) & 
                      (q5_df['AVERAGE_CLEANLINESS_RATING'] <= cleanliness_rating_filter[1])]

# Set the aesthetic style of the plots
sns.set_theme(style="ticks")

# Create a scatter plot with the filtered data
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='AVERAGE_PRICE', 
    y='AVERAGE_CLEANLINESS_RATING', 
    data=filtered_data
)

# Add titles and labels
plt.title('Average Price vs. Average Cleanliness Rating')
plt.xlabel('Average Price ($)')
plt.ylabel('Average Cleanliness Rating')

# Use Streamlit to display the plot
st.pyplot(plt)

st.markdown("Third, we will investigate the relationship between average price and the location rating.")

# Slider for selecting the location rating range
location_rating_range = st.slider(
    'Select the range of Location Rating',
    min_value=float(q5_df['AVERAGE_LOCATION_RATING'].min()),
    max_value=float(q5_df['AVERAGE_LOCATION_RATING'].max()),
    value=(float(q5_df['AVERAGE_LOCATION_RATING'].min()), float(q5_df['AVERAGE_LOCATION_RATING'].max()))
)

# Filtering the dataframe based on the selected location rating range
filtered_data = q5_df[(q5_df['AVERAGE_LOCATION_RATING'] >= location_rating_range[0]) & 
                      (q5_df['AVERAGE_LOCATION_RATING'] <= location_rating_range[1])]

# Set the aesthetic style of the plots
sns.set_theme(style="ticks")

# Create a scatter plot with the filtered data
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    x='AVERAGE_PRICE', 
    y='AVERAGE_LOCATION_RATING', 
    data=filtered_data, 
    ax=ax
)

# Add titles and labels
ax.set_title('Average Price vs. Average Location Rating')
ax.set_xlabel('Average Price ($)')
ax.set_ylabel('Average Location Rating')

# Display the plot in Streamlit
st.pyplot(fig)

st.markdown("### Insights")
st.markdown(
    """
    - **Trend Observation:** 
        - ?

    - **Implications for Hosts/Guests:** 
        - **For hosts:** ?
        - **For guests:** ?
    """
)


