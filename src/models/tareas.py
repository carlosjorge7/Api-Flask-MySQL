from app import db, ma

class Tareas(db.Model):
    idTarea = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(70), unique=True)
    descripcion = db.Column(db.String(100))
    
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion

db.create_all()

class TareasSchema(ma.Schema):
    class Meta:
        fields = ('idTarea', 'titulo', 'descripcion')

tarea_schema = TareasSchema()
tareas_schema = TareasSchema(many=True)