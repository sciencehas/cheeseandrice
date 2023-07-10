```python
from django.core.files import File
from app.models import Document

def update_document(document_id, new_content):
    document = Document.objects.get(id=document_id)
    document.content = new_content
    document.save()

def delete_paragraph(document_id, paragraph_id):
    document = Document.objects.get(id=document_id)
    paragraphs = document.content.split('\n')
    if paragraph_id < len(paragraphs):
        del paragraphs[paragraph_id]
        new_content = '\n'.join(paragraphs)
        update_document(document_id, new_content)

def update_paragraph(document_id, paragraph_id, new_paragraph):
    document = Document.objects.get(id=document_id)
    paragraphs = document.content.split('\n')
    if paragraph_id < len(paragraphs):
        paragraphs[paragraph_id] = new_paragraph
        new_content = '\n'.join(paragraphs)
        update_document(document_id, new_content)

def create_new_document(content, user):
    new_document = Document(content=content, user=user)
    new_document.save()
    return new_document.id
```