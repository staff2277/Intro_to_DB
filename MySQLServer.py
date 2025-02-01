import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (change user and password accordingly)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Change if using a different user
            password="yourpassword"  # Change to your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as e:  # Explicitly using mysql.connector.Error
        print(f"Error: {e}")
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
