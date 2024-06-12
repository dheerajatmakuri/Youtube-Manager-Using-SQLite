import sqlite3
conn = sqlite3.connect("yputube_manager.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXTNOT NULL,
               TIME TEXT NOT NULL)
''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    conn.commit()


def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()


def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def exit_app():
    pass


def main():
    while True:
        print("\n\n Youtube manager app with DB")
        print("1. List all your Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
           name  = input("enter the video name: ")
           time = input("enter your video time: ")
           add_videos(name,time)

        elif choice == '3':
           video_id = input("Enter Video ID to update: ")
           name = input("Enter the video name: ")
           time = input("Enter your video time: ")
           update_videos(video_id, name, time)
        
        elif choice == '4':
           video_id = input("Enter Video ID to delete: ")
           delete_videos(video_id)

        elif choice == '5':
           break

        else:
           print("Invalid Choice :)")
    conn.close()
 
 
if __name__ == "__main__":
    main()