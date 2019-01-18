import psycopg2
import Settings


def search_artist(artist_name):

    # Function to search Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM artista WHERE artista.nome like %s"""
    lista = []
    try:
        name = "%" + artist_name + "%"
        cur.execute(sql, (name,))
        lista=cur.fetchmany(size=10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def search_band(band_name):

    # Function to search Band

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM artista WHERE artista.nome like %s and tipo='banda';"""
    lista = []
    try:
        name = "%" + band_name + "%"
        cur.execute(sql, (name,))
        lista = cur.fetchmany(size=10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def add_artist(nome, data_nascimento, local_nascimento, tipo, descricao ):

    # Function to add Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO artista(nome,data_nascimento,local_nascimento,tipo,descricao)
            VALUES(%s,%s,%s,%s,%s) RETURNING id;"""
    id = None
    try:
        cur.execute(sql, (nome, data_nascimento, local_nascimento, tipo, descricao))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def remove_artist(artist_id):

    # Function to remove Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """DELETE FROM artista WHERE id=%s;"""
    rows_deleted = None
    try:
        cur.execute(sql, (artist_id,))
        rows_deleted = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted


def add_artist_to_band(artista_id, banda_id, data_entrada, data_saida):

    # Function to add Artist to a Band

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO participa(data_entrada, data_saida, artista_id, banda_id)
            VALUES(%s,%s,%s,%s);"""
    try:
        cur.execute(sql, (data_entrada, data_saida, artista_id, banda_id,))
        conn.commit()
        cur.close()
        x = "Added"
    except (Exception, psycopg2.DatabaseError) as error:
        x = error
    finally:
        if conn is not None:
            conn.close()

    return x


def artist_leaves_band(artista_id,banda_id, data_saida):

    # Function to update info when artist leaves band

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """UPDATE participa SET data_saida = %s 
    WHERE artista_id = %s and banda_id = %s;"""
    try:
        cur.execute(sql, (data_saida, artista_id, banda_id,))
        conn.commit()
        cur.close()
        x = "Updated."
    except (Exception, psycopg2.DatabaseError) as error:
        x = error
    finally:
        if conn is not None:
            conn.close()

    return x


def search_artists_from_band(banda_id):

    # Function to search Artists from a Band

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT artista_id,data_entrada,data_saida FROM participa WHERE banda_id = %s"""
    lista = []
    try:
        cur.execute(sql, (banda_id,))
        lista = cur.fetchmany(size=10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.close()

    return lista


def search_band_for_artist(artista_id):

    # Function to search Band by Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT banda_id, data_entrada, data_saida FROM participa WHERE artista_id=%s"""
    lista = []
    try:
        cur.execute(sql, (artista_id,))
        lista = cur.fetchmany(size=10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def search_albuns_of_artist(artista_id):

    # Function to search Albums related to an Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT album_id FROM artista_album WHERE artista_id = %s"""
    lista = []

    try:
        cur.execute(sql, (artista_id,))
        lista = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def search_concerts_of_artist(artista_id):

    # Function to search Concerts related to an Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT concerto_id_concerto FROM artista_concerto WHERE artista_id = %s"""
    lista = []
    try:
        cur.execute(sql, (artista_id,))
        lista = cur.fetchmany(size=10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def search_musics_for_artist(artista_id):

    # Function to search Musics related to an Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT musica_id FROM artista_musica WHERE artista_id = %s"""
    lista = []
    try:
        cur.execute(sql, (artista_id,))
        lista = cur.fetchmany(size=10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def view_artist(artista_id):

    # Function to view the Artist

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT artista.nome, artista.data_nascimento, artista.local_nascimento,artista.tipo, artista.descricao, concerto.id_concerto, concerto.nome,
    concerto.data, concerto.lugar, album.id, album.nome, album.data, album.descricao
    FROM artista, artista_concerto, concerto, artista_album, album
    WHERE artista_concerto.artista_id = artista.id and artista_concerto.concerto_id_concerto = concerto.id_concerto and
    artista_album.artista_id = artista.id and artista_album.album_id = album.id and artista.id = %s;"""

    lista = []
    try:
        cur.execute(sql, (artista_id,))
        lista = cur.fetchmany(size=10)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return lista


def delete_artist(artist_id):
    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    # create a new cursor
    cur = conn.cursor()

    """Delete artist from artist table"""
    sql = """DELETE FROM artista_concerto WHERE artista_id = %s;
    DELETE FROM artista_musica WHERE artista_id = %s;
    DELETE FROM artista_album WHERE artista_id = %s;
    DELETE FROM participa WHERE artista_id = %s;
    DELETE FROM artista WHERE id=%s;"""

    try:
        # execute the INSERT statement
        cur.execute(sql, (artist_id, artist_id, artist_id, artist_id, artist_id))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        x = "Success"
    except (Exception, psycopg2.DatabaseError) as error:
        x = error
    finally:
        if conn is not None:
            conn.close()

    return x
