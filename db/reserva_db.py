from typing import  Dict
from pydantic import BaseModel

class ReservaInDB(BaseModel):
    nombre: str
    identificacion: str
    fecha: str
    fecha_inicial: str
    fecha_final: str
    tipo_hab: str
    valor: int
    num_reserva: str

database_reservas = Dict[str, ReservaInDB]

database_reservas = {
    "rsrv01": ReservaInDB(**{"nombre":"Diana Potes",
                            "identificacion":"123456",
                            "fecha":"01-12-2020",
                            "fecha_inicial":"01-01-2021",
                            "fecha_final":"15-01-2021",
                            "tipo_hab":"Doble",
                            "valor":3000000,
                            "num_reserva": "rsrv01"}),

    "rsrv02": ReservaInDB(**{"nombre":"Alejandro Rodríguez",
                            "identificacion":"876545",
                            "fecha":"15-11-2020",
                            "fecha_inicial":"20-12-2020",
                            "fecha_final":"28-12-2020",
                            "tipo_hab":"Sencilla",
                            "valor":1800000,
                            "num_reserva": "rsrv02"}),

    "rsrv03": ReservaInDB(**{"nombre":"Jhon Jaimes",
                            "identificacion":"765645",
                            "fecha":"10-08-2020",
                            "fecha_inicial":"13-10-2020",
                            "fecha_final":"20-10-2020",
                            "tipo_hab":"Sencilla",
                            "valor":1200000,
                            "num_reserva": "rsrv03"}),

    "rsrv04": ReservaInDB(**{"nombre":"Giovanni Gutierrez",
                            "identificacion":"765454",
                            "fecha":"25-11-2020",
                            "fecha_inicial":"20-01-2021",
                            "fecha_final":"30-01-2021",
                            "tipo_hab":"Doble",
                            "valor":2200000,
                            "num_reserva": "rsrv04"}),

    "rsrv05": ReservaInDB(**{"nombre":"Mayer Monsalve",
                            "identificacion":"886453",
                            "fecha":"15-08-2020",
                            "fecha_inicial":"16-09-2020",
                            "fecha_final":"22-00-2021",
                            "tipo_hab":"Doble",
                            "valor":1050000,
                            "num_reserva": "rsrv05"}),
}

def get_reserva(num_reserva: str):
    if num_reserva in database_reservas.keys():
        return database_reservas[num_reserva]
    else:
        return None

def update_reserva(reserva_in_db: ReservaInDB):
    database_reservas[reserva_in_db.nombre] = reserva_in_db
    return reserva_in_db
