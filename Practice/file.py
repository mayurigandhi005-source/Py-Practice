with open("notes.txt","w") as f:
    f.write(" python \n program \n language" )

with open("notes.txt","r")as f:
    content=f.readlines()
    print(content)    