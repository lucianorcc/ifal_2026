from database.json_db import JsonDatabase
from controllers.movie_controller import MovieController
from controllers.room_controller import RoomController
from controllers.session_controller import SessionController
from controllers.ticket_controller import TicketController
from views.movie_view import MovieView
from views.main_view import MainView
from datetime import datetime

class CinemaManagementSystem:
    def __init__(self):
        # Inicializar banco de dados
        self.db = JsonDatabase()
        
        # Inicializar controllers
        self.movie_controller = MovieController(self.db)
        self.room_controller = RoomController(self.db)
        self.session_controller = SessionController(self.db)
        self.ticket_controller = TicketController(self.db)
        
        # Inicializar views
        self.movie_view = MovieView()
        self.main_view = MainView()
        
        # Dados de exemplo (apenas para primeira execução)
        self.initialize_sample_data()

    def initialize_sample_data(self):
        """Inicializa dados de exemplo se o sistema estiver vazio"""
        if not self.movie_controller.get_all_movies():
            # Criar filmes de exemplo
            movie1 = self.movie_controller.create_movie(
                title="O Poderoso Chefão",
                description="A saga da família Corleone",
                duration_minutes=175,
                genre="Drama",
                release_date="1972-03-24",
                rating=9.2
            )
            
            movie2 = self.movie_controller.create_movie(
                title="Matrix",
                description="Realidade virtual e revolução",
                duration_minutes=136,
                genre="Ficção Científica",
                release_date="1999-03-31",
                rating=8.7
            )
            
            movie3 = self.movie_controller.create_movie(
                title="Vingadores: Ultimato",
                description="A batalha final dos Vingadores",
                duration_minutes=181,
                genre="Ação",
                release_date="2019-04-26",
                rating=8.4
            )
            
            # Criar salas de exemplo
            room1 = self.room_controller.create_room(
                name="Sala 1",
                capacity=100,
                room_type="standard"
            )
            
            room2 = self.room_controller.create_room(
                name="Sala 2",
                capacity=150,
                room_type="vip"
            )
            
            room3 = self.room_controller.create_room(
                name="Sala 3D",
                capacity=80,
                room_type="3d"
            )
            
            # Criar sessões de exemplo
            session1 = self.session_controller.create_session(
                movie_id=movie1.id,
                room_id=room1.id,
                date_time="2024-01-15 19:00",
                price=35.00,
                available_seats=100
            )
            
            session2 = self.session_controller.create_session(
                movie_id=movie2.id,
                room_id=room2.id,
                date_time="2024-01-15 21:00",
                price=45.00,
                available_seats=150
            )
            
            session3 = self.session_controller.create_session(
                movie_id=movie3.id,
                room_id=room3.id,
                date_time="2024-01-16 18:30",
                price=50.00,
                available_seats=80
            )
            
            print("✅ Dados de exemplo criados com sucesso!")

    def run(self):
        """Executa o sistema principal"""
        while True:
            option = self.main_view.show_main_menu()
            
            if option == "1":
                self.manage_movies()
            elif option == "2":
                self.manage_rooms()
            elif option == "3":
                self.manage_sessions()
            elif option == "4":
                self.manage_tickets()
            elif option == "5":
                self.show_reports()
            elif option == "0":
                print("\n👋 Obrigado por usar o Sistema de Gerenciamento de Cinema!")
                break
            else:
                self.main_view.show_message("Opção inválida!", "error")

    def manage_movies(self):
        """Gerencia operações de filmes"""
        while True:
            option = self.main_view.show_movie_menu()
            
            if option == "1":
                # Adicionar filme
                movie_data = self.movie_view.get_movie_input()
                movie = self.movie_controller.create_movie(**movie_data)
                self.main_view.show_message(f"Filme '{movie.title}' criado com sucesso!", "success")
            
            elif option == "2":
                # Listar filmes
                movies = self.movie_controller.get_all_movies()
                self.movie_view.display_movies_list(movies)
            
            elif option == "3":
                # Buscar filme
                search_term = input("Digite o termo de busca: ").strip()
                results = self.movie_controller.search_movies(search_term)
                self.movie_view.display_movies_list(results)
            
            elif option == "4":
                # Atualizar filme
                movie_id = input("ID do filme a atualizar: ").strip()
                movie = self.movie_controller.get_movie(movie_id)
                if movie:
                    self.movie_view.display_movie(movie)
                    movie_data = self.movie_view.get_movie_input()
                    updated_movie = self.movie_controller.update_movie(movie_id, **movie_data)
                    if updated_movie:
                        self.main_view.show_message("Filme atualizado com sucesso!", "success")
                else:
                    self.main_view.show_message("Filme não encontrado!", "error")
            
            elif option == "5":
                # Remover filme
                movie_id = input("ID do filme a remover: ").strip()
                if self.movie_controller.delete_movie(movie_id):
                    self.main_view.show_message("Filme removido com sucesso!", "success")
                else:
                    self.main_view.show_message("Filme não encontrado!", "error")
            
            elif option == "0":
                break
            else:
                self.main_view.show_message("Opção inválida!", "error")

    def manage_rooms(self):
        """Gerencia operações de salas"""
        print("\n🏢 Gerenciamento de Salas")
        print("-" * 40)
        print("1. ➕ Adicionar Sala")
        print("2. 📋 Listar Salas")
        print("0. ⬅️  Voltar")
        print("-" * 40)
        
        option = input("Escolha uma opção: ").strip()
        
        if option == "1":
            name = input("Nome da sala: ").strip()
            capacity = int(input("Capacidade: "))
            room_type = input("Tipo (standard/vip/3d/imax): ").strip().lower()
            
            room = self.room_controller.create_room(name, capacity, room_type)
            self.main_view.show_message(f"Sala '{room.name}' criada com sucesso!", "success")
        
        elif option == "2":
            rooms = self.room_controller.get_all_rooms()
            if rooms:
                print("\n🏢 Lista de Salas")
                print("-" * 60)
                print(f"{'ID':<15} {'Nome':<20} {'Capacidade':<12} {'Tipo':<10}")
                print("-" * 60)
                for room in rooms:
                    print(f"{room.id:<15} {room.name:<20} {room.capacity:<12} {room.room_type:<10}")
                print("-" * 60)
            else:
                print("📭 Nenhuma sala cadastrada.")

    def manage_sessions(self):
        """Gerencia operações de sessões"""
        print("\n📅 Gerenciamento de Sessões")
        print("-" * 40)
        print("1. ➕ Adicionar Sessão")
        print("2. 📋 Listar Sessões")
        print("0. ⬅️  Voltar")
        print("-" * 40)
        
        option = input("Escolha uma opção: ").strip()
        
        if option == "1":
            # Listar filmes disponíveis
            movies = self.movie_controller.get_all_movies()
            self.movie_view.display_movies_list(movies)
            movie_id = input("ID do filme: ").strip()
            
            # Listar salas disponíveis
            rooms = self.room_controller.get_all_rooms()
            if rooms:
                print("\n🏢 Salas Disponíveis")
                for room in rooms:
                    print(f"  - ID: {room.id}, Nome: {room.name}, Capacidade: {room.capacity}")
            room_id = input("ID da sala: ").strip()
            
            date_time = input("Data e Hora (YYYY-MM-DD HH:MM): ").strip()
            price = float(input("Preço do ingresso: R$ "))
            
            # Buscar capacidade da sala
            room = self.room_controller.get_room(room_id)
            available_seats = room.capacity if room else 0
            
            session = self.session_controller.create_session(
                movie_id, room_id, date_time, price, available_seats
            )
            self.main_view.show_message("Sessão criada com sucesso!", "success")
        
        elif option == "2":
            sessions = self.session_controller.get_all_sessions()
            if sessions:
                print("\n📅 Lista de Sessões")
                print("-" * 80)
                print(f"{'ID':<15} {'Filme':<25} {'Sala':<15} {'Data/Hora':<20} {'Preço':<10} {'Assentos':<10}")
                print("-" * 80)
                
                for session in sessions:
                    movie = self.movie_controller.get_movie(session.movie_id)
                    room = self.room_controller.get_room(session.room_id)
                    
                    movie_title = movie.title if movie else "Filme não encontrado"
                    room_name = room.name if room else "Sala não encontrada"
                    
                    print(f"{session.id:<15} {movie_title[:23]:<25} {room_name:<15} "
                          f"{session.date_time:<20} R${session.price:<8.2f} {session.available_seats:<10}")
                print("-" * 80)
            else:
                print("📭 Nenhuma sessão cadastrada.")

    def manage_tickets(self):
        """Gerencia operações de tickets"""
        print("\n🎫 Gerenciamento de Tickets")
        print("-" * 40)
        print("1. 🎫 Vender Ticket")
        print("2. 📋 Listar Tickets")
        print("3. ❌ Cancelar Ticket")
        print("0. ⬅️  Voltar")
        print("-" * 40)
        
        option = input("Escolha uma opção: ").strip()
        
        if option == "1":
            # Listar sessões disponíveis
            sessions = self.session_controller.get_all_sessions()
            if sessions:
                print("\n📅 Sessões Disponíveis")
                for session in sessions:
                    movie = self.movie_controller.get_movie(session.movie_id)
                    room = self.room_controller.get_room(session.room_id)
                    movie_title = movie.title if movie else "Filme não encontrado"
                    room_name = room.name if room else "Sala não encontrada"
                    print(f"  - ID: {session.id}, Filme: {movie_title}, "
                          f"Sala: {room_name}, Data: {session.date_time}, "
                          f"Assentos: {session.available_seats}")
            
            session_id = input("\nID da sessão: ").strip()
            seat_number = input("Número do assento: ").strip()
            customer_name = input("Nome do cliente: ").strip()
            customer_email = input("Email do cliente: ").strip()
            
            ticket = self.ticket_controller.create_ticket(
                session_id, seat_number, customer_name, customer_email
            )
            
            # Vender o ticket
            sold_ticket = self.ticket_controller.sell_ticket(ticket.id)
            
            if sold_ticket:
                # Atualizar assentos disponíveis
                session = self.session_controller.get_session(session_id)
                if session:
                    self.session_controller.update_session(
                        session_id, 
                        available_seats=session.available_seats - 1
                    )
                
                self.main_view.show_message(
                    f"Ticket vendido com sucesso! Assento: {seat_number}", 
                    "success"
                )
            else:
                self.main_view.show_message("Erro ao vender ticket!", "error")
        
        elif option == "2":
            tickets = self.ticket_controller.get_all_tickets()
            if tickets:
                print("\n🎫 Lista de Tickets")
                print("-" * 80)
                print(f"{'ID':<15} {'Sessão':<15} {'Assento':<10} {'Cliente':<20} {'Status':<12}")
                print("-" * 80)
                
                for ticket in tickets:
                    print(f"{ticket.id:<15} {ticket.session_id[:13]:<15} "
                          f"{ticket.seat_number:<10} {ticket.customer_name:<20} "
                          f"{ticket.status:<12}")
                print("-" * 80)
            else:
                print("📭 Nenhum ticket cadastrado.")
        
        elif option == "3":
            ticket_id = input("ID do ticket a cancelar: ").strip()
            if self.ticket_controller.cancel_ticket(ticket_id):
                self.main_view.show_message("Ticket cancelado com sucesso!", "success")
            else:
                self.main_view.show_message("Ticket não encontrado!", "error")

    def show_reports(self):
        """Exibe relatórios do sistema"""
        while True:
            option = self.main_view.show_report_menu()
            
            if option == "1":
                self.report_sales_by_session()
            elif option == "2":
                self.report_popular_movies()
            elif option == "3":
                self.report_total_revenue()
            elif option == "0":
                break
            else:
                self.main_view.show_message("Opção inválida!", "error")

    def report_sales_by_session(self):
        """Relatório de vendas por sessão"""
        sessions = self.session_controller.get_all_sessions()
        tickets = self.ticket_controller.get_all_tickets()
        
        print("\n📈 Vendas por Sessão")
        print("-" * 60)
        
        for session in sessions:
            movie = self.movie_controller.get_movie(session.movie_id)
            movie_title = movie.title if movie else "Filme não encontrado"
            
            sold_tickets = [t for t in tickets 
                          if t.session_id == session.id and t.status == "sold"]
            
            revenue = len(sold_tickets) * session.price
            
            print(f"Sessão: {session.id[:8]}...")
            print(f"  Filme: {movie_title}")
            print(f"  Data: {session.date_time}")
            print(f"  Tickets Vendidos: {len(sold_tickets)}")
            print(f"  Receita: R$ {revenue:.2f}")
            print("-" * 60)

    def report_popular_movies(self):
        """Relatório de filmes mais populares"""
        movies = self.movie_controller.get_all_movies()
        sessions = self.session_controller.get_all_sessions()
        tickets = self.ticket_controller.get_all_tickets()
        
        print("\n🎬 Filmes Mais Populares")
        print("-" * 60)
        
        movie_stats = []
        
        for movie in movies:
            movie_sessions = [s for s in sessions if s.movie_id == movie.id]
            total_tickets = 0
            
            for session in movie_sessions:
                sold_tickets = [t for t in tickets 
                              if t.session_id == session.id and t.status == "sold"]
                total_tickets += len(sold_tickets)
            
            movie_stats.append({
                'title': movie.title,
                'sessions': len(movie_sessions),
                'tickets_sold': total_tickets,
                'rating': movie.rating
            })
        
        # Ordenar por tickets vendidos
        movie_stats.sort(key=lambda x: x['tickets_sold'], reverse=True)
        
        for i, stat in enumerate(movie_stats, 1):
            print(f"{i}. {stat['title']}")
            print(f"   Sessões: {stat['sessions']}")
            print(f"   Tickets Vendidos: {stat['tickets_sold']}")
            print(f"   Avaliação: {stat['rating']:.1f}/10")
            print()

    def report_total_revenue(self):
        """Relatório de receita total"""
        sessions = self.session_controller.get_all_sessions()
        tickets = self.ticket_controller.get_all_tickets()
        
        total_revenue = 0
        total_tickets = 0
        
        print("\n💰 Receita Total")
        print("-" * 40)
        
        for session in sessions:
            sold_tickets = [t for t in tickets 
                          if t.session_id == session.id and t.status == "sold"]
            
            session_revenue = len(sold_tickets) * session.price
            total_revenue += session_revenue
            total_tickets += len(sold_tickets)
        
        print(f"Total de Tickets Vendidos: {total_tickets}")
        print(f"Receita Total: R$ {total_revenue:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    system = CinemaManagementSystem()
    system.run()