from files_pack import rename_function as rf

if __name__ == '__main__':
    print("Переименование txt файлов в каталоге data_files")
    files_cnt = rf.rename_files("_text_", ".txt", path="./data_files")
    print(f"Переименовано файлов: {files_cnt}")
