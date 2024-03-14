import pandas as pd

print("\n**************COVID-19 DATA ANALYSIS**************\n")

print("*"*50,"\n")

DataSet="https://raw.githubusercontent.com/capabletg/naukrisaksham-data-science/main/Covid%20Analysis%20-%20Phase%201.csv"

df1 = pd.read_csv(DataSet)
unique_countries = df1['Country/Region'].unique()
#print("Number of unique countries:",len(set(df['Country/Region'])))

num_unique_countries = len(unique_countries)
print("Number of unique countries : ", num_unique_countries)

print("*"*50,"\n")

null = df1.isnull().sum()
print("Null values in the dataset : ")
print(null)

print("*"*50,"\n")

max_cases = df1.loc[df1['Confirmed'].idxmax()]['Country/Region']
confirmed_cases = df1['Confirmed'].max()

print("Country with the maximum number of confirmed cases:", max_cases)
print("Number of confirmed cases:", confirmed_cases)
print("\n")
print("*"*50,"\n")

country_deaths = df1.loc[df1['Deaths'].idxmax()]['Country/Region']
max_deaths = df1['Deaths'].max()

print("Country with the maximum number of deaths:", country_deaths)
print("Number of deaths:", max_deaths)

print("*"*50,"\n")

url="https://raw.githubusercontent.com/capabletg/naukrisaksham-data-science/main/country_vaccinations.csv"
df = pd.read_csv(url)

df['date'] = pd.to_datetime(df['date'])
#to extract the Year from date
df['Year'] = df['date'].dt.year
#to extract the Month from date
df['Month'] = df['date'].dt.month
#to extract the Day from date
df['Day'] = df['date'].dt.day

#to extract the month name from date
df['Month_name'] = df['date'].dt.strftime('%b')

#to extract the full month name from date
df['Full_Month_name'] = df['date'].dt.month_name()

india_may_2021_df = df[(df['country'] == 'India') & (df['Month'] == 5) & (df["Year"]==2021)]



print("In May 2021, a total number of ",int(india_may_2021_df['people_vaccinated'].sum()),"people in India recived vaccinations")

print("*"*50,"\n")

df['date'] = pd.to_datetime(df['date'])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["Month_name"]=df['date'].dt.month_name()

vac_ind_2020 = df[(df["year"] == 2020) & (df["country"] == "India")]
vac_ind_2021 = df[(df["year"] == 2021) & (df["country"] == "India")]
vac_ind_2022 = df[(df["year"] == 2022) & (df["country"] == "India")]

print("Total people vaccinated in India in 2020:", int(vac_ind_2020["total_vaccinations"].sum()))
print("Total people vaccinated in India in 2021:", int(vac_ind_2021["total_vaccinations"].sum()))
print("Total people vaccinated in India in 2022:", int(vac_ind_2022["total_vaccinations"].sum()))

print("*"*60)

vac_usa_2020 = df[(df["year"] == 2020) & (df["iso_code"] == "USA")]
print("*"*5,"Total Vaccination in USA and India","*"*5)
print("USA -- ", int(vac_usa_2020["total_vaccinations"].sum()))
print("India -- ", int(vac_ind_2020["total_vaccinations"].sum()))
if int(vac_usa_2020["total_vaccinations"].sum()) > int(vac_ind_2020["total_vaccinations"].sum()):
    print("Total vaccinations in USA is greater than Total vaccinations in India in 2020 ")
elif int(vac_usa_2020["total_vaccinations"].sum()) < int(vac_ind_2020["total_vaccinations"].sum()):
    print("Total vaccinations in India is greater than Total vaccinations in USA in 2020 ")
else:
    print("Both Countries Total vaccinations are equal")
    
print("*"*60)
    
vac_china_2021 = df[(df["year"] == 2021) & (df["country"] == "China")]
print("*"*5,"Total Vaccination in China and India","*"*5)
print("China -- ", int(vac_china_2021["total_vaccinations"].sum()))
print("India -- ", int(vac_ind_2021["total_vaccinations"].sum()))
if int(vac_china_2021["total_vaccinations"].sum()) > int(vac_ind_2021["total_vaccinations"].sum()):
    print("Total vaccinations in China is greater than Total vaccinations in India in 2021 ")
elif int(vac_china_2021["total_vaccinations"].sum()) < int(vac_ind_2021["total_vaccinations"].sum()):
    print("Total vaccinations in India is greater than Total vaccinations in China in 2021 ")
else:
    print("Both Country's Total vaccinations are equal")

print("*"*60)

ind_2021_data = []
Max_vaccinations = 0

for i in range(len(vac_ind_2021["Month_name"].unique())):
    month_name = vac_ind_2021["Month_name"].unique()[i]
    total_vaccinations_month = int(vac_ind_2021[vac_ind_2021["month"]==i]["total_vaccinations"].sum())
    print(month_name, "-", total_vaccinations_month)
    ind_2021_data.append({'Month_name': month_name, 'Total_vaccinations': total_vaccinations_month})
    if total_vaccinations_month > Max_vaccinations:
        Max_vaccinations = total_vaccinations_month
ind_2021 = pd.DataFrame(ind_2021_data).set_index("Month_name")


print("*"*60)
max_vaccinations_month = ind_2021[ind_2021["Total_vaccinations"] == Max_vaccinations].index[0]
print(max_vaccinations_month, "is the month in India with the most vaccinations in 2021. Total vaccinations =", Max_vaccinations)
