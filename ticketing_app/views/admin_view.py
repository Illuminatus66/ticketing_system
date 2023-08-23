from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from ..models import UserSubmittedData, RespondedData

def is_superuser_or_admin(user):
    return user.is_superuser or user.is_staff

@login_required
@user_passes_test(is_superuser_or_admin)
def admin_view(request):
    all_data = UserSubmittedData.objects.all()

    if request.method == 'POST':
        if 'response' in request.POST:
            data_id = request.POST['data_id']
            response = request.POST['response']

            user_data = UserSubmittedData.objects.get(pk=data_id)
            RespondedData.objects.create(user_data=user_data, response=response)

            '''I am setting and resetting flags in the current scenario. I had to find fixes for this for 3 hours.
            Initially I was deleting the entry using user_data.delete() instead of these boolean flags. The problem
            was that I had to keep either on delete cascade on or I had to protect it, but neither would be beneficial.
            I suddenly thought of the soluntion while wondering how to sort tickets as resolved and unresolved. This means
            a query made from a user account initially has resolved marked as False and adminview marked as True.
            Here when data is pulled from UserSubmittedData model and pushed along with the response through
            RespondedData model, it fetches the flags and reverses it so that I can filter out resolved tickets with responses
            in the user_dashboard.html template. The exact reverse would be true for the admin_view.html where I would filter
            out tickets based on the fact that unresolved tickets will also have adminview set as True by default.'''
            user_data.resolved = True
            user_data.adminview = False
            user_data.save()

            return redirect('admin_view')

    return render(request, 'ticketing_app/admin_view.html', {'all_data': all_data})
