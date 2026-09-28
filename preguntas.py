# Preguntas 1 a 6
CATEGORIAS = {
    "1": {
        "codigo": "indices",
        "nombre": "Consultas lentas por índices",
        "descripcion": "Evalúa síntomas relacionados con índices y planes de ejecución.",
    },
    "2": {
        "codigo": "sql",
        "nombre": "Consultas SQL ineficientes",
        "descripcion": "Evalúa consultas que recuperan datos excesivos o se ejecutan repetidamente.",
    },
    "3": {
        "codigo": "bloqueos",
        "nombre": "Bloqueos y conflictos de concurrencia",
        "descripcion": "Evalúa problemas causados por transacciones retenidas, interbloqueos (deadlocks) o timeouts.",
    },
    "4": {
        "codigo": "recursos",
        "nombre": "Saturación de recursos de hardware",
        "descripcion": "Evalúa el consumo excesivo de CPU, memoria RAM/Swap y latencia de I/O en disco.",
    },
    "5": {
        "codigo": "conectividad",
        "nombre": "Problemas de conectividad con DB2",
        "descripcion": "Evalúa fallos de conexión relacionados con los servicios y el acceso al servidor DB2.",
    },
    "6": {
        "codigo": "tablespaces",
        "nombre": "Falta de espacio en tablespaces",
        "descripcion": "Evalúa errores de asignación por capacidad insuficiente o límites de crecimiento de tablespaces.",
    },
}

PREGUNTAS = {
    "indices": [
        {
            "id": "P01",
            "texto": "¿La consulta tarda más de lo habitual?",
            "hecho_si": "consulta_lenta",
            "hecho_no": None,
        },
        {
            "id": "P02",
            "texto": "¿La tabla consultada contiene muchos registros?",
            "hecho_si": "tabla_grande",
            "hecho_no": None,
        },
        {
            "id": "P03",
            "texto": "¿El plan de ejecución muestra un escaneo secuencial?",
            "hecho_si": "plan_muestra_escaneo_secuencial",
            "hecho_no": None,
        },
        {
            "id": "P04",
            "texto": "¿Existe un índice adecuado para las columnas consultadas?",
            "hecho_si": None,
            "hecho_no": "indice_ausente",
        },
    ],
    "sql": [
        {
            "id": "P05",
            "texto": "¿La consulta tarda más de lo habitual?",
            "hecho_si": "consulta_lenta",
            "hecho_no": None,
        },
        {
            "id": "P06",
            "texto": "¿La consulta obtiene más columnas o filas de las necesarias?",
            "hecho_si": "consulta_recupera_datos_excesivos",
            "hecho_no": None,
        },
        {
            "id": "P07",
            "texto": "¿La consulta contiene JOIN, subconsultas o filtros complejos que no se han revisado?",
            "hecho_si": "consulta_sql_compleja",
            "hecho_no": None,
        },
        {
            "id": "P08",
            "texto": "¿La misma consulta se ejecuta muchas veces sin necesidad?",
            "hecho_si": "consulta_repetida_innecesariamente",
            "hecho_no": None,
        },
    ],
    "bloqueos": [
        {
            "id": "P09",
            "texto": "¿Existen transacciones retenidas esperando la liberación de recursos?",
            "hecho_si": "transacciones_esperando_bloqueo",
            "hecho_no": None,
        },
        {
            "id": "P10",
            "texto": "¿Se producen errores de timeout o tiempo de espera agotado en las conexiones?",
            "hecho_si": "tiempo_espera_agotado",
            "hecho_no": None,
        },
        {
            "id": "P11",
            "texto": "¿Hay transacciones que permanecen abiertas durante mucho tiempo?",
            "hecho_si": "transacciones_largas_abiertas",
            "hecho_no": None,
        },
    ],
    "recursos": [
        {
            "id": "P12",
            "texto": "¿El uso de CPU del servidor de base de datos es cercano al 100%?",
            "hecho_si": "uso_cpu_elevado",
            "hecho_no": None,
        },
        {
            "id": "P13",
            "texto": "¿La memoria RAM está saturada o se hace uso excesivo del espacio de intercambio (swap)?",
            "hecho_si": "alto_consumo_ram_swap",
            "hecho_no": None,
        },
        {
            "id": "P14",
            "texto": "¿Las operaciones de lectura y escritura en el disco presentan una alta latencia?",
            "hecho_si": "alta_latencia_lectura_escritura_disco",
            "hecho_no": None,
        },
    ],
    "conectividad": [
        {
            "id": "P15",
            "texto": "¿La aplicación no logra conectarse a la base de datos DB2?",
            "hecho_si": "conexion_db2_fallida",
            "hecho_no": None,
        },
        {
            "id": "P16",
            "texto": "¿El servicio de comunicación de DB2 está detenido o inactivo?",
            "hecho_si": "servicio_comunicacion_db2_inactivo",
            "hecho_no": None,
        },
        {
            "id": "P17",
            "texto": "¿El host o puerto configurado no es accesible desde el cliente?",
            "hecho_si": "host_puerto_db2_inaccesible",
            "hecho_no": None,
        },
    ],
    "tablespaces": [
        {
            "id": "P18",
            "texto": "¿El tablespace está lleno o cerca del límite de capacidad?",
            "hecho_si": "tablespace_sin_capacidad",
            "hecho_no": None,
        },
        {
            "id": "P19",
            "texto": "¿Las operaciones fallan al intentar asignar espacio en el tablespace?",
            "hecho_si": "fallo_asignacion_tablespace",
            "hecho_no": None,
        },
        {
            "id": "P20",
            "texto": "¿El auto-resize está deshabilitado o alcanzó su límite configurado?",
            "hecho_si": "auto_resize_tablespace_no_disponible",
            "hecho_no": None,
        },
    ],
}


def obtener_preguntas(codigo_categoria: str) -> list[dict]:
    """Obtiene las preguntas de una categoría seleccionada."""
    return PREGUNTAS.get(codigo_categoria, [])


def convertir_respuesta_en_hecho(pregunta: dict, respuesta: str) -> str | None:
    """Convierte una respuesta si/no en el hecho que corresponda."""
    if respuesta == "s":
        return pregunta["hecho_si"]
    return pregunta["hecho_no"]