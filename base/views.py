from django.http import HttpResponse
from django.shortcuts import render
from g4f.client import Client
import markdown


def chatwithbot(request):
    if request.method == 'POST':
        # Get the user's query from the frontend
        user_query = request.POST.get('user_query', '')

        # Initialize the g4f client
        client = Client()

        # Create a chat completion with the user's query
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_query}]
        )

        # Get the AI's response
        ai_response = chat_completion.choices[0].message.content or ""

        # Pass the AI's response to the template
        context = {"ai_response": markdown.markdown(ai_response)}
        
        # Render the template with the AI's response
        return render(request, 'bot_template.html', context)
    else:
        return render(request, 'bot_template.html')
