from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import *

def blog_page(request):
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 1)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render(request,"blog_page.html", dict(posts=posts))