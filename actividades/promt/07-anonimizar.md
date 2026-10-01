# Insumo 07 · Anonimizar antes de pegar

**Se usa en:** lámina «Qué no se sube a la IA», antes del Reto 1.

---

## Tabla de sustitución

La regla no es borrar: es **sustituir manteniendo la forma**, para que el modelo
siga entendiendo la estructura del texto.

| Dato real | Se reemplaza por | Por qué así |
|---|---|---|
| Nombre de persona | Un nombre genérico consistente: «el cliente», «Persona A» | Si se borra, el modelo pierde el hilo de quién hace qué |
| Cédula / documento | `XX.XXX.XXX` | Nunca hace falta para la tarea |
| NIT o razón social | «Proveedor A», «la empresa contratante» | Identifica a la organización tanto como un nombre propio |
| Correo y teléfono | `correo@ejemplo.com`, `300 000 0000` | Son identificadores directos |
| Dirección exacta | «sede norte», «sucursal principal» | La ciudad casi siempre basta |
| Monto exacto de un contrato | Redondeado o en rango: «cerca de $300 millones» | El orden de magnitud sirve igual para redactar |
| Número de contrato, factura, radicado | `[número de radicado]` | No aporta nada al texto |
| Fechas exactas de hechos sensibles | «hace tres semanas» | Combinadas con un cargo, identifican a la persona |
| Diagnósticos, incapacidades, procesos disciplinarios | No se pegan. Se describe la situación en abstracto | Son datos sensibles: la anonimización no basta |

**Regla de bolsillo:** si un tercero que conozca su sector pudiera reconstruir de
quién se habla juntando dos o tres datos del texto, todavía no está anonimizado.

---

## Ejercicio: anonimice este párrafo

Péguelo primero tal cual **no**: primero reescríbalo, y solo después péguelo en
la IA con el prompt de abajo.

> El señor Hernán Duarte Peláez, cédula 79.412.588, coordinador de la sede de la
> calle 127 con 15, radicó el 14 de marzo la queja 2026-0417 contra su jefe
> directo, Marcela Ospina, por el manejo del contrato 4400-SUM-23 con Distribuidora
> Andina S.A.S. (NIT 900.412.336-1) por valor de $487.320.000. Duarte adjuntó su
> incapacidad médica del 2 al 9 de marzo y pidió que se le responda al correo
> hduarte@empresa.com.co o al celular 315 447 2210.

**Prompt para después de anonimizar:**

```
Actúa como asistente jurídico de una oficina de talento humano. Con el texto de
abajo, redacta un resumen de una página para el comité de convivencia: hechos,
fechas relativas, solicitud concreta y qué información falta para tramitar el
caso. No agregues datos que no estén en el texto.
```

### Para revisar en grupo
- ¿Qué se conservó y qué se sustituyó? ¿El resumen sigue siendo útil?
- El dato de la incapacidad médica es sensible y **no se sustituye: se saca**.
  ¿Quién lo dejó dentro?
- ¿El texto anonimizado todavía permite adivinar de quién se habla dentro de esa
  empresa? Casi siempre sí. Esa es la conclusión del ejercicio: anonimizar no
  vuelve el texto público, solo lo vuelve menos peligroso.
