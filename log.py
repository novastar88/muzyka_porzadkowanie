import time

def log_time():
    return time.strftime("%d.%m.%Y %H:%M:%S")

def log_date():
    return time.strftime("%d_%m_%Y")

def save_to_log(done, funct):
    tim = log_time()
    dat = log_date()
    f = open(f"log_{dat}.txt", "a", encoding="utf-16")
    f.write(f"\n[{tim}] {done} [funkcja: {funct}]")
    f.close()
    

if __name__ == "__main__":
    pass