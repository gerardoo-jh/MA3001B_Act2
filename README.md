# README - Proyecto de Análisis y Consulta Automática de Datos

Este repositorio contiene un sistema de procesamiento y análisis de datos con capacidad de consulta automatizada mediante una interfaz sencilla basada en notebooks. Se compone de tres fases principales: preprocesamiento, análisis exploratorio y despliegue de un modelo para inferencia.

## Instrucciones para ejecutar el proyecto

**Paso 1:** Haz fork de este repositorio.  
**Paso 2:** Ejecuta el notebook `Act2.ipynb`.  
> Este archivo realiza el análisis exploratorio inicial y define las variables clave para el modelo.

**Paso 3:** Corre `Dep_Datos (1).ipynb`.  
> Aquí se depuran los datos, eliminando valores atípicos y estandarizando las variables para su uso posterior.

**Paso 4:** Corre `api.ipynb`.  
> Este archivo sirve como la "API" del proyecto. Solo necesitas ejecutarlo, y podrás utilizar el modelo para realizar inferencias.

> **Nota importante:** Sustituye el archivo `prueba.csv` por los datos que deseas consultar. El modelo leerá dicho archivo y devolverá las predicciones de forma automática.

## Especificaciones mínimas de software

- **Sistema operativo:** MacOS Classic, OS: System 1 (1984)  
- **RAM:** 256kb  
- **Ancho de banda:** Dos latas conectadas por una cuerda de fibra óptica
