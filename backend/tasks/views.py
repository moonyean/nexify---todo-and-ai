from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from tasks.models import Task
import json


def tasks_view(request):
    """GET /tasks - 사용자의 모든 태스크 목록 조회 (due_date 기준 정렬)"""
    if request.method == 'GET':
        date_param = request.GET.get('date')
        tasks = Task.objects.filter(user=request.user).order_by('due_date')
        
        # 특정 날짜로 필터링할 경우
        if date_param:
            try:
                dt = parse_datetime(date_param)
                if dt:
                    tasks = tasks.filter(due_date__date=dt.date())
            except:
                pass
        
        data = [{
            'id': str(t.id),
            'title': t.title,
            'content': t.content,
            'priority': t.priority,
            'is_done': t.is_done,
            'due_date': t.due_date.isoformat() if t.due_date else None,
            'created_at': t.created_at.isoformat() if t.created_at else None,
        } for t in tasks]
        
        return JsonResponse({'status': 'success', 'data': data})
    
    return HttpResponseNotAllowed(['GET'])


def is_done_view(request, id):
    """PATCH /tasks/{id}/done - 태스크 완료 상태 토글"""
    if request.method != 'PATCH':
        return HttpResponseNotAllowed(['PATCH'])
    
    task = get_object_or_404(Task, id=id, user=request.user)
    task.is_done = not task.is_done
    task.save()
    
    return JsonResponse({
        'status': 'success',
        'data': {
            'id': str(task.id),
            'is_done': task.is_done,
        }
    })


def change_status_view(request, id):
    """PATCH /tasks/{id} - 태스크 정보 수정 (title, content, due_date)"""
    if request.method != 'PATCH':
        return HttpResponseNotAllowed(['PATCH'])
    
    task = get_object_or_404(Task, id=id, user=request.user)
    
    try:
        if request.content_type == 'application/json':
            payload = json.loads(request.body.decode('utf-8') or '{}')
        else:
            payload = request.POST.dict()
    except Exception:
        payload = {}
    
    # title 수정
    if title := payload.get('title'):
        task.title = title
    
    # content 수정
    if content := payload.get('content'):
        task.content = content
    
    # due_date 수정
    if date_str := payload.get('due_date'):
        if dt := parse_datetime(date_str):
            if timezone.is_naive(dt):
                dt = timezone.make_aware(dt, timezone.get_default_timezone())
            task.due_date = dt
    
    # priority 수정
    if priority := payload.get('priority'):
        task.priority = priority
    
    task.save()
    
    return JsonResponse({
        'status': 'success',
        'data': {
            'id': str(task.id),
            'title': task.title,
            'content': task.content,
            'priority': task.priority,
            'due_date': task.due_date.isoformat() if task.due_date else None,
        }
    })
