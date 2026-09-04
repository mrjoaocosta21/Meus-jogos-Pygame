# Corrida de Algoritmos de Ordenação

Visualização em `pygame` onde vários algoritmos de ordenação recebem a
**mesma lista embaralhada** e correm ao vivo, lado a lado, para ver
qual termina primeiro — ideia baseada no vídeo
["Fiz algoritmos de ordenação competirem entre si."](https://www.youtube.com/watch?v=N4JVT3eVBP8)

## Arquivos

- `race.py` — arquivo principal. Roda a janela, o loop da corrida e o ranking.
- `sorting.py` — os algoritmos de ordenação, implementados como *generators*
  (cada `yield` é um passo/comparação, o que permite animar).
- `canvas.py` — desenho dos painéis (barras, destaques, texto).

## Requisitos

- Python 3.8+
- `pygame`

## Como instalar

Abra um terminal na pasta onde estão os 3 arquivos e rode:

```bash
pip install pygame
```

Se o seu sistema pedir (ex: Linux com Python gerenciado externamente):

```bash
pip install pygame --break-system-packages
```

## Como rodar

```bash
python3 race.py
```

Uma janela vai abrir com um painel por algoritmo, cada um ordenando sua
própria cópia da lista.

## Controles

| Tecla     | Ação                                              |
|-----------|---------------------------------------------------|
| `ESPAÇO`  | Pausa / retoma a corrida                           |
| `R`       | Reinicia com uma nova lista aleatória              |
| `1` – `9` | Ajusta quantos passos cada algoritmo dá por frame (velocidade) |
| `ESC`     | Fecha o programa                                   |

## Algoritmos incluídos na corrida

- Bubble Sort
- Insertion Sort
- Merge Sort
- Cocktail Shaker Sort
- Bucket Sort

`Bogo Sort` também está implementado em `sorting.py`, mas fica de fora
da corrida por padrão — com mais de ~7 elementos ele pode nunca
terminar em tempo razoável. Para testá-lo, edite `race.py` e remova o
filtro em `RACE_ALGORITHMS`.

## Ajustando a corrida

No topo de `race.py`:

```python
DATA_LENGTH = 60        # quantidade de elementos em cada lista
WINDOW_W, WINDOW_H = 1200, 800   # tamanho da janela
STEPS_PER_FRAME = 2     # velocidade inicial
```

Mude esses valores para listas maiores/menores, janelas diferentes ou
uma corrida mais rápida/lenta.