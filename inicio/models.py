from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='static/assets', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
# Modelo para representar los pedidos
class Pedido(models.Model):
    productos = models.ManyToManyField(Producto, through='ItemPedido')
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)

# Modelo para representar los elementos individuales de un pedido
class ItemPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)

# Modelo para representar información del cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=50)

    # Campos numéricos
    edad = models.PositiveIntegerField()

class UsuarioIngresado(models.Model):
    usuario=models.CharField(max_length=30)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.usuario
    
    


