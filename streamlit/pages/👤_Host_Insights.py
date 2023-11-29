"""
Distribution of hosts by number of listings (Srishti's code)
How many hosts have a profile pic and/or are a superhost (Srishti's code)
Is a host being a superhost correlated with more monthly reviews? (Srishti's code)
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Custom imports
from data import SnowflakeConnector
from util import handle_env

# Set up page configuration
st.set_page_config(page_title="👤 Chicago Airbnb Host Insights", page_icon="👤")

# Markdown for the page
st.markdown("# 👤 Chicago Airbnb Host Insights")
st.sidebar.header("👤 Chicago Airbnb Host Insights")

# Description
st.markdown(
    """
    Here, we'll explore the distribution of hosts in the Chicago Airbnb market by their number of listings, investigate the prevalence of profile pictures and superhost status, and analyze whether being a superhost is associated with an increase in monthly reviews. This exploration aims to shed light on the factors that may contribute to a host's success and visibility on the platform.
    
    ### 🗂️ Dataset Used:
    
    For this analysis, we are querying the `listings.csv` dataset, stored in Snowflake due to its astronomical size. Since this datset has over 70 features we cannot neatly display the head here, but the dataset includes a comprehensive range of information for each listing:
    
    * **Listing Details:** Listing ID, name, and detailed description.
    * **Host Information:** Host ID, name, since when they have been hosting, their location, about them, response time, and rates.
    * **Superhost Status:** Whether the host is a superhost, their neighborhood, total listings count.
    * **Location Details:** Latitude and longitude for geospatial analysis.
    * **Property Details:** Property type, room type, how many it accommodates, bathroom details, bedrooms, beds, and amenities offered.
    * **Pricing and Booking Conditions:** Price per night, minimum and maximum nights stay, average nights.
    * **Availability and Reviews:** Calendar availability, number of reviews, recent reviews, and review scores across various dimensions.
    * **Licensing and Booking:** Licensing information, if instant booking is available, and counts of host listings in various categories.
    * **Miscellaneous:** The average number of reviews per month, encoded categorical variables for analysis, community names, and IDs.

    """
)

# Set up environment and database connection
handle_env()
snowflake_cxn = SnowflakeConnector()


# ------------------------ ANALYIS 1 - VISUALIZE DISTRIBUTION OF HOSTS BY NUMBER OF LISTINGS ------------------------ #

st.markdown("## 1️⃣ Distribution of Hosts by Number of Listings")
st.markdown(
    """
    Here we will investigate the distribution of hosts by the number of listings they have on Airbnb.
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


# Get data
q2_df = snowflake_cxn.query_2()

# Define custom bins for the number of listings
bins = [0, 1, 5, 10, 20, 50, 100, 650]

# Use pd.cut to bin the number of listings into defined ranges
q2_df['Listing_Range'] = pd.cut(q2_df['LISTING_COUNT'], bins=bins, right=False)
# Convert the 'Listing_Range' to string, which is JSON serializable
q2_df['Listing_Range'] = q2_df['Listing_Range'].astype(str)

# Aggregate the number of hosts within each bin
binned_hosts = q2_df.groupby('Listing_Range')['HOST_COUNT'].sum().reset_index()

fig = px.pie(
    binned_hosts, 
    names='Listing_Range', 
    values='HOST_COUNT',
    # title="Proportion of Hosts by Listing Count",
    color_discrete_sequence=px.colors.sequential.RdBu  # Aesthetically pleasing color
)

# Enhance the layout
fig.update_traces(textinfo='percent+label', pull=[0.1 if i == binned_hosts['HOST_COUNT'].idxmax() else 0 for i in range(len(binned_hosts))])

# Display the figure in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Insights")
st.markdown(
    """
    - **Trend Observation:** 
        - Majority of Airbnb hosts have between 1 to 5 listings, suggesting a market dominated by individuals or small-scale operators rather than large property managers.
        - Hosts with a high number of listings (50-800) are significantly fewer.
        - There is only one host with 100+ listings, which is an outlier in the data.

    - **Implications for Hosts/Guests:** 
        - **For hosts:** The predominance of hosts with fewer listings suggests that new entrants to the Airbnb hosting market can compete effectively without the need for multiple properties. The focus for these hosts should be on quality and guest experience to stand out.
        - **For guests:** Guests are likely to encounter a more personalized service and unique listings, as the market is not saturated with mass-managed properties. There may also be a higher chance of dealing directly with property owners, which can lead to better communication and a more personal touch during their stay.
    """
)

# ------------------------ ANALYIS 2 - How many hosts have a profile pic and/or are a superhost ------------------------ #

st.markdown("## 2️⃣ Determine if Superhost Status is Associated with More Monthly Reviews")
st.markdown(
    """
    Here we aim to answer the question: **How many hosts have a profile pic and/or are a superhost?**
    
    First, we will look at the distribution of hosts by whether they have a profile picture and/or whether they are a superhost:
    """
)

q3_df = snowflake_cxn.query_3()
st.table(q3_df)

# Create a new column to represent the combination of profile pic and superhost status
conditions = [
    (q3_df['HOST_HAS_PROFILE_PIC'] == 1) & (q3_df['HOST_IS_SUPERHOST'] == 1),
    (q3_df['HOST_HAS_PROFILE_PIC'] == 1) & (q3_df['HOST_IS_SUPERHOST'] == 0),
    (q3_df['HOST_HAS_PROFILE_PIC'] == 0) & (q3_df['HOST_IS_SUPERHOST'] == 1),
    (q3_df['HOST_HAS_PROFILE_PIC'] == 0) & (q3_df['HOST_IS_SUPERHOST'] == 0)
]

choices = ['Profile Pic & Superhost', 'Profile Pic Only', 'Superhost Only', 'Neither']

q3_df['Category'] = np.select(conditions, choices)

# Create an interactive stacked bar chart using Plotly Express
fig = px.bar(
    q3_df, 
    x='Category', 
    y='HOST_COUNT',
    title="Host Distribution by Profile Picture and Superhost Status",
    labels={'HOST_COUNT':'Number of Hosts'},
    color='Category',
    color_discrete_map={
        'Profile Pic & Superhost': 'lightseagreen',
        'Profile Pic Only': 'gold',
        'Superhost Only': 'tomato',
        'Neither': 'silver'
    }
)

# Enhance the layout
fig.update_layout(
    plot_bgcolor='white',
    yaxis=dict(
        title='Number of Hosts',
        gridcolor='lightgray',
        gridwidth=1
    ),
    xaxis=dict(
        title='Category',
        tickangle=45
    ),
    title=dict(
        x=0.5,
        xanchor='center',
        font=dict(size=18)
    )
)

# Display the figure in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("Given these insights, let's now visualize how superhost status affects the number of monthly reviews a host receives.")

q6_df = snowflake_cxn.query_6()

# Create histograms for superhosts and non-superhosts
fig = go.Figure()

# Histogram for superhosts
fig.add_trace(go.Histogram(
    x=q6_df[q6_df['HOST_IS_SUPERHOST'] == 1]['AVG_REVIEWS_PER_MONTH'],
    name='Superhosts',
    marker_color='skyblue',
    opacity=0.75
))

# Histogram for non-superhosts
fig.add_trace(go.Histogram(
    x=q6_df[q6_df['HOST_IS_SUPERHOST'] == 0]['AVG_REVIEWS_PER_MONTH'],
    name='Non-Superhosts',
    marker_color='salmon',
    opacity=0.75
))

# Set plot labels and title
fig.update_layout(
    title='Distribution of Average Reviews per Month (Superhosts vs Non-Superhosts)',
    xaxis_title='Average Reviews per Month',
    yaxis_title='Frequency',
    bargap=0.2,
    xaxis=dict(range=[0, 8]),
    legend=dict(
        x=0.8,
        y=1,
        bgcolor='rgba(255, 255, 255, 0.5)',
        bordercolor='rgba(255, 255, 255, 1)'
    )
)

# Display the figure in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    ### Insights

    - **Trend Observation:** 
        - The distribution of average reviews per month for both superhosts and non-superhosts is right-skewed, with a higher concentration of hosts receiving fewer reviews.
        - Superhosts show a prominent peak at lower review counts, suggesting that even highly rated hosts may have months with fewer reviews.
        - The long tail for both groups indicates that very high review counts per month are less common.

    - **Implications for Hosts/Guests:** 
        - **For hosts:** The data suggests that maintaining superhost status does not necessarily equate to a higher number of reviews per month. Focus on consistent quality service may be more beneficial than solely aiming for a higher quantity of reviews.
        - **For guests:** When choosing hosts, the presence of a superhost badge indicates quality but not necessarily frequency of reviews, which could be due to various factors such as new listings or off-peak seasons.

    """
)