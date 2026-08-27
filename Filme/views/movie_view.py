class MovieView:
    @staticmethod
    def display_movie(movie):
        """Exibe informações de um filme"""
        print("\n" + "="*50)
        print(f"🎬 {movie.title}")
        print("="*50)
        print(f"ID: {movie.id}")
        print(f"Gênero: {movie.genre}")
        print(f"Duração: {movie.duration_minutes} minutos")
        print(f"Data de Lançamento: {movie.release_date}")
        print(f"Avaliação: {movie.rating:.1f}/10")
        print(f"Descrição: {movie.description}")
        print(f"Criado em: {movie.created_at}")
        print(f"Atualizado em: {movie.updated_at}")
        print("="*50)

    @staticmethod
    def display_movies_list(movies):
        """Exibe lista de filmes"""
        if not movies:
            print("📭 Nenhum filme cadastrado.")
            return
        
        print("\n🎬 Lista de Filmes")
        print("-" * 70)
        print(f"{'ID':<15} {'Título':<30} {'Gênero':<15} {'Duração':<10}")
        print("-" * 70)
        for movie in movies:
            print(f"{movie.id:<15} {movie.title[:28]:<30} {movie.genre:<15} {movie.duration_minutes}min")
        print("-" * 70)

    @staticmethod
    def get_movie_input():
        """Coleta dados para criar/atualizar filme"""
        print("\n📝 Dados do Filme")
        data = {}
        data['title'] = input("Título: ").strip()
        data['description'] = input("Descrição: ").strip()
        data['duration_minutes'] = int(input("Duração (minutos): "))
        data['genre'] = input("Gênero: ").strip()
        data['release_date'] = input("Data de Lançamento (YYYY-MM-DD): ").strip()
        data['rating'] = float(input("Avaliação (0-10): ") or 0.0)
        return data