# uego de 2048 con Pygame


## Tiles
### Archivo `tile.py`

El archivo `tile.py` contiene la definición de la clase `Tile`, que representa un mosaico en el juego. Cada mosaico tiene un valor y un color asociado. A continuación, se describen las funciones y la clase en detalle:

Esta clase representa una ficha en la cuadrícula del juego **2048**. Cada ficha tiene un valor, una posición (fila y columna) y coordenadas (x e y) en la pantalla del juego.

## Atributos:
- `value` (int): El valor de la ficha (por ejemplo, 2, 4, 8, etc.).
- `row` (int): El índice de fila de la ficha en la cuadrícula.
- `col` (int): El índice de columna de la ficha en la cuadrícula.
- `x` (int): La coordenada x de la esquina superior izquierda de la ficha en la pantalla del juego.
- `y` (int): La coordenada y de la esquina superior izquierda de la ficha en la pantalla del juego.

## Métodos:
- `get_color()`: Devuelve el color asociado al valor de la ficha. El color se determina según el logaritmo del valor de la ficha.
- `draw(window)`: Dibuja la ficha en la pantalla del juego utilizando la ventana especificada. Rellena un rectángulo con el color de la ficha y muestra el valor en el centro.
- `move(delta)`: Mueve la ficha según el delta especificado (cambio en las coordenadas x e y). Útil para animaciones o transiciones.
- `set_pos(ceil=False)`: Establece los índices de fila y columna según las coordenadas x e y actuales. Si `ceil` es True, redondea hacia arriba; de lo contrario, redondea hacia abajo.

## Constantes:
- `COLORS` (lista de tuplas): Una lista de valores RGB correspondientes a diferentes valores de ficha. Estos colores se utilizan para dibujar las fichas.

## Ejemplo de uso:
```python
tile = Tile(4, 1, 2)
tile.draw(ventana_juego)
tile.move((10, 0))
tile.set_pos(ceil=True)