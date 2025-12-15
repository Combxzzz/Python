from datetime import date

class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []
        self.playlists = []

    def inscrever(self, quantidade):
        self.inscritos += quantidade

    def add_playlist(self, playlist):
        if playlist in self.playlists:
            print(f"A playlist {playlist} ja foi adicionada!")
        else:
            self.playlists.append(playlist)

    def rmv_playlist(self, playlist):
        if playlist not in self.playlists:
            print(f"A playlist {playlist} nao foi encontrada")
        else:
            self.playlists.remove(playlist)

    #add ou rmv videos
    def add_video(self, video):
        if video in self.videos: 
            print("Esse video ja foi adicionado!")
        else:
            self.videos.append(video)

    def rmv_video(self, video):
        if video not in self.videos:
            print(f"O video {video} nao foi encontrado!")
        else:
            self.videos.remove(video)

    # CORRIGIDO
    def exibir_playlist(self):
        if not self.playlists:
            return "Nenhuma playlist cadastrada."

        saida = []
        for playlist in self.playlists:
            saida.append(playlist.exibir())

        return "\n\n".join(saida)

    def __str__(self):
        if not self.videos:
            videos_formatados = "  (Nenhum vídeo)"
        else:
            videos_formatados = "\n".join([
                f"\n{str(video)}"
                for video in self.videos
            ])

        return (
            f"\n========== CANAL ==========\n"
            f"Nome: {self.nome}\n"
            f"Descrição: {self.descricao}\n"
            f"Inscritos: {self.inscritos}\n"
            f"---------------------------\n"
            f"VÍDEOS:\n{videos_formatados}\n"
            f"===========================\n"
        )

class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []

    def add_membro_equipe(self, *membros):
        for membro in membros:
            if isinstance(membro, list):
                for item in membro:
                    if item not in self._equipe:
                        self._equipe.append(item)
                    else:
                        print(f"O membro {item} ja está na equipe!")
            else:
                if membro not in self._equipe:
                    self._equipe.append(membro)
                else:
                    print(f"O membro {membro} já está na equipe!")

    def rmv_membro_equipe(self, *membros):
        for membro in membros:
            if isinstance(membro, list):
                for item in membro:
                    if item in self._equipe:
                        self._equipe.remove(item)
                    else:
                        print(f"O membro {item} não foi encontrado!")
            else:
                if membro in self._equipe:
                    self._equipe.remove(membro)
                else:
                    print(f"O membro {membro} não foi encontrado!")

    @property
    def exibir_equipe(self):
        return self._equipe
    
    def __str__(self):
        return f"{super().__str__()} | Equipe: {self._equipe}"
    
class Video:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.comentarios = []
        self.likes = 0
        self.deslikes = 0
        self.vizualisao = 0
        self.data_publicacao = date.today().strftime("%d/%m/%Y")

    def assistir_video(self, quantidade):
        self.vizualisao += quantidade

    def like_video(self, quantidade):
        self.likes += quantidade

    def deslike_video(self, quantidade):
        self.deslikes += quantidade

    def add_comentario(self, comentario):
        self.comentarios.append(comentario)

    def __str__(self):
        comentarios_formatados = (
            "   (Sem comentários)" if not self.comentarios
            else "\n".join([f"   - {c}" for c in self.comentarios])
        )

        return (
            f"  Nome: {self.nome}\n"
            f"  Descrição: {self.descricao}\n"
            f"  Data de publicação: {self.data_publicacao}\n"
            f"  Likes: {self.likes} | Deslikes: {self.deslikes}\n"
            f"  Visualizações: {self.vizualisao}\n"
            f"  Comentários:\n{comentarios_formatados}"
        )
    
class Playlist:
    def __init__(self, canal, nome_playlist):
        self.canal = canal
        self.nome_playlist = nome_playlist
        self.videos = []

    def add_video(self, *videos):
        for video in videos:
            if isinstance(video, list):
                for item in video:
                    if item not in self.canal.videos:
                        print(f"O vídeo {item} não está no canal!")
                    elif item in self.videos:
                        print(f"O vídeo {item} já está na playlist!")
                    else:
                        self.videos.append(item)

            else:
                if video not in self.canal.videos:
                    print(f"O vídeo {video} não está no canal!")
                elif video in self.videos:
                    print(f"O vídeo {video} já está na playlist!")
                else:
                    self.videos.append(video)

    def rmv_video(self, *videos):
        for video in videos:
            if isinstance(video, list):
                for item in video:
                    if item in self.videos:
                        self.videos.remove(item)
                    else:
                        print(f"O vídeo {item} não está na playlist!")
            else:
                if video in self.videos:
                    self.videos.remove(video)
                else:
                    print(f"O vídeo {video} não está na playlist!")

    def exibir(self):
        if not self.videos:
            return f"Playlist {self.nome_playlist}:\n  (vazia)"

        linhas = [f"- {v.nome}" for v in self.videos]
        conteudo = "\n".join(linhas)

        return f"Playlist {self.nome_playlist}:\n{conteudo}"


# ------------------------- TESTES ------------------------------

if __name__ == "__main__":
    canal = Canal("ComboZada", "Canal de programação", 1500)

    v1 = Video("Python Básico", "Introdução ao Python")
    v2 = Video("POO Avançado", "Tudo sobre classes")
    v3 = Video("APIs com Python", "Usando requests")

    canal.add_video(v1)
    canal.add_video(v2)
    canal.add_video(v3)

    canal.add_video(v2)

    p1 = Playlist(canal, "Python para Iniciantes")
    p2 = Playlist(canal, "Conteúdo Avançado")

    canal.add_playlist(p1)
    canal.add_playlist(p2)
    canal.add_playlist(p1)

    p1.add_video(v1, v2)
    p2.add_video(v3)

    v_fake = Video("Fake", "Vídeo que não existe")
    p1.add_video(v_fake)

    p1.rmv_video(v2)
    p1.rmv_video(v_fake)

    v1.like_video(10)
    v1.assistir_video(200)
    v1.add_comentario("Muito bom!")
    v1.add_comentario("Excelente explicação!")

    print("\n====== EXIBINDO PLAYLISTS ======")
    print("Playlist 1:", p1.exibir())
    print("Playlist 2:", p2.exibir())

    print("\n====== EXIBINDO CANAL COMPLETO ======")
    print(canal)

    print("\n====== TESTANDO CANAL EMPRESARIAL ======")
    empresa = CanalEmpresarial("EmpresaX", "Canal corporativo", 5000)
    empresa.add_membro_equipe("João", "Maria", ["Carlos", "Ana"])
    empresa.add_membro_equipe("João")
    print(empresa.exibir_equipe)
    empresa.rmv_membro_equipe("Carlos", ["Ana", "Zé"])
    print(empresa)
