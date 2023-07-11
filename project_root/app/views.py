from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Document
from .utils import transformers, clean_data, rank_sort, word_to_vector, merge_data, identify_related, calculate_similarity, similarity_analysis, update_documents, create_new_document

def index(request):
    return render(request, 'app/index.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            return redirect('list')
    else:
        form = UploadFileForm()
    return render(request, 'app/upload.html', {'form': form})

def list(request):
    documents = Document.objects.all()
    return render(request, 'app/list.html', {'documents': documents})

def detail(request, doc_id):
    document = Document.objects.get(id=doc_id)
    return render(request, 'app/detail.html', {'document': document})

def edit(request, doc_id):
    document = Document.objects.get(id=doc_id)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = UploadFileForm(instance=document)
    return render(request, 'app/edit.html', {'form': form})

def process_documents(request):
    documents = Document.objects.all()
    for document in documents:
        text = transformers.ingest(document.docfile)
        cleaned_text = clean_data.clean(text)
        ranked_text = rank_sort.rank(cleaned_text)
        vector = word_to_vector.create(ranked_text)
        matrix = merge_data.merge(vector)
        related_text = identify_related.identify(matrix)
        similarity = calculate_similarity.calculate(related_text)
        analysis = similarity_analysis.analyze(similarity)
        update_documents.update(document, analysis)
    return redirect('list')

def create_new(request):
    documents = Document.objects.all()
    for document in documents:
        new_text = create_new_document.create(document)
        new_document = Document(docfile=new_text)
        new_document.save()
    return redirect('list')
