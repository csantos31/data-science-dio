import pandas as pd
import requests
import openai

df = pd.read_csv('sdw-itens.csv')
user_ids = df['UserID'].tolist()
api_link = "https://sdw-2023-prd.up.railway.app"
openai_api_key = "key_will_be_here"
openai.api_key = openai_api_key


def get_user(id):
    response = requests.get(f'{api_link}/users/{id}')
    return response.json() if response.status_code == 200 else None


users = [user for id in user_ids if (user := get_user(id)) is not None]


def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a fullstack software engineer."
            },
            {
                "role": "user",
                "content": f"Create a message for {user['name']} motivating about her or his career (maximum of 100 characters)"
            }
        ]
    )
    return completion.choices[0].message.content.strip("\"")


for user in users:
    news = generate_ai_news(user)
    user["news"].append({
        "icon": "https://i.pinimg.com/564x/9c/4e/0e/9c4e0e848f139cc4219d7b5f35b6c861.jpg",
        "description": news
    })


def update_user(user):
    response = requests.put(f"{api_link}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


for user in users:
    success = update_user(user)
    print(
        f"User {user['name']} updated ! " if success else f"User was not updated")
