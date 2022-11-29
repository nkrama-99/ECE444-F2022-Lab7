# ECE444-F2022-Lab7

Name: Ramakrishna Natarajan

I followed the official documentation to deploy the app to AWS:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

## To test locally

```powershell
python application.py
```

## Endpoint usage

Use any API tester (such as Postman) to make a post request to http://ece444-lab7-v1-env.us-east-2.elasticbeanstalk.com/predict or http://127.0.0.1:5000/predict 
```json
{
    "text": "The ocean is big"
}
```

## Expected Result

if real news:
```json
{
    "prediction": "REAL"
}
```

if fake news:
```json
{
    "prediction": "FAKE"
}
```
