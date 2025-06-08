import json

tareas = []

def cargar_tareas():
    global tareas
    try:
        with open('tareas.json', 'r') as f:
            tareas = json.load(f)
    except FileNotFoundError:
        tareas = []

def guardar_tareas():
    with open('tareas.json', 'w') as f:
        json.dump(tareas, f)