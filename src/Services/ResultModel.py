import segno 
from PyQt5.QtWidgets import QListWidgetItem
from io import BytesIO

class Result():
    def __init__(self,name:str,passwords:list[str]):
        self.name = name
        self.passwords = self.generate_passwords(passwords)
    
    def generate_passwords(self,passwords:list[str]) -> list['Password']:
        l = []
        for password in passwords:
            l.append(Password(password))
        return l


class Password(QListWidgetItem):

    def __init__(self,text):
        super().__init__()
        self.set_text(text)
        self.set_qr()
    
    def get_text(self) -> str:
        return self.text()
    
    def set_text(self,text):
        self.setText(text)

    def get_bytes(self):
        bytes = self.qr.read()
        self.qr.seek(0)
        return bytes

    def get_qr(self) -> BytesIO:
        return self.qr
    
    def set_qr(self):
        qr = segno.make(self.text())
        self.qr = BytesIO()
        qr.save(self.qr, kind='png',scale=10)
        self.qr.seek(0)
    