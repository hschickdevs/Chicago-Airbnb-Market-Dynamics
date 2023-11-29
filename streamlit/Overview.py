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

"""
)