# Despliegue de Modelo de Regresión en Azure usando Base de Datos SQL

Este repositorio contiene el proyecto para la actividad de evaluación del curso de **Cloud Computing**, en el cual se monta una base de datos en Azure, se entrena un modelo de regresión para predecir la columna `ModifiedDate` de la tabla `SalesLT.Customer`, y se despliega el modelo como servicio en la nube.

## Objetivo del Proyecto

Predecir la fecha de modificación (`ModifiedDate`) de los registros de clientes utilizando un modelo de regresión entrenado sobre una base de datos SQL montada en Azure. El modelo se expone como un servicio web.

---

## Integrantes del equipo

**Nombre del equipo:** *RAR Solutions*  
1. Rodrigo González – Departamento: Infraestructura y Nube – Puesto: Arquitecto de Despliegue
2. Andrés Villarreal – Departamento: Infraestructura y Nube – Puesto: Ingeniero de Servicios Cloud
3. Hibrán Tapia – Departamento: Base de Datos – Puesto: Administrador de Bases de Datos
4. David Figueroa – Departamento: Datos y Modelado – Puesto: Especialista en Modelado Predictivo
5. Blas Treviño – Departamento: Datos y Modelado – Puesto: Científico de Datos

---

## Estructura del proyecto

### 1. Lectura de datos (`recuperar_datos.ipynb`)
- Conexión a Azure SQL usando `pyodbc` o `SQLAlchemy`.
- Lectura de la tabla `SalesLT.Customer`.
- Limpieza y transformación de datos.

### 2. Entrenamiento del modelo (`modelo.ipynb`)
- Selección de variables relevantes.
- Entrenamiento de regresión para predecir `ModifiedDate`.
- Evaluación del modelo y guardado con `joblib`.

### 3. Despliegue del servicio (`despliegue.ipynb`)
- Creación del endpoint con Flask/FastAPI.
- Carga del modelo.
- Pruebas locales y despliegue en Azure.
