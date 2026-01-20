from django.db import models


class FileUpload(models.Model):
    file = models.FileField(upload_to="fileupload")
    date = models.DateTimeField(auto_now_add=True)