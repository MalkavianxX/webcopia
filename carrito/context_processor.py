def monto_total(request):
    subtotal=0.0 
    if request.user.is_authenticated:
        for key ,value in request.session["carrito"].items():
            subtotal=subtotal+(float(value["precio"])*value["cantidad"])              
    return {'monto_total':subtotal}  