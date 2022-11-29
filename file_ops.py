import os
from mutagen.apev2 import APEv2, APENoHeaderError
import log as lgr


dlist = [x[0] for x in os.walk(r"F:\muzyka\tagowanie")]

def lista_plikow():
    general_list = list()
    
    for topdi in dlist:
        for root, _, filen in os.walk(topdi):
            for file in filen:
                general_list.append((root, file))
                
    return general_list
            
            
def ape_from_mp3():
    general_list = lista_plikow()
           
    
    ape = list()     
    for root, file in general_list: 
        if file.endswith(".mp3"):
            try:
                APEv2(os.path.join(root, file))
                ape.append(os.path.join(root, file))
            except APENoHeaderError:
                pass
    
    if len(ape) != 0:
        for track in ape:
            curr = APEv2(track)
            try:
                curr.delete()
                lgr.save_to_log(f"Removed APE tags {track}", "ape_from_mp3")
            except APENoHeaderError:
                pass
    else:
        lgr.save_to_log(f"No ape tag files", "ape_from_mp3")
  
        
def remove_trash_files():
    filelist = lista_plikow()
    
    filtry = [".URL", ".ini"]
    
    for root, file in filelist:
        for filt in filtry:
            if file.endswith(filt):
                try:
                    os.remove(os.path.join(root, file))
                    lgr.save_to_log(f"Plik ({os.path.join(root, file)}) zgodny z filtrem {filt} - usunięty", "remove_trash_files")
                except Exception:
                    pass
  
      
def znajdz_do_konwersji():
    lip = lista_plikow()
    filt = [".ogg", ".wav", ".ape"]
    
    formaty = set()
    for _, filn in lip:
        for item in filt:
            if filn.endswith(item):
                formaty.add(item)
                break
            
    return formaty

              
                
def do_konwersji(rozszerzenie):
    dlist = [x[0] for x in os.walk(r"F:\muzyka\tagowanie")]
    dlist.remove("F:\\muzyka\\tagowanie")


    folders_ogg = []


    for item in dlist:
        a1 = []
        for root, _, filen in os.walk(item):
            currentd = item
            for filename in filen:
                a1 = os.path.join(filename)
                huj.append(a1)
            for f in a1:
                var = f
                if var.endswith(rozszerzenie):
                    folders_ogg.append(currentd)
                    break
                else:
                    pass


    files_to_move = []
    for item in folders_ogg:
        for root, _, filen in os.walk(item):
            for filename in filen:
                kloc = os.path.join(root, filename)
                files_to_move.append(kloc)
                
    files_to_move2 = []
    
    for item in files_to_move:
        ti = item
        ti2 = ti.replace("F:\\muzyka\\tagowanie", "F:\\muzyka\\konwersja2")
        files_to_move2.append(ti2)
        
        
    ## main

    operation_len1 = len(files_to_move)
    operation_len2 = len(files_to_move2)
                
    if operation_len1 != operation_len2:
        print("nie równe")
        lgr.save_to_log(f"Listy nie równe, exit", "do_konwersji")
    else:
        operation_number = 0
        for _ in range(operation_len1):
            fileor = files_to_move[operation_number]
            filedoc = files_to_move2[operation_number]
            try:
                os.renames(fileor, filedoc)
            except FileNotFoundError:
                lgr.save_to_log(f"File not found error (?)", "do_konwersji")
            lgr.save_to_log(f"Moving {fileor} to {filedoc}", "do_konwersji")
            operation_number += 1
            
            
def do_konwersji_main():
    lst = znajdz_do_konwersji()
    
    for item in lst:
        do_konwersji(item)
        lgr.save_to_log(f"Moving {item}, zakończono", "do_konwersji_main")
    
    lgr.save_to_log(f"Zakończono", "do_konwersji_main")
            
                
def puste_foldery(): 
    fold = list()
    
    for root, dirs, _ in os.walk(r"F:\muzyka\tagowanie"):
        for item in dirs:
            fold.append(os.path.join(root, item))
      
    fold2 = list()
            
    for item2 in fold:
        size = os.stat(item2).st_size
        if size == 0:
            try:
                os.rmdir(item2)
                lgr.save_to_log(f"Usuwanie pustego folderu: {item2}", "puste_foldery")
            except OSError:
                fold2.append(item2)
        else:
            pass
    
    for item3 in fold2:
        size = os.stat(item3).st_size
        if size == 0:
            try:
                os.rmdir(item3)
                lgr.save_to_log(f"Usuwanie pustego folderu: {item3}", "puste_foldery")
            except OSError:
                pass
        else:
            pass
        
        
if __name__ == "__main__":
    pass