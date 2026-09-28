# 1, 2, 3 y 4

from hechos import HECHOS_DIAGNOSTICO, HECHOS_PRELIMINARES, HECHOS_RECOMENDACION


def ejecutar_encadenamiento_hacia_adelante(
    hechos_iniciales: set[str], reglas: list[dict]
) -> dict:
    hechos_conocidos = set(hechos_iniciales)
    reglas_activadas = []
    se_genero_hecho = True

    while se_genero_hecho:
        se_genero_hecho = False

        for regla in reglas:
            antecedentes = regla["antecedentes"]
            consecuente = regla["consecuente"]

            if antecedentes.issubset(hechos_conocidos) and consecuente not in hechos_conocidos:
                hechos_conocidos.add(consecuente)
                reglas_activadas.append(regla)
                se_genero_hecho = True

    diagnosticos = sorted(HECHOS_DIAGNOSTICO.intersection(hechos_conocidos))
    recomendaciones = sorted(HECHOS_RECOMENDACION.intersection(hechos_conocidos))
    hallazgos_preliminares = sorted(HECHOS_PRELIMINARES.intersection(hechos_conocidos))

    return {
        "hechos_iniciales": set(hechos_iniciales),
        "hechos_conocidos": hechos_conocidos,
        "reglas_activadas": reglas_activadas,
        "diagnosticos": diagnosticos,
        "recomendaciones": recomendaciones,
        "hallazgos_preliminares": hallazgos_preliminares,
    }

def verificar_hipotesis_hacia_atras(
    hipotesis: str,
    hechos_conocidos: set[str],
    reglas: list[dict],
) -> dict:
    reglas_por_consecuente = {}

    for regla in reglas:
        consecuente = regla["consecuente"]

        if consecuente not in reglas_por_consecuente:
            reglas_por_consecuente[consecuente] = []

        reglas_por_consecuente[consecuente].append(regla)

    def demostrar(objetivo: str, objetivos_en_revision: set[str]):
        # Caso 1: el objetivo ya es un hecho confirmado.
        if objetivo in hechos_conocidos:
            return {
                "demostrado": True,
                "hechos_necesarios": {objetivo},
                "hechos_faltantes": set(),
                "reglas_usadas": [],
                "traza": [
                    f"Hecho confirmado: {objetivo}"
                ],
            }

        # Evita ciclos, por ejemplo: R1 produce A y R2 vuelve a pedir A.
        if objetivo in objetivos_en_revision:
            return {
                "demostrado": False,
                "hechos_necesarios": set(),
                "hechos_faltantes": {objetivo},
                "reglas_usadas": [],
                "traza": [
                    f"No se puede continuar: existe un ciclo con {objetivo}."
                ],
            }

        reglas_posibles = reglas_por_consecuente.get(objetivo, [])

        # Caso 2: no existe ninguna regla para demostrar el objetivo.
        if not reglas_posibles:
            return {
                "demostrado": False,
                "hechos_necesarios": {objetivo},
                "hechos_faltantes": {objetivo},
                "reglas_usadas": [],
                "traza": [
                    f"Falta confirmar el hecho: {objetivo}"
                ],
            }

        resultados_no_confirmados = []

        # Busca una regla que pueda demostrar el objetivo.
        for regla in reglas_posibles:
            hechos_necesarios = set()
            hechos_faltantes = set()
            reglas_usadas = []
            traza = []
            todos_demostrados = True

            nuevos_objetivos_en_revision = set(objetivos_en_revision)
            nuevos_objetivos_en_revision.add(objetivo)

            for antecedente in sorted(regla["antecedentes"]):
                resultado_antecedente = demostrar(
                    antecedente,
                    nuevos_objetivos_en_revision,
                )

                hechos_necesarios.update(
                    resultado_antecedente["hechos_necesarios"]
                )
                hechos_faltantes.update(
                    resultado_antecedente["hechos_faltantes"]
                )
                reglas_usadas.extend(
                    resultado_antecedente["reglas_usadas"]
                )
                traza.extend(resultado_antecedente["traza"])

                if not resultado_antecedente["demostrado"]:
                    todos_demostrados = False

            if todos_demostrados:
                reglas_usadas.append(regla)
                traza.append(
                    f"Regla {regla['id']} confirmada: "
                    f"se demuestra {objetivo}."
                )

                return {
                    "demostrado": True,
                    "hechos_necesarios": hechos_necesarios,
                    "hechos_faltantes": set(),
                    "reglas_usadas": reglas_usadas,
                    "traza": traza,
                }

            traza.append(
                f"Regla {regla['id']} no confirmada: "
                f"faltan hechos para demostrar {objetivo}."
            )

            resultados_no_confirmados.append(
                {
                    "demostrado": False,
                    "hechos_necesarios": hechos_necesarios,
                    "hechos_faltantes": hechos_faltantes,
                    "reglas_usadas": reglas_usadas,
                    "traza": traza,
                }
            )
        # Si ninguna regla funcionó, devuelve la que requiere menos hechos faltantes.
        mejor_resultado = min(
            resultados_no_confirmados,
            key=lambda resultado: len(resultado["hechos_faltantes"]),
        )
        return mejor_resultado
    resultado = demostrar(hipotesis, set())
    return {
        "hipotesis": hipotesis,
        "confirmada": resultado["demostrado"],
        "hechos_necesarios": resultado["hechos_necesarios"],
        "hechos_faltantes": resultado["hechos_faltantes"],
        "reglas_usadas": resultado["reglas_usadas"],
        "traza": resultado["traza"],
    }