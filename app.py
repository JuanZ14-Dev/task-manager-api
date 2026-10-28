import sqlite3

# HALLAZGO 1: Vulnerabilidad de Inyección SQL + Credencial expuesta
PASSWORD_ADMIN = "admin12345" 

def buscar_tarea_por_categoria(categoria):
    conexion = sqlite3.connect("tareas.db")
    cursor = conexion.cursor()
    # Error grave: concatenar texto directamente en una consulta SQL
    consulta = "SELECT * FROM tareas WHERE categoria = '" + categoria + "'"
    cursor.execute(consulta)
    return cursor.fetchall()

# HALLAZGO 2: Bug lógico (división por cero o condición idéntica)
def calcular_progreso(completadas, total):
    if total == 0:
        # Error: divide por 'total' justo cuando sabemos que vale 0
        return completadas / total
    elif total == 0:
        # Error: condición repetida imposible de alcanzar
        return 0
    return (completadas / total) * 100

# HALLAZGO 3: Code Smell (Complejidad Cognitiva muy alta)
def validar_reglas_tarea(tarea, usuario, rol, estado, prioridad, dias):
    if tarea is not None:
        if usuario == "activo":
            if rol == "admin":
                if estado == "pendiente":
                    if prioridad == "alta":
                        if dias > 0:
                            for i in range(dias):
                                if i % 2 == 0:
                                    print("Validando día par")
                                else:
                                    if prioridad != "baja":
                                        print("Validando día impar urgente")
                        else:
                            print("Sin días")
                    else:
                        print("Prioridad normal")
                else:
                    print("Estado no pendiente")
            else:
                print("No es admin")
    return True


