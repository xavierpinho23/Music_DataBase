import psycopg2
import Settings


def add_user(nome, password, data_entrada, tipo):

    # Function to add a User

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """INSERT INTO utilizador(nome,password,data_entrada,tipo)
            VALUES(%s,%s,%s,%s) RETURNING id;"""
    id = None
    try:
        cur.execute(sql, (nome, password, data_entrada, tipo))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def remove_user(user_id):

    # Function to remove User

    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """DELETE FROM utilizador WHERE id=%s;"""
    rows_deleted = None
    try:
        cur.execute(sql, (user_id,))
        rows_deleted = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted


def search_user(user_name):

    # Function to search User
    
    conn = psycopg2.connect(host=Settings.host, database=Settings.database, user=Settings.user,
                            password=Settings.password)
    cur = conn.cursor()
    sql = """SELECT * FROM utilizador 
         WHERE nome = %s;"""
    user = None
    try:
        cur.execute(sql, (user_name,))
        user = cur.fetchone()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return user
