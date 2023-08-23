from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import UserSubmittedData, RespondedData
import random

@login_required
def user_dashboard(request):
    submitted_tickets = UserSubmittedData.objects.filter(user=request.user)
    resolved_tickets = RespondedData.objects.filter(user_data__user=request.user)

    if request.method == 'POST':
        subject = request.POST['subject']
        description = request.POST['description']
        phone_number = request.POST['phone_number']
        ticket_number = random.randint(100, 99999)
        UserSubmittedData.objects.create(
            user=request.user, 
            subject=subject,
            description=description,
            phone_number=phone_number,
            ticket_number=ticket_number
        )

    return render(request, 'ticketing_app/user_dashboard.html', {
        'submitted_tickets': submitted_tickets,
        'resolved_tickets': resolved_tickets
    })
