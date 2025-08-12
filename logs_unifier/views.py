import json
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template, TemplateDoesNotExist


es = Elasticsearch("http://localhost:9200")

@csrf_exempt
def upload_files(request):
    print(">>> FUNZIONE upload_files ESEGUITA <<<")

    try:
        get_template('logs_unifier/upload.html')
    except TemplateDoesNotExist as e:
        return HttpResponse(f"Template not found: {e}. Looked in: {settings.TEMPLATES}")

    message = None  # per passare un feedback al template

    if request.method == "POST":
        files = request.FILES.getlist('files')
        unified_index = 'unified-index'
        total_uploaded = 0

        for f in files:
            index_name = request.POST.get(f'index_for_{f.name}') or 'default-index'
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                message = f"Errore nel parsing di {f.name}: {e}"
                return render(request, 'logs_unifier/upload.html', {'message': message})

            # Estraggo solo i documenti dai risultati Elasticsearch
            if "hits" in data and "hits" in data["hits"]:
                docs = [hit["_source"] for hit in data["hits"]["hits"]]
            else:
                docs = data if isinstance(data, list) else [data]

            for doc in docs:
                es.index(index=index_name, document=doc)
                es.index(index=unified_index, document=doc)
                total_uploaded += 1

        message = f"Upload completed: {total_uploaded} documents"

    return render(request, 'logs_unifier/upload.html', {'message': message})

