

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



def main():
  print("Vill du skapa en önskelista tryck 1, Vill du läsa upp en önskelista tryck 2")
  val = input("")
  if val == "1":
    skapa()
    
  elif val == "2":
      läsa()
    


if __name__=="__main__":
  main()