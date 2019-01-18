import psycopg2
import Settings


def create_playlist(nome, tipo, data_criacao, utilizador_id):

    # Function to create a Playlist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()

    sql = """INSERT INTO playlist(tipo,nome,data_criacao,utilizador_id)
                 VALUES(%s,%s,%s,%s) RETURNING id;"""
    id = None
    try:
        cur.execute(sql, (tipo, nome, data_criacao, utilizador_id))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def add_music_to_playlist(playlist_id, musica_id, indice):

    # Function to add a Music to a Playlist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO posmusicaplaylist(indice, playlist_id, musica_id)
                VALUES(%s,%s,%s);"""
    try:
        cur.execute(sql, (indice, playlist_id, musica_id,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return "Added"


def search_playlist(nome, utilizador_id):

    # Function to search Playlist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()

    sql = """SELECT playlist.id, playlist.nome, utilizador.nome, playlist.tipo FROM playlist, utilizador
        WHERE playlist.nome like %s and playlist.utilizador_id = utilizador.id and
        (playlist.tipo = 'public' OR utilizador_id = %s);"""
    lista = None
    try:
        nome = "%" + nome + "%"
        cur.execute(sql, (nome, utilizador_id,))
        lista = cur.fetchmany(size=10)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def musics_of_playlist(playlist_id):

    # Function to view the Musics of a Playlist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT indice, musica.nome, artista.nome, album.nome, musica.duracao FROM posmusicaplaylist, musica, 
    artista_musica, artista, artista_album, album
    WHERE playlist_id = %s and posmusicaplaylist.musica_id = musica.id 
    and musica.id=artista_musica.musica_id and artista.id = artista_musica.artista_id 
    and artista.id = artista_album.artista_id and album.id = artista_album.album_id;"""
    lista = None
    try:
        cur.execute(sql, (playlist_id,))
        lista = cur.fetchall()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def delete_playlist(playlist_id, user_id):
    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """DELETE FROM playlist WHERE id = %s and utilizador_id = %s;"""
    try:
        cur.execute(sql, (playlist_id, user_id,))
        conn.commit()
        cur.close()
        x = "Sucess."
    except (Exception, psycopg2.DatabaseError) as error:
        x = error
    finally:
        if conn is not None:
            conn.close()
    return x


def change_playlist_name(new_name, playlist_id, user_id):
    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """UPDATE playlist SET nome= %s WHERE id = %s and utilizador_id = %s;"""
    try:
        cur.execute(sql, (new_name, playlist_id, user_id,))
        conn.commit()
        cur.close()
        x = "Sucess."
    except (Exception, psycopg2.DatabaseError) as error:
        x = error
    finally:
        if conn is not None:
            conn.close()
    return x
