from pathlib import Path

def dir_file_size():
    file_path = Path(str(input("Enter a file path: ")))
    result = {}
    try:
        if file_path == None:
            file_path = Path.cwd()
        for path in file_path.iterdir():
            if path.is_file():
                result[str(path)] = path.stat().st_size
            if path.is_dir():
                dir_dict = {}
                for item in path.iterdir():
                    if item.is_file():
                        dir_dict[str(item)] = item.stat().st_size     
                result[str(path)] = dir_dict
    except:
        print("Invalid file path")
    return result