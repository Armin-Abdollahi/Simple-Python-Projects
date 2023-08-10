#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

def currency_converter(amount, from_currency, to_currency):
    # API endpoint to receive exchange rates
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    # GET request to get the currency price
    response = requests.get(url)

    # Checking the success of the request
    if response.status_code == 200:
        data = response.json()
        conversion_rate = data['rates'][to_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return "Error: Unable to retrieve exchange rate."

# Example of using the currency_converter function
amount = float(input("Enter the desired amount: "))
from_currency = "USD"
to_currency = "EUR"

converted_amount = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

