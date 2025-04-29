import re
from io import BytesIO
from pypdf import PdfReader

class PdfExtractor:
    def __init__(self, file_path_or_bytes):
        if isinstance(file_path_or_bytes, bytes):
            self.file_buffer = BytesIO(file_path_or_bytes)
        else:
            self.file_buffer = file_path_or_bytes
        
        self.text = self._extract_text()

    def _extract_text(self):
        try:
            reader = PdfReader(self.file_buffer)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
        except Exception as e:
            print(f"Erro ao extrair texto do PDF: {str(e)}")
            return None
    
    def extract_data(self, pattern):
        match = re.search(pattern, self.text)
        if match:
            if match.lastindex:
                return match.group(1).strip()
            return match.group(0).strip()
        return "N/A"

    def extract_fields(self, patterns):
        """
        Função para extrair múltiplos campos a partir de um dicionário de padrões.
        
        - patterns: Um dicionário de campos e padrões de regex.
        """
        extracted_data = {}
        for field, pattern in patterns.items():
            extracted_data[field] = self.extract_data(pattern)
        
        return extracted_data
