from django.shortcuts import render, redirect
from django.http import HttpResponse
from io import BytesIO
import qrcode
import qrcode.main
import base64
from .forms import FileUploadForm
from .models import *
from django.urls import reverse


# Create your views here.

def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_upload = form.save()
            return redirect("file_details", file_upload.unique_id)
        else:
            return HttpResponse("Please upload a valid file.")
    else:
        form = FileUploadForm()
        return render(request, 'index.html', {'form' : form})
    

def file_details(request, file_id):
    try:
        file_upload = FileUpload.objects.get(unique_id = file_id)
    except Exception:
        return redirect('index')
    file_url = request.build_absolute_uri(reverse(viewname='download_file', args=[file_upload.unique_id]))

    # Generate QRCode
    qr = qrcode.main.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=20,
        border=4
    )
    qr.add_data(file_url)
    qr.make(fit=True)

    # Generate Image
    image = qr.make_image(fill='black', back_color='white')

    #Save QRCode to an in-memory file
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('UTF-8')


    context = {
        'file_url' : file_url,
        'qr_code' : qr_code_base64        
    }

    return render(request, 'file_details.html', context)


def download_file(request, unique_id):
    file_upload = FileUpload.objects.get(unique_id = unique_id)
    response = HttpResponse(file_upload.file, content_type='application/octet_stream')
    response['Content_Disposition'] = f'attachment; filename="{file_upload.file.name}"'
    file_upload.delete()
    return response






