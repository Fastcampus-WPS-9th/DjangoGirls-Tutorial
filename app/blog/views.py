import os
import random

from django.http import HttpResponse
from django.template import loader


def post_list(request):
    # 템플릿을 가져옴 (단순 문자열이 아님)
    template = loader.get_template('blog/post_list.html')
    # 해당 템플릿을 렌더링
    context = {
        'pokemon': random.choice(['피카츄', '파이리', '꼬부기']),
    }
    content = template.render(context, request)
    return HttpResponse(content)
