# FinalProjectGroupD
Final Team Project

## TOPIC
Predict housing prices in New York City with additional features around broad economic factors.  

### Reason 
* We are looking to predict housing prices in NYC.  As we currently are living through a global pandemic that is dramatically effecting the housing markets in and around the city.  We wanted to see if we could draw any correlation between COVID and these prices.  As we did our EDA we discovered that there is a bit of 'lag time' and 'volativity' between COVID cases directly and hosing prices.  Therefore, we chose our additional features (income & unemployment) over COVID cases direclty to remove what we saw as having a negative impact our our predictions.  We still feel that as additional data becomes available these additional features will continue to enhance the accruace of the model where as other housing models may not be able to adapt to these dramatic changes in the NYC housing market.

### Description - source of data
* We are planning to use three sources of data.
  * Unemployment Data - https://www.bls.gov/lau/#tables
  * Income Data from IRS - https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2018-zip-code-data-soi
  * scraping housing data from online sources: price, sold date, sq ft, bedrooms, bathrooms, zipcode

* Database
  * pgAdmin
    * Table 1 - Housing Table
      * address
      * zipcode
      * Date Sold
      * number of bedrooms
      * number of Bathrooms
      * sq feet
      * Price
    
    * Table 2 - zipcode to boro (transaltion table)
        * zipcode
        * city
        * county
        * type
        * boro
     
     * Table 3 - Income
        * boro
        * number of people with income over 100k
        * number of people with income under 100k
      
     * Table 4 - Unemployed
        * boro
        * number of people employed
        * number of people unemployed



#google slides link
https://docs.google.com/presentation/u/1/d/1hO2fdHAkZdISUFA_js0r_3JiT6kwvqU1uQD0ovW75JQ/edit?usp=sharing

      
### Questions we hope to answer

* How does unemployement affected housing prices?
* How does income impacts housing prices?
* On the side - we are also planning to have seperate impact analysis due to COVID if time permits. - # of COVID CASES by the Zipcode and housing prices.
