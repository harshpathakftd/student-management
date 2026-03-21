import pandas as pd
from django.http import HttpResponse
from students.models import Student
from payments.models import Payment

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


# =========================
# 📊 EXCEL REPORT (CLEAN)
# =========================
def download_report(request):

    students = Student.objects.all()

    data = []
    for s in students:
        data.append({
            'Reg No': s.reg_no,
            'Name': s.name,
            'Email': s.email,
            'Mobile': s.mobile
        })

    df = pd.DataFrame(data)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=students_report.xlsx'

    df.to_excel(response, index=False)
    return response


# =========================
# 📄 PDF REPORT (STYLED)
# =========================
def download_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=payments_report.pdf'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("SoftApp Technologies", styles['Title']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("Payment Report", styles['Heading2']))
    elements.append(Spacer(1, 20))

    # Table Data
    data = [['Student', 'Course', 'Amount', 'Status']]

    payments = Payment.objects.select_related(
        'enrollment__student',
        'enrollment__course'
    )

    for p in payments:
        data.append([
            p.enrollment.student.name,
            p.enrollment.course.name,
            f"₹{p.amount}",
            "Paid" if p.paid else "Pending"
        ])

    # Table
    table = Table(data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),

        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)
    return response