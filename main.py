import re
from random import randint


def rpg_dice_throw(code: str):
    possible_sides = [3, 4, 6, 8, 10, 12, 20, 100]

    dice_pattern = re.compile(r"(\d)*[dD](\d+)([+-]\d)*")

    match = dice_pattern.search(code)
    if not match:
        return 'Invalid dice pattern'

    throws, sides, modifier = match.groups()
    throws = 1 if not throws else int(throws)
    sides = int(sides)

    if sides not in possible_sides:
        return 'Invalid dice pattern'
    return eval(f'{sum(randint(1, sides) for _ in range(throws))} {modifier}')
