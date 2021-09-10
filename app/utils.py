from datetime import timedelta

from app.constants import *
from app.models import *

from django.db.models.functions import ExtractWeek
from django.db.models import Count

def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def get_profile_score(user):
    score = 0
    if user.current == CURRENT.MENTOR:
        items = 5
        inc = int(100/items)
        if user.mentor.about_you:
            score += inc
        if user.mentor.meeting_duration:
            score += inc
        if user.mentor.cost > 0:
            score += inc
        if user.timezone:
            score += inc
        if user.mentor.tags.all().count() > 2:
            score += inc
    else:
        items = 3
        inc = int(100/items)
        if user.mentor.about_you:
            score += inc
        if user.mentee.tags.all().count() > 2:
            score += inc
        if user.timezone:
            score += inc

    return score

def get_activity_chart(user):
    score = 0
    result = []
    if user.current == CURRENT.MENTOR:
        stats = Meeting.objects.filter(mentor = user.mentor) \
            .annotate(week=ExtractWeek('created')) \
            .values( 'week') \
            .annotate(total_count=Count('id')) \
            .order_by('week')[:5]
    else:
        stats = Meeting.objects.filter(mentee = user.mentee) \
            .annotate(week=ExtractWeek('created')) \
            .values( 'week') \
            .annotate(total_count=Count('id')) \
            .order_by('week')[:5]
    if stats:
        for s in stats:
            result.append({"x" : f"Week {s['week']}", "y": f"{s['total_count']}"})
            if int(s['total_count']) > 0:
                score +=20
    else:
        result = [
            {"x" : "Week 1", "y": 0},
            {"x" : "Week 2", "y": 0},
            {"x": "Week 3", "y": 0},
            {"x": "Week 4", "y": 0},
            {"x": "Week 5", "y": 0},

        ]

    return (result, score)
