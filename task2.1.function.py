def get_season(number: int) -> str:
    match number:
        case 1 | 2 | 3:
            return "первый квартал"
        case 4 | 5 | 6:
            return "второй квартал"
        case 7 | 8 | 9:
            return "третий квартал"
        case 10 | 11 | 12:
            return "четвертый квартал"
        case _:
            return "Error"
print(get_season(int(input())))