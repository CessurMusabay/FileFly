from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TransferForm, Transfer
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import check_password
from django.conf import settings
import os


@csrf_exempt
def upload(request):
    form = TransferForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=True)
        return JsonResponse({'success': True, 'id': obj.id})
    return JsonResponse(form.errors, status=400)


def get_transfer(request, id):
    try:
        instance = Transfer.objects.get(id=id)
        return JsonResponse({
            'title': instance.title,
            'message': instance.message,
            'file': os.path.basename(instance.file.name)
        })
    except:
        return JsonResponse({}, status=401)


@csrf_exempt
def download(request, id):
    try:
        password = request.POST['password']
        instance = Transfer.objects.get(id=id)

        if check_password(password=password, encoded=instance.password):
            file_path = os.path.join(settings.MEDIA_ROOT, str(instance.file))
            with open(file_path, 'rb') as f:
                filename = os.path.basename(instance.file.name)
                response = HttpResponse(f.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
        return JsonResponse({}, status=401)
    except:
        return JsonResponse({}, status=401)
