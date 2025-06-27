Sistema de control de ingresos y gastos
Tecnologias usadas: Flask , Sqlite, Html, Javascript, Bootstrap

- Para correr el proyecto en tu maquina local debes abrir el terminal:
1. //Crear entorno virtual//           py -3 -m venv .venv 
2. //Activar entorno virtual//        .venv\Scripts\activate
3. //Instalar flask//                 pip install Flask
4. //Instalar SQLAlchemy//            pip install -U Flask-SQLAlchemy
5. //Ejecutar app flask//             flask run
6. Al ejecutar flask run se inicia el server localhost o http://127.0.0.1:5000

- Uso de la base de datos ,a traves del kit de herramientas SQL y ORM (Object Relational Mapper) para python.
  Dentro de app.py se importan la biblioteca SQLALCHEMY.

![image alt](https://github.com/Michael-Ruminot/controlmoney/blob/f8894f89770da4fb1df4ed75ee86466deaf0be28/SQLALCHEMY.png)

- Para el uso de framework boostrap debes incluir el CDN a tu plantilla HTML:
  <!-- En el <head> de tu plantilla -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  
  <!-- Al final del <body>, para el JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  
  Para el uso de los graficos se usa la biblioteca de javascript chart.js agregando el CDN a la plantilla HTML:
  <!-- Al final del <body>, para el JS -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

- El modelo de la base de datos es como la clase de ejemplo:
![image](https://github.com/Michael-Ruminot/controlmoney/blob/cba134257a1a53dfea6c0f0c2ea0c9158fef5bea/Class%20movimiento.png)


- El modelo de la base de datos se puede visualizar con el gestor de base de datos browser SQLite
![image](https://github.com/Michael-Ruminot/controlmoney/blob/88e7d67fb8ed87dc03f4ac1fd45b2beea373b7e3/basedatos.png)


Pagina principal del sistema:
![image](https://github.com/Michael-Ruminot/controlmoney/blob/69665d4c0b2f0ac072cc125c314850c8c10cc895/principal.png)
![image](https://github.com/Michael-Ruminot/controlmoney/blob/fda034353a7859d4cd0d1cd2ab944cc450bb75c2/editar.png)
![image](https://github.com/Michael-Ruminot/controlmoney/blob/fda034353a7859d4cd0d1cd2ab944cc450bb75c2/eliminar.png)








