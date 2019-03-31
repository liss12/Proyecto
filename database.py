import psycopg2
DATABASE_URL = 'postgres://xlnuwgypyqaamw:4f2dbb1b6727a40f0c900d91bb3e157d16c6ff5bc033267850dbd88dcbcd303e@ec2-54-247-85-251.eu-west-1.compute.amazonaws.com:5432/d7ol24ubggaeeh'
   

class DBHelper():
    def __init__(self):
        pass
    
    def crearTablalogin(self):
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        c = conn.cursor()
        c.execute("CREATE TABLE login(usuario text, contrasenia text)")
        conn.commit()
        conn.close()
    
    def crearTablaReserva(self):
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        c = conn.cursor()
        c.execute("CREATE TABLE reserva(id text, usuario text, estado text)")
        conn.commit()
        conn.close()

    def insertarlogin(self, _usuario, _contrasenia):
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        c = conn.cursor()
        c.execute("INSERT INTO login VALUES("+_usuario+","+ _contrasenia+")")
        conn.commit()
        conn.close()

    
    def insertarReserva(self, _id, _usuario, _estado):
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        c = conn.cursor()
        c.execute("INSERT INTO reserva VALUES (?, ?, ?)",[_id, _usuario, _estado])
        conn.commit()
        conn.close()

    def leer(self, _id):
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        c = conn.cursor()
        c.execute("SELECT * FROM reserva where id = ?" , (_id,))
        u = c.fetchone()
        conn.close()
        return u

    def todos(self):        
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        c = conn.cursor()
        c.execute("SELECT * FROM reserva")
        u = c.fetchall()
        conn.close()
        return u

    def update(self, _user, _id, _estado):
        print("UPDATING: " +" id:" + _id +",user: "+ _user +",estado:"+ _estado)
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        c = conn.cursor()
        cadena = "UPDATE reserva SET usuario='"+_user+"', estado='"+_estado+"' WHERE id='"+_id+"'"
        print(cadena)
        v = c.execute(cadena)
        conn.commit()
        conn.close()

    def quemada(self):
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        c = conn.cursor()
        c.execute("INSERT INTO reserva VALUES ('demo1', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo2', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo3', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo4', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo5', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo6', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo7', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo8', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo9', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo10', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo11', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo12', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo13', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo14', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo15', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo16', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo17', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo18', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo19', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo20', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo21', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo22', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo23', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo24', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo25', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo26', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo27', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo28', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo29', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo30', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo31', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo32', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo33', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo34', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo35', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo36', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo37', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo38', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo39', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo40', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo41', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo42', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo43', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo44', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo45', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo46', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo47', '', 'Disponible')")
        c.execute("INSERT INTO reserva VALUES ('demo48', '', 'Disponible')")
        conn.commit()
        conn.close()
