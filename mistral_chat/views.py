from django.http import JsonResponse
from django.shortcuts import render

from mistral_chat.LLMs import llm

model = llm.LLM(n_ctx=16384, max_tokens=2000)


def chat(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        print(prompt)
        response = model.ask(prompt)
        print(response)
        return JsonResponse({'response': response})
    return render(request, 'chat.html')
