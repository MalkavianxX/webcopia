from django import forms
inicial=1
ENTIDADES = (
    #grupoA
            (1, "Cuernavaca - CVJ"),
            (2, "Cd. México (Lago Tana) - FMX"),
            (3, "Cd. México (Hangares) - HMX"),
            (4, "Cd. México (Sor Juana) - JMX"),
            (5, "Cd. México"),
            (6, "Cd. México - Hangares - NLU"),
            (7, "Cd. México (Acoxpa) - OMX"),
            (8, "Puebla - PBC"),
            (9, "Cd. México (Reforma) - REF"),
            (10, "Cd. México (Mixcoac) - RMX"),
            (11, "Toluca - TLC"),
            #grupoB
            (12, "Aguascalientes - AGU"),
            (13, "Irapuato - BJX"),
            (14, "Celaya - CYY"),
            (15, "León - LEN"),
            (16, "Morelia - MLM"),
            (17, "Querétaro - QRO"),
            (18, "San Luis Potosí - SLP"),
            (19, "Zacatecas - ZCL"),
            (20, "Córdoba - DCB"),
            (21, "Jalapa - JAL"),
            (22, "Oaxaca - OAX"),
            (23, "Veracruz - VER"),
            #grupoc
            (24, "Acapulco - ACA"),
            (25, "Ciudad del Carmen - CME"),
            (26, "Guadalajara - GDL"),
            (27, "Minatitlán - MTT"),
            (28, "Monterrey - MTY"),
            (29, "Poza Rica - PAX"),
            (30, "Saltillo - SLW"),
            (31, "Tampico - TAM"),
            (32, "Tapachula - TAP"),
            (33, "Tuxtla Gutiérrez - TGZ"),
            (34, "Villahermosa - VSA"),
            (35, "Zihuatanejo - ZIH"),
            #grupoD
            (36, "Colima - CLQ"),
            (37, "Durango - DGG"),
            (38, "Matamoros - MAM"),
            (39, "Nuevo Laredo - NLD"),
            (40, "Puerto Vallarta - PVR"),
            (41, "Tepic - TNY"),
            (42, "Torreón - TRC"),
            (43, "Manzanillo - ZLO"),
            #grupo f
            (44, "Ciudad Juárez - CJS"),
            (45, "Cancún - CUN"),
            (46, "Chihuahua - CUU"),
            (47, "Mérida - MID"),
            (48, "Culiacán - CUL"),
            (49, "La Paz - LAP"),
            (50, "Los Mochis - LMM"),
            (51, "Mazatlán - MZT"),
            #grupoG
            (52, "Ciudad Obregón - CEN"),
            (53, "Hermosillo - HMO"),
            (54, "Mexicali - MXL"),
            (55, "Tijuana - TIJ"),

)




class FormularioEnvio(forms.Form):

    nombre = forms.CharField(label='Nombre', required=True,max_length=150,help_text="nombre")    
    apellidos=forms.CharField(label='Apellidos' ,required=True, max_length=200,help_text="apellido")
    telefono=forms.CharField(label='Celular',required=True, max_length=14,help_text="telefono")
    email = forms.CharField(label='E-mail', required=True,max_length=100,help_text="correo")    

    estado=forms.ChoiceField(choices=ENTIDADES,label='Estado',required=True,initial=1)



    municipio=forms.CharField(label='Municipio',required=True,max_length=100,help_text="municipio")
    colonia=forms.CharField(label='Colonia',required=True,max_length=100,help_text="colonia")
    codigo_postal=forms.CharField(label='Codigo Postal',required=True,max_length=10,help_text="codigo postal")
    calle=forms.CharField(label='Calle',required=True,max_length=100,help_text="calle")
    noexterior=forms.CharField(label='Numero exterior',required=True,max_length=100,help_text="numero exterior")
    nointerior=forms.CharField(label='Numero interior',required=False,max_length=100,help_text="numero interior (opcional)")
    referencias=forms.CharField(label='Referencias',required=True,max_length=100,widget=forms.Textarea(),help_text="referencia de tu domicilio")

    


