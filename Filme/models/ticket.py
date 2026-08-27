from datetime import datetime
from enum import Enum

class TicketStatus(Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    SOLD = "sold"
    CANCELLED = "cancelled"

class Ticket:
    def __init__(self, id=None, session_id="", seat_number="", 
                 customer_name="", customer_email="", status=TicketStatus.AVAILABLE.value):
        self.id = id or datetime.now().strftime("%Y%m%d%H%M%S")
        self.session_id = session_id
        self.seat_number = seat_number
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.status = status
        self.purchase_date = None
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            'id': self.id,
            'session_id': self.session_id,
            'seat_number': self.seat_number,
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'status': self.status,
            'purchase_date': self.purchase_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        ticket = cls(
            id=data.get('id'),
            session_id=data.get('session_id', ''),
            seat_number=data.get('seat_number', ''),
            customer_name=data.get('customer_name', ''),
            customer_email=data.get('customer_email', ''),
            status=data.get('status', TicketStatus.AVAILABLE.value)
        )
        ticket.purchase_date = data.get('purchase_date')
        ticket.created_at = data.get('created_at', ticket.created_at)
        ticket.updated_at = data.get('updated_at', ticket.updated_at)
        return ticket