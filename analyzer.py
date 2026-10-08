"""
Analizador y procesador de logs e incidencias de soporte mediante Pandas.
Filtra eventos críticos, agrupa incidencias y exporta un informe estructurado.
"""

import pandas as pd
import json

def generar_datos_prueba():
    """Genera datos de ejemplo simulando registros de un servidor/helpdesk."""
    datos = {
        "timestamp": [
            "2026-10-01 10:14:02", "2026-10-01 10:15:30", "2026-10-01 10:20:11",
            "2026-10-01 11:05:44", "2026-10-01 11:12:00", "2026-10-01 11:45:19"
        ],
        "nivel": ["INFO", "ERROR", "WARNING", "CRITICAL", "INFO", "CRITICAL"],
        "servicio": ["DHCP", "DNS_Resolver", "Auth_Service", "Database", "DHCP", "Database"],
        "mensaje": [
            "Concesion de IP renovada",
            "Fallo al resolver dominio externo",
            "Tiempo de respuesta elevado en autenticacion",
            "Conexion rechazada por sobrecarga en base de datos",
            "Nueva solicitud recibida",
            "Fallo de persistencia en disco principal"
        ]
    }
    df = pd.DataFrame(datos)
    df.to_csv("servidor_logs.csv", index=False)
    print("[+] Archivo de log de prueba generado: servidor_logs.csv")

def analizar_logs(archivo_csv):
    """Carga los logs en un DataFrame, analiza incidencias y genera reporte."""
    print(f"\n[+] Cargando y procesando {archivo_csv}...")
    df = pd.read_csv(archivo_csv)

    # Filtrar solo eventos de alerta o error
    errores = df[df["nivel"].isin(["ERROR", "CRITICAL"])]
    print(f"[!] Total de eventos criticos detectados: {len(errores)}")

    # Conteo de fallos por servicio
    resumen_servicios = errores["servicio"].value_counts().to_dict()

    reporte = {
        "total_registros_analizados": int(len(df)),
        "total_errores_criticos": int(len(errores)),
        "servicios_afectados": resumen_servicios,
        "detalle_errores": errores.to_dict(orient="records")
    }

    # Exportar reporte en formato JSON
    with open("reporte_incidencias.json", "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=4, ensure_ascii=False)

    print("[+] Reporte generado exitosamente: reporte_incidencias.json")
    print("\n--- Resumen de Servicios con Errores ---")
    for servicio, cantidad in resumen_servicios.items():
        print(f" - {servicio}: {cantidad} fallo(s)")

if __name__ == "__main__":
    generar_datos_prueba()
    analizar_logs("servidor_logs.csv")
