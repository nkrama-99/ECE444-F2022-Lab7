import requests
from datetime import datetime

results = []

for i in range(100):
    startTime = datetime.now()
    response = requests.post('http://ece444-lab7-v1-env.us-east-2.elasticbeanstalk.com/predict', json = {'text':'The ocean is big'})
    response = response.json()
    endTime = datetime.now()
    delta = (endTime - startTime).total_seconds() * 1000
    
    if (response['prediction'] == "REAL"):
        results.append(delta)
        print(i, "Response time:", delta, "ms")
    else:
        print("unexpected failure")
        
averageLatency = sum(results) / len(results)
print("Number of requests made:", len(results))
print("Average latency:", averageLatency)
