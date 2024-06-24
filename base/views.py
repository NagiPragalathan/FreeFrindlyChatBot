from django.http import HttpResponse
from django.shortcuts import render
from g4f.client import Client
import markdown
from django.http import JsonResponse

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


def apichatwithbot(request):
    # Get the user's query from the query parameters
    user_query = request.GET.get('user_query', '')

    if user_query:
        # Initialize the g4f client
        client = Client()

        # Create a chat completion with the user's query
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"system":"you are a use ful ai to give the answers about medical to user in english.","role": "user", "content": user_query}]
        )

        # Get the AI's response
        ai_response = chat_completion.choices[0].message.content or ""
        print(ai_response)
        # Create the JSON response with the AI's response
        response_data = {
            "ai_response": ai_response
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "No user query provided."}, status=400)