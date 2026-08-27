from datetime import datetime

class Session:
    def __init__(self, id=None, movie_id="", room_id="", date_time="", 
                 price=0.0, available_seats=0):
        self.id = id or datetime.now().strftime("%Y%m%d%H%M%S")
        self.movie_id = movie_id
        self.room_id = room_id
        self.date_time = date_time
        self.price = price
        self.available_seats = available_seats
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'room_id': self.room_id,
            'date_time': self.date_time,
            'price': self.price,
            'available_seats': self.available_seats,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        session = cls(
            id=data.get('id'),
            movie_id=data.get('movie_id', ''),
            room_id=data.get('room_id', ''),
            date_time=data.get('date_time', ''),
            price=data.get('price', 0.0),
            available_seats=data.get('available_seats', 0)
        )
        session.created_at = data.get('created_at', session.created_at)
        session.updated_at = data.get('updated_at', session.updated_at)
        return session