input_file = "day2/input_day_2.1.txt"
with open(input_file, "r") as file:
    lines = file.readlines()

def split_line(line):
    return line.split(":")

GREEN = "green"
RED = "red"
BLUE = "blue"

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def parse_draw(draw_text: str):
    draws = draw_text.split(",")
    outcome = {
        GREEN : 0,
        RED : 0,
        BLUE : 0,
    }
    for draw in draws:
        number, color = draw.strip().split(" ")
        outcome[color] = int(number)
    return outcome

def validate_outcome(outcome):
    return (outcome[GREEN]<= MAX_GREEN) and (outcome[RED]<= MAX_RED) and (outcome[BLUE]<= MAX_BLUE)

def validate_game(game_text: str):
    draws = game_text.split(";")
    for draw in draws:
        if not validate_outcome(parse_draw(draw)):
            return False
    return True

sum = 0
for line in lines:
    game_id_text, game_text = split_line(line)
    if validate_game(game_text):
        sum += int(game_id_text.split(" ")[-1])

print(sum)
    
