import pyodbc
import uuid
from werkzeug.security import generate_password_hash, check_password_hash


class usersdb:
    def __init__(self):
        self.conn=pyodbc.connect(r'DRIVER={SQL Server};SERVER=ShahdPC;DATABASE=eurodb')
        self.cursor=self.conn.cursor()
    


    def signUp(self, username, email, password ,phone,docID,docSource,carType,carModel,carLetters,carChassis,carNumbers,address):
        user_id = str(uuid.uuid4())  # Generate a unique hex identifier
        hashed_password = generate_password_hash(password)
        query = "INSERT INTO users (uid, name, email, password , phone,docID,docSource,carType,carModel,carLetters,carChassis,carNumbers,address) VALUES (?,?,?,?,?,?, ?, ?,?,?,?,?,?)"
        self.cursor.execute(query, (user_id, username, email, hashed_password,phone,docID,docSource,carType,carModel,carLetters,carChassis,carNumbers,address))
        self.conn.commit()

    def login(self, email, password):
        query = "SELECT uid, password FROM users WHERE email = ?"
        self.cursor.execute(query, (email))
        row = self.cursor.fetchone()
        if row and check_password_hash(row[1], password):
            return row[0]  # Return the user_id if login is successful
        return None

    def edit(self, email, new_password):
        hashed_password = generate_password_hash(new_password)
        query = "UPDATE users SET password = ? WHERE email = ?"
        self.cursor.execute(query, (hashed_password, email))
        self.conn.commit()
    
