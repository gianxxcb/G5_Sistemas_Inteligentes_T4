# 1 a 6
REGLAS = [
    # --- Problema 1: Índices ---
    {
        "id": "R01",
        "antecedentes": {"consulta_lenta", "tabla_grande"},
        "consecuente": "requiere_revision_rendimiento",
        "descripcion": "La consulta es lenta y trabaja sobre una tabla grande.",
    },
    {
        "id": "R02",
        "antecedentes": {
            "requiere_revision_rendimiento",
            "plan_muestra_escaneo_secuencial",
        },
        "consecuente": "posible_problema_indice",
        "descripcion": "El rendimiento requiere revisión y el plan muestra un escaneo secuencial.",
    },
    {
        "id": "R03",
        "antecedentes": {"posible_problema_indice", "indice_ausente"},
        "consecuente": "diagnostico_indice_inadecuado",
        "descripcion": "Se encontró un posible problema de índice y no existe un índice adecuado.",
    },
    {
        "id": "R04",
        "antecedentes": {"diagnostico_indice_inadecuado"},
        "consecuente": "recomendacion_revisar_indice",
        "descripcion": "El diagnóstico requiere revisar los índices de la consulta.",
    },
    # --- Problema 2: Consultas SQL ---
    {
        "id": "R05",
        "antecedentes": {"consulta_lenta", "consulta_recupera_datos_excesivos"},
        "consecuente": "posible_consulta_ineficiente",
        "descripcion": "La consulta es lenta y recupera más datos de los necesarios.",
    },
    {
        "id": "R06",
        "antecedentes": {"posible_consulta_ineficiente", "consulta_sql_compleja"},
        "consecuente": "requiere_optimizacion_sql",
        "descripcion": "La consulta posiblemente ineficiente contiene operaciones complejas.",
    },
    {
        "id": "R07",
        "antecedentes": {
            "requiere_optimizacion_sql",
            "consulta_repetida_innecesariamente",
        },
        "consecuente": "diagnostico_sql_ineficiente",
        "descripcion": "La consulta necesita optimización y se ejecuta repetidamente sin necesidad.",
    },
    {
        "id": "R08",
        "antecedentes": {"diagnostico_sql_ineficiente"},
        "consecuente": "recomendacion_optimizar_sql",
        "descripcion": "El diagnóstico requiere optimizar la consulta SQL.",
    },
    # --- Problema 3: Bloqueos y Concurrencia ---
    {
        "id": "R09",
        "antecedentes": {
            "transacciones_esperando_bloqueo",
            "tiempo_espera_agotado",
        },
        "consecuente": "posible_bloqueo_concurrencia",
        "descripcion": "Existen transacciones retenidas y errores de timeout por bloqueos.",
    },
    {
        "id": "R10",
        "antecedentes": {
            "posible_bloqueo_concurrencia",
            "transacciones_largas_abiertas",
        },
        "consecuente": "requiere_gestion_transacciones",
        "descripcion": "Existe un posible conflicto de concurrencia acentuado por transacciones de larga duración.",
    },
    {
        "id": "R11",
        "antecedentes": {"requiere_gestion_transacciones"},
        "consecuente": "diagnostico_bloqueo_concurrencia",
        "descripcion": "Se confirma el diagnóstico de conflicto de bloqueos o interbloqueo (deadlock).",
    },
    {
        "id": "R12",
        "antecedentes": {"diagnostico_bloqueo_concurrencia"},
        "consecuente": "recomendacion_gestionar_concurrencia",
        "descripcion": "El diagnóstico requiere optimizar la duración y gestión de transacciones.",
    },
    # --- Problema 4: Saturación de Recursos de Hardware ---
    {
        "id": "R13",
        "antecedentes": {"uso_cpu_elevado", "alto_consumo_ram_swap"},
        "consecuente": "posible_saturacion_recursos",
        "descripcion": "El uso elevado de CPU y memoria indica un posible problema de recursos del servidor.",
    },
    {
        "id": "R14",
        "antecedentes": {
            "posible_saturacion_recursos",
            "alta_latencia_lectura_escritura_disco",
        },
        "consecuente": "requiere_optimizacion_sistema",
        "descripcion": "Existe una saturación general combinada con cuellos de botella en la I/O de disco.",
    },
    {
        "id": "R15",
        "antecedentes": {"requiere_optimizacion_sistema"},
        "consecuente": "diagnostico_saturacion_recursos",
        "descripcion": "Se confirma el diagnóstico de saturación de recursos del servidor (CPU, RAM o Disco).",
    },
    {
        "id": "R16",
        "antecedentes": {"diagnostico_saturacion_recursos"},
        "consecuente": "recomendacion_optimizar_recursos",
        "descripcion": "El diagnóstico requiere escalado de hardware o tuning de configuración del sistema.",
    },
    # --- Problema 5: Conectividad con DB2 ---
    {
        "id": "R17",
        "antecedentes": {
            "conexion_db2_fallida",
            "servicio_comunicacion_db2_inactivo",
        },
        "consecuente": "posible_servicio_db2_inactivo",
        "descripcion": "La conexión falla y el servicio de comunicación de DB2 está inactivo.",
    },
    {
        "id": "R18",
        "antecedentes": {
            "posible_servicio_db2_inactivo",
            "host_puerto_db2_inaccesible",
        },
        "consecuente": "requiere_revision_conectividad_db2",
        "descripcion": "El servicio está inactivo y el host o puerto tampoco es accesible desde el cliente.",
    },
    {
        "id": "R19",
        "antecedentes": {"requiere_revision_conectividad_db2"},
        "consecuente": "diagnostico_conectividad_db2",
        "descripcion": "Se confirma un fallo de conectividad con DB2.",
    },
    {
        "id": "R20",
        "antecedentes": {"diagnostico_conectividad_db2"},
        "consecuente": "recomendacion_revisar_conectividad_db2",
        "descripcion": "El diagnóstico requiere verificar los servicios, la configuración y el acceso de red de DB2.",
    },
    # --- Problema 6: Espacio en tablespaces ---
    {
        "id": "R21",
        "antecedentes": {
            "tablespace_sin_capacidad",
            "fallo_asignacion_tablespace",
        },
        "consecuente": "posible_falta_espacio_tablespace",
        "descripcion": "El tablespace está lleno y las operaciones no pueden asignar más espacio.",
    },
    {
        "id": "R22",
        "antecedentes": {
            "posible_falta_espacio_tablespace",
            "auto_resize_tablespace_no_disponible",
        },
        "consecuente": "requiere_ampliar_tablespace",
        "descripcion": "La falta de espacio coincide con un auto-resize deshabilitado o limitado.",
    },
    {
        "id": "R23",
        "antecedentes": {"requiere_ampliar_tablespace"},
        "consecuente": "diagnostico_falta_espacio_tablespace",
        "descripcion": "Se confirma capacidad insuficiente o un límite de crecimiento en el tablespace.",
    },
    {
        "id": "R24",
        "antecedentes": {"diagnostico_falta_espacio_tablespace"},
        "consecuente": "recomendacion_ampliar_tablespace",
        "descripcion": "El diagnóstico requiere ampliar el tablespace o revisar su crecimiento automático.",
    },
]