#Importamos MongoClientes para conectarnos a mongo db
from unittest import result
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

#Crear una base de datos
db = client["University"]

colection = db["students"]
colection = db["teachers"]

list_students = [{"name": "Ana Gómez", "age": "22", "career": "Ingeniería Civil", "email": "ana.gomez@gmail.com", "address": "Calle Ficticia 123"},
  {"name": "Carlos Martínez", "age": "21", "career": "Medicina", "email": "carlos.martinez@gmail.com", "address": "Avenida Central 456"},
  {"name": "Luis Pérez", "age": "23", "career": "Derecho", "email": "luis.perez@gmail.com", "address": "Calle de los Abetos 789"},
  {"name": "Marta Ruiz", "age": "20", "career": "Psicología", "email": "marta.ruiz@gmail.com", "address": "Calle Luna 101"},
  {"name": "Juan Díaz", "age": "24", "career": "Arquitectura", "email": "juan.diaz@gmail.com", "address": "Calle Sol 202"},
  {"name": "Patricia López", "age": "21", "career": "Economía", "email": "patricia.lopez@gmail.com", "address": "Calle Cielo 303"},
  {"name": "Pedro Gómez", "age": "25", "career": "Contaduría", "email": "pedro.gomez@gmail.com", "address": "Avenida del Mar 404"},
  {"name": "Sara González", "age": "22", "career": "Biología", "email": "sara.gonzalez@gmail.com", "address": "Calle Árbol 505"},
  {"name": "José Sánchez", "age": "23", "career": "Química", "email": "jose.sanchez@gmail.com", "address": "Calle de las Flores 606"},
  {"name": "Raquel Martín", "age": "20", "career": "Ingeniería Industrial", "email": "raquel.martin@gmail.com", "address": "Calle del Sol 707"},
  {"name": "David Torres", "age": "24", "career": "Filosofía", "email": "david.torres@gmail.com", "address": "Calle de los Pinos 808"},
  {"name": "Lucía Fernández", "age": "21", "career": "Derecho", "email": "lucia.fernandez@gmail.com", "address": "Calle 11 909"},
  {"name": "Miguel Castro", "age": "22", "career": "Historia", "email": "miguel.castro@gmail.com", "address": "Calle del Viento 1001"},
  {"name": "Sofía Ramírez", "age": "23", "career": "Trabajo Social", "email": "sofia.ramirez@gmail.com", "address": "Calle del Río 1111"},
  {"name": "Andrés Morales", "age": "25", "career": "Arquitectura", "email": "andres.morales@gmail.com", "address": "Avenida Montaña 1212"},
  {"name": "Elena Pérez", "age": "20", "career": "Literatura", "email": "elena.perez@gmail.com", "address": "Calle Estrella 1313"},
  {"name": "Javier Hernández", "age": "22", "career": "Ciencias Políticas", "email": "javier.hernandez@gmail.com", "address": "Calle Luna 1414"},
  {"name": "Claudia Ruiz", "age": "24", "career": "Arte", "email": "claudia.ruiz@gmail.com", "address": "Calle Cielo 1515"},
  {"name": "Ricardo Díaz", "age": "23", "career": "Mecatrónica", "email": "ricardo.diaz@gmail.com", "address": "Calle Mármol 1616"}
    
]
list_teachers = [{"name": "Carlos Herrera", "age": "45", "career": "Filosofía", "email": "carlos.herrera@universidad.com", "address": "Calle Principal 100", "profession": "Profesor Universitario"},
  {"name": "María López", "age": "50", "career": "Medicina", "email": "maria.lopez@universidad.com", "address": "Avenida Las Flores 200", "profession": "Profesora de Medicina"},
  {"name": "Luis Sánchez", "age": "48", "career": "Ingeniería Civil", "email": "luis.sanchez@universidad.com", "address": "Calle del Sol 300", "profession": "Profesor de Ingeniería"},
  {"name": "Patricia García", "age": "42", "career": "Historia", "email": "patricia.garcia@universidad.com", "address": "Calle de la Historia 400", "profession": "Profesora de Historia"},
  {"name": "Juan González", "age": "40", "career": "Derecho", "email": "juan.gonzalez@universidad.com", "address": "Avenida Derecho 500", "profession": "Profesor de Derecho"},
  {"name": "Elena Ruiz", "age": "37", "career": "Psicología", "email": "elena.ruiz@universidad.com", "address": "Calle Psico 600", "profession": "Profesora de Psicología"},
  {"name": "Antonio Morales", "age": "52", "career": "Matemáticas", "email": "antonio.morales@universidad.com", "address": "Calle Matemática 700", "profession": "Profesor de Matemáticas"},
  {"name": "Beatriz Fernández", "age": "44", "career": "Literatura", "email": "beatriz.fernandez@universidad.com", "address": "Avenida Literaria 800", "profession": "Profesora de Literatura"},
  {"name": "Ricardo Pérez", "age": "46", "career": "Economía", "email": "ricardo.perez@universidad.com", "address": "Calle de la Economía 900", "profession": "Profesor de Economía"},
  {"name": "Ana Martínez", "age": "49", "career": "Biología", "email": "ana.martinez@universidad.com", "address": "Calle Verde 1000", "profession": "Profesora de Biología"}
]

result_list = colection.insert_many(list_students)
print("El alumno insertado con ID:", result.inserted_id)

search_student = colection.find_one({"name": ""})
print("El alumno encontrado es:", search_student)

result_list = colection.insert_many(list_teachers)
print("El profesor insertado con ID:", result.inserted_id)

search_teacher = colection.find_one({"name": ""})
print("El profesor encontrado es:", search_teacher)

colection.update_one(
    {"$set":{"": ""}}
)

colection.update_one(
    {"name": ""},
    {
        "$unset":
            {"": ""}

    }
)

colection.delete_one(
    {"name": ""}
)