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

# ------------------------ ANALYIS 1 - Average Price of a Listing by Airbnb Type ------------------------ #

st.markdown("## 1️⃣ Average Price of a Listing by Airbnb Type")

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