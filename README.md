<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/1280px-Airbnb_Logo_B%C3%A9lo.svg.png" height="200"/>

## Project Overview

> 📊 Please see our analysis at [**🔗https://airbnb-analysis.streamlit.app/**](https://airbnb-analysis.streamlit.app/)

This repository contains the code for the final project of our UT Austin MSITM Data Management course. The goal of this project is to analyze Airbnb market dynamics in Chicago. We chose Chicago because it is an extremely diverse city that  has a rich history with multiple communities. Since Chicago is also a destination city in the US we wanted to analyze the AirBNBs in Chicago.

Our analysis investigates the following topics:

### Tab 1: Market Dynamics 📈

* Change of listing’s price over time

* Time series analysis of the frequency of reviews for the listing

### Tab 2: Host Insights 👤

* Distribution of hosts by number of listings 

* How many hosts have a profile pic and/or are a superhost 

* Is a host being a superhost correlated with more monthly reviews? 

* Relationship between a host's experience (days/duration) on the platform vs average price of listings

### Tab 3: Neighborhood Analysis 🏘️

* Top 15 Chicago neighborhoods by average Airbnb rental cost

* Bottom 15 Chicago neighborhoods by average Airbnb rental cost

* Are listing prices positively or negatively correlated with changes in the amount of crime reports in Chicago as a whole?

### Tab 4: Price and Reviews 🏷️💬

* Relationship between average price vs average reviews grouped by neighborhood 

* Relationship between the average price of a listing and the overall rating 

* Relationship between the average price of a listing and the cleanliness rating 

* Relationship between the average price of a listing and the average location rating 

### Tab 5: Listing Characteristics 🛏️

* How does Airbnb type (room type) affect the average price of a listing? 

* Availability of which amenity has the highest impact on price and what is the average price of an Airbnb with that amenity?

## Local Deployment

cd into the project directory and run the following commands:

```
pip install -r requirements.txt
```

```bash
streamlit run streamlit/Overview.py
```