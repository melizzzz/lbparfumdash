import sqlite3

DB_NAME = 'database.db'
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE perfumes')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS perfumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ref_number TEXT NOT NULL,
            name TEXT NOT NULL,
            fournisseur TEXT NOT NULL,
            in_stock INTEGER NOT NULL,
            fm TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

#if __name__ == "__main__":
   #init_db()


def get_db():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute('''SELECT * FROM perfumes''')
        results = cur.fetchall()
        return results


def create_new_parfume(ref_parfum, name, fournisseur, genre,number_stock):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO perfumes (ref_number, name, fournisseur,fm, in_stock) VALUES (?, ?,?, ?,?)", (ref_parfum, name,fournisseur,genre, number_stock))
        conn.commit()


def delete_parfume(ref):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM perfumes WHERE ref_number = ?", (ref,))
        conn.commit()


def change(ref, stock):
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE perfumes SET in_stock = ? WHERE ref_number = ?", (stock, ref))
            conn.commit()


def update_parfume(old_ref, new_ref, name, fournisseur):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE perfumes SET ref_number = ?, name = ?, fournisseur = ? WHERE ref_number = ?",
            (new_ref, name, fournisseur, old_ref)
        )
        conn.commit()


def search_all_fields(keyword):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM perfumes WHERE fm LIKE ? OR name LIKE ? OR in_stock = ? OR ref_number LIKE ? OR fournisseur LIKE ?",
                    ('%' + keyword + '%', '%' + keyword + '%', keyword, '%' + keyword + '%', '%' + keyword + '%'))
        results = cur.fetchall()
    return results

