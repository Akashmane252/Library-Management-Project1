import mysql.connector as a
con=a.connect(host="localhost",user="root",password="2528",database="books")
import datetime as b
def addbook():

    bn=input("Enter Book Name:")
    c=input("Enter BOOK Code:")
    t=input("Total Books:")
    s=input("Enter Subject:")
    data=(bn,c,t,s)
    sql='insert into books values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">_________________________________________________________________________________<")
    print("Data Entered Successfully")
    main()


def issueb():
    n=input("Enter Name:")
    r=input("Enter Reg No:")
    co=input("Enter Book code:")
    d=input("Enter Date:",b)
    data = (n, r, co, d)
    a="inser into issue values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">________________________________________________________________________<")
    print("Book issued to:",n)
    main()
def submitb():
    n=input("Enter Name:")
    r=input("Reg no:")
    co=input("Enter Book code:")
    d=input("Enter date:")
    a="inser into submit values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">__________________________________________________________________________<")
    print("Book Submitted from:",n)
    bookup=(co,1)
    main()
def bookup(co,u):
    a="Selcet Total from books where BCODE=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="updte books set TOTAL=%s where BCODE=%s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()
def dbook():
    ac=input("Enter Book Code:")
    a="delete from books where BCODE=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()
def disbook():
    a="select * from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Books Name:",i[0])
        print("Boo Code:",i[1])
        print("Total:",i[2])
        print(">________________<")
        main()

def main():

    print("""
                               LIBRARY MANAGER
  1 ADD BOOK
  2 ISSUE BOOK
  3 SUBMIT BOOK
  4 DELETE BOOK
  5 DISPLAY BOOKS
  """)
    choice=input("Enter Task No:")
    print("<___________________________________________________________________________>")
    if choice=='1':
        addbook()
    elif choice=='2':
        issueb()
    elif choice=='3':
        submitb()
    elif choice=='4':
        dbook()
    elif choice=='5':
        disbook()
    else:
        print("Wrong choice........")
        main()
def pswd():
    ps=input("Enter THe password:")
    if ps=="py123":
        main()
    else:
        print("Wrong password")
        pswd()
pswd()