from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            statuses = Task.StatusChoices.choices
            tasks = Task.objects.filter(user=request.user).order_by('-status', 'deadline')
            context = {
                'statuses':statuses,
                'tasks':tasks
            }
            return render(request,'index.html', context=context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Task.objects.create(
                title=request.POST.get('title'),
                deadline=request.POST.get('deadline') if request.POST.get('deadline') else None,
                details=request.POST.get('details') ,
                status=request.POST.get('status'),
                user=request.user,
            )
            return redirect('home')
        return redirect('login')

class TaskEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, id=pk, user=request.user)

            context = {
                'task':task,
            }

            return render(request,'edit.html', context=context)
        return redirect('login')

    def post(self,request,pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task,id=pk, user=request.user)
            task.title = request.POST.get('title')
            task.details = request.POST.get('details')
            task.status = request.POST.get('status')
            task.deadline = request.POST.get('deadline') if request.POST.get('deadline') else None
            task.save()
            return redirect('home')
        return redirect('login')

class DeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, id=pk, user=request.user)
            context = {
                'task':task,
            }
            return render(request,'delete.html', context = context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, id=pk, user=request.user)
            task.delete()
            return redirect('home')
        return redirect('login')


