from datetime import datetime
import json

class Movie:
    def __init__(self, id=None, title="", description="", duration_minutes=0, 
                 genre="", release_date="", rating=0.0):
        self.id = id or datetime.now().strftime("%Y%m%d%H%M%S")
        self.title = title
        self.description = description
        self.duration_minutes = duration_minutes
        self.genre = genre
        self.release_date = release_date
        self.rating = rating
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'duration_minutes': self.duration_minutes,
            'genre': self.genre,
            'release_date': self.release_date,
            'rating': self.rating,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        movie = cls(
            id=data.get('id'),
            title=data.get('title', ''),
            description=data.get('description', ''),
            duration_minutes=data.get('duration_minutes', 0),
            genre=data.get('genre', ''),
            release_date=data.get('release_date', ''),
            rating=data.get('rating', 0.0)
        )
        movie.created_at = data.get('created_at', movie.created_at)
        movie.updated_at = data.get('updated_at', movie.updated_at)
        return movie