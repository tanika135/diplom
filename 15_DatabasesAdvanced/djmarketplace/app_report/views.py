from django.shortcuts import render

from app_report.forms import ReportCreateForm
from app_shop.models import Product
from orders.models import Order, OrderItem


def report_view(request):
    report = ''
    if request.method == 'POST':
        form = ReportCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            date_from = cd.get('date_report_from')
            date_to = cd.get('date_report_to')
            report = build_report(date_from, date_to)
            return render(request, 'reports/bestsellers.html',
                          {'report': report, 'form': form})

    else:
        form = ReportCreateForm()
    return render(request, 'reports/bestsellers.html',
                  {'report': report, 'form': form})


def build_report(date_from, date_to):
    report = {}
    # orders = Order.objects.filter(created__range=[date_from, date_to])
    items = OrderItem.objects.filter(order__created__range=[date_from, date_to])
    for item in items.values():

        if item['product_id'] not in report:
            report[item['product_id']] = {
                'id': item['product_id'],
                'quantity': item['quantity']
            }
        else:
            report[item['product_id']]['quantity'] += item['quantity']

    product_ids = report.keys()
    products = Product.objects.filter(id__in=product_ids)
    for product in products:
        report[product.id]['name'] = product.name

    return report

