from models.session import Session
from database.json_db import JsonDatabase
from typing import List, Optional

class SessionController:
    def __init__(self, db: JsonDatabase):
        self.db = db
        self.entity_type = 'sessions'

    def create_session(self, movie_id, room_id, date_time, price, available_seats) -> Session:
        """Cria uma nova sessão"""
        session = Session(
            movie_id=movie_id,
            room_id=room_id,
            date_time=date_time,
            price=price,
            available_seats=available_seats
        )
        self.db.insert(self.entity_type, session.to_dict())
        return session

    def get_session(self, session_id: str) -> Optional[Session]:
        """Busca sessão por ID"""
        session_data = self.db.find_by_id(self.entity_type, session_id)
        return Session.from_dict(session_data) if session_data else None

    def get_all_sessions(self) -> List[Session]:
        """Retorna todas as sessões"""
        sessions_data = self.db.read_all(self.entity_type)
        return [Session.from_dict(data) for data in sessions_data]

    def get_sessions_by_movie(self, movie_id: str) -> List[Session]:
        """Retorna sessões de um filme específico"""
        all_sessions = self.get_all_sessions()
        return [session for session in all_sessions if session.movie_id == movie_id]

    def update_session(self, session_id: str, **kwargs) -> Optional[Session]:
        """Atualiza uma sessão"""
        session = self.get_session(session_id)
        if not session:
            return None
        
        for key, value in kwargs.items():
            if hasattr(session, key):
                setattr(session, key, value)
        
        from datetime import datetime
        session.updated_at = datetime.now().isoformat()
        
        if self.db.update(self.entity_type, session_id, session.to_dict()):
            return session
        return None

    def delete_session(self, session_id: str) -> bool:
        """Remove uma sessão"""
        return self.db.delete(self.entity_type, session_id)