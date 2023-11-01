from django.urls import path
from inicio.views import ingresarUsuario, agregarcliente, crearProducto, inicio,formulario, detalle_cliente, confirmacion_registro, lista_productos, lista_pedidos,lista_clientes,detalle_pedido,detalle_producto,formulario_cliente


urlpatterns =[
    path('', inicio, name='inicio'),
    path('agregarcliente',agregarcliente, name='agregar_cliente'),
    path('detallecliente/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('listaproductos/', lista_productos, name='lista_productos'),
    path('listapedidos/', lista_pedidos, name='lista_pedidos'),
    path('detallepedido/<int:pedido_id>/', detalle_pedido, name='detalle_pedido'),
    path('listaclientes/',lista_clientes, name='lista_clientes'),
    path('detalleproducto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('formulariocliente/', formulario_cliente, name='formulariocliente_sin_id'),
    path('confirmacionregistro/',confirmacion_registro, name='confirmacion_registro'),
    path('formulario/', formulario, name="formulario"),
    path('formulaireproducto/', crearProducto, name='formulaire'),
    path('ingresarusuario',ingresarUsuario, name='ingresarusuario')
]
