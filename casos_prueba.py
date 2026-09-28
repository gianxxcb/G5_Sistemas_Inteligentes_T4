# 1 a 6 y CP07-CP08 (Integrante 4)

from diagnostico import ejecutar_encadenamiento_hacia_adelante
from reglas import REGLAS

CASOS_PRUEBA = [
    {
        "id": "CP01",
        "nombre": "Índice inadecuado o ausente",
        "hechos": {"consulta_lenta", "tabla_grande", "plan_muestra_escaneo_secuencial", "indice_ausente"},
        "diagnosticos_esperados": ["diagnostico_indice_inadecuado"],
        "reglas_esperadas": ["R01", "R02", "R03", "R04"],
    },
    {
        "id": "CP02",
        "nombre": "Consulta SQL ineficiente",
        "hechos": {"consulta_lenta", "consulta_recupera_datos_excesivos", "consulta_sql_compleja", "consulta_repetida_innecesariamente"},
        "diagnosticos_esperados": ["diagnostico_sql_ineficiente"],
        "reglas_esperadas": ["R05", "R06", "R07", "R08"],
    },
    {
        "id": "CP03",
        "nombre": "Bloqueo y conflicto de concurrencia",
        "hechos": {"transacciones_esperando_bloqueo", "tiempo_espera_agotado", "transacciones_largas_abiertas"},
        "diagnosticos_esperados": ["diagnostico_bloqueo_concurrencia"],
        "reglas_esperadas": ["R09", "R10", "R11", "R12"],
    },
    {
        "id": "CP04",
        "nombre": "Saturación de recursos de hardware",
        "hechos": {"uso_cpu_elevado", "alto_consumo_ram_swap", "alta_latencia_lectura_escritura_disco"},
        "diagnosticos_esperados": ["diagnostico_saturacion_recursos"],
        "reglas_esperadas": ["R13", "R14", "R15", "R16"],
    },
    {
        "id": "CP05",
        "nombre": "Fallo de conectividad con DB2",
        "hechos": {"conexion_db2_fallida", "servicio_comunicacion_db2_inactivo", "host_puerto_db2_inaccesible"},
        "diagnosticos_esperados": ["diagnostico_conectividad_db2"],
        "reglas_esperadas": ["R17", "R18", "R19", "R20"],
    },
    {
        "id": "CP06",
        "nombre": "Falta de espacio en tablespace",
        "hechos": {"tablespace_sin_capacidad", "fallo_asignacion_tablespace", "auto_resize_tablespace_no_disponible"},
        "diagnosticos_esperados": ["diagnostico_falta_espacio_tablespace"],
        "reglas_esperadas": ["R21", "R22", "R23", "R24"],
    },
    {
        "id": "CP07",
        "nombre": "Información insuficiente (sin diagnóstico)",
        "hechos": {"consulta_lenta", "tabla_grande"}, 
        "diagnosticos_esperados": [], 
        "reglas_esperadas": ["R01"],
    },
    {
        "id": "CP08",
        "nombre": "Múltiples diagnósticos (Índices y Recursos)",
        "hechos": {
            "consulta_lenta", "tabla_grande", "plan_muestra_escaneo_secuencial", "indice_ausente",
            "uso_cpu_elevado", "alto_consumo_ram_swap", "alta_latencia_lectura_escritura_disco"
        },
        "diagnosticos_esperados": ["diagnostico_indice_inadecuado", "diagnostico_saturacion_recursos"],
        "reglas_esperadas": ["R01", "R02", "R03", "R04", "R13", "R14", "R15", "R16"],
    }
]

def ejecutar_casos_prueba() -> str:
    resultados = []
    for caso in CASOS_PRUEBA:
        resultado = ejecutar_encadenamiento_hacia_adelante(caso["hechos"], REGLAS)
        ids_reglas = [regla["id"] for regla in resultado["reglas_activadas"]]

        # Verificación de Diagnósticos
        if not caso["diagnosticos_esperados"]:
            assert len(resultado["diagnosticos"]) == 0, f"{caso['id']}: Se esperaba 0 diagnósticos."
        else:
            for diag in caso["diagnosticos_esperados"]:
                assert diag in resultado["diagnosticos"], f"{caso['id']}: Falta el diagnóstico {diag}."

        # Verificación de Reglas (Se usa set porque el orden de evaluación puede variar)
        assert set(ids_reglas) == set(caso["reglas_esperadas"]), (
            f"{caso['id']}: La traza no coincide. Obtenido: {ids_reglas}"
        )
        resultados.append(f"✅ {caso['id']} aprobado: {caso['nombre']}")
        
    return "\n".join(resultados)

if __name__ == "__main__":
    print("Ejecutando suite de pruebas...")
    print(ejecutar_casos_prueba())