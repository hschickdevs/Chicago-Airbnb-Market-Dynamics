"""
* Top 15 Chicago neighborhoods by average Airbnb rental cost (Suhas's code)
* Bottom 15 Chicago neighborhoods by average Airbnb rental cost (Suhas's code)
* Are listing prices positively or negatively correlated with changes in the amount of crime reports in Chicago as a whole? (Poon's code)
"""
import json
from streamlit_folium import folium_static
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import streamlit as st
import geopandas as gpd
from shapely.geometry import shape, Polygon
import folium

# Custom imports
from data import SnowflakeConnector
from util import handle_env

# Set up page configuration
st.set_page_config(page_title="🏘️ Neighborhood Analysis.py", page_icon="🏘️")

# Set up environment and database connection
handle_env()
snowflake_cxn = SnowflakeConnector()

# Markdown for the page
st.markdown(
    """
    # 🏘️ Neighborhood Analysis
    
    In this analysis we aim to answer the following two questions:
    
    * What are the top & bottom 15 Chicago neighborhoods by average Airbnb rental cost?
    * Are listing prices positively or negatively correlated with changes in the amount of crime reports in Chicago as a whole? (Poon's code)
    """
)

# ------------------------ ANALYIS 1 - Top & Bottom Chicago Neighborhoods ------------------------ #

st.markdown(
    """
    ## 1️⃣ Top and Bottom 15 Chicago Neighborhoods on Average Listing Price
    
    In the following analysis we aim to investigate the top and bottom 15 chicago neighborhoods by average listing price.
    
    ### Top 15 Neighborhoods
    """
)
q1_df = snowflake_cxn.suhas_query_1()
q1_df = q1_df.sort_values(by='AVERAGE_PRICE', ascending=False)

plt.figure(figsize=(15, 10))  # Adjust the size of the plot as needed
ax = sns.barplot(x='NEIGHBOURHOOD', y='AVERAGE_PRICE', data=q1_df[:15], palette='cool')

# Add titles and labels
plt.title('Average Price by Neighbourhood')
plt.ylabel('Average Price ($)')
plt.xlabel('Neighbourhood')

# Rotate X-axis labels
plt.xticks(rotation=45)  # Rotate labels to 45 degrees

# Display the average price above each bar
for p in ax.patches:
    ax.annotate(f'${p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points')

# Show the plot
plt.tight_layout()  # Adjust the layout

# Display the plot in Streamlit
st.pyplot(plt)

st.markdown("### Bottom 15 Neighborhoods")

# Create a bar plot
sns.set_theme(style="ticks")

plt.figure(figsize=(15, 10))  # Adjust the size of the plot as needed
ax = sns.barplot(x='NEIGHBOURHOOD', y='AVERAGE_PRICE', data=q1_df[-15:], palette='cool')

# Add titles and labels
plt.title('Average Price by Neighbourhood')
plt.ylabel('Average Price ($)')
plt.xlabel('Neighbourhood')

# Rotate X-axis labels
plt.xticks(rotation=45)  # Rotate labels to 45 degrees

# Display the average price above each bar
for p in ax.patches:
    ax.annotate(f'${p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points')

# Show the plot
plt.tight_layout()  # Adjust the layout

# Display the plot in Streamlit
st.pyplot(plt)

st.markdown(
    """
    ### Insights

    - **Trend Observation:** 
        - ?

    - **Implications for Hosts/Guests:** 
        - **For hosts:** ?
        - **For guests:** ?
    """
)

# ------------------------ ANALYIS 2 - Top & Bottom Chicago Neighborhoods ------------------------ #

st.markdown(
    """
    ## 2️⃣ Airbnb Listing Price Correlation with Crime Reports Delta in Chicago
    
    In the following analysis we aim to investiaget the correlation of Airbnb listings with crime reports in Chicago.
    """
)

df = snowflake_cxn.retrieve_community_data()

# Convert stringified GeoJSON to dictionary
df['GEOMETRY'] = df['GEOMETRY'].apply(lambda x: json.loads(x))

# Function to calculate centroids and create folium map
def create_folium_map(df):
    x_list = []
    y_list = []
    
    # Calculate centroids
    for index, row in df.iterrows():
        polygon = Polygon(row['GEOMETRY']['coordinates'][0][0])
        centroid_point = polygon.centroid
        x_list.append(centroid_point.x)
        y_list.append(centroid_point.y)
    
    df['X'] = x_list
    df['Y'] = y_list
    
    # Now you can apply 'shape' to each GeoJSON object
    gdf = gpd.GeoDataFrame(df, geometry=[shape(geojson) for geojson in df['GEOMETRY']])
    gdf.set_crs(epsg=4326, inplace=True)  # Set the coordinate reference system to WGS84
    
    # Create a folium map centered on Chicago
    chicago_map = folium.Map(location=[41.8781, -87.6298], zoom_start=10)
    
    # Add the geospatial data to the map
    folium.Choropleth(
        geo_data=gdf,
        data=gdf,
        columns=['COMMUNITY_ID', 'CRIME_RATE'],
        key_on='feature.properties.COMMUNITY_ID',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Crime Rate',
    ).add_to(chicago_map)
    
    # Add markers for average room prices
    for index, row in df.iterrows():
        folium.Marker(
            location=[row['Y'], row['X']],
            popup=row['NAME'],
            icon=folium.DivIcon(html=f"<div style='font-size: 8pt; color: black;'>${row['AVG_PRICE']}</div>")
        ).add_to(chicago_map)
    
    return chicago_map

# Assuming df is your DataFrame with the necessary data
# You would call your database or CSV load function here to get the df ready

# Display the map in Streamlit
st_folium_map = create_folium_map(df)
folium_static(st_folium_map)

st.markdown(
    """
    ### Insights

    - **Trend Observation:** 
        - ?

    - **Implications for Hosts/Guests:** 
        - **For hosts:** ?
        - **For guests:** ?
    """
)