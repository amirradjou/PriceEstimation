# Car Price Estimator

This Python script estimates the price of a car model based on its year and mileage. It utilizes web scraping techniques to extract data from a website and uses the scikit-learn library for machine learning-based prediction.

## Requirements
- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- scikit-learn library (`pip install scikit-learn`)

## Usage
1. Run the script.
2. Input the car company (brand) when prompted.
3. Input the car model when prompted.
4. Input your car's model year and mileage when prompted.

## How It Works
1. The script prompts the user to input the car company (brand) and model.
2. It then requests data from the website https://www.cazoo.co.uk/used-cars/ for the specified car brand and model.
3. The script extracts relevant information such as year, mileage, and price using BeautifulSoup.
4. It prepares the data for estimation by converting it into a suitable format.
5. Machine learning, utilizing a decision tree classifier from scikit-learn, is employed to estimate the car's price based on year and mileage.
6. The user is prompted to input their car's model year and mileage.
7. The script predicts the price of the user's car based on the input data and displays the result.

## Note
- The accuracy of the price estimation heavily depends on the availability and accuracy of data from the website.
- This code serves as an educational example of web scraping and basic machine learning techniques for estimating car prices and may require further refinement for practical use.

## Disclaimer
- This script is provided for educational purposes only.
- The accuracy of the estimated prices may vary, and it is recommended to consult multiple sources for accurate pricing information when buying or selling a car.
