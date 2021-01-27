# fileuploader
Web app on the python

App has upload and download page, when you can upload and download files

## Run app
#pip install flask<br>
#FLASK_APP=main.py FLASK_DEBUG=1 flask run


### Download page has static links, you can change it for youself.
```python
@app.route('/test.txt')
def download_file():
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename='test.txt', as_attachment=True) 
                               
```
