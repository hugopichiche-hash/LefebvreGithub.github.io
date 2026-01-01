from random import *

def adresses_ip(classe:str="A") -> str:
    if classe =='A':
        l= f"{random.randint(0,127)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    elif classe == "B":
        l= f"{random.randint(128,191)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    elif classe == "C":
        l= f"{random.randint(192,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    elif classe == "D":
        l= f"{random.randint(224,239)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    elif classe == "E":
        l= f"{random.randint(240,254)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    return l

def classe(adresse:str) -> str:
    x=adresse.split(".")
    if int(x[0])<=127:
        classe="A"
    elif int(x[0])>128 and int(x[0])<191:
        classe="B"
    elif int(x[0])>128 and int(x[0])<191:
        classe="C"
    elif int(x[0])>128 and int(x[0])<191:
        classe="D"
    elif int(x[0])>128 and int(x[0])<191:
        classe="E"
    return classe

if __name__ == "__main__":
    adr = adresses_ip("A")
    print(f"{adr} est de classe {classe(adr)}")