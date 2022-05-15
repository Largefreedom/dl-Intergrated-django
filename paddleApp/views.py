from django.shortcuts import render
from django.views.decorators.http import  require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .tools import handle_upload_file
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
# Create your views here.




@csrf_exempt
@require_http_methods(["POST"])
def paddle_image_upload(request):
    file_info = request.FILES.get('file',None)
    result,detedPath,oriPath = handle_upload_file(file_info)

    print(result,detedPath,oriPath)
    return JsonResponse({
        'code': 0,
        'message': 'SUCCESS',
        'data': {
            'result': result,
            'detePath':detedPath,
            'oriPath':oriPath
        }
    })