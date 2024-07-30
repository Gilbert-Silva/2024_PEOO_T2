from playlist import Playlist
from musica import Musica

class UI:
    @staticmethod
    def menu():
        print("1-Nova Playlist, 2-Inserir Música, 3-Listar Músicas, 4-Info, 5-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        print("Bem-vindo(a) ao IF Música")
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: p = UI.nova_playlist()
            if op == 2: UI.inserir_musica(p)
            if op == 3: UI.listar_musica(p)
            if op == 4: UI.info(p)
        print("Bye") 
    @staticmethod
    def nova_playlist():
        nome = input("Informe o nome da playlist: ")
        desc = input("Informe uma descrição para a playlist: ")
        p = Playlist(nome, desc)
        return p
    @staticmethod
    def inserir_musica(p):
        titulo = input("Informe o título da música: ")
        artista = input("Informe o artista: ")
        album = input("Informe o álbum: ")
        m = Musica()
        m.set_titulo(titulo)
        m.set_artista(artista)
        m.set_album(album)
        p.inserir(m)
    @staticmethod
    def listar_musica(p):
        print("Músicas inseridas na Playlist")
        for m in p.listar(): print(m)
    @staticmethod
    def info(p):
        print(p)

UI.main()
