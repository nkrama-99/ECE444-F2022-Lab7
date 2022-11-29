import requests
from datetime import datetime

numberOfRequests = 100

testData = [
    ['The ocean is big', 'REAL'],
    ['biden is president', 'REAL'],
    ['The earth is flat', 'FAKE'],
    ['The ocean is red', 'FAKE']
]

for data in testData:
    text = data[0]
    res = data[1]

    results = []

    print("Testing \"{input1}\" with {input2} requests".format(input1=text, input2=numberOfRequests))

    for i in range(numberOfRequests):
        startTime = datetime.now()
        response = requests.post('http://ece444-lab7-v1-env.us-east-2.elasticbeanstalk.com/predict', json={'text': text})
        response = response.json()
        endTime = datetime.now()
        delta = (endTime - startTime).total_seconds() * 1000

        if (response['prediction'] == res):
            results.append(delta)
            # print(i, "Response time:", delta, "ms")
        # else:
            # print("unexpected failure")

    averageLatency = sum(results) / len(results)
    print("Number of requests successfully made:", len(results))
    print("Average latency:", averageLatency, "ms")
    print()
