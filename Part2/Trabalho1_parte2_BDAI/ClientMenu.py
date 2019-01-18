# Main
import psycopg2
import sys
import Music
import Album
import Concert
import Settings
import User
import Artist
import Playlist
import datetime

def menu(user_id):
    option = "0"
    while option != "2" or option != "3" or option != "4" or option != "5" or option != "6" or option != "7" or option != "8" or option != "9" or option != "10":
    
        print("|  1 | - Search Music")
        print("|  2 | - Search Album")
        print("|  3 | - Search Concert")
        print("|  4 | - Search Artist")
        print("|  5 | - Search Genre")
        print("|  6 | - Search Playlist")
        print("|  7 | - Download Music")
        print("|  8 | - Create Playlist")
        print("|  9 | - Add Music to Playlist")
        print("| 10 | - Make Critic")

        option = input("Please choose one of these options: \n")

        if option == "1":
            # Search Music
            name = input("Name: ")

            print('{:3s} {:20s} {:20s} {:10s}'.format("ID","NAME","ARTIST","DATE", "ALBUM"))
            lista_1 = Music.search_music_name(name = name)
            for m in lista_1:
                print ('{:3s} {:20s} {:20s} {:10s}'.format(str(m[0]),m[1],m[7],m[8]))

            id = input("Choose a Music ID to see more info.")

            print('{:20s} {:20s} {:20s} {:10s} {:20s}'.format("NAME","GENRE","ARTIST", "DURATION","LYRICS"))
            lista_2 = Music.view_music(id = id)
            for i in lista_2:
                print ('{:20s} {:20s} {:20s} {:10s} {:20s}'.format(i[1],i[7],i[12],i[3],i[2]))

        elif option == "2":
            # Search Album
            name = input("Name: ")
            
            print('{:3s} {:10s} {:30s} {:50s} {:6s}'.format("ID","NAME","RELEASE DATE", "DESCRIPTION","DURATION"))
            lista_1 = Album.search_album_name(name = name)
            for m in lista_1:
                print('{:3s} {:10s} {:30s} {:50s} {:6s}'.format(str(m[0]),m[1],m[2],m[3],m[4]))

            id_1 = input("Choose a Album ID to see more info.")

            lista_2 = Album.view_album(id = id_1)
            print('{:3s} {:10s} {:20s} {:15s} {:5s} {:20s} {:10s}'.format("ID","NAME","ARTIST","REVIEW" ,"TRACK" ,"MUSIC", "GENRE"))
            for i in lista_2:
                print('{:3s} {:10s} {:20s} {:15s} {:5s} {:20s} {:10s}'.format(str(i[0]),i[1],i[8],i[20],str(i[13]),i[17],i[25]))

        elif option == "3":
            # Search Concert
            concert_name = input("Name: ")

            print('{:3s} {:10s} {:20s} {:20s} {:10s}'.format("ID","NAME","DATE", "PLACE","LOTATION"))
            lista_1 = Concert.search_concert_name(name  = concert_name)
            for m in lista_1:
                print('{:3s} {:10s} {:20s} {:20s} {:10s}'.format(str(m[0]),m[1],m[2],m[3],str(m[4])))

            id = input("Choose a Concert ID to see more info.")

            lista_2 = Concert.view_concert(id = id)
            print('{:15s} {:10s} {:10s} {:20s}'.format("NAME","TRACK","MUSIC","ARTIST","DURATION"))
            for i in lista_2:
                print('{:15s} {:10s} {:10s} {:20s}'.format(i[1],str(i[13]),i[17],i[8],i[19]))

        elif option == "4":
            # Search Artist
            artist_name = input("Name: ")

            lista_1 = Artist.search_artist(artist_name=artist_name)
            print('{:3s} {:10s} {:10s}'.format("ID","NAME","TYPE"))
            
            for m in lista_1:
                print('{:3s} {:10s} {:10s}'.format(str(m[0]),m[1],m[4]))

            artist_id = input("Choose artist ID to see more info: ")
            lista_2 = Artist.view_artist(artista_id=artist_id)
            print('{:30s} {:10s} {:15s} {:40s}'.format("NAME","BIRTH", "BIRTH PLACE","DESCRIPTION"))
            for i in lista_2:
                print('{:30s} {:10s} {:15s} {:40s}'.format(i[0],i[1],i[2],i[4]))

        elif option == "5":
            # Search Genre
            genre = input("Genre: ")
            lista_1 = Music.search_music_genre(genre = genre)

            print('{:3s} {:20s} {:20s} {:10s}'.format("ID","NAME","DURATION","LYRICS"))
            for m in lista_1:
                print ('{:3s} {:20s} {:20s} {:10s}'.format(str(m[0]),m[1],m[3],m[2]))

            #print(artist.search_artist_genre(genre = genre))

        elif option == "6":
            # Search Playlist
            playlist_name = input("Name: ")
            lista_1 = Playlist.search_playlist(nome=playlist_name, utilizador_id=user_id)

            print('{:3s} {:20s} {:20s} {:10s}'.format("ID","NAME","AUTHOR","TYPE"))
            for m in lista_1:
                print('{:3s} {:20s} {:20s} {:10s}'.format(str(m[0]),m[1],m[2],m[3]))

            playlist_id = input("Write playlist ID to see more: ")
            lista_2 = Playlist.musics_of_playlist(playlist_id)
            print(lista_2)


        elif option == "7":
            # Download Music
            id = input("Choose the ID of the Music you want to download.")
            date = datetime.datetime.now().date()
            user_id = user_id
            x = Music.download_music(music_id = id, date = date, user_id = user_id)
            print(x)

        elif option == "8":
            # Create PLaylist
            playlist_name = input("Name: ")
            playlist_type = input("Type (public or private): ")
            playlist_date = datetime.datetime.now().date()
            playlist_id = Playlist.create_playlist(nome=playlist_name, tipo=playlist_type, data_criacao=playlist_date,utilizador_id=user_id)
            print("Playlist sucessfully created with id: " + str(playlist_id))

        elif option == "9":
            # Add music to playlist
            playlist_id = input("Playlist ID: ")
            music_id = input("Music ID: ")
            index = input("Index of music: ")
            print(Playlist.add_music_to_playlist(playlist_id=playlist_id, musica_id=music_id, indice=index))

        elif option == "10":
            # Make Critic
            critic = input("Critic: ")
            pontuation = input("Pontuation: ")
            album_id = input("Album ID: ")
            x = Album.make_critic(text = critic, pontuation = pontuation, user_id = user_id, album_id = album_id)
            print(x)
        else:
            print("Option invalid. \n Please try again.")

