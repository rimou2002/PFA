import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150
        )

        chatbot_message = response.choices[0].message['content'].strip()
        return JsonResponse({'message': chatbot_message})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def chat_view(request):
    return render(request, 'chatbot/chat.html')
