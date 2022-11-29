# ECE444-F2022-Lab7

## Local testing

```powershell
python application.py
```

## Endpoint usage

Make a post request to http://ece444-lab7-v1-env.us-east-2.elasticbeanstalk.com/predict or http://127.0.0.1:5000/predict 
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
