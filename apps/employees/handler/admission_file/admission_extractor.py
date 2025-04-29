from utils.pdf_parse import PdfExtractor
from apps.employees.handler.admission_file.patterns import pj

class FileAdmissionExtractor(PdfExtractor):
    def __init__(self, file_path_or_bytes):
        super().__init__(file_path_or_bytes)
    
    def extract_pj(self):
        extracted_fields = self.extract_fields(pj)
        return extracted_fields
