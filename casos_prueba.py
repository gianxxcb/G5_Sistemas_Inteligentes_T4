# 1 a 6

from diagnostico import ejecutar_encadenamiento_hacia_adelante
from reglas import REGLAS

CASOS_PRUEBA = [
    {
        "id": "CP01",
        "nombre": "Índice inadecuado o ausente",
        "hechos": {
            "consulta_lenta",
            "tabla_grande",
            "plan_muestra_escaneo_secuencial",
            "indice_ausente",
        },
        "diagnostico_esperado": "diagnostico_indice_inadecuado",
        "reglas_esperadas": ["R01", "R02", "R03", "R04"],
    },
    {
        "id": "CP02",
        "nombre": "Consulta SQL ineficiente",
        "hechos": {
            "consulta_lenta",
            "consulta_recupera_datos_excesivos",
            "consulta_sql_compleja",
            "consulta_repetida_innecesariamente",
        },
        "diagnostico_esperado": "diagnostico_sql_ineficiente",
        "reglas_esperadas": ["R05", "R06", "R07", "R08"],
    },
    {
        "id": "CP03",
        "nombre": "Bloqueo y conflicto de concurrencia",
        "hechos": {
            "transacciones_esperando_bloqueo",
            "tiempo_espera_agotado",
            "transacciones_largas_abiertas",
        },
        "diagnostico_esperado": "diagnostico_bloqueo_concurrencia",
        "reglas_esperadas": ["R09", "R10", "R11", "R12"],
    },
    {
        "id": "CP04",
        "nombre": "Saturación de recursos de hardware",
        "hechos": {
            "uso_cpu_elevado",
            "alto_consumo_ram_swap",
            "alta_latencia_lectura_escritura_disco",
        },
        "diagnostico_esperado": "diagnostico_saturacion_recursos",
        "reglas_esperadas": ["R13", "R14", "R15", "R16"],
    },
    {
        "id": "CP05",
        "nombre": "Fallo de conectividad con DB2",
        "hechos": {
            "conexion_db2_fallida",
            "servicio_comunicacion_db2_inactivo",
            "host_puerto_db2_inaccesible",
        },
        "diagnostico_esperado": "diagnostico_conectividad_db2",
        "reglas_esperadas": ["R17", "R18", "R19", "R20"],
    },
    {
        "id": "CP06",
        "nombre": "Falta de espacio en tablespace",
        "hechos": {
            "tablespace_sin_capacidad",
            "fallo_asignacion_tablespace",
            "auto_resize_tablespace_no_disponible",
        },
        "diagnostico_esperado": "diagnostico_falta_espacio_tablespace",
        "reglas_esperadas": ["R21", "R22", "R23", "R24"],
    },
]


def ejecutar_casos_prueba() -> None:
    for caso in CASOS_PRUEBA:
        resultado = ejecutar_encadenamiento_hacia_adelante(caso["hechos"], REGLAS)
        ids_reglas = [regla["id"] for regla in resultado["reglas_activadas"]]

        assert caso["diagnostico_esperado"] in resultado["diagnosticos"], (
            f"{caso['id']}: no se obtuvo el diagnóstico esperado."
        )
        assert ids_reglas == caso["reglas_esperadas"], (
            f"{caso['id']}: la traza de reglas no coincide."
        )
        print(f"{caso['id']} aprobado: {caso['nombre']}")


if __name__ == "__main__":
    ejecutar_casos_prueba()