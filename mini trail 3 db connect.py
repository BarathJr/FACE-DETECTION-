
'''import mysql.connector
import os

def insert_image_to_db(name, image_path):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR PASS",
            database="YOUR DATA BASE"
        )
        cursor = conn.cursor()

        with open(image_path, "rb") as file:
            binary_data = file.read()

        cursor.execute("INSERT INTO known_faces (name, image) VALUES (%s, %s)", (name, binary_data))
        conn.commit()
        print(f"Image for '{name}' inserted successfully.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except FileNotFoundError:
        print("The image file was not found. Please check the path.")
    finally:
        if conn.is_connected():
            conn.close()

def main():
    choice = input("Do you want to insert a new image into the database? (yes/no): ").strip().lower()
    if choice in ['yes', 'y']:
        name = input("Enter the name: ").strip()
        image_path = input("Enter the full path to the image: ").strip()

        if not os.path.exists(image_path):
            print("Invalid image path. Please try again.")
        else:
            insert_image_to_db(name, image_path)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()'''

'''import mysql.connector
import os

def insert_image_to_db(name, image_path):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR PASS",
            database="YOUR DATA BASE"
        )
        cursor = conn.cursor()

        with open(image_path, "rb") as file:
            binary_data = file.read()

        cursor.execute("INSERT INTO known_faces (name, image) VALUES (%s, %s)", (name, binary_data))
        conn.commit()
        print(f"Image for '{name}' inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    except FileNotFoundError:
        print("Image file not found. Please check the path.")
    finally:
        if conn.is_connected():
            conn.close()

def display_images_from_db(output_folder="output_images"):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR PASS",
            database="YOUR DATA BASE"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT name, image FROM known_faces")
        results = cursor.fetchall()

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for name, image_data in results:
            filename = os.path.join(output_folder, f"{name}.jpg")
            with open(filename, "wb") as f:
                f.write(image_data)
            print(f"Saved image for '{name}': {filename}")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        if conn.is_connected():
            conn.close()

def main():
    while True:
        print("\nOptions:")
        print("1. Insert a new image")
        print("2. Display all stored images")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            name = input("Enter the name: ").strip()
            image_path = input("Enter the full path to the image: ").strip()
            if os.path.exists(image_path):
                insert_image_to_db(name, image_path)
            else:
                print("Invalid image path.")
        elif choice == "2":
            display_images_from_db()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
'''

import mysql.connector
import os
from PIL import Image
from io import BytesIO

def insert_image_to_db(name, image_path):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="190505",
            database="caseyminipro"
        )
        cursor = conn.cursor()

        # Check if the file exists and is an image
        if os.path.exists(image_path):
            with open(image_path, "rb") as file:
                binary_data = file.read()

            cursor.execute("INSERT INTO known_faces (name, image) VALUES (%s, %s)", (name, binary_data))
            conn.commit()
            print(f"Image for '{name}' inserted successfully.")
        else:
            print("Invalid image path.")
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    except FileNotFoundError:
        print("Image file not found. Please check the path.")
    except IOError:
        print("Error reading the image file.")
    finally:
        if conn.is_connected():
            conn.close()

def display_images_from_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="190505",
            database="caseyminipro"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT name, image FROM known_faces")
        results = cursor.fetchall()

        for name, image_data in results:
            try:
                image = Image.open(BytesIO(image_data))
                image.show(title=name)
                print(f"Displayed image for '{name}'.")
            except IOError:
                print(f"Error displaying image for '{name}'.")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        if conn.is_connected():
            conn.close()

def main():
    while True:
        print("\nOptions:")
        print("1. Insert a new image")
        print("2. Display all stored images")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            name = input("Enter the name: ").strip()
            image_path = input("Enter the full path to the image: ").strip()
            insert_image_to_db(name, image_path)
        elif choice == "2":
            display_images_from_db()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
