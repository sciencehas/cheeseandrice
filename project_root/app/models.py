```python
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    processed = models.BooleanField(default=False)
    similarity_index = models.FloatField(default=0.0)
    content = models.TextField(blank=True)

class Content(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    text = models.TextField()
    similarity_index = models.FloatField(default=0.0)
    duplicate_count = models.IntegerField(default=0)
    duplicate_docs = models.TextField(blank=True)

class Error(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    error_text = models.TextField()

class NewDocument(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    new_text = models.TextField()
```