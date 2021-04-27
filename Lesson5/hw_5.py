def normalize(some_text):
    my_dict = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd',
               ord('е'): 'e', ord('ё'): 'e', ord('ж'): 'j', ord('з'): 'z', ord('и'): 'i', ord('й'): 'y',
               ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',
               ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'y', ord('ф'): 'f', ord('х'): 'h',
               ord('ц'): 'c', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'sh\'', ord('ь'): 'b', ord('ы'): 'bi',
               ord('э'): 'e', ord('ю'): 'yu', ord('я'): 'ya', ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D',
               ord('Е'): 'E', ord('Ё'): 'Е', ord('Ж'): 'J', ord('З'): 'Z', ord('И'): 'I', ord('Й'): 'Y',
               ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P',
               ord('Р'): 'R', ord('С'): 's', ord('Т'): 'T', ord('У'): 'Y', ord('Ф'): 'F', ord('Х'): 'H',
               ord('Ц'): 'C', ord('Ч'): 'CH', ord('Ш'): 'SH', ord('Щ'): 'SH\'', ord('Ь'): 'b', ord('Ы'): 'BI',
               ord('Э'): 'E', ord('Ю'): 'YU', ord('Я'): 'YA', ord('!'): '_', ord('@'): '_', ord('#'): '_',
               ord('$'): '_', ord('%'): '_', ord('^'): '_', ord('&'): '_', ord('*'): '_', ord('!'): '_', ord(')'): '_', ord(' '): '_'}
    trans = some_text.translate(my_dict)
    return trans


def main():
    some_text = input('Введите какое-либо сообщение: ')
    print(normalize(some_text))


if __name__ == ('__main__'):
    main()
