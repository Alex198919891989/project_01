def n(number: int) -> str:
    match number:
        case 1:
            return "один"
        case 2:
            return "два"
        case 3:
            return "три"
        case 4:
            return "четыре"
        case 5:
            return "пять"
        case 6:
            return "шесть"
        case 7:
            return "семь"
        case 8:
            return "восемь"
        case 9:
            return "девять"
        case 0:
            return "ноль"
        case _:
            return "Error"
print(n(int(input())))