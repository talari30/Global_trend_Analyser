# Import libraries
import sys
import csv
import os

data = "../data/obesity.csv"
sql = "../sql_commands/obesity.sql"
country_sql = "../sql_commands/obesity_country.sql"
year_sql = "../sql_commands/obesity_year.sql"

TABLE_NAME = "OBESITY"

# Create .sql file for obesity 
with open(data, 'r') as infile:
    with open(sql, 'w') as outfile:
        with open(country_sql, 'w') as countryfile:
            with open(year_sql, 'w') as yearfile:
                csv_reader = csv.reader(infile)
                # First line is all the years. Have to do some preprocessing.
                years = list(set(next(csv_reader)))
                int_years = []
                for year in years:
                    if len(year) != 0:
                        int_years.append(int(year))
                # Sort the int years in descending order to get same ordering
                int_years.sort(reverse = True)
                # Skip next few rows 
                next(csv_reader)
                next(csv_reader)
                next(csv_reader)

                # Each preceding row contains country information
                hiID = 0
                for row in csv_reader:
                    COUNTRY = row[0].split("(")[0].replace("'","")
                    row = row[1:] # Subset the row to remove first element
                    year_counter = 0
                    for i in range(len(row)):
                        if (i % 3) == 0:
                            BOTH_SEXES = row[i].split(" ")[0] if row[i].split(" ")[0] != "No" else "NULL"
                        if (i % 3) == 1:
                            MALE = row[i].split(" ")[0] if row[i].split(" ")[0] != "No" else "NULL"
                        if (i % 3) == 2:
                            FEMALE = row[i].split(" ")[0] if row[i].split(" ")[0] != "No" else "NULL"
                            YEAR = str(int_years[year_counter])
                            outfile.write("INSERT INTO " + TABLE_NAME + " VALUES (" + str(hiID) + "," + "'" + COUNTRY + "'" + "," + YEAR + "," + BOTH_SEXES + "," + MALE + "," + FEMALE + ");" + "\n")
                            countryfile.write("INSERT INTO " + "COUNTRY" + " VALUES (" + "'" + COUNTRY + "'" + ");" + "\n")
                            yearfile.write("INSERT INTO " + "TIME_YEAR" + " VALUES (" + YEAR + ");" + "\n")
                            hiID += 1
                            year_counter += 1
                            

           