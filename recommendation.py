import pandas as pd

data = pd.read_csv("movies_metadata.csv")
print(data.info())

#2 types of recommendation systems 
#best ratings

"""weighted rating
v/(v + m) * r + (m/v + m) * c
v = number of votes (vote count)
m = minimum votes required to be listed in chart
r = average rating for the movie 
c = mean vote across the whole report
"""

r = data["vote_average"]
c = data["vote_average"].mean()
m = data["vote_count"].quantile(0.9)

print(r)
print(c)
print(m)

top10p = data.loc[data["vote_count"] >= m]
print(top10p.shape)
def weighted_rating(x,m=m,c=c):
    v = x["vote_count"]
    r = x["vote_average"]
    ans = v/(v + m) * r + (m/(v + m)) * c
    return ans
top10p["score"] = top10p.apply(weighted_rating,axis = 1)
print(top10p)