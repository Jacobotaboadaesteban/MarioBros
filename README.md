# Mario Bros

Un juego de plataformas inspirado en *Mario Bros*, creado en Python con [Pyxel](https://github.com/kitao/pyxel). Mario puede moverse por las plataformas, saltar, recoger monedas y enfrentarse a tortugas, cangrejos y moscas.

## Requisitos

- Python 3.9 o posterior.
- Pyxel 1.9.18 (versión usada en este proyecto).

Instala Pyxel si todavía no está instalado:

```bash
python -m pip install pyxel==1.9.18
```

## Ejecutar

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python main.py
```

En Windows, si quieres usar el entorno virtual incluido en el proyecto:

```powershell
.\venv\Scripts\python.exe main.py
```

Ejecuta el comando desde la carpeta del proyecto: el juego carga los gráficos y sonidos desde `assets/resources.pyxres` con una ruta relativa.

## Controles

| Tecla | Acción |
| --- | --- |
| Flecha izquierda | Mover a la izquierda |
| Flecha derecha | Mover a la derecha |
| Flecha arriba o espacio | Saltar |
| Q | Salir del juego |

## Archivos principales

- `main.py`: inicia el juego.
- `tablero.py`: crea el escenario y gestiona el bucle, las colisiones, los enemigos y la puntuación.
- `mario.py`: movimiento, salto y vidas de Mario.
- `turtle.py`, `crab.py`, `flies.py`: comportamiento de los enemigos.
- `coins.py`, `pow.py`: monedas y bloque POW.
- `assets/resources.pyxres`: recursos gráficos y de audio de Pyxel.
