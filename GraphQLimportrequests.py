import requests

# Set the GraphQL endpoint URL
endpoint = "https://api.yelp.com/v3/graphql"

# Set the API key
api_key = "XkgpGFswfyPZ3TS1I0RVYZp6VXsEKWqzsTNfRpXaeKwWJHaNJTARh_s5SIYFRanopJH6nSOIRPBjKwBxPrGu88tk838DJJL-1h7YTVsGsirrONUDCwbz6qIKzHarY3Yx"


# Set the headers for the GraphQL request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/graphql"
}

# Set the GraphQL query
query = """
query {
  search(term: "restaurants", location: "Los Angeles, CA", limit: 50) {
    total
    business {
      id
      name
      rating
      price
      location {
        address1
        city
        state
      }
      coordinates {
        latitude
        longitude
        }
    reviews {
        id
        text
        }
    }
  }
}
"""

# Send the GraphQL request to the endpoint
response = requests.post(endpoint, headers=headers, data=query)

# Print the response from the GraphQL API
print(response.json())

json_data = response.json()

import pandas as pd

import pandas as pd

# Load the JSON data into a pandas DataFrame
df = pd.json_normalize(json_data['data']['search']['business']['reviews'])

# Print the DataFrame
print(df)


df.to_csv('~/projects/YelpData/yelpgraphQL.csv', index=False)