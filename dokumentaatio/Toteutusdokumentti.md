# Toetutusdokumentti

Projektissa on toteutettu 3 eri reitinetsintä algoritmia. Pääpainona on onnlut Fringe search algoritmi jota vertaillaa a* algoritmiin. Dijkstra on tullut ns. vahingossa mukaan ja implementoitu antamalla a_star algoritmin heureettiseksi funktioksi 0.

## Ohjelman rakenne

```text
    └── src                    
        ├── index.py
        ├── functions
        |   ├── fringe_search.py
        |   ├── a_star.py
        |   ├── height_mapping_function.py
        |   └── heurestic_function.py
        |
        ├──objects
        |   ├── node.py
        |   └── doubly_linked_list.py
        |
        ├──services
        |   ├── algorithm_handler.py
        |   └── running_service.py
        |
        ├── map_generation
        |   ├── get_shape.py
        |   ├── shape_functions.py
        |   ├── node_list_generator.py
        |   ├── translator.py
        |   ├── two_d_translator.py
        |   └── maps
        |       └── ...
        |   
        └── drawing_functions
            ├── draw_path.py
            ├── draw_pointmap.py
            └── draw_plots.py
            

```

## File docstring

### index.py

- index runs the program
- Combines all the other methods and classes and executes them in the right order etc.

### functions

- Holds the neccessary functions for execution of the algorithms.
- a_star.py and fringe_search.py are those algorithms respectively.
- heurestic.py and two_d_heurestic.py hold heurestic functions for 3d and 2d navigation.
- height_mapping.py holds height mapping function for 3d maps.

### Objects

- Holds the neccessary objects for execution of the algorithms.
- node.py and two_d_node.py hold node objects for 3d and 2d maps.
- doubly_linked_list.py holds doubly linked list object that has the following cabibilities.
  * Check if object in list in O(0) time.
  * Remove object from list in O(0) time.
  * Remove current object in O(0) time.
  * iterate 
  * get current

### Services

- algorithm handler holds a single method. It's a middleman in running the algorithms from index.
  - calls drawing functions and prints everything to console.
- running_service.py holds a class that is the boundary layer between UI and the rest of the program.

### Map generation

- get_shape has a function that given a function f(x, y) = z generates a map of given dataresolutioin and data range.
- shape_functions holds multiple functions intended for use with get_shape. Most of them are there for ns. storage. The one that is usesd is layered_noise.
- node_list_generator.py holds a method that takes in either a 2d or 3d raw map and converts it to node_lists. 
- tranlators (translator.py and two_d_translator.py) hold functions that take in nodelist an algorithm parameters then translates parameters like start, goal and path between node_list and actual cordinates.
- maps is a directory holding multiple movingai maps and their solutions. Only one is used, but the rest are there for possible further implementation.

### Drawing functions

  - holds 3 functions responsible for the visuals

## Algoritmejen suoritus

```mermaid
sequenceDiagram title Algoritmin suoritus UI:n kautta 3d kartassa
  actor Käyttäjä
  participant UI
  participant app_service
  participant get_shape
  participant node_list_generator
  participant algorithm_handler
  participant translator
  participant algorithm
  participant drawing_funcs
  Käyttäjä->>UI: click "Start" button
  UI->> app_service: execute()
  app_service->>get_shape:get_shape(layered_noise(args))
  get_shape->>app_service:grid
  app_service->>node_list_generator:node_list_generator(grid, False)
  node_list_generator->>app_service:node_list
  app_service->>drawing_funcs:draw a plain
  app_service->>algorithm_handler:algorithm_handler(start, goal, node_list, args)
  algorithm_handler->>translator:translator(start, goal, node_list, args)
  translator->>translator:Translates goal and start
  translator->>algorithm:algorithm(args)
  algorithm->>translator:results
  translator->>translator:translates path, measures time
  translator->>algorithm_handler: results + time
  algorithm_handler->>Käyttäjä:prints relevant results
  algorithm_handler->>drawing_funcs: adds algorithm output to plain
  app_service->>Käyttäjä:Shows all drawings.

```

Ylläoleva taulukko on tarkoitettu antamaan lukija yleiskuva miten algoritmin suoritus toimii UI:n kautta 3d kartassa. Siitä puuttuu  hieman  nuanssia.

## Aikavaatimukset

**A starin** aikavaatimus on huonoimmassa tapauksessa $$O\left(b^d\right)$$ missä d on lyhin reitti ja b on noden lapsien keskiarvoinen määrä.

**Dijkstran** aikavaatimus on tässä tapauksessa 
$$O\left(V+E\log V\right)$$

**Fringe searchin** aikavaatimuksesta oli hanka löytää resursseja. Kotikeittonen fringe search on noin 7.5 kertaa hitaampi kuin a star, mutta [kirjallisuuden](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf) mukaan sen pitäisi olla noin 25 % - 40 % nopeampi.

### Algoritmejen nopeus

Optimointejen jälkeen djikstra on noin kolme kertaa hitaampi kuin a star. Fringe search ei pääse oikeuksiinsa pythonissa. Pythonissa on kallista katsoa node[i] listasta ja tämän fringe search tekee eri suuruusluokassa kun a star ja djikstra.

Suorituskykytesti parametreilla
- num_of_maps = 10
- num_of_runs_per_map = 25
- data_resolution = 75

Mitattiin tulokset l
- fringe_search_time: 429.8073649406433 s
- dijkstra_time: 88.70072555541992 s
- a_star_time: 27.70150637626648 s

Mittasin kyseisessä testissä myös kuinka monessa nodessa a_star ja djikstra kävivät. Tämä korreloi todella hyvin aikojen kanssa
- djikstra 9313970
- a star 2514890

A starin sekä fringe searchin tehokkuutta voisi parantaa kehittämällä paremman heureettisen funktion. Miten tämä pitäisi toteuttaa on vaikea sanoa. Tällä hetkellä heureettinen funktion on eukleedinen pituus pisteestä maaliin.

## Selvitys kielimallien käytöstä

Käytin muutamassa kohdassa kielimalleja ratkaisemaan jonkun tietyn bugin. Muuten en ole käyttänyt kielimalleja.

## Parannusehdotuksia

On selkeää että koko projekti pitäisi kirjoittaa sille sopivammalla / nopeammalla keilellä esim. c++. Sen lisäksi koordinaatisto systeemi pitäisi rakentaa eri tavalla, jotta saataisiin parhaat mahdolliset tulokse. Tätä voi kompensoida genroimalla isompia karttoja, mutta parhaat tulokset saataisiin jos koordinaatit rakennettaisiin korkeuskäyrille. 

Lähteet:

A star [wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)

Dijkstra [hackerearth](https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/#:~:text=Time%20Complexity%20of%20Dijkstra's%20Algorithm,E%20l%20o%20g%20V%20)

Fringe search [University of Alberta](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf)

Tirakirja [Tirakirja](https://github.com/hy-tira/tirakirja/raw/master/tirakirja.pdf)