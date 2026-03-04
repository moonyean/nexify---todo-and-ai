from django.shortcuts import render
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional
from tasks.models import Task
from django.http import JsonResponse
from .models import AIInsight
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

# Create your views here.
# https://ai.google.dev/gemini-api/docs/structured-output?hl=ko&example=recipe

class Ingredient(BaseModel):
    title : str = Field(description="제목")
    content : str = Field(description="내용")
    type: str = Field(description="인사이트 종류 (Focus, Schedule, Warning 중 하나)")
# class Ingredient(BaseModel):
#     name: str = Field(description="Name of the ingredient.")
#     quantity: str = Field(description="Quantity of the ingredient, including units.")


def insights_view(request):
    if request.method == 'GET':
        # class TodosContent(BaseModel):
            # title: str = Field(description="The title of the TODO item.")
            # priority: str = Field(description="The priority level of the TODO item, such as 'High', 'Medium', or 'Low'.")
            # due_date: str = Field(description="The due date for the TODO item in ISO 8601 format (YYYY-MM-DD).")

        user_tasks = Task.objects.filter(user=request.user, is_done=False)
        task_list_text = "\n".join([f"- {t.title} (중요도: {t.priority}, 마감: {t.due_date})" for t in user_tasks])

        client = genai.Client(api_key = "GEMINI_API_KEY")

        prompt = """
        오늘의 TODO 리스트를 보고 주요 인사이트를 요약해줘. {task_list_text}
        """

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_json_schema": Ingredient.model_json_schema(),
            },
        )

        result = Ingredient.model_validate_json(response.text)
        new_insight = AIInsight.objects.create(
            user=request.user,
            title=result.title,
            content=result.content,
            type=result.type
        )

        return JsonResponse({
            "status": "success",
            "data": {
                "id": str(new_insight.id),
                "title": new_insight.title,
                "content": new_insight.content,
                "type": new_insight.type
            }
        })


def insights_list_view(request):
    """GET /insights - 현재 유저의 dismissed 되지 않은 인사이트 목록 반환"""
    if request.method != 'GET':
        return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

    insights = AIInsight.objects.filter(user=request.user, is_dismissed=False).order_by('-created_at')
    data = [{
        "id": str(i.id),
        "title": i.title,
        "content": i.content,
        "type": i.type,
        "created_at": i.created_at.isoformat(),
    } for i in insights]

    return JsonResponse({"status": "success", "data": data})

def delete_view(request, insight_id):
    if request.method == 'DELETE':
        try:
            insight = AIInsight.objects.get(id=insight_id, user=request.user)
            insight.is_dismissed = True
            insight.save()
            return JsonResponse({"status": "success", "message": "인사이트가 삭제되었습니다."})
        except AIInsight.DoesNotExist:
            return JsonResponse({"status": "error", "message": "인사이트를 찾을 수 없습니다."}, status=404)
        

@require_http_methods(["DELETE"])
def insight_dismiss_view(request, id):
    """DELETE /insights/{id} - 카드 우측 상단 [X] 클릭 시 목록에서 제외"""
    insight = get_object_or_404(AIInsight, id=id, user=request.user)
    insight.is_dismissed = True
    insight.save()

    return JsonResponse({
        "status": "success",
        "message": "카드가 목록에서 제외되었습니다.",
        "dismissed_id": str(insight.id)
    })