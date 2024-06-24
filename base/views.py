from django.http import HttpResponse
from django.shortcuts import render
from g4f.client import Client
import markdown
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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


@csrf_exempt  # To bypass CSRF protection for this example, you might want to handle CSRF tokens properly in production
def apichatwithbot(request):
    if request.method == 'POST':
        try:
            # Get the JSON body from the request
            request_data = json.loads(request.body.decode('utf-8'))
            user_query = request_data.get('user_query', '')
            language = request_data.get('language', 'english')
            print(user_query, language)

            if not user_query:
                return JsonResponse({"error": "No user query provided."}, status=400)

            # Initialize the g4f client
            client = Client()
            system = f"""
                1. you are a useful AI to give the answers about medical to the user in language of {language} 
                2. whatever language the input can be but you should response in {language}. 
                3. Note: Dont Give readme just give plain text.
                4. the response should be in {language}
            """
            user = f""" 
            Note:
            1. answer should be in {language}.
            2. Dont give any of the other ack or any unwanted text.
            3. just give the answer of query.
            4. Note: Dont Give readme just give plain text.
            
            Question:
            {user_query}.
            """
            print(system)

            # Create a chat completion with the user's query
            chat_completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"system": system, "role": "user", "content": user}
                ]
            )

            # Get the AI's response
            ai_response = chat_completion.choices[0].message.content or ""
            print(ai_response)
            # Create the JSON response with the AI's response
            response_data = {
                "ai_response": ai_response
            }
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
    
def render_chat(request):
    return render(request, "talking_Head.html")