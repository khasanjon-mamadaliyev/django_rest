from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from apps.models import Poll


# Create your views here.

def polls_list(request):
    # MAX_OBJECTS =
    polls = Poll.objects.all()
    data = {
        "results": list(polls.values("question", "created_by__username", "pub_date"))
    }
    return JsonResponse(data)


def polls_details(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "results": {
            "question": poll.question,
            "created_by": poll.created_by.username,
            "pub_date": poll.pub_date,
        }
    }

    return JsonResponse(data)
