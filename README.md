# prueba2_contruccion
Resolucion de prueba 2 Ejercicio Práctico: Programación Defensiva, por Contrato y Aserciones + Creación de una API
Para ejecutar este codigo toca tener intalado Flask de no tenerlo ejecutar pip install flask

Ejecutar el codigo es: python app.py

Puede hacer pruebas en postman 
Get(Consulta): 
GET /producto/{id_producto}
ejemplo para postman: http://127.0.0.1:5000/producto
Body (JSON):
{
  "id_producto": 2,
}
Post(Agregar):
ejemplo para postman: http://127.0.0.1:5000/producto
Body (JSON):
{
  "id_producto": 3,
  "cantidad": 15
}
Put(Actualizar):
ejemplo para postman: http://127.0.0.1:5000/producto
Body (JSON):
{
  "id_producto": 3
  "nueva_cantidad": 20
}
