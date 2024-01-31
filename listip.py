# python script.py acces.log
#
import sys
from collections import Counter

def leer_archivo_log(archivo_log):
    # Diccionario para contar las direcciones IP
    direcciones_ip = Counter()

    try:
        with open(archivo_log, 'r') as archivo:
            for linea in archivo:
                # Suponiendo que las direcciones IP están en la primera columna
                ip = linea.split()[0]
                direcciones_ip[ip] += 1
    except FileNotFoundError:
        print(f"El archivo {archivo_log} no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return direcciones_ip

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <archivo_log>")
        sys.exit(1)

    archivo_log = sys.argv[1]
    direcciones_ip = leer_archivo_log(archivo_log)

    # Ordenar las direcciones IP por cantidad de apariciones
    direcciones_ip_ordenadas = sorted(direcciones_ip.items(), key=lambda x: x[1], reverse=True)

    # Imprimir las direcciones IP y su cantidad de apariciones
    for ip, cantidad in direcciones_ip_ordenadas:
        print(f"{ip}: {cantidad} veces")

if __name__ == "__main__":
    main()
