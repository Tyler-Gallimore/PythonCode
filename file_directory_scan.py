from pathlib import Path

def final_code():
    file_path = Path(str(input("Enter a file path: ")))
    result = {}
    try:
        if file_path == None:
            file_path = Path.cwd()
        for path in file_path.iterdir():
            if path.is_file():
                result[str(path)] = path.stat().st_size
            if path.is_dir():
                apple = {}
                for item in path.iterdir():
                    if item.is_file():
                        apple[str(item)] = item.stat().st_size     
                result[str(path)] = apple
    except:
        print("Invalid file path")
    return result

