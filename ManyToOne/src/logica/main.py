import sys
import os

# Agregar el directorio "src" al sys.path para encontrar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from modelo.database import MisDatos, Asignaturas, Session

def insertar_datos():
    session = Session()

    # Insertar datos en la tabla MisDatos
    mis_datos = MisDatos(
        nombre='Jose',
        apellido='Lazaro',
        edad=20,
        sexo='masculino',
        carrera='Ing. Sistemas'
    )
    session.add(mis_datos)
    session.commit()

    # Insertar datos en la tabla Asignaturas
    asignaturas = [
        Asignaturas(curso='Construccion de software', mis_datos_id=mis_datos.id),
        Asignaturas(curso='Simulacion', mis_datos_id=mis_datos.id),
        Asignaturas(curso='Investigacion Operativa', mis_datos_id=mis_datos.id),
        Asignaturas(curso='Arquitectura Empresarial', mis_datos_id=mis_datos.id)
    ]
    session.add_all(asignaturas)

    # Guardar cambios y cerrar la sesión
    session.commit()
    session.close()

    print("Datos insertados correctamente.")

if __name__ == '__main__':
    insertar_datos()
