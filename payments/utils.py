from datetime import date
from twilio.rest import Client
from django.conf import settings
from .models import Payment


# =========================
# 🔐 TWILIO CONFIG (SAFE)
# =========================
client = Client(settings.TWILIO_SID, settings.TWILIO_TOKEN)


# =========================
# 📱 SEND WHATSAPP
# =========================
def send_whatsapp(number, message):
    try:
        # Ensure number format
        if not number.startswith('+91'):
            number = f'+91{number}'

        client.messages.create(
            body=message,
            from_='whatsapp:+14155238886',
            to=f'whatsapp:{number}'
        )

    except Exception as e:
        print("WhatsApp Error:", e)


# =========================
# ⏰ EMI REMINDER LOGIC
# =========================
def emi_reminder():
    today = date.today()

    payments = Payment.objects.filter(paid=False)

    for p in payments:
        days_left = (p.due_date - today).days

        if days_left in [5, 3, 1]:

            message = (
                f"Hi {p.enrollment.student.name},\n"
                f"Your EMI of ₹{p.amount} for {p.enrollment.course.name} "
                f"is due in {days_left} days.\n"
                f"- Student Management"
            )

            send_whatsapp(
                p.enrollment.student.mobile,
                message
            )