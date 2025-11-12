import csv

try:
    with open("lab9.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        print("Country Name: 2010-2019")

        for row in reader:
            if len(row) >= 14:
                country_code = row[4].strip().replace('"', '')
                years_data = row[5:14]
                years_data = [x.strip().replace('"','') for x in years_data]
                print(f"Inflation: {country_code}, {', '.join(years_data)}")

except Exception as e:
    print(f"File lab9.csv not found or reading error: {e}")


try:
    with open("lab9.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = [ [x.strip().replace('"','') for x in row] for row in reader if len(row) >= 14 ]

    usa_row = None
    ukr_row = None
    for row in data:
        country_code = row[4]
        if country_code == "USA":
            usa_row = row
        elif country_code == "UKR":
            ukr_row = row

    if not usa_row or not ukr_row:
        print("Data for USA or Ukraine not found!")
    else:
        usa_values = usa_row[5:]
        ukr_values = ukr_row[5:]
        n_years = min(len(usa_values), len(ukr_values))
        years = list(range(2010, 2010 + n_years))

        usa_data = [float(x) for x in usa_values[:n_years]]
        ukr_data = [float(x) for x in ukr_values[:n_years]]

        with open("new_lab9.csv", "w", newline='') as out_csv:
            writer = csv.writer(out_csv, delimiter=';')
            writer.writerow(["Year", "USA", "UKR", "HigherInflation"])

            for i, year in enumerate(years):
                if usa_data[i] > ukr_data[i]:
                    higher = "USA"
                elif ukr_data[i] > usa_data[i]:
                    higher = "UKR"
                else:
                    higher = "Equal"
                writer.writerow([year, usa_data[i], ukr_data[i], higher])

        print("\nComparison between USA and Ukraine saved to new_lab9.csv")

except Exception as e:
    print(f"Error: {e}")














