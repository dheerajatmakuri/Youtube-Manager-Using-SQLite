# Youtube-Manager-Using-SQLite-Database

## Overview

This Python script provides a simple command-line application to manage YouTube videos using an SQLite database. It lets you list, add, update, and delete video records.

## Features

- **List Videos**: Display all videos stored in the database.
- **Add Video**: Add a new video with its name and time.
- **Update Video**: Update the name and time of an existing video.
- **Delete Video**: Delete a video from the database.
- **Exit**: Exit the application.

## Database

The application uses an SQLite database named `youtube_manager.db` with a single table `videos`. The `videos` table has the following columns:

- `id`: Integer, Primary Key
- `name`: Text, Not Null
- `time`: Text, Not Null

## Prerequisites

- Python 3. x
- `sqlite3` library (included in the Python standard library)

## How to Use

1. **Clone or download the script.**
2. **Run the script using Python.** Execute the following command in your terminal:

   ```sh
   python youtube_manager.py
   ```

3. **Follow the on-screen instructions.** You will be presented with a menu to list, add, update, delete videos, or exit the application.

## Code Explanation

### Database Setup

The script connects to an SQLite database named `youtube_manager.db` and creates a `videos` table if it doesn't exist:

```python
import sqlite3
conn = sqlite3.connect("youtube_manager.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL)
''')
```

### Functions

- **list_videos**: Fetches and prints all records from the `videos` table.
  
  ```python
  def list_videos():
      cursor.execute("SELECT * FROM videos")
      for row in cursor.fetchall():
          print(row)
  ```

- **add_videos**: Inserts a new record into the `videos` table.
  
  ```python
  def add_videos(name, time):
      cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
      conn.commit()
  ```

- **update_videos**: Updates an existing record in the `videos` table.
  
  ```python
  def update_videos(video_id, new_name, new_time):
      cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
      conn.commit()
  ```

- **delete_videos**: Deletes a record from the `videos` table.
  
  ```python
  def delete_videos(video_id):
      cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
      conn.commit()
  ```

- **exit_app**: Placeholder function for future enhancements.

  ```python
  def exit_app():
      pass
  ```

### Main Application Loop

The main loop presents a menu to the user and calls the appropriate function based on the user's choice:

```python
def main():
    while True:
        print("\n\n YouTube Manager App with DB")
        print("1. List all your Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
        elif choice == '3':
            video_id = input("Enter Video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
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
```

## Closing Notes

- Ensure that the database connection is after the application exits.
- This is a simple application. You can expand its functionality by adding features like searching for videos, more detailed video information, etc.

Feel free to modify and enhance this script to suit your needs!
