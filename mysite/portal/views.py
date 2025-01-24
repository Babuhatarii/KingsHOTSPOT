from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Plan, Payment, Session
from django.utils.timezone import now
import requests
import random
import logging

logger = logging.getLogger(__name__)

def home(request):
    plans = Plan.objects.all()
    return render(request, 'portal/home.html', {'plans': plans})

@csrf_exempt
def process_payment(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        plan_id = request.POST.get("plan_id")

        if not phone_number or not plan_id:
            return render(request, 'portal/error.html', {"message": "Invalid input. Please try again."})

        try:
            plan = Plan.objects.get(id=plan_id)
        except Plan.DoesNotExist:
            return render(request, "portal/error.html", {"message": "Selected plan does not exist."})

        response = initiate_mpesa_payment(phone_number, plan.price)

        if response and response.get("success"):
            return render(request, 'portal/success.html', {"message": "Payment successful!", "plan": plan})
        else:
            return render(request, 'portal/error.html', {"message": response.get("error", "Payment failed. Please try again.")})

    return redirect("home")  # Adjust the URL name to match your URLs

def initiate_mpesa_payment(phone_number, amount):
    """
    Mock function to simulate M-Pesa payment response.
    """
    success = random.choice([True, False])  # Randomly simulate success or failure
    return {"success": success, "error": None if success else "Simulated failure"}

def access_granted(request):
    return render(request, 'portal/access_granted.html')
