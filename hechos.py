# 1 y 2 (Índices y Consultas SQL) + 3 y 4 (Bloqueos y Recursos de Hardware)
TEXTOS_HECHOS = {
    # Hechos iniciales: problema 1, índices.
    "consulta_lenta": "La consulta tarda más de lo habitual.",
    "tabla_grande": "La tabla consultada contiene muchos registros.",
    "plan_muestra_escaneo_secuencial": "El plan de ejecución muestra un escaneo secuencial.",
    "indice_ausente": "No existe un índice adecuado para la consulta.",

    # Hechos iniciales: problema 2, consulta SQL.
    "consulta_recupera_datos_excesivos": "La consulta obtiene más columnas o filas de las necesarias.",
    "consulta_sql_compleja": "La consulta contiene operaciones complejas que deben revisarse.",
    "consulta_repetida_innecesariamente": "La misma consulta se ejecuta muchas veces sin necesidad.",

    # Hechos iniciales: problema 3, bloqueos y concurrencia.
    "transacciones_esperando_bloqueo": "Existen transacciones retenidas esperando la liberación de recursos.",
    "tiempo_espera_agotado": "Se producen errores de timeout o tiempo de espera agotado en las conexiones.",
    "transacciones_largas_abiertas": "Hay transacciones que permanecen abiertas durante mucho tiempo.",

    # Hechos iniciales: problema 4, saturación de recursos (hardware/sistema).
    "uso_cpu_elevado": "El uso de CPU del servidor de base de datos es cercano al 100%.",
    "alto_consumo_ram_swap": "La memoria RAM está saturada o se está haciendo uso excesivo del espacio de intercambio (swap).",
    "alta_latencia_lectura_escritura_disco": "Las operaciones de I/O en el disco presentan una alta latencia.",

    # Hechos iniciales: problema 5, conectividad con DB2.
    "conexion_db2_fallida": "La aplicación no logra conectarse a la base de datos DB2.",
    "servicio_comunicacion_db2_inactivo": "El servicio de comunicación de DB2 está detenido o inactivo.",
    "host_puerto_db2_inaccesible": "El host o puerto configurado no es accesible desde el cliente.",

    # Hechos iniciales: problema 6, espacio en tablespaces.
    "tablespace_sin_capacidad": "El tablespace está lleno o cerca del límite de capacidad.",
    "fallo_asignacion_tablespace": "Las operaciones fallan al intentar asignar espacio en el tablespace.",
    "auto_resize_tablespace_no_disponible": "El auto-resize está deshabilitado o alcanzó su límite configurado.",

    # Hechos intermedios, diagnósticos y recomendaciones.
    # --- Problema 1 ---
    "requiere_revision_rendimiento": "La consulta requiere una revisión de rendimiento.",
    "posible_problema_indice": "Existe un posible problema de índice.",
    "diagnostico_indice_inadecuado": "Posible índice inadecuado o ausente.",
    "recomendacion_revisar_indice": "Revisar y evaluar la creación de un índice adecuado.",

    # --- Problema 2 ---
    "posible_consulta_ineficiente": "Existe una posible consulta SQL ineficiente.",
    "requiere_optimizacion_sql": "La consulta requiere optimización SQL.",
    "diagnostico_sql_ineficiente": "Consulta SQL ineficiente.",
    "recomendacion_optimizar_sql": "Reducir los datos consultados, simplificar la sentencia y evitar ejecuciones repetidas.",

    # --- Problema 3 ---
    "posible_bloqueo_concurrencia": "Existe un posible conflicto de bloqueos o concurrencia.",
    "requiere_gestion_transacciones": "Se requiere optimizar el manejo y duración de las transacciones.",
    "diagnostico_bloqueo_concurrencia": "Conflicto de bloqueos o interbloqueo (deadlock) en la base de datos.",
    "recomendacion_gestionar_concurrencia": "Reducir el tiempo de las transacciones, ajustar los niveles de aislamiento y revisar el orden de acceso a las tablas.",

    # --- Problema 4 ---
    "posible_saturacion_recursos": "Existe una posible saturación de recursos de hardware en el servidor.",
    "requiere_optimizacion_sistema": "El sistema requiere tuning de parámetros o escalado de recursos.",
    "diagnostico_saturacion_recursos": "Saturación de recursos del servidor (CPU, RAM o Disco).",
    "recomendacion_optimizar_recursos": "Aumentar capacidad de hardware, configurar adecuadamente los pools de memoria/conexiones y limitar procesos concurrentes pesados.",

    # --- Problema 5 ---
    "posible_servicio_db2_inactivo": "Existe un posible problema con el servicio de comunicación de DB2.",
    "requiere_revision_conectividad_db2": "Se requiere revisar la conectividad entre el cliente y el servidor DB2.",
    "diagnostico_conectividad_db2": "Fallo de conectividad con DB2 por servicio inactivo o host/puerto inaccesible.",
    "recomendacion_revisar_conectividad_db2": "Verificar que la instancia y el servicio de comunicación de DB2 estén activos, y revisar host, puerto y reglas de red.",

    # --- Problema 6 ---
    "posible_falta_espacio_tablespace": "Existe una posible falta de espacio en el tablespace.",
    "requiere_ampliar_tablespace": "Se requiere ampliar la capacidad disponible del tablespace.",
    "diagnostico_falta_espacio_tablespace": "Capacidad insuficiente o límite de crecimiento alcanzado en el tablespace.",
    "recomendacion_ampliar_tablespace": "Ampliar el tablespace o habilitar/configurar su crecimiento automático tras verificar el espacio disponible en almacenamiento.",
}

HECHOS_DIAGNOSTICO = {
    "diagnostico_indice_inadecuado",
    "diagnostico_sql_ineficiente",
    "diagnostico_bloqueo_concurrencia",
    "diagnostico_saturacion_recursos",
    "diagnostico_conectividad_db2",
    "diagnostico_falta_espacio_tablespace",
}

HECHOS_RECOMENDACION = {
    "recomendacion_revisar_indice",
    "recomendacion_optimizar_sql",
    "recomendacion_gestionar_concurrencia",
    "recomendacion_optimizar_recursos",
    "recomendacion_revisar_conectividad_db2",
    "recomendacion_ampliar_tablespace",
}

HECHOS_PRELIMINARES = {
    "requiere_revision_rendimiento",
    "posible_problema_indice",
    "posible_consulta_ineficiente",
    "requiere_optimizacion_sql",
    "posible_bloqueo_concurrencia",
    "requiere_gestion_transacciones",
    "posible_saturacion_recursos",
    "requiere_optimizacion_sistema",
    "posible_servicio_db2_inactivo",
    "requiere_revision_conectividad_db2",
    "posible_falta_espacio_tablespace",
    "requiere_ampliar_tablespace",
}


def obtener_texto_hecho(hecho: str) -> str:
    """Devuelve una descripción legible de un hecho conocido."""
    return TEXTOS_HECHOS.get(hecho, hecho.replace("_", " "))