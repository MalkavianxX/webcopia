 
class Carrito:
    def __init__(self,request):
        self.request = request
        self.session= request.session
        self.carrito = {} 
        if self.session.get('carrito'): 
            self.carrito = self.session.get('carrito')
    def agregar(self, producto):    
        if(str(producto.id)not in self.carrito.keys()): 
            self.carrito[producto.id]={
                "producto_id":producto.id, 
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":self.request.GET.get("aumento_producto",1),
                "imagen":producto.imagen.url,
            }     
        else:     
            for key,value in self.carrito.items():
                if key==str(producto.id):
                    if int(self.request.GET.get("aumento_producto"))==1:
                        value["cantidad"]=value["cantidad"]+int(self.request.GET.get("aumento_producto",1))
                    else:    
                        value["cantidad"]=value["cantidad"]+int(self.request.GET.get("aumento_producto",1))
                        break    
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True

    def eliminar(self,producto):

        producto.id= str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carrito()       
 
    def restar_producto(self,producto):

        for key,value in self.carrito.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"]<1:
                    self.eliminar(producto)
                else:
                    self.guardar_carrito()
                break    
        self.guardar_carrito()   
        
    def limpiar_carrito(self):
        self.session["carrito"]={}   
        self.session.modified=True






            



           




 