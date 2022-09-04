#TicTacToe

import sys
def main():
    emt()
    turn()

def emt():
    #Make empty matrix 3X3
    global mat
    r=c=3
    mat=[]
    for i in range(c):
        a=[]
        for j in range(r):
            w=str(i)
            v=str(j)
            a.append(w+"."+v)
        mat.append(a)
    print(*mat,sep="\n")

def turn():
    #turn for X or O
    global seta
    for s in range(9):
      if s%2==0:
        seta='X'
        print("Your Turn: ",seta)
        data()
        s+=1
      else:
        seta='O'
        print("Your Turn: ",seta)
        data()
        s+=1

def data():
    global seta
    #input in a perticular position
    pos=list(map(int,input("Enter Position: ").strip().split(".")))
    print(pos)
    x=pos[0]
    y=pos[1]
    for i in range(x+1):
      if i==x:
        a=mat[i]
        a[y]=seta
    mat[i]=a
    print("    ",*mat,sep="\n")
    match()

def match():
    m=mat[0]
    n=mat[1]
    t=mat[2]
    if(m[0]==m[1]==m[2]):
        print(m[0],"Win")
        sys.exit()
    elif(n[0]==n[1]==n[2]):
        print(n[0],"Win")
        sys.exit()
    elif(t[0]==t[1]==t[2]):
        print(t[0],"Win")
        sys.exit()
    elif(m[0]==n[0]==t[0]):
        print(m[0],"Win")
        sys.exit()
    elif(m[1]==n[1]==t[1]):
        print(m[1],"Win")
        sys.exit()
    elif(m[2]==n[2]==t[2]):
        print(m[2],"Win")
        sys.exit()
    elif(m[0]==n[1]==t[2]):
        print(m[0],"Win")
        sys.exit()
        sys.exit()
    elif(m[2]==n[1]==t[0]):
        print(m[2],"Win")
        sys.exit()

main()
