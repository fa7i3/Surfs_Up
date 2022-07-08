# Surfs_Up
# Overview of the Analysis.
The purpose of the analysis is to get more information about temperature trends which will assist W. Avy make decisions about opening a surf shop. He specifically wants to get the temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round. He wants us to specifically use Python, Pandas functions and methods, and SQLAlchemy, to filter the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the months of June and December. He wants us to convert the temperatures to a list, create a DataFrame from the list, and generate the summary statistics.

* The analysis consists of two parts:

i) Rainfall analysis for June and December for 2010-2017;
ii) Temperature analysis for June and December for 2010-2017.

# Resources
Dependencies:
* pandas
* numpy
* matplotlib.pyplot
* sqlalchemy
* psycopg2
* datetime

Languages:
* Python SQL toolkit and Object Relational Mapper
* SQL

Software:
* SQL
* Flask Web Server
* Jupyter Notebook

# Results.
# Differences in weather between June and December.
The first 2 charts below show the temperature statistics for June and December.
1. Data:
  June has more data points (1700) while December has a reduced number of data points (1517).
2. Data Dispersion:
  * The mean of June's temperature is 74.94 while that of December is 71.04.
  * The median of June's temperature is 75.00 while that of December is 71.00.
  * December has a more spread out temperature than June.

  ![june temp stata](https://user-images.githubusercontent.com/104453593/178044974-9088c07e-a74d-4bd8-9849-c97c124b1e81.PNG)
  
  
![dec temp stats](https://user-images.githubusercontent.com/104453593/178045026-f2d64e9c-cfc6-4e6d-926f-7ae76d467c2f.PNG)

# Summary.
# An additional query shows the precipitation (Rainfall) comparison for June and December.
The first 2 charts below show the rainfall statistics for June and December.
1. Data:
  June has more data points (1574) while December has a reduced number of data points (1405).
2. Data Dispersion:
  * Rainfall is more spread out in December than June.
  * The mean of June's rainfall is 0.13 while that of December is 0.21.
  * The median of June's rainfall is 0.02 while that of December is 0.03.
  
  ![june precip stats](https://user-images.githubusercontent.com/104453593/178046663-fefcbb9c-37d0-4b51-a12e-02f264df1cb4.PNG)
  
  ![Dec precip stats](https://user-images.githubusercontent.com/104453593/178046706-83bbeed8-b9d2-465b-8209-2995891e0471.PNG)


  
