import psycopg2
import sys
import Settings

# MUSICS


def search_music_name(name):

    # Function to search music by name

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM musica, artista_musica, artista
     WHERE musica.nome like %s
     AND musica.id = artista_musica.musica_id
     AND artista_musica.artista_id = artista.id"""
    try:
        name = name.lower()
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


def search_music_genre(genre):

    # Function to search music by genre

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM musica, genero_musica,genero WHERE musica.id = genero_musica.musica_id 
    AND genero_musica.genero_id = genero.id AND genero.nome LIKE %s"""
    lista = []
    try:
        genre = "%" + genre + "%"
        cur.execute(sql, (genre,))
        lista = cur.fetchmany(size = 10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return lista


def search_music_album(id):

    #Function to search music by album

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM musica, album, posmusicaalbum 
    WHERE musica.id = %s AND musica.id = posmusicaalbum.musica_id 
    AND posmusicaalbum.album_id = album.id like"""
    try:
        id = "%" + id + "%"
        cur.execute(sql, (id,))
        lista = cur.fetchmany(size = 10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return lista


def view_music(id):

    # Function to show all the information about the Music

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM musica, genero_musica, genero, artista_musica, artista WHERE musica.id = %s
    AND musica.id = genero_musica.musica_id
    AND genero_musica.genero_id = genero.id
    AND musica.id = artista_musica.musica_id
    AND artista_musica.artista_id = artista.id"""
    lista = []
    try:
        cur.execute(sql,(id,))
        lista = cur.fetchmany(size = 10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return lista


def insert_music(name, lyrics, duration):

    # Function to insert Music

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO musica(nome, letra, duracao)
    VALUES(%s, %s, %s) RETURNING id;"""
    id = None
    try:
        cur.execute(sql, (name, lyrics, duration,))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def download_music(music_id, date, user_id):

    # Function to Download Music

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO download
    VALUES (%s, %s, %s)"""
    try:
        cur.execute(sql, (date, user_id,music_id,))
        conn.commit()
        cur.close()
        x = "Sucess"
    except (Exception, psycopg2.DatabaseError) as error:
        x = error
    finally:
        if conn is not None:
            conn.close()

    return x


def insert_music_album(album_id, musica_id, index):

    # Function to insert Music into Album

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO posmusicaalbum(indice, album_id, musica_id)
    VALUES(%s, %s, %s);"""
    try:
        cur.execute(sql, (index, album_id, musica_id,))
        conn.commit()
        cur.close()
        x = "Sucess"
    except (Exception, psycopg2.DatabaseError) as error:
        x = error
    finally:
        if conn is not None:
            conn.close()
    return x


def insert_music_concert(concert_id, musica_id, index):

    # Function to insert Music into Concert

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO posmusicaconcerto(indice, concerto_id_concerto, musica_id)
    VALUES(%s, %s,%s);"""
    try:
        cur.execute(sql, (index, concert_id, musica_id,))
        conn.commit()
        cur.close()
        x = "Sucess"
    except (Exception, psycopg2.DatabaseError) as error:
        x =error
    finally:
        if conn is not None:
            conn.close()

    return x


def insert_music_artist(artist_id, musica_id):

    # Function to insert Music into Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO artista_musica(artista_id, musica_id)
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


def relate_music_genre(genre_name, music_id):
    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,password=Settings.password)
    cur = conn.cursor()

    sql = """INSERT INTO genero_musica
    VALUES(%s, %s);"""
    try:
        cur.execute(sql, (genre_name, music_id,))
        conn.commit()
        cur.close()
        x = "Sucess"
    except (Exception, psycopg2.DatabaseError) as error:
        x = (error)
    finally:
        if conn is not None:
            conn.close()

        return x


def delete_music(music_id):
    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                                password=Settings.password)
    cur = conn.cursor()

    sql = """DELETE FROM artista_musica WHERE musica_id = %s;
    DELETE FROM genero_musica WHERE musica_id = %s;
    DELETE FROM posmusicaalbum WHERE musica_id = %s;
    DELETE FROM posmusicaplaylist WHERE musica_id = %s;
    DELETE FROM posmusicaconcerto WHERE musica_id = %s;
    DELETE FROM download WHERE musica_id = %s;
    DELETE FROM musica WHERE id = %s;"""
    try:
        cur.execute(sql, (music_id, music_id, music_id, music_id, music_id, music_id, music_id,))
        conn.commit()
        cur.close()
        x = "Sucess"
    except (Exception, psycopg2.DatabaseError) as error:
        x = error
    finally:
        if conn is not None:
            conn.close()

    return x
