import os
import shutil

ruta = os.getcwd()
contenido = os.listdir(ruta)

for elemento in contenido:
    ruta_completa = os.path.join(ruta, elemento)

    if elemento == 'organizador.py':
        continue

    if os.path.isfile(ruta_completa):
        (nombre, tipo) = os.path.splitext(elemento)
        tipo_sin_punto = tipo[1:]
        print(f'Archivo: {tipo_sin_punto}')

        ruta_carpeta_nueva = os.path.join(ruta, tipo_sin_punto)
        if not os.path.exists(ruta_carpeta_nueva):
            os.mkdir(ruta_carpeta_nueva)

        ruta_destino = os.path.join(ruta_carpeta_nueva, elemento)
        shutil.move(ruta_completa, ruta_destino)        


    elif os.path.isdir(ruta_completa):
        print(f'Carpeta: {elemento}')
