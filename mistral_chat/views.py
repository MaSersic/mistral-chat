from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from mistral_chat.LLMs import llm

model = llm.LLM(n_ctx=16384, max_tokens=2000)


def chat(request):
    if request.method == 'POST':

        if 'file' in request.FILES:
            pdf = request.FILES('file')
            fs = FileSystemStorage()
            filename = fs.save(pdf.name, pdf)
            llm.load_file_from_pdf(pdf)

        prompt = request.POST.get('prompt')
        if prompt:
            print(prompt)
            response = model.ask(prompt)
            print(response)

        return JsonResponse({'response': response})
    return render(request, 'chat.html')


def upload_pdf(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']

    else:
        return render(request, 'chat.html')
