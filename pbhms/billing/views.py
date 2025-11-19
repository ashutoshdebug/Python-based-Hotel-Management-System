from django.shortcuts import render
from .forms import billing_form
from guests.models import CheckOut

def billing(request):
    guest = None
    form = billing_form()

    # Handle GET search
    aadhaar_search = request.GET.get("aadhaar_search")
    if aadhaar_search:
        try:
            guest = CheckOut.objects.select_related("check_in").get(
                check_in__aadhaar_card=aadhaar_search
            )
        except CheckOut.DoesNotExist:
            guest = None

    # Handle POST billing submission
    if request.method == "POST":
        form = billing_form(request.POST)
        if form.is_valid():
            form.save()
        # else: form with errors is returned automatically

    return render(request, 'billing.html', {
        'form': form,
        'guest': guest,
    })
