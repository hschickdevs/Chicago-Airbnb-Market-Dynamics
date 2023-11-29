# data-management-final
 Contains the code files & streamlit app for the MSITM Data Management final project.

## Local Deployment

cd into the project directory and run the following commands:

```
pip install -r requirements.txt
```

```bash
streamlit run streamlit/Overview.py
```

## Pages:

### Overview Page:

1. Project Selection & Motivations - Why did we choose this project?

2. Data Sourcing & Acquisition process + challenges faced

3. Data sample(s)

3. Notable steps from the Data Cleaning & Transformation process

    * ETL tools used?

    * Provide a sample of the cleaned data.

4. Questions we are trying to answer with the data

    * Outline the types of questions your group aimed to answer through the project.

5. Tools used for the analysis

    * Detail the tools and technologies used during the project. Mention any specific requirements.

6. Real-world impact

    * Explain how the outcomes of your work could be applied to address real-life problems or challenges.

### Questions:

* (in poon's code) Change of listing’s price over time 
* (in poon's code)Time series analysis of the frequency of reviews for the listing
* (in poon's code) Are listing prices positively or negatively correlated with changes in the amount of
crime reports in Chicago as a whole? 

* (In Srishti code) What is the distribution of hosts by number of listings?
* (In Srishti code) Distribution - How many hosts have a profile pic and/or are a superhost
* (In Srishti code) Is a host being a superhost correlated with more monthly reviews?

* (In Suhas code) Top 15 Chicago neghborhoods by average airbnb rental cost
* (In Suhas code) Bottom 15 Chicago neghborhoods by average airbnb rental cost
* (In Suhas code) What is the relationship between average price vs average reviews grouped by neighborhood?
* (In Suhas code) How does airbnb type (room type) affect the average price of a listing?
* (In Suhas code) Availability of which amenity has the highest impact on price and what is the average price of an AirBnB with that amenity?
* (In Suhas code) What is the relationship between the average price of a listing and the overall rating?
* (In Suhas code) What is the relationship between the average price of a listing and the cleanliness rating?
* (In Suhas code) What is the relationship between the average price of a listing and the average location rating?
* (In Suhas code) What is the relationship between a host's experience (days/duration) on the platform vs average price of listings?

### Page Structure:

#### Tab 1: Market Dynamics 📈
* Change of listing’s price over time (Poon's code)
* Time series analysis of the frequency of reviews for the listing (Poon's code)
#### Tab 2: Host Insights 👤
* Distribution of hosts by number of listings (Srishti's code)
* How many hosts have a profile pic and/or are a superhost (Srishti's code)
* Is a host being a superhost correlated with more monthly reviews? (Srishti's code)

ADDED -> * Relationship between a host's experience (days/duration) on the platform vs average price of listings (Suhas's code)
#### Tab 3: Neighborhood Analysis 🏘️
* Top 15 Chicago neighborhoods by average Airbnb rental cost (Suhas's code)
* Bottom 15 Chicago neighborhoods by average Airbnb rental cost (Suhas's code)
* Are listing prices positively or negatively correlated with changes in the amount of crime reports in Chicago as a whole? (Poon's code)
#### Tab 4: Price and Reviews 🏷️💬
* Relationship between average price vs average reviews grouped by neighborhood (Suhas's code)
* Relationship between the average price of a listing and the overall rating (Suhas's code)
* Relationship between the average price of a listing and the cleanliness rating (Suhas's code)
* Relationship between the average price of a listing and the average location rating (Suhas's code)
#### Tab 5: Listing Characteristics 🛏️
* How does Airbnb type (room type) affect the average price of a listing? (Suhas's code)
* Availability of which amenity has the highest impact on price and what is the average price of an Airbnb with that amenity? (Suhas's code)
