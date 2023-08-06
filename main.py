import os
import yaml
from utils import convertir_torrents_en_carpeta
from colorama import init, Fore

init(autoreset=True)


def load_config():
    config_file = "config.yaml"

    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            config_data = yaml.safe_load(f)
            ruta_carpeta = config_data.get("ruta_carpeta")

            if ruta_carpeta:
                return ruta_carpeta
            else:
                print("La configuración 'ruta_carpeta' no está definida en el archivo 'config.yaml'.")
    else:
        print("El archivo 'config.yaml' no existe.")

    return None

def main():
    ruta_carpeta = load_config()

    if ruta_carpeta:
        enlaces_magnet = convertir_torrents_en_carpeta(ruta_carpeta)

        if enlaces_magnet:
            torrents_generados = 0
            errores = 0

            with open('enlaces_magnet.txt', 'w') as f_magnet, open('nombres_torrent.txt', 'w') as f_nombres:
                for i, (enlace_magnet, torrent_file_path) in enumerate(enlaces_magnet, 1):
                    try:
                        magnet_path = os.path.basename(torrent_file_path)
                        magnet_path = os.path.join(ruta_carpeta, magnet_path)

                        print(Fore.GREEN + f"[{i}] {enlace_magnet} se ha generado correctamente. {torrent_file_path}")

                        # Guardar enlaces magnet en el archivo "enlaces_magnet.txt"
                        f_magnet.write(enlace_magnet + '\n')

                        # Guardar nombres de torrents en el archivo "nombres_torrent.txt"
                        f_nombres.write(os.path.basename(torrent_file_path) + '\n')

                        torrents_generados += 1
                    except Exception as e:
                        print(Fore.RED + f"[{i}] El magnet no se ha generado correctamente {torrent_file_path}")
                        errores += 1

            print(f"Se han generado correctamente {torrents_generados} magnets.")
            print(f"{errores} torrents han dado error.")
        else:
            print("No se encontraron archivos .torrent en la carpeta. Revisa la ruta de los torrents en config.yaml")
    else:
        print("No se pudo obtener la ruta de la carpeta desde 'config.yaml'.")

if __name__ == '__main__':
    main()

