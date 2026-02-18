from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from tasks.models import Task


def tasks_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    context = {
        'todos': tasks,
    }
    return render(request, 'tasks/tasks.html', context)

def is_done_view(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id, user=request.user)
        task.is_done = not task.is_done
        task.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'tasks/is_done.html', {'id': id})


def change_status_view(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        if title := request.POST.get('title'):
            task.title = title
        if content := request.POST.get('content'):
            task.content = content
        if date_str := request.POST.get('date') or request.GET.get('date'):
            if dt := parse_datetime(date_str):
                if timezone.is_naive(dt):
                    dt = timezone.make_aware(dt, timezone.get_default_timezone())
                task.due_date = dt
        task.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'tasks/change_status.html', {'task': task})
