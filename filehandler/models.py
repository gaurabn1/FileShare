from django.db import models
import uuid
# Create your models here.


class FileUpload(models.Model):
    file = models.FileField(upload_to='files')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return self.file.name