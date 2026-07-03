## Optimitzacions de rendiment (Roadmap)

☐ Cache dels rendiments constants ⭐⭐⭐⭐⭐
- Guardar el rendiment base de pilots, equips i cotxes (per circuit) en lloc de recalcular-lo a cada cursa.
- Impacte: molt alt.
- Implementació: quan la lògica del simulador estigui pràcticament definitiva.

☐ Reutilitzar objectes de temporada ⭐⭐⭐⭐☆
- Evitar crear nous DriverSeason, TeamSeason i Championship a cada simulació; reinicialitzar els existents.
- Impacte: alt (menys creació d'objectes i menys treball del garbage collector).
- Implementació: després de tenir el simulador complet.

☐ Evitar crear diccionaris repetidament ⭐⭐⭐⭐☆
- Construir els lookup de pilots i equips una sola vegada i reutilitzar-los durant totes les simulacions.
- Impacte: mitjà-alt.
- Implementació: juntament amb la resta d'optimitzacions internes.

☐ Utilitzar índexs en comptes de noms ⭐⭐⭐☆☆
- Substituir diccionaris amb claus de tipus string per llistes indexades (0-21 per als pilots, 0-10 per als equips).
- Impacte: mitjà.
- Implementació: només si es busca el màxim rendiment; no és prioritari.

☐ Precalcular el rendiment base de cada Entry ⭐⭐⭐⭐⭐
- Cada Entry tindrà un rendiment base (pilot + equip) i, si és possible, el rendiment del cotxe per a cada circuit ja calculat.
- Durant la cursa només s'afegiran els modificadors (forma, aleatorietat, pluja, etc.).
- Impacte: molt alt.
- Implementació: quan la fórmula definitiva del rendiment estigui tancada.

☐ Paral·lelitzar les simulacions Monte Carlo ⭐⭐⭐⭐⭐
- Executar diferents temporades simultàniament aprofitant tots els nuclis del processador (multiprocessing).
- Impacte: enorme (pot reduir el temps diverses vegades segons la CPU).
- Implementació: últim pas del projecte, quan tot el simulador estigui acabat i estable.

fer diverses funci0ns per calcular la performance és a dir separar-ho en:

calculate_driver_qualifying()
calculate_driver_race()
calculate_driver_wet()

en comptes de 
calculate_driver_performance()


implementacions a fer:

☐ Simulació de classificació ⭐⭐⭐⭐⭐
- Simular la sessió de classificació abans de la cursa.
- Utilitzar principalment Qualifying Pace, però també cotxe, equip i forma.
- La posició de sortida influirà en el resultat de la cursa.

☐ Avantatge de la posició de sortida ⭐⭐⭐⭐☆
- Sortir davant ha de donar una petita probabilitat extra d'obtenir un bon resultat.
- Especialment important en circuits com Mònaco o Singapur.

☐ Errors dels pilots ⭐⭐⭐⭐⭐
- Petites errades durant la cursa segons Consistency, Control, Accuracy, etc.
- Poden fer perdre temps sense provocar un abandonament.

☐ Abandonaments ⭐⭐⭐⭐⭐
- Mecànics (fiabilitat del cotxe i de l'equip).
- Errors greus del pilot.
- Accidents entre pilots.

☐ Meteorologia ⭐⭐⭐⭐☆
- Determinar si la cursa és en sec o en mullat.
- Utilitzar la probabilitat de pluja del circuit.
- Fer servir Wet Skill del pilot i modificar el rendiment dels cotxes.

☐ Safety Car / Virtual Safety Car ⭐⭐⭐☆☆
- Basat en la probabilitat del circuit i els incidents.
- Pot reduir diferències i alterar el desenvolupament de la cursa.

☐ Evolució dels equips ⭐⭐⭐⭐☆
- Els equips milloren o empitjoren lleugerament durant la temporada segons Development Rate.
- Fa que el cotxe no sigui exactament el mateix a la cursa 1 que a la 24.