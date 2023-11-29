import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Custom imports
from data import SnowflakeConnector
from util import handle_env

# Set up page configuration
st.set_page_config(page_title="🛏️ Listing Characteristics", page_icon="🛏️")

# Markdown for the page
st.markdown(
    """
    # 🛏️ Listing Characteristics
    
    In this analysis we aim to answer the following two questions:
    
    1. How does Airbnb type (room type) affect the average price of a listing?
    2. Availability of which amenity has the highest impact on price and what is the average price of an Airbnb with that amenity?
    """
)

# Set up environment and database connection
handle_env()
snowflake_cxn = SnowflakeConnector()

q3_df = snowflake_cxn.suhas_query_3()

# ------------------------ ANALYIS 1 - Effect of Airbnb Type on Average Listing Price ------------------------ #

st.markdown(
    """
    ## 1️⃣ Effect of Airbnb Type on Average Listing Price
    
    In the following analysis we aim to investigate the effect of Airbnb (room type) on average listing price.
    """
)

# Set the theme for the seaborn plot
sns.set_theme(style="ticks")

# Create the bar plot
plt.figure(figsize=(15, 10))
ax = sns.barplot(x='ROOM_TYPE', y='AVERAGE_PRICE', data=q3_df, palette='cool')

# Add titles and labels
plt.title('Average Price by Room Type')
plt.ylabel('Average Price ($)')
plt.xlabel('Room Type')

# Rotate X-axis labels
plt.xticks(rotation=45)

# Display the average price above each bar
for p in ax.patches:
    ax.annotate(f'${p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points')

# Use Streamlit to display the plot
st.pyplot(plt)

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

# ------------------------ ANALYIS 2 - Availability of amenity impact on price, and what is the average price of an Airbnb with that amenity ------------------------ #

st.markdown(
    """
    ## 2️⃣ Amenity Availability Impact on Price
    
    In the following analysis we aim to investigate the impact of amenity availability on price.
    """
)

q4_df = snowflake_cxn.suhas_query_4()
q4_df = q4_df.T.reset_index()
q4_df.columns = ['AMENITIES', 'AVERAGE_PRICE']

# Streamlit sidebar widgets for interactivity, if needed
# For example, a multiselect widget to choose specific amenities to display
selected_amenities = st.multiselect(
    'Select Amenities to Display',
    options=q4_df['AMENITIES'].unique(),
    default=q4_df['AMENITIES'].unique()
)

# Filter the dataframe based on the selected amenities
filtered_data = q4_df[q4_df['AMENITIES'].isin(selected_amenities)]

# Set the aesthetic style of the plots
sns.set_theme(style="ticks")

# Create a figure for matplotlib
fig, ax = plt.subplots(figsize=(15, 10))

# Create a bar plot
sns.barplot(x='AMENITIES', y='AVERAGE_PRICE', data=filtered_data, palette='cool', ax=ax)

# Add titles and labels
ax.set_title('Average Price by Availability of Amenities')
ax.set_ylabel('Average Price ($)')
ax.set_xlabel('Amenities')

# Rotate X-axis labels
plt.xticks(rotation=45)

# Display the average price above each bar
for p in ax.patches:
    ax.annotate(f'${p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points')

# Adjust the layout
plt.tight_layout()

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