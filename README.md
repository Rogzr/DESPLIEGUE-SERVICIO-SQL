# Despliegue de Modelo de Regresión en Azure usando Base de Datos SQL

Este repositorio contiene el proyecto para la actividad de evaluación del curso de **Cloud Computing**, en el cual se monta una base de datos en Azure, se entrena un modelo de regresión para predecir la columna `ModifiedDate` de la tabla `SalesLT.Customer`, y se despliega el modelo como servicio en la nube.

## Objetivo del Proyecto

Predecir la fecha de modificación (`ModifiedDate`) de los registros de clientes utilizando un modelo de regresión entrenado sobre una base de datos SQL montada en Azure. El modelo se expone como un servicio web.

---

## Integrantes del equipo

**Nombre del equipo:** *RAR Solutions*  
1. Nombre 1 – Departamento: [Área] – Puesto: [Rol]  
2. Nombre 2 – Departamento: [Área] – Puesto: [Rol]  
3. Nombre 3 – Departamento: [Área] – Puesto: [Rol]
2. Nombre 2 – Departamento: [Área] – Puesto: [Rol]  
3. Nombre 3 – Departamento: [Área] – Puesto: [Rol]

---

## Estructura del proyecto

### 1. Lectura de datos (`1_lectura_datos.ipynb`)
- Conexión a Azure SQL usando `pyodbc` o `SQLAlchemy`.
- Lectura de la tabla `SalesLT.Customer`.
- Limpieza y transformación de datos.

### 2. Entrenamiento del modelo (`2_entrenamiento_modelo.ipynb`)
- Selección de variables relevantes.
- Entrenamiento de regresión para predecir `ModifiedDate`.
- Evaluación del modelo y guardado con `joblib`.

### 3. Despliegue del servicio (`3_despliegue_servicio.ipynb`)
- Creación del endpoint con Flask/FastAPI.
- Carga del modelo.
- Pruebas locales y despliegue en Azure.
