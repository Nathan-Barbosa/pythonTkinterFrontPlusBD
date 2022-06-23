from tkinter import *
import mysql.connector as mysql

app = Tk()
app.title('Prova Av2')
app.config(padx=150, pady=150)


def insert():
    status.delete(0,END)
    userID = e_UserID.get()
    name = e_Name.get()
    tel = e_Tel.get()
    email = e_Email.get()
    user = e_User.get()
    password = e_Password.get()
    if(userID == '' or name=='' or tel=='' or email=='' or user=='' or password==''):
        status.insert(0, 'Campos em branco!')
    else:
        con=mysql.connect(host='localhost', user='root', password='', database='lab12')
        cursor=con.cursor()
        cursor.execute(f"insert into users values({userID}, '{name}','{tel}', '{email}', '{user}', '{password}')")
        cursor.execute('commit')
        status.insert(0, 'Usuário cadastrado')
        con.close()

def search():
    userID = e_UserID.get()
    if(userID == ''): 
        status.insert(0, 'Campo usuarioID vazio')    
    else:
        con=mysql.connect(host='localhost',user='root', password='', database='lab12' )
        cursor=con.cursor()
        cursor.execute(f'select * from users where id_user = {userID}')
        row = cursor.fetchall()
        
        e_Name.delete(0,END)
        e_Tel.delete(0,END)
        e_Email.delete(0,END)
        e_User.delete(0,END)
        e_Password.delete(0,END)
        status.delete(0,END)

        if(row):
            for r in row:
                e_Name.insert(0,r[1])
                e_Tel.insert(0,r[2])
                e_Email.insert(0,r[3])
                e_User.insert(0,r[4])
                e_Password.insert(0,r[5])
            status.insert(0,'Usuario Encontrado!')
        else:
            e_UserID.delete(0,END)
            status.insert(0, 'Usuario Não Encontrado!')
        con.close()
  
def delete():
    status.delete(0,END)
    userID = e_UserID.get()
    if(userID == ''): 
        status.insert(0, 'Campo usuarioID vazio')
    else:
        con = mysql.connect(host='localhost',user='root', password='', database='lab12')
        cursor=con.cursor()
        cursor.execute(f'delete from users where id_user = {userID}')
        cursor.execute('commit')
        status.insert(0,'Usuario deletado')
        con.close()

def update():
    status.delete(0,END)
    userID = e_UserID.get()
    name = e_Name.get()
    tel = e_Tel.get()
    email = e_Email.get()
    user = e_User.get()
    password = e_Password.get()
    if(userID==''):
        status.insert(0, 'Campo usuarioID vazio')
    else:
        if(name != ''):
            con = mysql.connect(host='localhost', user = 'root', password = '', database='lab12')
            cursor=con.cursor()
            cursor.execute(f'update users set name="{name}" where id_user = {userID}')
            cursor.execute('commit')
            con.close()
        if(tel != ''):
            con = mysql.connect(host='localhost', user = 'root', password = '', database='lab12')
            cursor=con.cursor()
            cursor.execute(f'update users set tel="{tel}" where id_user = {userID}')
            cursor.execute('commit')
            con.close()
        if(email != ''):
            con = mysql.connect(host='localhost', user = 'root', password = '', database='lab12')
            cursor=con.cursor()
            cursor.execute(f'update users set email="{email}" where id_user = {userID}')
            cursor.execute('commit')
            con.close()
        if(user != ''):
            con = mysql.connect(host='localhost', user = 'root', password = '', database='lab12')
            cursor=con.cursor()
            cursor.execute(f'update users set user="{user}" where id_user = {userID}')
            cursor.execute('commit')
            con.close()
        if(password != ''):
            con = mysql.connect(host='localhost', user = 'root', password = '', database='lab12')
            cursor=con.cursor()
            cursor.execute(f'update users set password="{password}" where id_user = {userID}')
            cursor.execute('commit')
            con.close()
        status.insert(0,' status atualizado(s)!')

Label(app, text='Informe os Dados: ',font=(SOLID, 20)).grid(columnspan=3, row=0, column=0)
Label(app, text='idUsuário: ').grid(row=1, column=0)
Label(app, text='Nome: ').grid(row=2, column=0)
Label(app, text='Tel: ').grid(row=3, column=0)
Label(app, text='E-mail').grid(row=4, column=0)
Label(app, text='Usuário').grid(row=5, column=0)
Label(app, text='Senha').grid(row=6, column=0)
#columnspan=3,
e_UserID = Entry()
e_UserID.grid(row=1,column=1)

e_Name = Entry()
e_Name.grid( row=2,column=1)

e_Tel = Entry()
e_Tel.grid( row=3,column=1)

e_Email = Entry()
e_Email.grid( row=4,column=1)

e_User = Entry()
e_User.grid(row=5,column=1)

e_Password = Entry()
e_Password.grid(row=6,column=1)


searchButton = Button(app, text='Buscar',command=search)
searchButton.grid(row=1, column=2)


insertButton = Button(app, text='Inserir', width=17, command=insert)
insertButton.grid(row=7, column=0)

updateButton = Button(app, text='Atualizar',width=17,command=update)
updateButton.grid(row=7, column=1)

deleteButton = Button(app, text='Delete',width=17,command=delete)
deleteButton.grid(row=7, column=2)

status = Entry(app, text='show status')
status.grid(columnspan=3,row=8)

app.mainloop()

""" #create database
con=mysql.connect(host='localhost', user='root', password='', database='')
cursor=con.cursor()
cursor.execute('create database lab12')
cursor.execute('commit')

#create table
con=mysql.connect(host='localhost', user='root', password='', database='lab12')
cursor=con.cursor()
sql = "CREATE TABLE users(id_user int primary key, name varchar(30), tel varchar(16), email varchar(30), user varchar(30), password varchar(30))"
cursor.execute(sql)
cursor.execute('commit')
"""