# 🏦 Simulación de Banco con Colas y Pilas

## 📌 Descripción

Este proyecto consiste en una simulación de atención en un banco utilizando estructuras de datos como **colas** y **pilas** en Python.

El sistema permite manejar clientes con diferentes prioridades, asignarlos a cajas disponibles y llevar un registro de las atenciones realizadas.

---

## 🎯 Objetivo

Simular el funcionamiento de una fila de banco donde:

* Los clientes son atendidos según su prioridad
* Se manejan múltiples cajas de atención
* Se registra el historial de clientes atendidos

---

## ⚙️ Funcionalidades

* Ingresar clientes a la cola (con validación de cédula)
* Manejo de prioridades:

  * Prioridad 1 (preferencial)
  * Prioridad 2 (normal)
* Asignación automática de clientes a cajas
* Manejo de 3 cajas (activas o inactivas)
* Finalizar atención de clientes
* Registro de atenciones mediante pilas
* Consultar:

  * Últimas atenciones por caja
  * Últimas atenciones generales
* Reportes:

  * Cantidad de clientes atendidos por prioridad
  * Detalle de clientes atendidos con su trámite
* Visualización de:

  * Cola de clientes
  * Estado de las cajas

---

## 🧠 Estructuras utilizadas

* **Colas:** para manejar los clientes en espera
* **Pilas:** para guardar el historial de atención por cada caja
* **Diccionarios:** para representar las cajas y los clientes

---

## ▶️ Cómo ejecutar

1. Tener Python instalado
2. Ejecutar el archivo en consola:

```
python nombre_del_archivo.py
```

3. Usar el menú interactivo para probar el sistema

---

## 📝 Notas

* No se permiten cédulas repetidas en la cola
* Las cajas pueden activarse o desactivarse
* Los clientes con prioridad 1 siempre se atienden primero

---

## 👩‍💻 Autor

Proyecto realizado por una estudiante de informática como parte de la asignatura de Desarrollo Web.
