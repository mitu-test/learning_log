from django.shortcuts import render
from learning_logs.models import Topic
from learning_logs.models import Entry
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """学习笔记主页"""
    return render(request,'index.html')
@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    return render(request,'topics.html',{'topics':topics})
@login_required
def topic(request,topic_id):
    """显示单个主题及所有条目"""
    topic = Topic.objects.get(id=topic_id)
    #确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
    entries =topic.entry_set.all()
    return render(request,'topic.html',{'topic':topic,'entries':entries})
@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据：创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect('/learning_logs/topics/')
    return render(request,'new_topic.html',{'form':form})
@login_required
def new_entry(request,topic_id):
    """在特定主题下添加"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        #为提交数据，创建一个新表单
        form = EntryForm()
    else:
        #POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
    return render(request,'new_entry.html',{'topic':topic,'form':form})
@login_required
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        #POST请求提交的数据，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
    return render(request,'edit_entry.html',{'entry':entry,'topic':topic,'form':form})



