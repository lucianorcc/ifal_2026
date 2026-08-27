from models.room import Room
from database.json_db import JsonDatabase
from typing import List, Optional

class RoomController:
    def __init__(self, db: JsonDatabase):
        self.db = db
        self.entity_type = 'rooms'

    def create_room(self, name, capacity, room_type="standard") -> Room:
        """Cria uma nova sala"""
        room = Room(
            name=name,
            capacity=capacity,
            room_type=room_type
        )
        self.db.insert(self.entity_type, room.to_dict())
        return room

    def get_room(self, room_id: str) -> Optional[Room]:
        """Busca sala por ID"""
        room_data = self.db.find_by_id(self.entity_type, room_id)
        return Room.from_dict(room_data) if room_data else None

    def get_all_rooms(self) -> List[Room]:
        """Retorna todas as salas"""
        rooms_data = self.db.read_all(self.entity_type)
        return [Room.from_dict(data) for data in rooms_data]

    def update_room(self, room_id: str, **kwargs) -> Optional[Room]:
        """Atualiza uma sala"""
        room = self.get_room(room_id)
        if not room:
            return None
        
        for key, value in kwargs.items():
            if hasattr(room, key):
                setattr(room, key, value)
        
        from datetime import datetime
        room.updated_at = datetime.now().isoformat()
        
        if self.db.update(self.entity_type, room_id, room.to_dict()):
            return room
        return None

    def delete_room(self, room_id: str) -> bool:
        """Remove uma sala"""
        return self.db.delete(self.entity_type, room_id)