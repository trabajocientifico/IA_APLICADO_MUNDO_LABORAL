# Insumo 06 · Tres proveedores de empaque

**Se usa en:** Reto 4 (paso a paso).
**Cómo se usa:** se pega la tabla y los criterios debajo del prompt A, y después
debajo del prompt B, en conversaciones separadas. Se comparan las dos respuestas.

---

## El caso

Distribuidora Andina necesita un proveedor de empaque para el próximo año. El
consumo estimado es de 240.000 unidades. Hay tres cotizaciones.

| | Empaques del Valle | Cartonera Pacífico | Soluciones Embalar |
|---|---|---|---|
| Precio por unidad | $1.180 | $1.290 | $1.355 |
| Plazo de entrega | 20 días | 12 días | 8 días |
| Pedido mínimo | 50.000 unidades | 20.000 unidades | 10.000 unidades |
| Garantía por defectos | Sin garantía escrita | Reposición en 30 días | Reposición en 15 días |
| Años en el mercado | 3 | 14 | 9 |
| Certificación de calidad | No tiene | ISO 9001 | ISO 9001 + FSC |
| Clientes de referencia | 1, no contesta el teléfono | 3 verificadas | 2 verificadas |
| Forma de pago | 100% anticipado | 50/50 | 30 días después de entrega |
| Incumplimientos reportados | Sin información | 1 en los últimos 2 años | Sin información |

## Criterios y pesos

| Criterio | Peso |
|---|---|
| Costo total del año | 30 % |
| Confiabilidad de entrega (plazo + incumplimientos) | 25 % |
| Calidad y garantía | 20 % |
| Flexibilidad (pedido mínimo + forma de pago) | 15 % |
| Trayectoria y referencias | 10 % |

---

## Nota para quien prepara la clase

- **El más barato pierde al ponderar.** Empaques del Valle gana el 30 % del
  costo, pero se cae en los otros cuatro criterios, que suman 70 %. Cuando se
  pide «dime cuál contrato» sin más, el modelo tiende a irse por el precio o por
  la opción del medio, y luego construye una justificación convincente.
- **Hay dos casillas «sin información» a propósito.** El prompt B dice «si te
  falta algún dato para puntuar un criterio, dilo en vez de estimarlo». Sirve
  para ver si el modelo declara el vacío o le inventa un puntaje.
- **El costo total del año no está calculado.** 240.000 unidades × precio
  unitario: $283,2 / $309,6 / $325,2 millones. Si el modelo no hace la
  multiplicación y compara solo precios unitarios, se lo señala: es exactamente
  el paso intermedio que el prompt A se salta.
- **La pregunta de cierre del reto:** ¿cambió la recomendación entre A y B, o
  cambió solo la explicación? Las dos respuestas son interesantes.
