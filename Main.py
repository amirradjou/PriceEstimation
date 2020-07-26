import requests
from bs4 import BeautifulSoup
from sklearn import tree
import re

# Take Brand and Model From User
print("What is your car company?")
brand = input()
print("What is your car model?")
model = input()

# Request site address with data which given by user
req = requests.get('https://www.cazoo.co.uk/used-cars/' + brand + '/' + model + '/')

# req = requests.get('https://www.cazoo.co.uk/used-cars/volvo/xc60/')

# Using BS4 library for make data readable (Beautiful Soup)
soup = BeautifulSoup(req.text, 'html.parser')

# Initializing x,y for Estimation the price
x = []
y = []

# Separating list of cars from data
list_of_cars = soup.find_all('li', attrs={'class': 'resultsstyles__ResultsListItem-sc-11kjmxu-1 cxpeqB'})

for car in list_of_cars:
    distance, year = car.find_all(attrs={'class': "vehicle-cardstyles__Tag-sc-1bxv5iu-8 bnKmZw"})
    name = car.find(attrs={'class': "vehicle-cardstyles__Title-sc-1bxv5iu-5 WlyWk"})
    price = car.find(attrs={'class': "vehicle-cardstyles__PriceValue-sc-1bxv5iu-11 iFsKIn"})

    # Convert them to String
    price = str(price.text).replace('£', '')
    name = str(name.text)
    year = str(year.text).replace(' reg', '')
    distance = str(distance.text).replace(' miles', '')

    year = int(year)
    distance = int(distance.replace(',', ''))
    price = int(price.replace(',', ''))

    # Check this to observe your data!
    # print('name: ' + name + " year: " + str(year) + " distance: " + str(distance) + " price: " + str(price))

    # Using sk-learn library for estimating price
    x.append([year, distance])
    y.append(price)

# Making our prediction engine ready!!!
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
test_data = [[19, 5], [19, 500], [20, 5], [20, 500]]

# Car's Model and Distance
print("Please enter your car's model(year): ")
user_car_model = input()
print("How many KMs your car drive till now?")
user_car_km = input()

# Prediction !!!
for data in (clf.predict(test_data)):
    print(data)
predicted_price = clf.predict([[user_car_model, user_car_km], ])
print("You can sell your car about " + str(predicted_price) + " euro right now!!!")

"""Unfortunately this library is not good enough for estimating car's price right."""
'''But this code can introduce you the way of estimating the car's price with web scraping'''
