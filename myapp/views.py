# app_name/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Video

@csrf_exempt
def upload_video_chunk(request):
    if request.method == 'POST':
        video_chunk = request.FILES.get('video_chunk')
        if video_chunk:
            # Save the video chunk to disk
            with open('media/videos/models.mp4', 'wb+') as destination:
                for chunk in video_chunk.chunks():
                    destination.write(chunk)
            return JsonResponse({'status': 'success'})

@csrf_exempt
def render_video_page(request):
    return render(request, 'playvideo.html')
