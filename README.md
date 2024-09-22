# Stock Market ETL


## Overview
The stock market ETL process involves collecting stock data from various sources, transforming it into a structured format, and loading it into a data warehouse or database for analysis and visualization. This process can be scheduled to run periodically (e.g., daily, hourly) to keep your data up-to-date.


## Detailed Steps
1. Data Extraction
Objective: Fetch stock market data using an external API (e.g., Alpha Vantage, IEX Cloud).
Process:
Use the requests library to connect to the API endpoint and retrieve data in JSON format.
Handle potential errors such as failed requests or missing data.
Output: Raw stock data in JSON format, which is converted into a pandas DataFrame for further processing.
2. Data Transformation
Objective: Prepare the raw data for insertion into the PostgreSQL database.
Process:
Clean the data, handle missing values, and convert data types as necessary.
Create new columns or features if needed (e.g., moving averages).
Output: A structured and cleaned pandas DataFrame ready for database insertion.
3. Data Loading
Objective: Insert the cleaned data into a PostgreSQL database.
Process:
Establish a connection to the PostgreSQL database using psycopg2.
Create the necessary table if it doesn’t exist.
Insert the data into the table, handling any potential conflicts or duplicate entries.
Output: Data successfully stored in the PostgreSQL database.
4. Notification System
Objective: Notify the user about the ETL process status via Telegram.
Process:
Use the python-telegram-bot library to send a message to a specified Telegram chat upon successful data loading or in case of any errors during the ETL process.
Output: A Telegram message indicating the success or failure of the ETL process.
