# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени
#   добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только
#   для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
#   берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя,
#   если оно передано. Далее счётчик файлов и расширение.

from pathlib import Path
import os

my_path = Path('Домашка\Python_Homework\Sem_7\Example')


def group_rename_files(final_name: str, num_dig: int, ext: str, final_ext: str,
                       start_orig_name: int, stop_orig_name: int):

    count = 0
    my_list = os.listdir(my_path)
    for el in my_list:
        el_ext = el.split('.')
        if el_ext[-1] == ext:
            count += 1
            os.rename(f'{my_path}\{el}',
                      f'{my_path}\{el_ext[0][start_orig_name:stop_orig_name]}{final_name}_{count:0{num_dig}}.{final_ext}')


group_rename_files('task', 3, 'txt', 'bin', 2, 6)
