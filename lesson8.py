import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("covid_data.csv")
print(data)
"""
# DO FOR HW and other countries

print(data.loc[data["Country_Region"] == "Afghanistan", "Deaths"].sum())

max_deaths = data.groupby("Country_Region")["Deaths"].sum().nlargest(5)
print(max_deaths)

max_recovery = data.groupby("Country_Region")["Recovered"].sum().nlargest(10)
print(max_recovery)

max_confirmed = data.groupby("Country_Region")["Confirmed"].sum().nlargest(5)
print(max_confirmed)

death_chart= px.bar(max_deaths,x = max_deaths.index,y = "Deaths")
death_chart.write_html("COVID_death_chart.html", auto_open = True )

recovery_graph= px.scatter(max_recovery,x = max_recovery.index,y = "Recovered",size = "Recovered",size_max=50)
recovery_graph.write_html("COVID_recovered_graph.html", auto_open = True )

confirmed_chart= px.bar(max_confirmed,x = max_confirmed.index,y = "Confirmed")
confirmed_chart.write_html("COVID_confirmed_chart.html", auto_open = True )
"""
US = data.loc[data["Country_Region"] == "US"]
max_deaths_US = US.nlargest(5,"Deaths")
print(max_deaths_US)

death_chart_US= px.bar(max_deaths_US,x = max_deaths_US["Province_State"],y = "Deaths")
death_chart_US.write_html("COVID_death_chart_US.html", auto_open = True )