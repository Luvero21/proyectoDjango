from django import forms
from .models import Producto
from .models import Pedido, ItemPedido
from .models import Cliente, Usuario, UsuarioIngresado

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['productos', 'cliente']
        
class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['producto', 'cantidad', 'subtotal']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'email']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'nombre',
            'email',
            'edad',
            'password'
        ]

class UsuIngForm(forms.ModelForm):
    class Meta:
        model=UsuarioIngresado
        fields=[
            'usuario',
            'password'
            
]


