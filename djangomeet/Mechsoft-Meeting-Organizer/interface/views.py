from django.shortcuts import render
from datetime import datetime
from .models import Meeting

# Create your views here.
def current_meeting(request):
    current_time = datetime.now()

    meeting_list = list(Meeting.objects.all())

    if request.method == 'POST':
        Meeting.objects.get(meeting_name = request.POST['delete']).delete()
    # we see first meeting at the calender if we have 3 meeting at week that have been.

    if meeting_list == None:
        return render(request, 'nomeetings.html')
    else:
        return render(request, 'linktoclick.html', {'obj': meeting_list})

def add_meeting(request):
    
    if request.method == 'POST':

        Meeting(meeting_name= request.POST['meeting_name'],
                meeting_link= request.POST['meeting_link'],
                start_time = request.POST['start_time'],
                end_time = request.POST['end_time'],
                meeting_day = request.POST['meeting_day'],
                participants = request.POST['participants']).save()

        return render(request, 'add_meeting.html')

    return render(request, 'add_meeting.html')

def update_meeting(request):

    meeting_list = list(Meeting.objects.all())

    if request.method == 'POST':
        try:
            obj = Meeting.objects.get(meeting_name = request.POST['meeting_name'])
            obj.meeting_name = request.POST['meeting_name']
            obj.meeting_link = request.POST['meeting_link']
            obj.start_time = request.POST['start_time']
            obj.end_time = request.POST['end_time']
            obj.meeting_day = request.POST['meeting_day']
            obj.participants = request.POST['participants']
            obj.save()
        except Meeting.DoesNotExist:
            Meeting(meeting_name=request.POST['meeting_name'],
                    meeting_link=request.POST['meeting_link'],
                    start_time=request.POST['start_time'],
                    end_time=request.POST['end_time'],
                    meeting_day=request.POST['meeting_day'],
                    participants=request.POST['participants']).save()

            return render(request, 'update_meeting.html', {'meetings': meeting_list})

    return render(request, 'update_meeting.html', {'meetings': meeting_list})
    

