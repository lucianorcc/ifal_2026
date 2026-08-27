class MainView:
    @staticmethod
    def show_main_menu():
        """Exibe o menu principal"""
        print("\n🎬 SISTEMA DE GERENCIAMENTO DE CINEMA 🎬")
        print("=" * 50)
        print("1. 📽️  Gerenciar Filmes")
        print("2. 🏢 Gerenciar Salas")
        print("3. 📅 Gerenciar Sessões")
        print("4. 🎫 Gerenciar Tickets")
        print("5. 📊 Relatórios")
        print("0. 🚪 Sair")
        print("=" * 50)
        return input("Escolha uma opção: ").strip()

    @staticmethod
    def show_movie_menu():
        """Exibe o menu de filmes"""
        print("\n📽️  GERENCIAR FILMES")
        print("-" * 40)
        print("1. ➕ Adicionar Filme")
        print("2. 📋 Listar Filmes")
        print("3. 🔍 Buscar Filme")
        print("4. ✏️  Atualizar Filme")
        print("5. 🗑️  Remover Filme")
        print("0. ⬅️  Voltar")
        print("-" * 40)
        return input("Escolha uma opção: ").strip()

    @staticmethod
    def show_report_menu():
        """Exibe o menu de relatórios"""
        print("\n📊 RELATÓRIOS")
        print("-" * 40)
        print("1. 📈 Vendas por Sessão")
        print("2. 🎬 Filmes Mais Populares")
        print("3. 💰 Receita Total")
        print("0. ⬅️  Voltar")
        print("-" * 40)
        return input("Escolha uma opção: ").strip()

    @staticmethod
    def show_message(message, type="info"):
        """Exibe mensagens formatadas"""
        symbols = {
            "info": "ℹ️",
            "success": "✅",
            "error": "❌",
            "warning": "⚠️"
        }
        symbol = symbols.get(type, "ℹ️")
        print(f"\n{symbol} {message}")