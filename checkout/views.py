from re import template
from django.shortcuts import render
from paypalcheckoutsdk.orders.orders_capture_request import OrdersCaptureRequest
from stripe.api_resources import charge, source
from .forms import FormularioEnvio
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from django.conf import settings
from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalhttp import HttpError
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import Ventas_por_enviar
import mercadopago
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request): 
 
    formulario_envio = FormularioEnvio()
    return render(request, "checkout/checkout.html",{'formulario_envios':formulario_envio})  

def envio_email_confirmacion(dic):
    nombre=dic['nombre']
    context={
        'nombre':nombre,
    }    
    mail=dic['email']
    template=get_template('checkout/correo.html')
    content= template.render(context)    
    email=EmailMultiAlternatives(
        'Confirmacion de pago',
        'Joyapan',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def resumen(request):
    estado=int(request.GET.get("estado"))
    if estado>=1 and estado<=11:
        resultado=141.16
    elif estado>=12 and estado<=23:
        resultado=149.16
    elif estado>=24 and estado <=35:
        resultado=156.02
    elif estado>=36 and estado<=43:
        resultado=173.69
    elif estado>=44 and estado<=51:
        resultado=221.31
    elif estado >=52 and estado<=55:
        resultado=229.84
    else:
        resultado=173.69
    subtotal=0.0 
    productos_nombres=""
    cantidad_articulos=""
    if request.user.is_authenticated:
        for key ,value in request.session["carrito"].items():
            subtotal=subtotal+(float(value["precio"])*value["cantidad"])
            productos_nombres = productos_nombres+str(value["producto_id"])+","
            cantidad_articulos = cantidad_articulos+str(value["cantidad"])+","
    else:
        for key ,value in request.session["carrito"].items():
            subtotal=subtotal+(float(value["precio"])*value["cantidad"])
            productos_nombres = productos_nombres+str(value["producto_id"])+","
            cantidad_articulos = cantidad_articulos+str(value["cantidad"])+","
    sesion_id=request.session.session_key

    total=resultado+subtotal             
    if total>=950.00 and total<1900.00:
        descuento="5% de descuento!"
        sub=total*0.05
        total=total-sub
    elif total>=1900 and total<3762.00:
        sub=total*0.10
        total=total-sub    
        descuento="10% de descuento!"

    elif total>=3762.00 and total<7600.00:
        sub=total*0.15
        total=total-sub      
        descuento="15% de descuento!"

    elif total>=7600.00 and total<11400.00:
        sub=total*0.20
        total=total-sub
        descuento="20% de descuento!"

    elif total>=11400.00 and total<15200.00:
        sub=total*0.25
        total=total-sub
        descuento="25% de descuento!"

    elif total>=15200.00 and total<19000.00:
        sub=total*0.30
        total=total-sub     
        descuento="30% de descuento!"

    elif total>=19000.00:
        sub=total*0.40
        total=total-sub 
        descuento="40% de descuento!"

    else:
        total=total
        descuento="No aplica"
    total=round(total,2)    
    datos={ 
        'nombre':str( request.GET.get("nombre")), 
        'apellidos':str( request.GET.get("apellidos")), 
        'telefono':str( request.GET.get("telefono")), 
        'email':str( request.GET.get("email")), 
        'municipio':str( request.GET.get("municipio")), 
        'colonia':str( request.GET.get("colonia")), 
        'codigo_postal':str( request.GET.get("codigo_postal")), 
        'calle':str( request.GET.get("calle")), 
        'num_exterior':str( request.GET.get("noexterior")), 
        'num_interior':str( request.GET.get("nointerior")), 
        'referencias':str( request.GET.get("referencias")),
        'envio':str(resultado), 
        'total':str(total),
        'subtotal':str(subtotal),
        'descuento':str(descuento),
    }  
    registro=Ventas_por_enviar( 
        enviado=False,
        sesion = sesion_id,
        nombre=datos['nombre'], 
        apellidos = datos['apellidos'],
        telefono =datos['telefono'],
        email = datos['email'],
        municipio = datos['municipio'],
        colonia = datos['colonia'],
        codigo_postal= datos['codigo_postal'],
        calle= datos['calle'],
        num_exterior = datos['num_exterior'],
        num_interior = datos['num_interior'],
        referencias = datos['referencias'],
        envio = datos['envio'],
        total = datos['total'],
        productos=productos_nombres,
        cantidad = cantidad_articulos,
    )
    registro.save()
    return render(request,"checkout/resumen.html",{'dic':datos})  

def pago_cancelado(request):

    return render(request,"checkout/pago_cancelado.html")
def hecho(request):
    sesion_id=request.session.session_key
    registro=Ventas_por_enviar.objects.filter(sesion=sesion_id)
    posicion=(len(registro))
    total=float(registro[posicion-1].total)+0.5
    total=total*100
        
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=round(total),
            currency="mxn",
            description='Un cargo',
            source=request.POST['stripeToken'],
        )
        registro[posicion-1].autorizacion=str(source)+str("stripe")
        registro[posicion-1].verificacion=str(source)+str("stripe")
        diccionario={
            'nombre':registro[posicion-1].nombre,
            'email':registro[posicion-1].email,
        }
        registro[posicion-1].save()         
        envio_email_confirmacion(diccionario)

        return render(request,"checkout/pago_hecho.html")
    else:
        return render(request,"checkout/pago_cancelado.html")

#PAYPALBUTTON
def pago(request):
    # Creating Access Token for Sandbox
    client_id = "AWKxRtjpmHR9Jd8n8fMGO77lqcIw7fFHML19xSzd1Scfv4Mk-XGwnjBYJIkaRaFa_y2LC2PXBulTMPFK"
    client_secret = "EGlVhQYGDzop2HftvmEqh726ChUjz4e7x_Ai4Hp900iA8troRX5feiS6ThlfB-HSVwzKNdHW2W3BzCyf"
    # Creating an environment
    environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
    client = PayPalHttpClient(environment)
    # Construct a request object and set desired parameters
    # Here, OrdersCreateRequest() creates a POST request to /v2/checkout/orders
    requestPaypal = OrdersCreateRequest()
    sesion_id=request.session.session_key
    registro=Ventas_por_enviar.objects.filter(sesion=sesion_id)
    posicion=(len(registro))
    total=registro[posicion-1].total
    total_stripe=float(total)
    total_stripe=total_stripe*100
    requestPaypal.prefer('return=representation')
    requestPaypal.request_body (
        {
            "intent": "CAPTURE",
            "purchase_units": [
                { 
                    "amount": {
                        "currency_code": 'MXN',
                        "value": float(total),
                    }
                }
            ],
            "application_context":{
                "return_url":"http://127.0.0.1:8000/checkout/exitoso",
                "cancel_url":"http://127.0.0.1:8000/checkout/cancelado",
                "brand_name":"Joyapan"
            }
        }
    )
    try:
        # Call API with your client and get a response for your call
        response = client.execute(requestPaypal)
        if response.result.status == 'CREATED':
            approval_url = str(response.result.links[1].href)
            print(approval_url)


            return render(request, 'checkout/pago.html',{#aqui es donde esta el boton 
            'approval_url':approval_url,'STRIPE_PUBLISHABLE_KEY':settings.STRIPE_PUBLISHABLE_KEY,'total':total,'total_stripe':total_stripe,
            })
        
    except IOError as ioe:
        print (ioe)
        if isinstance(ioe, HttpError):
            # Something went wrong server-side
            return render(request,'checkout/pago_cancelado.html')    
#PAYPAL
def pago_exitoso(request):
    # Creating Access Token for Sandbox
    client_id = "AWKxRtjpmHR9Jd8n8fMGO77lqcIw7fFHML19xSzd1Scfv4Mk-XGwnjBYJIkaRaFa_y2LC2PXBulTMPFK"
    client_secret = "EGlVhQYGDzop2HftvmEqh726ChUjz4e7x_Ai4Hp900iA8troRX5feiS6ThlfB-HSVwzKNdHW2W3BzCyf"
    # Creating an environment
    environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
    client = PayPalHttpClient(environment)
    ordenId=request.GET.get('token')
    payerId=request.GET.get('PayerID')





    requestPaypal =OrdersCaptureRequest(ordenId)
    print("RequestPaypal")
    print(requestPaypal)
    requestPaypal.prefer('return=representation')    
    try:
        # Call API with your client and get a response for your call
        response = client.execute(requestPaypal)
            # If call returns body in response, you can get the deserialized version from the result attribute of the response
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
      
        order = response.result.id
        sesion_id=request.session.session_key
        registro=Ventas_por_enviar.objects.filter(sesion=sesion_id)
        posicion=(len(registro))
        registro[posicion-1].autorizacion=order
        registro[posicion-1].verificacion=payerId
        diccionario={
            'nombre':registro[posicion-1].nombre,
            'email':registro[posicion-1].email,
        }
        registro[posicion-1].save()         
        envio_email_confirmacion(diccionario)

    except IOError as ioe:
        if isinstance(ioe, HttpError):
            # Something went wrong server-side
            print("Algo salio mal :c")
            print (ioe.status_code)
            print (ioe.headers)
            print (ioe)
            return render(request,'checkout/pago_cancelado.html')    
        else:
            # Something went wrong client side
            print (ioe)
        return render(request,'checkout/pago_cancelado.html')    
    
    return render(request,'checkout/pago_exitoso.html')    

 
def mercado_pago(request):
    sdk = mercadopago.SDK("TEST-7464376773457318-041401-5b77309039187c1aa6183f465644f152-742154279") 
    preference_data = {
    "items": [
        {
            "title": "Prueba",
            "quantity": 1,
            "currency_id": "MXN",
            "unit_price": 100.00,
        }        
    ],
    "back_urls": [
        {
        "success": "http://127.0.0.1:8000/checkout/hecho",
        "failure": "http://127.0.0.1:8000/checkout/cancelado",
        "pending": "http://127.0.0.1:8000/checkout/cancelado",
        }

    ],
    "auto_return": "approved"    
}
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]