import psycopg2
import sys
import Settings

# ALBUMS

def search_concert_name(name):

    # Function to search Concert by name

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM concerto WHERE concerto.nome like %s"""
    lista = []
    try:
        name = "%" + name + "%"
        cur.execute(sql, (name,))                
        lista = cur.fetchmany(size = 10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return lista

def view_concert(id):

    # Function to show all the information about the Concert

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM concerto, artista_concerto, artista, posmusicaconcerto, musica
    WHERE concerto.id_concerto = %s AND concerto.id_concerto = artista_concerto.concerto_id_concerto 
    AND artista_concerto.artista_id = artista.id
    AND   concerto.id_concerto = posmusicaconcerto.concerto_id_concerto 
    AND posmusicaconcerto.musica_id = musica.id"""
    lista = []
    try:
        cur.execute(sql, (id,))
        lista = cur.fetchmany(size = 10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return lista

def insert_concert(name, data, place, lotation):

    # Function to insert a Concert

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO concerto(nome, data, lugar, ocupacao)
    VALUES(%s, %s, %s, %s) RETURNING id;"""
    id = None
    try:
        cur.execute(sql, (name, data, place, lotation,))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id

def insert_concert_artist(artist_id, concert_id):

    # Function to associate a Concert to an Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO artista_concerto(artist_ida, concerto_id)
    VALUES(%s, %s)"""
    try:
        cur.execute(sql, (artist_id, musica_id,))
        conn.commit()
        cur.close()
        x = "Sucess"
    except (Exception, psycopg2.DatabaseError) as error:
        x = (error)
    finally:
        if conn is not None:
            conn.close()

    return x
