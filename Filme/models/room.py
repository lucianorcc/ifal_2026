from datetime import datetime

class Room:
    def __init__(self, id=None, name="", capacity=0, room_type="standard"):
        self.id = id or datetime.now().strftime("%Y%m%d%H%M%S")
        self.name = name
        self.capacity = capacity
        self.room_type = room_type  # standard, vip, 3d, imax
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'capacity': self.capacity,
            'room_type': self.room_type,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        room = cls(
            id=data.get('id'),
            name=data.get('name', ''),
            capacity=data.get('capacity', 0),
            room_type=data.get('room_type', 'standard')
        )
        room.created_at = data.get('created_at', room.created_at)
        room.updated_at = data.get('updated_at', room.updated_at)
        return room