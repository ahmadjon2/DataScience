import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as gu

data = pd.read_csv("WHO-COVID-19-global-data.csv")
#print(data.info())
data["DateReported"] = pd.to_datetime(data["DateReported"])
print(data.info())
timeData = data.groupby("DateReported").sum()
print(timeData["New_cases"])
timeDeathData = data.groupby("DateReported").sum()
print(timeDeathData["New_deaths"])

figure1 = gu.Figure()
figure1.add_trace(gu.Scatter(x=timeData.index,y=timeData["Cumulative_cases"],fill="tonexty",line_color="yellow"))
figure1.update_layout(title = "Cumulative cases over time")
figure1.write_html("figure1.html", auto_open = True ,)


figure2 = gu.Figure()
figure2.add_trace(gu.Scatter(x=timeData.index,y=timeData["Cumulative_deaths"],fill="tonexty",line_color="red"))
figure2.update_layout(title = "Cumulative deaths over time")
figure2.write_html("figure2.html", auto_open = True )

figure3 = gu.Figure()
figure3.add_trace(gu.Scatter(x=timeData.index,y=timeData["New_cases"],fill="tonexty",line_color="yellow"))
figure3.update_layout(title = "New cases over time")
figure3.write_html("figure3.html", auto_open = True )

figure4 = gu.Figure()
figure4.add_trace(gu.Scatter(x=timeData.index,y=timeData["New_deaths"],fill="tonexty",line_color="red"))
figure4.update_layout(title = "New deaths over time")
figure4.write_html("figure4.html", auto_open = True )