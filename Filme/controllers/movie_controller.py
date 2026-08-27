from models.movie import Movie
from database.json_db import JsonDatabase
from typing import List, Optional

class MovieController:
    def __init__(self, db: JsonDatabase):
        self.db = db
        self.entity_type = 'movies'

    def create_movie(self, title, description, duration_minutes, genre, 
                     release_date, rating=0.0) -> Movie:
        """Cria um novo filme"""
        movie = Movie(
            title=title,
            description=description,
            duration_minutes=duration_minutes,
            genre=genre,
            release_date=release_date,
            rating=rating
        )
        self.db.insert(self.entity_type, movie.to_dict())
        return movie

    def get_movie(self, movie_id: str) -> Optional[Movie]:
        """Busca filme por ID"""
        movie_data = self.db.find_by_id(self.entity_type, movie_id)
        return Movie.from_dict(movie_data) if movie_data else None

    def get_all_movies(self) -> List[Movie]:
        """Retorna todos os filmes"""
        movies_data = self.db.read_all(self.entity_type)
        return [Movie.from_dict(data) for data in movies_data]

    def update_movie(self, movie_id: str, **kwargs) -> Optional[Movie]:
        """Atualiza um filme"""
        movie = self.get_movie(movie_id)
        if not movie:
            return None
        
        for key, value in kwargs.items():
            if hasattr(movie, key):
                setattr(movie, key, value)
        
        from datetime import datetime
        movie.updated_at = datetime.now().isoformat()
        
        if self.db.update(self.entity_type, movie_id, movie.to_dict()):
            return movie
        return None

    def delete_movie(self, movie_id: str) -> bool:
        """Remove um filme"""
        return self.db.delete(self.entity_type, movie_id)

    def search_movies(self, search_term: str) -> List[Movie]:
        """Busca filmes por título ou gênero"""
        all_movies = self.get_all_movies()
        search_term = search_term.lower()
        return [
            movie for movie in all_movies
            if search_term in movie.title.lower() or 
               search_term in movie.genre.lower()
        ]