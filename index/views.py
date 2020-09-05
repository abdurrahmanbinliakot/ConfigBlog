from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Subscribe, Post

# Create your views here.

def index(request):
    featured = Post.objects.order_by('-timestamp')[0:6]


    if request.method == "POST":
        email = request.POST["email"]
        new_subscribe = Subscribe()
        new_subscribe.email = email
        new_subscribe.save()

    
    context = {
        'object_list': featured,
    }
    return render(request,'index.html',context)

def post(request,id):
    post = get_object_or_404(Post,id=id)
    context = {
        'post':post,
        
    }
    return render(request,'blog-post.html',context)







# 

def blog(request):
 #   most_recent = Post.objects.order_by('-timestamp')[3:]
    post_list = Post.objects.all().order_by('-timestamp')[6:]
    paginator = Paginator(post_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'blog-list.html', context)
