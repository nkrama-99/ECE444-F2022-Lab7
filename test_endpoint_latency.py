import requests

response = requests.post('http://ece444-lab7-v1-env.us-east-2.elasticbeanstalk.com/predict', json = {'text':'The ocean is big'})
response = response.json()
print(response['prediction'])
