class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
class MusicPlaylist:
    def __init__(self):
        self.head = None
    def create_playlist(self, title):
        if self.head is None:
            self.head = SongNode(title)
            print(f"Playlist created with song: '{title}'")
        else:
            print("Playlist already exists. Use insert_song to add more songs.")
    def insert_song(self, title):
        new_song = SongNode(title)
        if self.head is None:
            self.head = new_song
            print(f"Inserted '{title}' as the first song in the playlist.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_song
        print(f"Inserted '{title}' into the playlist.")
    def delete_song(self, title):
        if self.head is None:
            print("Playlist is empty. Cannot delete.")
            return
        if self.head.title == title:
            self.head = self.head.next
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.title == title:
                prev.next = curr.next
                print(f"Deleted '{title}' from the playlist.")
                return 
            prev = curr
            curr = curr.next
        print(f"Song '{title}' not found in the playlist.")
    def display_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return
        print(" Current Playlist:")
        temp = self.head
        index = 1
        while temp:
            print(f"{index}. {temp.title}")
            temp = temp.next
            index += 1
if __name__ == "__main__":
    playlist = MusicPlaylist()
    while True:
        print("\n===== Music Playlist Menu =====")
        print("1. Create Playlist")
        print("2. Insert Song")
        print("3. Delete Song")
        print("4. Display Playlist")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            title = input("Enter song title to create playlist: ")
            playlist.create_playlist(title)
        elif choice == '2':
            title = input("Enter song title to insert: ")
            playlist.insert_song(title)
        elif choice == '3':
            title = input("Enter song title to delete: ")
            playlist.delete_song(title)
        elif choice == '4':
            playlist.display_playlist()
        elif choice == '5':
            print("Exiting playlist manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
