import requests
from datetime import datetime

TOKEN = "wjkjklfsuihfjs"
USERNAME = "nataliagvcs"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_params = {"token": TOKEN ,
                 "username": USERNAME,
                 "agreeTermsOfService": "yes",
                 "notMinor": "yes"
                 }

# post_response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(post_response.text)

GRAPH_ID = "graph0"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {"id": GRAPH_ID,
                "name": "Coding Practice Graph",
                "unit": "commit",
                "type": "int",
                "color": "shibafu"}
headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
today = datetime(year=2023, month=2, day=14).strftime("%Y%m%d")

post_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_value_params = {"date": today,
                     "quantity": "15"
                     }

# response = requests.post(url=post_value_endpoint, json=post_value_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_pixel_params = {"quantity": "7"}
#
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)

