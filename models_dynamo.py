from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute


class DesempenoAcademico(Model):
    estudiantes = NumberAttribute(hash_key=True)
    proyectoacademico = UnicodeAttribute()
    promedioacumulado = NumberAttribute()
    renovacionesmatricula = NumberAttribute()
    cantidadpruebas = NumberAttribute()

    class Meta:
        table_name = 'desempenoacademico'
        region = 'us-east-2'
        read_capacity_units = 1
        write_capacity_units = 1


def calcdesempeno():
    query = DesempenoAcademico.scan((DesempenoAcademico.promedioacumulado < 34) |
                                    (DesempenoAcademico.renovacionesmatricula > 6) |
                                    (DesempenoAcademico.cantidadpruebas > 1))
    alerta_desempeno = []
    for estudiante in query:
        alerta_desempeno.append(estudiante.estudiantes)
    return alerta_desempeno

