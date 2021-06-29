# import os
# import string
#
#
# #1
# def create_dir(dir_name):
#     if not os.path.isdir(dir_name):
#         os.mkdir(dir_name)
#
#     # try:
#     #     os.mkdir(dir_name)
#     # except FileExistsError:
#     #     pass
#
# def create_file(symbol, dir_name):
#     # filename = f"{dir_name}/{symbol}.txt"
#     filename = os.path.join(dir_name, f"{symbol}.txt")
#     with open(filename, "w") as file:
#         file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))
#
# def creat_all_files(dir_name):
#     for symbol in string.ascii_lowercase:
#         create_file(symbol, dir_name)
#
# def tanos_click(dir_name):
#     files = list(os.listdir(dir_name))
#     for file in files[:len(files) // 2]:
#         os.remove(os.path.join(dir_name, file))
#
# folder = "alpherbet"
# # create_dir(folder)
# creat_all_files(folder)
# tanos_click(folder)