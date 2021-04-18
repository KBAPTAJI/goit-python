from pathlib import Path
import os
my_directory_files = {'изображения': {'.JPEG', '.png', '.JPG', '.SVG'},
                      'видео файлы': {'.avi', '.mp4', '.mov', '.mkv'},
                      'документы': {'.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'},
                      'музыка': {'.mp3', '.ogg', '.wav', '.amr'},
                      'архивы': {'.zip', '.gz', '.tar'},
                      'неизвестные расширения': {'.'}
                      }


def main():
    pathroot = input('Введите путь какую папку нужно разобрать?: ')
    p = Path(pathroot)
    new_suffix = set()
    files_path = []
    files_stem = []
    files_name = []

    if p.exists():
        for element in p.glob('**/*'):
            if element.is_file():
                print(f'{element} это файл')
                new_suffix.add(element.suffix)
                files_path.append(element)
                files_stem.append(element.stem)
                files_name.append(element.name)
            else:
                print(f'{element} это папка')
        for i in my_directory_files:
            if i == 'изображения':
                directory_name = f'{p}\{i}'
                new_p = Path(directory_name)
                try:
                    Path.mkdir(new_p)
                except FileExistsError:
                    print('Папка уже существует, создавать не надо')
                for key, value in my_directory_files.items():
                    if key == 'изображения':
                        a = value & new_suffix
                        print(a)
                        for elements in a:
                            for names in files_name:
                                if elements in names:
                                    print(names)
                                    os.replace(f'{p}\{names}',
                                               f'{new_p}\{names}')
                try:
                    Path.rmdir(new_p)
                except OSError:
                    print('В папке есть файлы')

            elif i == 'видео файлы':
                directory_name = f'{p}\{i}'
                new_p = Path(directory_name)
                try:
                    Path.mkdir(new_p)
                except FileExistsError:
                    print('Папка уже существует, создавать не надо')
                for key, value in my_directory_files.items():
                    if key == 'видео файлы':
                        a = value & new_suffix
                        print(a)
                        for elements in a:
                            for names in files_name:
                                if elements in names:
                                    print(names)
                                    os.replace(f'{p}\{names}',
                                               f'{new_p}\{names}')
                try:
                    Path.rmdir(new_p)
                except OSError:
                    print('В папке есть файлы')
            elif i == 'документы':
                directory_name = f'{p}\{i}'
                new_p = Path(directory_name)
                try:
                    Path.mkdir(new_p)
                except FileExistsError:
                    print('Папка уже существует, создавать не надо')
                for key, value in my_directory_files.items():
                    if key == 'документы':
                        a = value & new_suffix
                        print(a)
                        for elements in a:
                            for names in files_name:
                                if elements in names:
                                    print(names)
                                    os.replace(f'{p}\{names}',
                                               f'{new_p}\{names}')
                try:
                    Path.rmdir(new_p)
                except OSError:
                    print('В папке есть файлы')
            elif i == 'музыка':
                directory_name = f'{p}\{i}'
                new_p = Path(directory_name)
                try:
                    Path.mkdir(new_p)
                except FileExistsError:
                    print('Папка уже существует, создавать не надо')
                for key, value in my_directory_files.items():
                    if key == 'музыка':
                        a = value & new_suffix
                        print(a)
                        for elements in a:
                            for names in files_name:
                                if elements in names:
                                    print(names)
                                    os.replace(f'{p}\{names}',
                                               f'{new_p}\{names}')
                try:
                    Path.rmdir(new_p)
                except OSError:
                    print('В папке есть файлы')
            elif i == 'архивы':
                directory_name = f'{p}\{i}'
                new_p = Path(directory_name)
                try:
                    Path.mkdir(new_p)
                except FileExistsError:
                    print('Папка уже существует, создавать не надо')
                for key, value in my_directory_files.items():
                    if key == 'архивы':
                        a = value & new_suffix
                        print(a)
                        for elements in a:
                            for names in files_name:
                                if elements in names:
                                    print(names)
                                    os.replace(f'{p}\{names}',
                                               f'{new_p}\{names}')
                try:
                    Path.rmdir(new_p)
                except OSError:
                    print('В папке есть файлы')
            elif i == 'неизвестные расширения':
                print(i)
                directory_name = f'{p}\{i}'
                new_p = Path(directory_name)
                try:
                    Path.mkdir(new_p)
                except FileExistsError:
                    print('Папка уже существует, создавать не надо')
                for key, value in my_directory_files.items():
                    print(key, value)
                    if key == 'неизвестные расширения':
                        a = new_suffix
                        print(a)
                        for elements in a:
                            for names in files_name:
                                if elements in names:
                                    print(names)
                                    try:
                                        os.replace(
                                            f'{p}\{names}', f'{new_p}\{names}')
                                    except FileNotFoundError:
                                        pass
                try:
                    Path.rmdir(new_p)
                except OSError:
                    print('В папке есть файлы')

    else:
        print(f'Путь {p.absolute()} не найден')
    return new_suffix


if __name__ == ('__main__'):
    main()
