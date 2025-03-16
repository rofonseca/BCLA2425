# BCLA2425

Este repositorio contiene herramientas y análisis de datos relacionados con la Basketball Champions League Americas (BCLA). Aquí se recopilan, procesan y visualizan estadísticas de los partidos, jugadores y equipos.


# Four factors of basketball success
- Shooting (40%)
- Turnovers (25%)
- Rebounding (20%)
- Free Throws (15%)

Los tiros son el factor más importante, seguido por las pérdidas de balon, los rebotes y los tiros libres. Estos factores se pueden aplicar tanto a la ofensiva como a la defensa de un equipo, lo que en cierto sentido nos da ocho factores.

## Shooting
El factor de tiro (shooting) se mide usando el porcentaje de tiros de campo efectivos (eFG%)
La fórmula tanto para la ofensiva como para la defensiva es : (FG+0.5*3P)/FGA

- FG = tiros de campo (incluye tanto tiros de 2 puntos como de 3 puntos) - CONVERTIDOS
- 3P = tiros de 3 puntos convertidos
- FGA = tiros de campo intentados (incluye tanto tiros de 2 puntos como de 3 puntos intentados)

## Turnovers
El factor de pérdidas (turnover) se mire utilizando el porcentaje de pérdidas (TOV%). La fórmula tanto para la ofensiva como para la defensiva es: TOV/(FGA+0.44*FTA+TOV)

- TOV = pérdidas
- FTA = tiros libres intentados

## Rebounding

El factor de rebotes (rebounding) se mide utilizando el porcentaje de rebote ofensivo y defensivo (ORB% y DRB% respectivamente). La fórmula para el ataque es: ORB/(ORB+DRB del oponente)

mientras que la fórmula para la defensa es: DRB/(ORB del oponente + DRB)

- ORB = rebores defensivos
- DRB = rebotes defensivos

## Free Throws
El factor de tiros libres es una medida de la frecuencia con la que un equipo llega a la linea y la frecuencia con la que anota. La fórmula tanto para la ofensiva como para la defensiva es: FT/FGA

- FT = tiros libres - ACERTADOS

# Glosario

- FT: Tiros libres tirados o intentados
- FTA: Tiros libres acertados o convertidos
- 2P:
- 2PA:
- 3P:
- 3PA:
- FG: tiros de campo (incluye tanto tiros de 2 puntos como de 3 puntos)
- FGA: tiros de campo (incluye tanto tiros de 2 puntos como de 3 puntos) acertados o convertidos
- ORB : rebores defensivos
- DRB : rebotes defensivos
- REB : rebotes incluye ofensivos y defensivos
- AST: asistencias
- FP: Faltas personales
- TOV: Pérdidas
- ROB: recupero o robo de la pelota
- TAP: Tapas o bloqueos realizados


Los Four Factors son un conjunto de métricas clave que ayudan a entender el rendimiento de un equipo de baloncesto y cómo influyen en el resultado de los partidos. Los cuatro factores son:

Eficiencia de campo (eFG%): Este factor ajusta el porcentaje de tiros de campo para tener en cuenta el valor adicional de los triples. Los equipos con una alta eFG% tienden a ser más eficientes en la ofensiva.

Ratio de rebotes (REB%): Este mide la capacidad de un equipo para capturar rebotes ofensivos y defensivos. Un alto porcentaje de rebotes generalmente significa que un equipo puede tener más oportunidades de anotar o evitar que su oponente anote.

Ratio de pérdidas (TOV%): Este factor se refiere a la cantidad de veces que un equipo pierde el balón. Un bajo porcentaje de pérdidas es positivo porque significa que el equipo está tomando buenas decisiones y controlando el balón.

Ratio de faltas (FT%): Este factor mide la capacidad de un equipo para capitalizar en la línea de tiros libres, tanto en términos de frecuencia como de efectividad. Los equipos que tienen una alta tasa de tiros libres suelen tener una ventaja, ya que suman puntos con pocas oportunidades de tiempo.