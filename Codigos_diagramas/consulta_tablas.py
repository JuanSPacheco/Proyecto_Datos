print("Tabla departamento")
import psycopg2
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'sec_entrega'
    )
    print("Conexión exitosa")
    cursor = connection.cursor()
    cursor.execute("select * from departamento")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexión finalizada")
    
print("\n")    

#-----------------------------------------------
print("Tabla municipio")
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'sec_entrega'
    )
    print("Conexión exitosa")
    cursor = connection.cursor()
    cursor.execute("select * from municipio")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexión finalizada")    
    
print("\n")     

#-----------------------------------------------
print("Tabla caso")       
try:
       connection = psycopg2.connect(
           host = 'localhost',
           user = 'postgres',
           password = '123456789',
           database = 'sec_entrega'
       )
       print("Conexión exitosa")
       cursor = connection.cursor()
       cursor.execute("select * from caso")
       rows = cursor.fetchall()
       for row in rows:
           print(row)
except Exception as ex:
       print(ex)
finally:
       connection.close()
       print("Conexión finalizada")
              
print("\n")   

#-----------------------------------------------
print("Tabla contagio")          
try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = '123456789',
            database = 'sec_entrega'
        )
        print("Conexión exitosa")
        cursor = connection.cursor()
        cursor.execute("select * from contagio")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as ex:
        print(ex)
finally:
        connection.close()
        print("Conexión finalizada")       
   
print("\n")     

#-----------------------------------------------
print("Tabla etnia")      
try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = '123456789',
            database = 'sec_entrega'
        )
        print("Conexión exitosa")
        cursor = connection.cursor()
        cursor.execute("select * from etnia")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as ex:
        print(ex)
finally:
        connection.close()
        print("Conexión finalizada")       
    
print("\n")     
  
#-----------------------------------------------  
print("Tabla persona")      
try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = '123456789',
            database = 'sec_entrega'
        )
        print("Conexión exitosa")
        cursor = connection.cursor()
        cursor.execute("select * from persona")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as ex:
        print(ex)
finally:
        connection.close()
        print("Conexión finalizada")        
     
print("\n")     

#-----------------------------------------------
print("Tabla recuperacion")      
try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = '123456789',
            database = 'sec_entrega'
        )
        print("Conexión exitosa")
        cursor = connection.cursor()
        cursor.execute("select * from recuperacion")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as ex:
        print(ex)
finally:
        connection.close()
        print("Conexión finalizada")    
        
    
