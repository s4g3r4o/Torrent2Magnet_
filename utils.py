import os
import hashlib
import bencodepy
from binascii import hexlify
from fake_useragent import UserAgent

def torrent_to_magnet(torrent_file_path):
    with open(torrent_file_path, 'rb') as f:
        torrent_data = f.read()

    metadata = bencodepy.decode(torrent_data)
    info_hash = hashlib.sha1(bencodepy.encode(metadata[b'info'])).digest()
    hex_hash = hexlify(info_hash).decode('utf-8')

    magnet_uri = 'magnet:?xt=urn:btih:' + hex_hash

    return magnet_uri

def convertir_torrents_en_carpeta(ruta_carpeta):
    enlaces_magnet = []
    for nombre_archivo in os.listdir(ruta_carpeta):
        if nombre_archivo.endswith('.torrent'):
            ruta_archivo_torrent = os.path.join(ruta_carpeta, nombre_archivo)
            print(f"Procesando archivo .torrent: {ruta_archivo_torrent}")
            enlace_magnet = torrent_to_magnet(ruta_archivo_torrent)
            enlaces_magnet.append((enlace_magnet, ruta_archivo_torrent))
    return enlaces_magnet

if __name__ == '__main__':
    ruta_carpeta = 'torrents'  # Reemplaza con la ruta de la carpeta que contiene tus archivos .torrent
    enlaces_magnet = convertir_torrents_en_carpeta(ruta_carpeta)
    for enlace_magnet in enlaces_magnet:
        print(enlace_magnet)