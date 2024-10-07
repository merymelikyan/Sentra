from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message



def receive_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')

        if name and email and subject and content:
            Message.objects.create(name=name, email=email, subject=subject, content=content)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


