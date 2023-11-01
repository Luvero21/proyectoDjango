# Proyecto Django

Es un proyecto web desarrollado en Django que se encarga de gestionar usuarios, clientes y productos. El proyecto incluye un buscador de productos en la interfaz de usuario.

## Modelos

### Usuario
El modelo de Usuario se utiliza para representar a los usuarios del sistema. Cada usuario tiene un nombre de usuario, nombre, email,password y edad . Este modelo es la base para la generacion de un usuario nuevo.

### Cliente
El modelo de Cliente representa a los clientes de la empresa. Contiene campos como nombre, dirección, teléfono y correo electrónico. Los clientes se pueden registrar en el sistema a través de un formulario y los lleva a una confirmacion si se registraron exitosamente.

### Producto
El modelo de Producto se utiliza para representar los productos que ofrece la empresa. Contiene detalles sobre cada producto, como nombre, descripción ,precio e imagen. Los productos se pueden buscar a través de la interfaz de usuario.

## Buscador de Producto
La interfaz de usuario incluye un buscador de productos que permite a los usuarios buscar productos por nombre. Los resultados de la búsqueda se muestran en una lista, lo que facilita a los usuarios encontrar los productos que necesitan.

## Requisitos
asgiref==3.7.2
Django==4.2.6
sqlparse==0.4.4
tzdata==2023.3


¡Gracias ! Luciana

