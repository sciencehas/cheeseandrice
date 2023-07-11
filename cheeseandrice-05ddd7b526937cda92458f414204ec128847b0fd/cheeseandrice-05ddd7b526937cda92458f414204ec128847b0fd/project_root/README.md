# Document Similarity App

This is a Django-based web application that allows users to upload Word or PDF documents and find similarities between them. The application uses the transformers pretrained model stsb-mpnet-base-v2 to process the documents and present the results in an interactive list.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project root directory.
3. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Django server:

```bash
python manage.py runserver
```

2. Open a web browser and navigate to the server's address (default is http://127.0.0.1:8000/).
3. Use the upload form to upload your documents. The total size of all documents should not exceed 1GB.
4. After the upload is complete, the application will process the documents and present the results in an interactive list. The list will show the content of the documents, categorized by similarity.
5. You can select any item in the list to view it in its original context in the uploaded documents. The selected item will be highlighted in the documents.
6. You can delete or change items in the list. The changes will be reflected in the uploaded documents.
7. You can create new documents from the remaining text in the list.

## Note

The application uses several utility functions to process the documents. These functions are located in the utils directory. The application also uses Django's built-in models, views, and forms, which are defined in the models.py, views.py, and forms.py files, respectively. The URLs for the application are defined in the urls.py file. The HTML structure of the application is defined in the templates directory, and the styling and interactivity are defined in the static directory.

The application uses the transformers pretrained model stsb-mpnet-base-v2 to process the documents. The model is defined in the transformers.py file in the utils directory. The application also uses several other Python packages, which are listed in the requirements.txt file.