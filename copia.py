import os
import shutil
import datetime
import logging
import zipfile

USERPROFILE = os.environ["USERPROFILE"]

CARPETAS_ORIGEN = [
    os.path.join(USERPROFILE, 'Documents', 'Banc'),
    os.path.join(USERPROFILE, 'Documents', 'Carnets'),
    os.path.join(USERPROFILE, 'Documents', 'Classe'),
    os.path.join(USERPROFILE, 'Documents', 'Factures'),
    os.path.join(USERPROFILE, 'Documents', 'Gastos'),
    os.path.join(USERPROFILE, 'Documents', 'Guardats'),
    os.path.join(USERPROFILE, 'Documents', 'Importants'),
    os.path.join(USERPROFILE, 'Documents', 'Informàtica'),
    os.path.join(USERPROFILE, 'Documents', 'Inversions'),
    os.path.join(USERPROFILE, 'Documents', 'Matrícula i Beca'),
    os.path.join(USERPROFILE, 'Documents', 'Programs'),
    os.path.join(USERPROFILE, 'Documents', 'Renta'),
    os.path.join(USERPROFILE, 'Documents', 'Seguretat'),
    os.path.join(USERPROFILE, 'Documents', 'Títols'),
    os.path.join(USERPROFILE, 'Documents', 'Treball'),
    os.path.join(USERPROFILE, 'Documents', 'Viatges'),
    os.path.join(USERPROFILE, 'Pictures', 'Iconos'),
    os.path.join(USERPROFILE, 'Pictures', 'Fotos perfil'),
    os.path.join(USERPROFILE, 'Pictures', 'Imágenes guardadas')
]
EXCLUIR_CARPETAS = ['venv']
CARPETA_BACKUP_BASE = r"D:\Backups"

logging.basicConfig(filename='backup_service.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def copiar_carpeta(origen, destino):
    for root, dirs, files in os.walk(origen):
        dirs[:] = [d for d in dirs if d not in EXCLUIR_CARPETAS]
        ruta_relativa = os.path.relpath(root, origen)
        destino_dir = os.path.join(destino, ruta_relativa)
        os.makedirs(destino_dir, exist_ok=True)
        for archivo in files:
            origen_archivo = os.path.join(root, archivo)
            destino_archivo = os.path.join(destino_dir, archivo)
            if not os.path.exists(destino_archivo) or \
                os.path.getmtime(origen_archivo) > os.path.getmtime(destino_archivo):
                shutil.copy2(origen_archivo, destino_archivo)
                # logging.info(f'Copiado: {origen_archivo} -> {destino_archivo}')

def comprimir_a_zip(carpeta_origen, zip_destino):
    with zipfile.ZipFile(zip_destino, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(carpeta_origen):
            ruta_relativa = os.path.relpath(root, os.path.dirname(carpeta_origen))
            for archivo in files:
                archivo_completo = os.path.join(root, archivo)
                ruta_en_zip = os.path.join(ruta_relativa, archivo)
                zipf.write(archivo_completo, ruta_en_zip)
                # logging.info(f'Archivo añadido al ZIP: {ruta_en_zip}')

if __name__ == '__main__':
    hoy = datetime.date.today().strftime('%Y-%m-%d')
    carpeta_backup = os.path.join(CARPETA_BACKUP_BASE, f'backup_{hoy}')
    zip_backup_path = os.path.join(CARPETA_BACKUP_BASE, f'backup_{hoy}.zip')
    os.makedirs(carpeta_backup, exist_ok=True)
    logging.info(f'Iniciando backup en {carpeta_backup}')
    for carpeta_origen in CARPETAS_ORIGEN:
        if os.path.exists(carpeta_origen):
            nombre_carpeta = os.path.basename(carpeta_origen)
            destino_carpeta = os.path.join(carpeta_backup, nombre_carpeta)
            # logging.info(f'Copiando {carpeta_origen} a {destino_carpeta}')
            copiar_carpeta(carpeta_origen, destino_carpeta)
        else:
            logging.warning(f'Carpeta no encontrada: {carpeta_origen}')
    logging.info('Compresión a ZIP iniciada.')
    comprimir_a_zip(carpeta_backup, zip_backup_path)
    logging.info(f'Backup comprimido en: {zip_backup_path}')
    shutil.rmtree(carpeta_backup)
    logging.info(f'Carpeta temporal {carpeta_backup} eliminada.')
    logging.info('Backup finalizado.')