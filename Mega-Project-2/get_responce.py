import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


prompt = input("enter query")
# Define your assistant's personality here
personality = ("skips hi hello and give short reply"
        "You're a funny, witty AI assistant who always explains things in an easy and simple way, "
        "like a chill friend who’s a tech genius. Your replies are short, sharp, and packed with insight, "
        "but you're not afraid to add some humor and light roasting when needed. Keep things fun and helpful."
    )
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
    messages=[
            {"role": "system", "content": personality},
            {"role": "user", "content": prompt}
        ],
    max_tokens=100,
    temperature=0.8  # Slightly more creative
)

res = response['choices'][0]['message']['content'].strip()
print(res)