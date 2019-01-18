import psycopg2
import Settings

# ALBUMS


def search_album_name(name):
    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM album WHERE album.nome like %s"""
    lista = None
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


def view_album(id):

    # Function to show all the information about the Album

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM album, artista_album, artista, posmusicaalbum, musica, critica, genero, genero_musica
     WHERE album.id = %s AND album.id = artista_album.album_id  AND artista_album.artista_id = artista.id
     AND   album.id  = posmusicaalbum.album_id AND posmusicaalbum.musica_id = musica.id
     AND   album.id  = critica.album_id AND musica.id = genero_musica.musica_id
     AND   genero_musica.genero_id = genero.id"""
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


def insert_album(name, data, description, duration):

    # Function to insert an Album

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO album(nome, data, descricao, duracao)
    VALUES(%s, %s, %s, %s) RETURNING id;"""
    id = None
    try:
        cur.execute(sql, (name, data, description, duration,))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def make_critic(text, pontuation, user_id, album_id):

    # Function to make a Critic to an Album

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO critica(texto, pontuacao, utilizador_id, album_id)
    VALUES(%s, %s, %s, %s);"""
    try:
        cur.execute(sql, (text, pontuation,user_id, album_id,))
        conn.commit()
        cur.close()
        x = "Sucess"
    except (Exception, psycopg2.DatabaseError) as error:
        x = (error)
    finally:
        if conn is not None:
            conn.close()

    return x


def insert_album_artist(artist_id, album_id):

    # Function to insert Album into Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO artista_album(artista_id,album_id)
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


def search_reviews(album_id):
    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                             password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT utilizador_id, texto, pontuacao FROM critica WHERE critica.album_id=%s"""
    lista = None
    try:
        cur.execute(sql, (album_id,))
        lista = cur.fetchmany(size=10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def delete_album(album_id):
    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """DELETE FROM artista_album WHERE album_id = %s;
    DELETE FROM posmusicaalbum WHERE album_id = %s;
    DELETE FROM critica WHERE album_id = %s;
    DELETE FROM album WHERE id = %s;"""
    try:
        cur.execute(sql, (album_id, album_id, album_id, album_id,))
        conn.commit()
        cur.close()
        x = "Sucess."
    except (Exception, psycopg2.DatabaseError) as error:
        x = error
    finally:
        if conn is not None:
            conn.close()
    return x
