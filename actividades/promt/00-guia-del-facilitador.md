# Módulo 2 · Guía del facilitador

Insumos para `modulo2-laboratorio-prompts.html`. Este archivo es **solo para quien
dicta**: revela dónde está plantado el defecto de cada insumo.

---

## Qué se reparte y cuándo

| # | Insumo | Lámina / momento | Cómo se reparte |
|---|---|---|---|
| 01 | `01-rescate-de-prompts.md` | Reto 1 · Rescate de prompts | Impreso, **una por pareja** |
| 02 | `02-transcripcion-reunion.txt` | Reto 1 · caso 02 (Acta) | Digital, para pegar en el chat |
| 03 | `03-ventas-por-sucursal.md` / `.csv` | Reto 1 · caso 04 (Informe) | Digital. El `.md` se pega; el `.csv` es por si alguien quiere abrirlo en Excel |
| 04 | `04-asuntos-de-correo.txt` | Reto 5 · Estación A | Digital |
| 05 | `05-notas-de-bodega.txt` | Reto 5 · Estación D | Digital |
| 06 | `06-proveedores.md` | Reto 4 · Paso a paso | Digital |
| 07 | `07-anonimizar.md` | Lámina «Qué no se sube a la IA» | Impreso o digital |
| 08 | `08-verificacion.md` | Lámina «Verificar no se delega» | **Solo la Parte 1.** La Parte 2 es la hoja de respuestas |
| 09 | `09-reglamento-de-respaldo.md` | Reto 6 · Documentos propios | Digital, **solo para quien no traiga documento**. La nota final no se reparte |
| 10 | `10-hoja-para-fotografiar.html` | Lámina «Foto a dato» | Proyectado o impreso, para fotografiar con el celular |
| 11 | `11-duelo-de-ias-planilla.md` | Reto 2 · Duelo de IAs | Impreso, **una por participante** |
| 12 | `12-kit-entregable.md` | Proyecto final | Digital, es el formato del entregable |
| 13 | `13-mensaje-cliente-molesto.txt` | Lámina «restricciones» (cliente molesto) | Digital, para pegar en el chat |
| 14 | `14-texto-para-corregir.txt` | Lámina «tarea en dos pasos» (corrección) | Digital, para pegar en el chat |

**Lo único que hay que imprimir:** 01, 11 y, si quiere, 10. Todo lo demás se
comparte por el canal del diplomado.

> **Nota sobre el deck.** Desde la lámina 7, `modulo2.html` lleva el texto de cada
> insumo **dentro de la propia lámina**, con botón «Copiar». Los archivos de esta
> carpeta siguen siendo la versión imprimible y la que se comparte por el canal,
> pero en clase no hace falta abrirlos: basta con proyectar la lámina.

---

## Lo que hay que anunciar antes de empezar

- Traer **dos tareas reales del trabajo**.
- Cuentas activas en **dos herramientas de IA** distintas. Para el Reto 2 hacen
  falta tres, pero se puede trabajar en parejas para cubrir la tercera.
- Traer un **documento propio** (manual, reglamento, informe) anonimizado para el
  Reto 6. Quien no lo traiga usa el insumo 09.
- El Reto 7 es en **modo voz**: hacen falta audífonos o salir de la sala.

---

## Los defectos plantados, uno por uno

Cada insumo tiene algo mal a propósito. Ahí es donde el reto enseña. **No los
anticipe**: si el grupo los encuentra, el ejercicio funcionó; si no, el hallazgo
lo pone usted al cerrar.

**02 · Transcripción.** Dos compromisos quedan sin responsable nombrado («que
alguien lo mire» para el costo de parada, «alguien tiene que llevarlo a jurídica»
para el acuerdo con el proveedor). Un tema queda **sin decisión**: la elección del
proveedor de empaque. Y hay un dato que Marcela pide y nadie tiene (cuántos
pedidos salieron en total). El prompt dice «si no aparece el nombre, escribe *sin
asignar*»: eso es lo que se va a poner a prueba.

**03 · Ventas.** Abril de Occidente está vacío. Norte se desploma desde mayo sin
explicación en los datos. Aeropuerto tiene dos picos sueltos que invitan a narrar
de más. Detalle en el propio insumo.

**04 · Asuntos de correo.** De los 20, unos seis son frontera y dependen del
criterio, no del asunto: la auditoría con hora límite, la póliza que vence en
3 días, el cliente que amenaza con cancelar, el «RV: RV: RV:», las vacaciones
represadas hace 8 días, y el «URGENTE URGENTE» en mayúsculas que **no** es urgente.
Ese último es el bueno: los ejemplos del prompt no cubren el caso de alguien que
grita. Si dos participantes clasifican distinto y ambos pueden defenderlo, el
ejercicio está funcionando: el criterio es propio y por eso se enseña con
ejemplos, no con definiciones.

**05 · Notas de bodega.** Cantidades vagas («como 20, creo», «40 y algo»,
«bastante»), un ítem del que se pregunta si llegó y no se sabe, una fecha que el
proveedor no confirmó, y una calibración sin fecha de inicio. El prompt dice «si
un dato no está, escribe *sin dato*: no lo completes por lógica». La trampa
grande son las grapas: no dice cuántas hay porque **no quedan**, y muchos modelos
escriben 0 —que es correcto por deducción, pero es deducción.

**06 · Proveedores.** El más barato pierde al ponderar. Hay dos casillas «sin
información» para ver si el modelo declara el vacío o inventa un puntaje. Y el
costo total del año no está calculado: 240.000 unidades × precio unitario. Si
compara precios unitarios sin multiplicar, se saltó justo el paso intermedio que
el reto quiere hacer visible.

**07 · Anonimizar.** El párrafo del ejercicio incluye una incapacidad médica, que
es dato sensible: **no se sustituye, se saca**. Casi siempre alguien la deja
dentro «anonimizada». Y aunque se anonimice todo, dentro de esa empresa se sigue
sabiendo de quién se habla: esa es la conclusión.

**08 · Verificación.** Tres de las cinco afirmaciones son falsas. La 2 se puede
desmontar **sin internet**, solo con aritmética. **Antes de la clase, confirme
usted los datos 3 y 4 en la fuente original**: si ya cambiaron, dígalo — es la
mejor demostración posible de por qué se verifica.

**09 · Reglamento.** Contradicción entre los artículos 7 y 21 (tres días contra
dos, para lo mismo, separados por catorce artículos). Plazo ambiguo en el
artículo 8 («oportunamente»). Paso sin responsable en el artículo 20. Y un vacío:
qué pasa con los permisos e incapacidades del personal temporal.

**13 · Mensaje del cliente.** Son tres mensajes del mismo cliente y el tono sube en
cada uno. El tercero exige **una hora exacta de restablecimiento**, que es justo lo
que el prompt prohíbe prometer: ahí se ve si la restricción funcionó o si el modelo
cedió para sonar satisfactorio. Además, en el segundo mensaje el cliente da su
cédula sin que nadie se la pida: sirve para volver sobre la lámina de privacidad
—ese dato no hace falta para redactar la respuesta y no debería viajar al chat—.
Y la factura llegó completa: casi nadie lo menciona en la respuesta, aunque es el
reclamo más concreto de los tres.

**14 · Texto para corregir.** Defectos reales y de distinto tipo: tildes faltantes
en todo el texto, una primera frase de seis líneas sin un solo punto, dos siglas sin
explicar (TH y TI) que en el comité fueron talento humano y sistemas —o sea que una
está mal—, una cifra vaga («como once pedidos, más o menos un diez por ciento») y un
cierre que repite la misma idea dos veces («creemos que vale la pena / creemos que va
a valer la pena»). El prompt pide conservar la voz del autor: el texto es
deliberadamente cercano y hablado, así que si vuelve convertido en comunicado
corporativo impecable, la instrucción se perdió. Esa es la discusión.

**10 · Hoja para fotografiar.** En el recibo, el valor borroso de la extensión se
puede **deducir por resta** porque el subtotal sí cuadra: es la inferencia
razonable que el prompt prohíbe. En el tablero, la nota «centro de costo de los
temporales: ¿cuál?» no es tarea ni idea, y suele salir clasificada como tarea con
responsable inventado.

---

## Dos cosas que conviene decir en voz alta

**Al empezar, en la lámina de privacidad:** que el material de los insumos es
ficticio precisamente para que puedan trabajar sin exponer nada. Cuando pasen a
sus propias tareas, la regla aplica.

**Al cerrar, después del proyecto final:** el kit no es la meta. La meta es la
separación entre lo que es fijo en una tarea (rol, formato, restricciones) y lo
que cambia cada semana (los corchetes). Eso es lo que se automatiza en el módulo
3, y por eso el entregable exige que las plantillas estén **probadas**, no solo
escritas.
