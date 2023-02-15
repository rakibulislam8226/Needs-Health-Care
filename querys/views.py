from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .forms import SearchForm, AnswerForm, PostForm
from . import models
from . import serializers
from django.http import Http404
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.db.models import Q 

# Create your views here.
def post_list_view(request):
    dataset = models.Post.objects.all()
    querysetlen = models.Post.objects.filter().count()
    answersetlen = models.AnswerPost.objects.filter().count()
    pending_answer = querysetlen - answersetlen
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post = models.Post.objects.get(post_title=title)
            return redirect(f'/post/{post.id}')
    else:
        form = SearchForm()

    context = {
        'dataset':dataset,
        'form':form,
        "querysetlen":querysetlen,
        "answersetlen":answersetlen,
        "pending_answer":pending_answer,
    }
    return render(request,'querys/listview.html',context)
 

def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Query create successfully.')
        return redirect("posts")
    return render(request,'querys/post.html',{'form':form})

 
def post_details_view(request,_id):
    try:
        data = models.Post.objects.get(id =_id)
        answers = models.AnswerPost.objects.filter(post = data)
    except models.Post.DoesNotExist:
        raise Http404('Data does not exist')
     
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answers = models.AnswerPost(name= request.user.username,
            answer_text=form.cleaned_data['answer_text'],
            post=data)
            answers.save()
            return redirect(f'../post/{_id}')
    else:
        form = AnswerForm()
 
    context = {
            'data':data,
            'form':form,
            'answers':answers,
            'number_of_answer': len(answers)
        }
    return render(request,'querys/detailview.html',context)


class SearchResultView(ListView):
    model = models.Post
    template_name = 'querys/search_results.html'
    
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = models.Post.objects.filter(
            Q(post_title__icontains=query) | Q(descriptions__icontains=query)
        )
        return object_list


# # rest api start #
# class QueryList(generics.ListCreateAPIView):
#   queryset = models.Query.objects.all()
#   serializer_class = serializers.QuerySerializer
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#   def perform_create(self, serializer):
#     serializer.save(creator=self.request.user)

# class QueryDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = models.Query.objects.all()
#   serializer_class = serializers.QuerySerializer
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]



# class AnswerList(generics.ListCreateAPIView):
#   queryset = models.Answer.objects.all()
#   serializer_class = serializers.AnswerSerializer
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#   def perform_create(self, serializer):
#     serializer.save(creator=self.request.user)

# class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = models.Answer.objects.all()
#   serializer_class = serializers.AnswerSerializer
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

# end rest api #