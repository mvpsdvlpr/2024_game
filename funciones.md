
### Archivo `main.py`

El archivo `main.py` es el punto de entrada principal para el juego. Aquí se encuentra la lógica principal y la interfaz de usuario. Veamos en detalle:

1. **Función `draw_grid(window)`**:
    - Dibuja una cuadrícula en la ventana de Pygame proporcionada.
    - Parámetros:
        - `window`: La ventana de Pygame donde se dibujará la cuadrícula.

2. **Función `draw(window, tiles)`**:
    - Dibuja los mosaicos en la ventana de Pygame.
    - Parámetros:
        - `window`: La ventana de Pygame.
        - `tiles`: Una lista de objetos `Tile` que representan los mosaicos.

3. **Función `get_random_pos(tiles)`**:
    - Devuelve una posición aleatoria en la cuadrícula que no está ocupada por un mosaico existente.
    - Parámetros:
        - `tiles`: Lista de mosaicos existentes.

4. **Función `move_tiles(window, tiles, clock, direction)`**:
    - Maneja el movimiento de los mosaicos en la dirección especificada (arriba, abajo, izquierda o derecha).
    - Parámetros:
        - `window`: La ventana de Pygame.
        - `tiles`: Lista de mosaicos.
        - `clock`: Reloj de Pygame para controlar la velocidad de movimiento.
        - `direction`: Dirección del movimiento (por ejemplo, "up", "down", "left" o "right").

5. **Función `end_move(tiles)`**:
    - Se llama al final de un movimiento para generar un nuevo mosaico en una posición aleatoria.
    - Parámetros:
        - `tiles`: Lista de mosaicos.

6. **Función `update_tiles(window, tiles, sorted_tiles)`**:
    - Actualiza la posición de los mosaicos después de un movimiento.
    - Parámetros:
        - `window`: La ventana de Pygame.
        - `tiles`: Lista de mosaicos.
        - `sorted_tiles`: Lista ordenada de mosaicos.

7. **Función `generate_tiles()`**:
    - Genera los mosaicos iniciales al comienzo del juego.

8. **Función `main(window)`**:
    - Función principal que coordina todo el juego.
    - Controla la lógica del juego, la entrada del usuario y la actualización de la pantalla.