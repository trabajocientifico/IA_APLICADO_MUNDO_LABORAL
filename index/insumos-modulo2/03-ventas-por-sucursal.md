# Insumo 03 · Ventas mensuales por sucursal

**Se usa en:** Reto 1, prompt 04 (Informe).
**Cómo se usa:** se copia la tabla completa y se pega debajo del prompt reescrito.

Distribuidora Andina S.A.S. — ventas en pesos colombianos, enero a agosto.

| Sucursal | Enero | Febrero | Marzo | Abril | Mayo | Junio | Julio | Agosto |
|---|---|---|---|---|---|---|---|---|
| Centro | 182.400.000 | 175.900.000 | 191.200.000 | 188.700.000 | 193.500.000 | 186.200.000 | 190.800.000 | 195.100.000 |
| Norte | 143.700.000 | 139.800.000 | 151.600.000 | 148.200.000 | 112.400.000 | 87.300.000 | 79.600.000 | 74.100.000 |
| Sur | 98.200.000 | 101.500.000 | 96.800.000 | 103.700.000 | 99.400.000 | 105.200.000 | 108.900.000 | 111.300.000 |
| Occidente | 121.600.000 | 118.300.000 | 124.900.000 | | 127.800.000 | 131.400.000 | 129.700.000 | 134.600.000 |
| Aeropuerto | 67.300.000 | 71.900.000 | 88.400.000 | 69.100.000 | 66.800.000 | 64.200.000 | 63.500.000 | 92.700.000 |

---

## Contexto que el participante puede dar (opcional)

Si quiere darle más material al modelo, puede agregar estos datos al prompt. Todo
lo demás hay que dejarlo sin explicar a propósito.

- La meta mensual por sucursal es de $120.000.000, salvo Centro, que tiene meta de $180.000.000.
- En marzo hubo una campaña nacional de descuentos.
- La sucursal Aeropuerto depende del tráfico de viajeros.

---

## Nota para quien prepara la clase

Esta tabla tiene tres cosas plantadas. No se las anticipe al grupo: la gracia del
ejercicio es que el prompt bien escrito las saque solo.

1. **Abril de Occidente está vacío.** El prompt de referencia dice «señala
   cualquier dato faltante». Un modelo sin esa instrucción suele interpolar un
   valor entre marzo y mayo y presentarlo como si fuera real.
2. **Norte se desploma desde mayo** (de 148 a 74 millones en cuatro meses). Es la
   caída que obliga a formular hipótesis, y ninguna se puede confirmar con estos
   datos: el prompt exige rotularlas como hipótesis, no como hallazgos.
3. **Aeropuerto tiene dos picos sueltos** (marzo y agosto) sin tendencia. Sirve
   para discutir la diferencia entre un patrón y dos datos sueltos, que es donde
   los modelos tienden a narrar de más.
