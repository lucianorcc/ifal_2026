from models.ticket import Ticket, TicketStatus
from database.json_db import JsonDatabase
from typing import List, Optional

class TicketController:
    def __init__(self, db: JsonDatabase):
        self.db = db
        self.entity_type = 'tickets'

    def create_ticket(self, session_id, seat_number, customer_name="", 
                      customer_email="") -> Ticket:
        """Cria um novo ticket"""
        ticket = Ticket(
            session_id=session_id,
            seat_number=seat_number,
            customer_name=customer_name,
            customer_email=customer_email
        )
        self.db.insert(self.entity_type, ticket.to_dict())
        return ticket

    def get_ticket(self, ticket_id: str) -> Optional[Ticket]:
        """Busca ticket por ID"""
        ticket_data = self.db.find_by_id(self.entity_type, ticket_id)
        return Ticket.from_dict(ticket_data) if ticket_data else None

    def get_all_tickets(self) -> List[Ticket]:
        """Retorna todos os tickets"""
        tickets_data = self.db.read_all(self.entity_type)
        return [Ticket.from_dict(data) for data in tickets_data]

    def get_tickets_by_session(self, session_id: str) -> List[Ticket]:
        """Retorna tickets de uma sessão específica"""
        all_tickets = self.get_all_tickets()
        return [ticket for ticket in all_tickets if ticket.session_id == session_id]

    def sell_ticket(self, ticket_id: str) -> Optional[Ticket]:
        """Vende um ticket"""
        ticket = self.get_ticket(ticket_id)
        if not ticket or ticket.status != TicketStatus.AVAILABLE.value:
            return None
        
        from datetime import datetime
        ticket.status = TicketStatus.SOLD.value
        ticket.purchase_date = datetime.now().isoformat()
        ticket.updated_at = datetime.now().isoformat()
        
        if self.db.update(self.entity_type, ticket_id, ticket.to_dict()):
            return ticket
        return None

    def cancel_ticket(self, ticket_id: str) -> Optional[Ticket]:
        """Cancela um ticket"""
        ticket = self.get_ticket(ticket_id)
        if not ticket:
            return None
        
        from datetime import datetime
        ticket.status = TicketStatus.CANCELLED.value
        ticket.updated_at = datetime.now().isoformat()
        
        if self.db.update(self.entity_type, ticket_id, ticket.to_dict()):
            return ticket
        return None

    def delete_ticket(self, ticket_id: str) -> bool:
        """Remove um ticket"""
        return self.db.delete(self.entity_type, ticket_id)