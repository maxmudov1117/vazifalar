from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *

class HomeView(View):
    def get(self, request):
        statuses = Task.StatusChoices.choices
        tasks = Task.objects.order_by('-status', 'deadline')
        context = {
            'statuses':statuses,
            'tasks':tasks
        }
        return render(request,'index.html', context=context)

    def post(self, request):
        Task.objects.create(
            title=request.POST.get('title'),
            deadline=request.POST.get('deadline') if request.POST.get('deadline') else None,
            details=request.POST.get('details') ,
            status=request.POST.get('status')
        )
        return redirect('home')

class TaskEditView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)

        context = {
            'task':task,
        }

        return render(request,'edit.html', context=context)

    def post(self,request,pk):
        task = get_object_or_404(Task,id=pk)
        task.title = request.POST.get('title')
        task.details = request.POST.get('details')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline') if request.POST.get('deadline') else None
        task.save()
        return redirect('home')

class DeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        context = {
            'task':task,
        }
        return render(request,'delete.html', context = context)

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return redirect('home')



