from app import app, db
from src.models.tareas import  Tareas, tarea_schema, tareas_schema
from flask import request, jsonify

@app.route('/', methods=['GET'])
def welcome():
    return {'author': 'Carlos Jorge',
            'description': 'API REST FULL con Flask y Mysql'}

@app.route('/tarea', methods=['POST'])
def create_tarea():
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    new_task = Tareas(titulo, descripcion)
    db.session.add(new_task)
    db.session.commit()
    return tarea_schema.jsonify(new_task)

@app.route('/tareas', methods=['GET'])
def get_tareas():
    all_tasks = Tareas.query.all()
    result = tareas_schema.dump(all_tasks)
    return jsonify(result)

@app.route('/tarea/<idTarea>', methods=['GET'])
def get_tarea(idTarea):
    tarea = Tareas.query.get(idTarea)
    res = tarea_schema.dump(tarea)
    return jsonify(res)

@app.route('/tarea/<idTarea>', methods=['PUT'])
def update_tarea(idTarea):
    tarea = Tareas.query.get(idTarea)

    titulo = request.json['titulo']
    descripcion = request.json['descripcion']

    tarea.titulo = titulo
    tarea.descripcion = descripcion

    db.session.commit()
    return tarea_schema.jsonify(tarea)

@app.route('/tarea/<id>', methods=['DELETE'])
def delete_tarea(id):
    tarea = Tareas.query.get(id)
    db.session.delete(tarea)
    db.session.commit()
    return tarea_schema.jsonify(tarea)