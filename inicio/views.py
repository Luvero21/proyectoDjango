from django.shortcuts import render, get_object_or_404, redirect

from inicio.models import Producto, Pedido, Cliente, UsuarioIngresado

from inicio.forms import ProductoForm, PedidoForm, ClienteForm, UsuarioForm,UsuIngForm

from inicio.formulaire import formulaireProducto


def inicio(request):
    #version1
    #template=loader.get_template('inicio.html')
    #template_renderizado= template.render({})

    #return HttpResponse(template_renderizado)
    #version2
    return render(request,'inicio.html',{})

def lista_productos(request):
    nombre_a_buscar=request.GET.get('nombre')
    if nombre_a_buscar:
        productos = Producto.objects.filter(nombre=nombre_a_buscar)
    else:
        productos = Producto.objects.all()
    
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def lista_pedidos(request,):
   pedidos = Pedido.objects.all()
   return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'detalle_pedido.html', {'pedido': pedido})


def lista_clientes(request):
    cliente_a_buscar = request.GET.get('nombre')
    if cliente_a_buscar:
        clientes= Cliente.objects.filter(nombre=cliente_a_buscar)
    else:
        clientes=Cliente.objects.all()
        
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

def agregarcliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'agregar_cliente.html', {'form': form})

    
def confirmacion_registro(request):
    if request.method == 'POST':
        # Aquí se procesa el formulario y se guarda en la base de datos
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la página de confirmación
            return redirect('confirmacion_registro')
    else:
        # Si no se ha enviado el formulario, muestra la página de confirmación
        form = ClienteForm()

    # Recupera los últimos clientes registrados
    ultimos_clientes = Cliente.objects.order_by('-id')[:1]

    return render(request, 'confirmacion_registro.html', {'ultimos_clientes': ultimos_clientes, 'form': form})

def formulario_cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion_registro')
    form= ClienteForm()

    
    return render(request, 'formulario_cliente.html',{'form':form})

    
def formulario(request):
    mensaje=''
    context={}
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje='¡Gracias por registrarse!'
           

    context['form'] = UsuarioForm()
    context['mensaje']=mensaje
    
    return render(request, 'formulario.html', context)


def ingresarUsuario(request):
    if request.method == 'POST':
        form= UsuIngForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form=UsuIngForm()
    return render(request, 'ingresar_usuario.html', {'form':form} )

def crearProducto(request):
    if request.method =='POST':
        formulaire=formulaireProducto(request.POST)
        if formulaire.is_valid():
            info_clean= formulaire.cleaned_data
            
            nombre= info_clean.get('nombre')
            descripcion= info_clean.get('descripcion')
            precio= info_clean.get('precio')
            imagen=info_clean.get('imagen')
            
            producto=Producto(nombre=nombre,descripcion=descripcion,precio=precio,imagen=imagen)
            producto.save()
            
            return redirect('lista_productos')
        else:
            return render(request,'crear_producto.html',{'':formulaire})
            
    formulaire=formulaireProducto()
    return render(request,'crear_producto.html',{'formulaire':formulaire})

    
    
            

    








