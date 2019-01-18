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
    while option != "2" or option != "3" or option != "4" or option != "5" or option != "6" or option != "7" or option != "8" or option != "9" or option != "10" or option != "11" or option != "12" or option != "13" or option != "14" or option != "15" or option != "16" or option != "17" or option != "18" or option != "19":

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
        print("| 11 | - Insert Music")
        print("| 12 | - Insert Album")
        print("| 13 | - Insert Concert")
        print("| 14 | - Insert Artist")
        print("| 15 | - Delete Music")
        print("| 16 | - Delete Album")
        print("| 17 | - Delete Artist")
        print("| 18 | - Delete Playlist")
        print("| 19 | - Change Playlist Name")
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
            print('{:10s} {:10s} {:10s} {:40s}'.format("NAME","BIRTH", "BIRTH PLACE","DESCRIPTION"))
            for i in lista_2:
                print('{:10s} {:10s} {:10s} {:40s}'.format(i[0],i[1],i[2],i[4]))

        elif option == "5":
            # Search Genre
            genre = input("Genre: ")
            lista_1 = Music.search_music_genre(genre = genre)
            print(genre, "musics: \n")
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
            index = input("Index of musica: ")
            print(Playlist.add_music_to_playlist(playlist_id=playlist_id, musica_id=music_id, indice=index))

        elif option == "10":
            # Make Critic
            critic = input("Critic: ")
            pontuation = input("Pontuation: ")
            album_id = input("Album ID: ")
            Album.make_critic(text = critic, pontuation = pontuation, user_id = user_id, album_id = album_id)

        elif option == "11":
            # Insert Music
            music_name     = input("Name:")
            music_lyrics   = input("Lyrics:")
            music_duration = input("Duration:")
            music_id = Music.insert_music(name = music_name, lyrics = music_lyrics, duration = music_duration)

            x = input("Associate Music to an Album? \n 1 - Yes | 2 - No \n")
            if x == "1":
                album_id = input("Album ID: ")
                index = input("Music position: ")
                print(Music.insert_music_album(album_id = album_id, musica_id = music_id, index = index))

            y = input("Associate Music to an Concert? \n 1 - Yes | 2 - No \n")
            if y == "1":
                concert_id = input("Concert ID: ")
                index = input("Music position: ")
                print(Music.insert_music_concert(concert_id = concert_id, musica_id = music_id, index = index))

            z = input("Associate Music to an Artist? \n 1 - Yes | 2 - No \n")
            if z == "1":
                artist_id = input("Artist ID: ")
                print(Music.insert_music_artist(artist_id = artist_id, musica_id = music_id))

        elif option == "12":
            # Insert Album
            album_name   = input("Name:")
            album_data   = input("Data:")
            album_description = input("Description:")
            album_duration    = input("Duration:")
            album_id = Album.insert_album(name = album_name, data = album_data, description = album_description, duration = album_duration)

            x = input("Associate Album to an Artist? \n 1 - Yes | 2 - No \n")
            if x == "1":
                artist_id = input("Artist ID: ")
                Album.insert_album_artist(artist_id = artist_id, album_id = album_id)

        elif option == "13":
            # Insert Concert
            concert_name  = input("Name:")
            concert_data  = input("Data:")
            concert_place = input("Place:")
            concert_lotation = input("Lotation:")
            concert_id = Concert.insert_concert(name = concert_name, data = concert_data, place = concert_place, lotation = concert_lotation)

            x = input("Associate Concert to an Artist? \n 1 - Yes | 2 - No \n")
            if x == "1":
                artist_id = input("Artist ID: ")
                concert.insert_concert_artist(artist_id = artist_id, concert_id = concert_id)

        elif option == "14":
            # Insert Artist
            artist_name = input("Name: ")
            artist_data_nascimento  = input("Birthday: ")
            artist_local_nascimento = input("Place of birth: ")
            artist_tipo = input("Type: ")
            artist_descricao = input("Description: ")
            id = Artist.add_artist(nome=artist_name, data_nascimento=artist_data_nascimento, local_nascimento=artist_local_nascimento, tipo=artist_tipo, descricao=artist_descricao)
            print("Artist added sucessfully with id: " + str(id))
            answer = input("Does this artist belong to any band? [1] if Yes, [2] if No: \n")
            if answer == "1":
                band_id = input("Band id: ")
                entering_date = input("Joining date (yyyy-mm-dd): ")
                is_artist_at_band = input("Is the artist curretly in the band? [1] if Yes, [2] if No: \n")
                if is_artist_at_band == "1":
                    leaving_date = 'None'
                else:
                    leaving_date = input("Insert date (yyyy-mm-dd): ")
                sysout = Artist.add_artist_to_band(artista_id=id,banda_id=band_id, data_entrada=entering_date, data_saida=leaving_date)
                if sysout == "Added":
                    print("Artist added to band successfully.")
                else:
                    print("Something went wrong.")

        elif option == "15":
            # Remove Music
            music_id = input("Music ID: ")
            x = Music.delete_music(music_id=music_id)
            print(x)

        elif option == "16":
            # Remove Album
            album_id = input("Album ID: ")
            x = Album.delete_album(album_id)
            print(x)

        elif option == "17":
            # Remove Artist
            artist_id = input("Artist ID: ")
            x = Artist.delete_artist(artist_id=artist_id)
            print(x)

        elif option == "18":
            #Remove playlist
            playlist_id = input("Playlist ID: ")
            x = Playlist.delete_playlist(playlist_id, user_id)
            print(x)

        elif option == "19":
            # Update Playlist Name
            playlist_id = input("Playlist ID: ")
            playlist_name = input("New name: ")
            x = Playlist.change_playlist_name(new_name=playlist_name, playlist_id=playlist_id, user_id=user_id)
            print(x)
        else:
            print("Option invalid. \n Please try again.")


