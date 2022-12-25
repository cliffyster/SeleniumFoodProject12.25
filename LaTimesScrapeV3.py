from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd

data = []

driver = webdriver.Chrome()
driver.get('https://archive.ph/eX295')

# Create a list of XPath expressions
xpaths = [
    '//div[@data-map-marker-latitude]'
]

# Loop over the list of XPath expressions
for xpath in xpaths:
    # Find all elements that match the current pattern
    elements = driver.find_elements(By.XPATH, xpath)

    # Create a list of attribute names
    attributes = ['data-map-marker-latitude', 'data-map-marker-longitude', 'data-map-marker-title',
                 'data-module-cuisines', 'data-module-neighborhood', 'data-module-price']

    # Loop over the elements and process them
    for element in elements:
        element_data = {}
        # Loop over the attributes and extract their values
        for attribute in attributes:
            value = element.get_attribute(attribute)
            element_data[attribute] = value
            print(value)
        data.append(element_data)

df = pd.DataFrame(data)
print(df)

driver.close()

df.to_csv('~/projects/LaTimesBestOfData/LaTimes2022101.csv', index=False)


"""
It looks like the issue is that the data variable is being overwritten with the value of element.get_attribute(attribute) in the loop over attributes. This is causing the append method to fail, because data is now a string and does not have an append method.

To fix the issue, you can modify the code to use a different variable name for the data being extracted from the element.get_attribute(attribute) method. For example, you could change the code to use the value variable like this:
"""