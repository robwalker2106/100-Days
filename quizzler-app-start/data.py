import requests

parameters = {
    "amount": 10,
    "type": 'boolean'
}

response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
response_questions = response.json()

question_data = response_questions['results']