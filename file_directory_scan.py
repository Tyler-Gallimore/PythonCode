from pathlib import Path

def file_size(item):
    #test = Path(str(input("Enter a file path: ")))
    test = item
    result = {}    
    try:
        if test == None:
            test = Path.cwd()
        for i in test.iterdir():
            if i.is_file():
                info = i.stat()
                output = info.st_size
                result.update({str(i.name):output})
    except:
        print("Invalid file path")
    return(result)
    
    
def dir_search():
    file_path = Path(str(input("Enter a file path: ")))
    bacon = {}
    if file_path == None:
        file_path = Path.cwd()
    for i in file_path.iterdir():
        if i.is_dir():
            egg = file_size(i)
            #bacon.update({str(i.name):file_size(i)})
            #egg.update(file_size(i))
            #bacon.update({str(i.name):egg})
            print(egg)
    #return(bacon)


dir_search()