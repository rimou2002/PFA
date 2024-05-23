import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    print("Error: OpenAI API key not found in environment variables.")
    exit()

# Set the API key
openai.api_key = openai_api_key

try:
    # Create a completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, how are you?"}
        ],
        max_tokens=50
    )

    # Print the chatbot response
    chatbot_message = response.choices[0].message['content'].strip()
    print("Chatbot response:", chatbot_message)

except openai.error.RateLimitError:
    print("Error: You have exceeded your quota. Please try again later.")

except openai.error.AuthenticationError:
    print("Error: Authentication Error. Please check your API key.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
