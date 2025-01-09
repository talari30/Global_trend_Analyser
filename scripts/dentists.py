# Import libraries
import sys
import csv
import os

data = "../data/dentists.csv"
sql = "../sql_commands/dentists.sql"
country_sql = "../sql_commands/dentists_country.sql"
year_sql = "../sql_commands/dentists_year.sql"

TABLE_NAME = "NUMBER_OF_DENTISTS"

# Create .sql file for medical doctors
with open(data, 'r') as infile:
    with open(sql, 'w') as outfile:
        with open(country_sql, 'w') as countryfile:
            with open(year_sql, 'w') as yearfile:
                csv_reader = csv.reader(infile)
                # Skip the first two header rows
                next(csv_reader)
                hiID = 0 
                for row in csv_reader:
                    COUNTRY = row[0].split("(")[0].replace("'","")
                    YEAR = row[1]
                    NUM_DENTISTS = row[3] if len(row[3]) != 0 else "NULL"
                    outfile.write("INSERT INTO " + TABLE_NAME + " VALUES (" + str(hiID) + "," + "'" + COUNTRY + "'" + "," + YEAR + "," + NUM_DENTISTS + ");" + "\n")
                    countryfile.write("INSERT INTO " + "COUNTRY" + " VALUES (" + "'" + COUNTRY + "'" + ");" + "\n")
                    yearfile.write("INSERT INTO " + "TIME_YEAR" + " VALUES (" + YEAR + ");" + "\n")
                    hiID += 1
                