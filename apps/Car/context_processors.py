def total_car(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session['car'].items():
            total += value['price']
    return {'total_car': total}