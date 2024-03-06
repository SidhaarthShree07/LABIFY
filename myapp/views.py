from django.shortcuts import render
from django.http import HttpResponse
from Labify.forms import PostForming
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse
from myapp.models import Post,Posting
from django.contrib.auth.decorators import user_passes_test

def Home(request):
    return render(request,"home.html")

def home2(request):
    return render(request,"home2.html")

def Lab(request):
    posts = Post.objects.all()
    return render(request,"Lab.html",{'posts': posts})

def Contact(request):
    return render(request, "Contact.html")

def About(request):
    return render(request, "about.html")

def Vlab(request, pk):
    post = get_object_or_404(Post, pk=pk)
    feedbacks = Posting.objects.filter(post=post)

    if request.method == 'POST':
        form = PostForming(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            text = form.cleaned_data['text']
            posting = Posting.objects.create(user=user, text=text, post=post)
            posting.save()
            return JsonResponse({'user': user, 'text': text})  # Return JSON response
    else:
        form = PostForming(initial={'post': pk})  # Set initial value for the post field

    return render(request, 'Vlab.html', {'post': post, 'form': form, 'feedbacks': feedbacks})

@user_passes_test(lambda u: u.is_superuser)
def delete(request, pk):
    Posting.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/Lab')
