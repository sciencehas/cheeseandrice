```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    const uploadForm = document.getElementById('upload-form');
    const fileList = document.getElementById('file-list');
    const detailView = document.getElementById('detail-view');
    const editForm = document.getElementById('edit-form');

    uploadForm.addEventListener('submit', (event) => {
        event.preventDefault();
        // TODO: Add AJAX call to upload files and update fileList
    });

    fileList.addEventListener('click', (event) => {
        if (event.target.tagName === 'LI') {
            const fileId = event.target.dataset.fileId;
            // TODO: Add AJAX call to fetch file details and update detailView
        }
    });

    detailView.addEventListener('click', (event) => {
        if (event.target.tagName === 'P') {
            const paragraphId = event.target.dataset.paragraphId;
            // TODO: Add AJAX call to fetch paragraph in original context and highlight it
        }
    });

    editForm.addEventListener('submit', (event) => {
        event.preventDefault();
        // TODO: Add AJAX call to update file and update detailView
    });
});
```