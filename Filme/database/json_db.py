import json
import os
from typing import List, Dict, Any, Optional

class JsonDatabase:
    def __init__(self, base_path="data"):
        self.base_path = base_path
        self.ensure_base_path()
        self.files = {
            'movies': 'movies.json',
            'rooms': 'rooms.json',
            'sessions': 'sessions.json',
            'tickets': 'tickets.json'
        }

    def ensure_base_path(self):
        """Cria o diretório base se não existir"""
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def get_file_path(self, entity_type: str) -> str:
        """Retorna o caminho completo do arquivo JSON"""
        return os.path.join(self.base_path, self.files[entity_type])

    def read_all(self, entity_type: str) -> List[Dict[str, Any]]:
        """Lê todos os dados de um arquivo JSON"""
        file_path = self.get_file_path(entity_type)
        if not os.path.exists(file_path):
            return []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def write_all(self, entity_type: str, data: List[Dict[str, Any]]):
        """Escreve todos os dados em um arquivo JSON"""
        file_path = self.get_file_path(entity_type)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def find_by_id(self, entity_type: str, entity_id: str) -> Optional[Dict[str, Any]]:
        """Encontra uma entidade pelo ID"""
        all_data = self.read_all(entity_type)
        for item in all_data:
            if item.get('id') == entity_id:
                return item
        return None

    def insert(self, entity_type: str, entity_data: Dict[str, Any]) -> Dict[str, Any]:
        """Insere uma nova entidade"""
        all_data = self.read_all(entity_type)
        all_data.append(entity_data)
        self.write_all(entity_type, all_data)
        return entity_data

    def update(self, entity_type: str, entity_id: str, entity_data: Dict[str, Any]) -> bool:
        """Atualiza uma entidade existente"""
        all_data = self.read_all(entity_type)
        for i, item in enumerate(all_data):
            if item.get('id') == entity_id:
                all_data[i] = entity_data
                self.write_all(entity_type, all_data)
                return True
        return False

    def delete(self, entity_type: str, entity_id: str) -> bool:
        """Remove uma entidade"""
        all_data = self.read_all(entity_type)
        original_length = len(all_data)
        all_data = [item for item in all_data if item.get('id') != entity_id]
        
        if len(all_data) < original_length:
            self.write_all(entity_type, all_data)
            return True
        return False