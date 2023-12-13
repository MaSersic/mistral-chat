from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadPDFForm

from mistral_chat.LLMs import llm

model = llm.LLM(n_ctx=16384, max_tokens=2000)


def chat(request):
    if request.method == "POST":
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            model.load_file_from_pdf(request.FILES["file"])
            response = model.ask(request.POST.get('prompt'))
            return JsonResponse({'response': response})
        form.prompt = ""
    else:
        form = UploadPDFForm()
    return render(request, "chat.html", {"form": form})


def ochat(request):
    if request.method == 'POST':

        if 'pdf_file' in request.FILES:
            pdf = request.FILES('pdf_file')
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
