```python
from django.core.files.storage import FileSystemStorage
from app.models import Document

def create_new_document(user, text_content):
    # Create a new document instance
    new_document = Document()
    new_document.user = user
    new_document.content = text_content

    # Save the document instance
    new_document.save()

    # Save the document content to a file
    fs = FileSystemStorage()
    filename = fs.save(f'{new_document.id}.txt', ContentFile(text_content))

    # Update the document instance with the file path
    new_document.file = filename
    new_document.save()

    return new_document
```