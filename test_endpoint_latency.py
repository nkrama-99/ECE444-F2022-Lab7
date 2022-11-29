import requests
from random import shuffle
from datetime import datetime

numberOfRequests = 100

testData = [
    ['The ocean is big', 0],
    ['Biden is president', 0],
    ['The earth is flat', 1],
    ['The ocean is red', 1]
]

shuffle(testData)

for data in testData:
    text = data[0]
    res = data[1]

    results = []

    print("Testing \"{input1}\" ({input2} news) with {input3} requests".format(input1=text, input2=res, input3=numberOfRequests))

    for i in range(numberOfRequests):
        startTime = datetime.now()
        response = requests.post('http://ece444-lab7-v1-env.us-east-2.elasticbeanstalk.com/predict', json={'text': text})
        response = response.json()
        endTime = datetime.now()
        delta = (endTime - startTime).total_seconds() * 1000

        if (response['isFake'] == res):
            results.append(delta)
        #     print(i, "Response time:", delta, "ms")
        # else:
        #     print("unexpected failure")

    averageLatency = sum(results) / len(results)
    print("Number of requests successfully made:", len(results))
    print("Average latency:", averageLatency, "ms")
    print()