

def skapa():
    filnamn = input("Vad ska filen heta? ")  
    with open(f"programering/{filnamn}.txt", "w", encoding="utf8") as f:
        barnnamn = input("Vad heter barnet? ")
        f.write(f"{barnnamn}\n")
        while True:
            saklista = input("Vilka saker ska skrivas på önskelistan, om du är klar skriv # ")
            if "#" in saklista:
                break
            else:
                f.write(f"{saklista}\n")


def läsa():
    filnamn = input("Vad heter filen? ")
    with open(f"programering/{filnamn}.txt", "r", encoding="utf8") as f:
        lista = f.readlines()
        print(f"{lista[0]}ÖNSKELISTA")
        for i in range(1,len(lista)):
            print(f"{lista[i]}")

def dumdum():
    with open(f"programering/dåligabarn.txt", "r", encoding="utf8") as f:
        barn = f.readlines()
        print("Här är barnen på listan")
        for i in barn:
            print(i, end="")
        while True:
            dumbarn = input("Skriv namnet på dumt barn, om du är klar skriv # ")
            if "#" in dumbarn:
                break
            else:
                dumbarn = dumbarn+"\n"
                barn += dumbarn 
        with open(f"programering/dåligabarn.txt", "w", encoding="utf8") as f:        
            for i in range(0,len(barn)):
                f.write(barn[i])
        

def main():
  print("""\nVill du skapa en önskelista tryck 1, Vill du läsa upp en önskelista tryck 2, 
För att lägga till barn på dum listan tryck 3""")
  val = input("")
  if val == "1":
    skapa()
    
  elif val == "2":
    läsa()

  elif val == "3":
    dumdum()
    


if __name__=="__main__":
  main()