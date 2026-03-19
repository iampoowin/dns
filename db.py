import sqlite3

def init_db():
    conn = sqlite3.connect("payments.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT,
        email TEXT,
        amount INTEGER,
        status TEXT,
        gateway_txn TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_payment(order_id,email,amount,status,txn):
    conn = sqlite3.connect("payments.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO payments(order_id,email,amount,status,gateway_txn)
    VALUES(?,?,?,?,?)
    """,(order_id,email,amount,status,txn))

    conn.commit()
    conn.close()