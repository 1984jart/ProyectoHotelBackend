from db.reserva_db import ReservaInDB
from db.reserva_db import update_reserva, get_reserva, database_reservas
from models.reserva_models import ReservaIn, ReservaOut
from datetime import datetime, date

from fastapi import FastAPI, HTTPException

api = FastAPI()
consecutivo=5
reserva_in_db:ReservaInDB

@api.get("/reserva/vista/{num_reserva}")
async def listar_reserva(num_reserva: str):

    reserva_in_db = get_reserva(num_reserva)

    if reserva_in_db == None:
        raise HTTPException(status_code=404, detail="La reserva no existe")

    
    reserva_out = ReservaOut(**reserva_in_db.dict())

    return  reserva_out

@api.post("/reserva/crear")
async def crear_reserva(nombre:str, identificacion:str, fecha_inicio:str, fecha_fin:str, tipo_habitacion:str):
    global consecutivo
    try:
        fechai = datetime.strptime(fecha_inicio, '%d/%m/%Y')
        fechaf = datetime.strptime(fecha_fin, '%d/%m/%Y')
        
    except:
        raise HTTPException(status_code=422, detail="Formato de fecha inválido. debe ser dd/mm/aaaa")
    
    if(fechaf<fechai):
        raise HTTPException(status_code=422, detail="La fecha final debe ser mayor que la fecha inicial")
       
  
    fecha=date.today()
    dias= (fechaf-fechai).days
    valor=150000*dias
    consecutivo+=1
    if(consecutivo<10):
        pre="rsrv0"
    else:
        pre ="rsrv"
    idreserva=pre+str(consecutivo)
       

    reserva_in_db=ReservaInDB(**{"nombre":nombre,
                            "identificacion":identificacion,
                            "fecha":fecha.strftime('%d/%m/%Y'),
                            "fecha_inicial":fecha_inicio,
                            "fecha_final":fecha_fin,
                            "tipo_hab":tipo_habitacion,
                            "valor":valor,
                            "num_reserva": idreserva})
    
    
    database_reservas[reserva_in_db.num_reserva]=reserva_in_db

    return "Se ha creado la reserva "+idreserva