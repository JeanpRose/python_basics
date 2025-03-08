'''
Crea un classe Studente che abbia come attributi:
nome, cognome, anno di nascita, classe, voto_ita, voto_mate, voto_inglese
- Crea un metodo per calcolare l'etÃ
- Crea un metodo per calcolare la media di ogni studente
- Crea un metodo scheda per vedere i dati di ogni studente (__str__)
'''
from datetime import datetime
class Studente:
    def __init__(self, nome : str, cognome: str, anno_nascita : int, classe: str, voto_ita: float, voto_mate: float, voto_ing: float):
        self.nome = nome.title()
        self.cognome = cognome. title()
        self.anno_nascita  = int(anno_nascita)
        self.classe = classe
        self.voto_ita = float(voto_ita)
        self.voto_mate = float(voto_mate)
        self.voto_ing =  float(voto_ing)
    
    def eta_alunno(self):
        anno_corrente = datetime.now()
        eta = anno_corrente.year - self.anno_nascita
        return eta
    
    def media_studente (self):
        media = (self.voto_ing+ self.voto_mate+self.voto_ita)/3
        return media
    def __str__(self):
        return f"""{"-"*50}
Nome: {self.nome}
Cognome: {self.cognome}
Anno di nascita: {self.anno_nascita}
Classe: {self.classe}
Voto italiano: {self.voto_ita}
Voto matematica: {self.voto_mate}
Voto inglese : {self.voto_ing} 

L'età di {self.nome} è {self.eta_alunno()} anni
La media di {self.nome} è {round (self.media_studente(), 2)}
{"-"*50}
"""
    

        

    
