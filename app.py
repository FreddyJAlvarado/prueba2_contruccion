from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulamos una base de datos 
inventario = {
    1: {"nombre": "Producto A", "cantidad": 10},
    2: {"nombre": "Producto B", "cantidad": 5}
}

# Parte 1: Programación defensiva
def consultar_producto(id_producto):
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un entero positivo."}, 400
    producto = inventario.get(id_producto)
    if not producto:
        return {"error": "Producto no encontrado."}, 404
    return producto, 200

def agregar_producto(id_producto, cantidad):
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un entero positivo."}, 400
    if not isinstance(cantidad, int) or cantidad <= 0:
        return {"error": "La cantidad debe ser un entero positivo."}, 400
    if id_producto in inventario:
        inventario[id_producto]["cantidad"] += cantidad
    else:
        inventario[id_producto] = {"nombre": f"Producto {id_producto}", "cantidad": cantidad}
    return {"mensaje": "Producto agregado/actualizado con éxito."}, 200

# Parte 2: Programación por contrato y aserciones
def actualizar_stock(id_producto, nueva_cantidad):
    assert isinstance(id_producto, int) and id_producto > 0, "El ID del producto debe ser un entero positivo."
    assert isinstance(nueva_cantidad, int) and nueva_cantidad >= 0, "La cantidad debe ser un entero no negativo."

    if id_producto not in inventario:
        return {"error": "Producto no encontrado."}, 404
    inventario[id_producto]["cantidad"] = nueva_cantidad
    return {"mensaje": "Stock actualizado con éxito."}, 200

# Parte 3: Creación de la API
@app.route('/producto/<int:id_producto>', methods=['GET'])
def get_producto(id_producto):
    response, status = consultar_producto(id_producto)
    return jsonify(response), status

@app.route('/producto', methods=['POST'])
def post_producto():
    data = request.get_json()
    id_producto = data.get("id_producto")
    cantidad = data.get("cantidad")
    response, status = agregar_producto(id_producto, cantidad)
    return jsonify(response), status

@app.route('/producto/<int:id_producto>', methods=['PUT'])
def put_producto(id_producto):
    data = request.get_json()
    nueva_cantidad = data.get("nueva_cantidad")
    try:
        response, status = actualizar_stock(id_producto, nueva_cantidad)
    except AssertionError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(response), status

if __name__ == '__main__':
    app.run(debug=True)
