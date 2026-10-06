## Implementacions implementades

✅ Errors dels pilots ⭐⭐⭐⭐⭐
- Petites errades durant la cursa segons Consistency, Control, Accuracy, etc.
- Poden fer perdre temps sense provocar un abandonament.

✅ Abandonaments ⭐⭐⭐⭐⭐
- Mecànics (fiabilitat del cotxe i de l'equip).
- Errors greus del pilot.
- Accidents entre pilots.

✅ Meteorologia ⭐⭐⭐⭐☆
- Determinar si la cursa és en sec o en mullat.
- Utilitzar la probabilitat de pluja del circuit.
- Fer servir Wet Skill del pilot i modificar el rendiment dels cotxes.

✅ Safety Car / Virtual Safety Car ⭐⭐⭐☆☆
- Basat en la probabilitat del circuit i els incidents.
- Pot reduir diferències i alterar el desenvolupament de la cursa.

✅ Evolució dels equips ⭐⭐⭐⭐☆
- Els equips milloren o empitjoren lleugerament durant la temporada segons Development Rate.
- Fa que el cotxe no sigui exactament el mateix a la cursa 1 que a la 24.

✅ Calibratge històric de pilots i equips ⭐⭐⭐⭐⭐
- Utilitza les classificacions facilitades de 2024, 2025 i 2026.
- Normalitza els punts respecte del líder de cada temporada.
- Per als pilots, aplica pesos del 65% per al 2026, 25% per al 2025 i 10% per al 2024.
- Per als equips, aplica pesos del 50% per al 2026, 30% per al 2025 i 20% per al 2024.
- La influència històrica és moderada per conservar les especialitats individuals dels pilots.

Per als monoplaces, la classificació de constructors utilitza una ponderació més centrada en l'estat actual:

- 2026: 90%
- 2025: 7.5%
- 2024: 2.5%


## Millores de rendiment pendents de implementar

### 1) Precomputar puntuacions per circuit i clima ⭐⭐⭐⭐⭐
- Calcular el rendiment base del pilot, cotxe i equip per circuit i condicions meteorològiques abans de la cursa.
- Impacte: molt alt.
- Per què: evita repetir càlculs que no canvien entre temporades ni entre pilots del mateix equip.
- Àmbit principal: `src/simulation/race.py` i `src/models/entry.py`.

### 2) Reduir la sobrecàrrega de tuples i diccionaris temporals ⭐⭐⭐⭐☆
- Substituir estructures com `(driver, score, team)` o `{"weather": ..., "retirements": ...}` per representacions més compactes.
- Impacte: alt.
- Per què: les llistes i dicts intermedis s’allocan molt sovint a cada cursa.
- Àmbit principal: bucles interns de la simulació de cursa i la classificació.

### 3) Optimitzar la generació aleatòria i el consum de `random` ⭐⭐⭐⭐☆
- Crear un `random.Random` per worker o per temporada per reduir la sobrecàrrega de crides globals.
- Impacte: alt.
- Per què: la simulació genera moltes variables aleatòries per pilot i per cursa.
- Àmbit principal: `src/simulation/race.py` i `main_montecarlo.py`.

### 4) Agregació numèrica directa per Monte Carlo ⭐⭐⭐⭐☆
- Acumular els resultats de cada temporada en arrays o estructures planes en lloc de crear `driver_stats` complets.
- Impacte: alt.
- Per què: reduïx la serialització i el cost de processament del procés principal.
- Àmbit principal: `main_montecarlo.py`.

### 5) Ajustar la mida i l’estratègia dels chunks de workers ⭐⭐⭐⭐☆
- Optimitzar `batch_count`, mides de lot i ordre de processament per adaptar-se millor a la CPU.
- Impacte: mitjà-alt.
- Per què: el rendiment depèn molt de com es reparteixen les temporades entre workers.
- Àmbit principal: `main_montecarlo.py`.

### 6) Eliminar checks repetits dins del bucle de cursa ⭐⭐⭐☆☆
- Replace condicions com `if isinstance(forms, dict)` o `if keep_details` amb una estructura homogènia i preparada per a aquesta ruta.
- Impacte: mitjà.
- Per què: els checks repetits passen per cada pilot i cada cursa.
- Àmbit principal: `src/simulation/race.py` i `src/simulation/season.py`.

### 7) Reduir treball intermediat a la qualificació ⭐⭐⭐☆☆
- Minimitzar la creació de sublistes i còpies durant Q1, Q2 i Q3.
- Impacte: mitjà.
- Per què: la qualificació fa diverses passades i és una part costosa del flux total.
- Àmbit principal: `src/simulation/qualifying.py`.

### 8) Separar flux de simulació esportiva i flux estadístic ⭐⭐⭐☆☆
- Crear un mode de simulació “purament esportiva” i un altre “estadístic / Monte Carlo” amb menys objectes intermedis.
- Impacte: mitjà.
- Per què: permet mantenir el detall complet per la UI i reduir la feina per a les simulacions massives.
- Àmbit principal: arquitectura global del projecte.

### 9) Reducir la pressió de memòria i del garbage collector ⭐⭐⭐☆☆
- Reutilitzar buffers temporals i evitar crear objectes innecessaris en la ruta ràpida.
- Impacte: mitjà.
- Per què: les simulacions massives generen molta allocació i la GC pot arribar a penalitzar.
- Àmbit principal: tota la simulació de temporada.

### 10) Vectorització amb NumPy o arrays de lots ⭐⭐⭐☆☆
- Representar els pilots i els resultats com a vectors numèrics per fer la simulació per lots.
- Impacte: molt alt en els casos grans.
- Per què: és el salt de rendiment més gran, però també el més gran canvi d’arquitectura.
- Àmbit principal: refactorització global del motor.

Potser baixar una mica tots els de dalt des de antonelli a piastri


git status
git add .
git diff --cached --check
git commit -m "Add F1 simulator and Monte Carlo season simulation"
git status

git add README.md Roadmap.md main.py main_montecarlo.py src tests .gitignore
git commit -m "Add F1 simulator and Monte Carlo season simulation"