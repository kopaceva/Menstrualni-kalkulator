import datetime
import random
import json

danes = datetime.date.today()

def razlika_dni(x):
    return datetime.timedelta(days=x)

class Cikel:
    def __init__(self, zacetek_cikla, dolzina_cikla, trajanje_menstruacije):
        self.zacetek_cikla = zacetek_cikla
        self.dolzina_cikla = dolzina_cikla
        self.trajanje_menstruacije = trajanje_menstruacije

    def __repr__(self):
        return "Cikel(zacetek_cikla = {0}, dolzina_cikla = {1}, trajanje_mestruacije = {2}".format(self.zacetek_cikla, self.dolzina_cikla, self.trajanje_menstruacije)

    def naslednji_cikel(self, zaporedna_stevilka = 1):
        nov_cikel = self.zacetek_cikla + razlika_dni(zaporedna_stevilka * self.dolzina_cikla)
        return nov_cikel

    def dnevi_menstruacije(self, stevilo_ciklov = 1):
        m_dnevi = []
        for i in range(stevilo_ciklov):
            dan = self.naslednji_cikel(i)
            for j in range(self.trajanje_menstruacije):
                m_dnevi.append(dan)
                dan = dan + razlika_dni(1)
        return m_dnevi

    def prihodnji_cikel(self):
        if self.naslednji_cikel() >= danes:
            return self.naslednji_cikel()
        else:
            x = 2
            while self.naslednji_cikel(x) < danes:
                x += 1
            return self.naslednji_cikel(x)

    def ovulacija(self, stevilo_ciklov = 1):
        return self.zacetek_cikla - razlika_dni(14) + stevilo_ciklov * razlika_dni(self.dolzina_cikla)
    
    def dnevi_ovulacije(self, stevilo_ciklov = 1):
        o_dnevi = []
        dan = self.ovulacija()
        for i in range(stevilo_ciklov):
            o_dnevi.append(dan)
            dan = dan + razlika_dni(self.dolzina_cikla)
        return o_dnevi

    def prihodnja_ovulacija(self):
        if self.ovulacija() >= danes:
            return self.ovulacija()
        else:
            x = 1
            while self.ovulacija(x) < danes:
                x += 1
            return self.ovulacija(x)

    def plodni_dnevi(self, stevilo_ciklov = 1):
        p_dnevi = []
        for i in self.dnevi_ovulacije(stevilo_ciklov):
            a = razlika_dni(4)
            b = razlika_dni(3)
            c = razlika_dni(2)
            d = razlika_dni(1)
            p_dnevi += [i - a, i - b, i - c, i - d, i]
        return p_dnevi

    def kdaj_menstruacija(self):
        return self.prihodnji_cikel() - danes

    def kdaj_ovulacija(self):
        return self.prihodnja_ovulacija() - danes

    def kdaj_prvi_plodni_dan(self):
        x = self.prihodnja_ovulacija() - razlika_dni(4) - danes
        if x.days >= 0:
            return x
        elif -4 <= x.days <= -1:
            return razlika_dni(0)
        else:
            return x + self.dolzina_cikla()

with open('c:\\Users\\Eva\\Matematika\\Uvod v programiranje\\Menstrualni kalkulator\\zbirka_citatov.txt', 'r', encoding = 'utf-8') as dat:
    citati = [citat.strip() for citat in dat]

def citat():
    return random.choice(citati)