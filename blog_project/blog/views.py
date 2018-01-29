from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView
                                  ,DetailView,CreateView,
                                  UpdateView,DeleteView)
from blog.models import post,comments
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import postform,commentform
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

class aboutview(TemplateView):
    template_name='about.html'


class postlistview(ListView):
    model= post


    def get_queryset(self):
        return post.objects.filter(published_date__lte= timezone.now()).order_by('-published_date')

class postdetailview(DetailView):
    model=post


class createpostview(LoginRequiredMixin,CreateView):

    login_url='/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = postform
    model= post

class updatepostview(LoginRequiredMixin,UpdateView):
    model=post
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class = postform


class postdeleteview(LoginRequiredMixin,DeleteView):
    model=post
    success_url = reverse_lazy('blog:post_list')


class draftlistview(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name = 'blog/post_list.html'
    model=post

    def get_queryset(self):
        return post.objects.filter(published_date__isnull=True).order_by('create_time')


#####################################
#####################################comment section



@login_required
def post_publish(request,pk):
    Post=get_object_or_404(post,pk=pk)
    Post.publish()
    return redirect('blog:detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    Post=get_object_or_404(post,pk=pk)# if the post exists then return the post or return 404 error

    if request.method =='POST':
        form=commentform(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=Post# the post which we made eright now should be equal to post object in models
            comment.save()
            return redirect('blog:detail',pk=Post.pk)
    else:
        form=commentform()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(comments,pk=pk)
    comment.approve()
    return redirect('blog:detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(comments,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('blog:detail',pk=post_pk)

















