import os

from django.http import HttpResponse


def post_list(request):
    """
    / (Root URL)에 해당하는 view
    :param request:
    :return:
    """
    views_file_path = os.path.abspath(__file__)
    blog_application_path = os.path.dirname(views_file_path)
    app_dir = os.path.dirname(blog_application_path)
    template_path = os.path.join(app_dir, 'templates', 'blog', 'post_list.html')

    # with문 사용
    with open(template_path, 'rt') as f:
        content = f.read()

    # 파일객체 직접 사용 후 close
    f = open(template_path, 'rt')
    content = f.read()
    f.close()

    # 파일객체를 변수에 할당하지 않고 사용
    content = open(template_path, 'rt').read()

    return HttpResponse(content)
