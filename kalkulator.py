import bottle
import model
import vmesnik

danes = model.danes
danes_dat = vmesnik.datum_izpis_py(danes)
c = model.citat()

def preberi(vnos):
    return int(bottle.request.query.getunicode(vnos))

def razlika(dni):
    return model.razlika_dni(dni)

def d_izpis(datum):
    return vmesnik.datum_izpis_py(datum)

def r_izpis(razlika):
    return vmesnik.razlika_izpis(razlika)

@bottle.get('/')
def prva_stran():
    c = model.citat()
    dan_vnos = danes.day
    mesec_vnos = danes.month
    leto_vnos = danes.year
    dolzina_vnos = 28
    trajanje_vnos = 5
    return bottle.template('prva_stran.tpl', citat=c, danes_dat=danes_dat, dan_vnos=dan_vnos, mesec_vnos=mesec_vnos, leto_vnos=leto_vnos, dolzina_vnos=dolzina_vnos, trajanje_vnos=trajanje_vnos)

@bottle.get('/cikel/')
def datumi_na_dlani():
    dan_vnos = preberi("v_dan")
    mesec_vnos = preberi("v_mesec")
    leto_vnos = preberi("v_leto")
    dolzina_vnos = preberi("v_dolzina")
    trajanje_vnos = preberi("v_trajanje")
    datum_vnos = vmesnik.datum_izpis(dan_vnos, mesec_vnos, leto_vnos)
    datum_v_py = vmesnik.datum_py(dan_vnos, mesec_vnos, leto_vnos)
    cikel_osebe = model.Cikel(zacetek_cikla=datum_v_py, dolzina_cikla=dolzina_vnos, trajanje_menstruacije=trajanje_vnos)
    m1 = d_izpis(cikel_osebe.prihodnji_cikel())
    m2 = d_izpis(cikel_osebe.prihodnji_cikel() + razlika(trajanje_vnos - 1))
    m3 = r_izpis(cikel_osebe.kdaj_menstruacija())
    o1 = d_izpis(cikel_osebe.prihodnja_ovulacija())
    o2 = r_izpis(cikel_osebe.kdaj_ovulacija())
    p1 = d_izpis(danes + cikel_osebe.kdaj_prvi_plodni_dan())
    p2 = r_izpis(cikel_osebe.kdaj_prvi_plodni_dan())
    if dolzina_vnos < trajanje_vnos or (datum_v_py - razlika(7)) > danes or (danes - datum_v_py) > razlika(365):
        return bottle.template('opozorilo.tpl', citat=c, datum_vnos=datum_vnos, trajanje_vnos=trajanje_vnos, dolzina_vnos=dolzina_vnos, danes_dat=danes_dat, dan_vnos=dan_vnos, mesec_vnos=mesec_vnos, leto_vnos=leto_vnos)
    else:
        if (danes - datum_v_py) > razlika(dolzina_vnos):
            z1 = d_izpis(cikel_osebe.naslednji_cikel())
            z2 = r_izpis(abs(danes - cikel_osebe.naslednji_cikel()))
            return bottle.template('dat2.tpl', citat=c, danes_dat=danes_dat, datum_vnos=datum_vnos, trajanje_vnos=trajanje_vnos, dolzina_vnos=dolzina_vnos, cikel_osebe=cikel_osebe, m1=m1, m2=m2, m3=m3, o1=o1, o2=o2, p1=p1, p2=p2, z1=z1, z2=z2, dan_vnos=dan_vnos, mesec_vnos=mesec_vnos, leto_vnos=leto_vnos)
        else:
            return bottle.template('dat1.tpl', citat=c, danes_dat=danes_dat, datum_vnos=datum_vnos, trajanje_vnos=trajanje_vnos, dolzina_vnos=dolzina_vnos, cikel_osebe=cikel_osebe, m1=m1, m2=m2, m3=m3, o1=o1, o2=o2, p1=p1, p2=p2, dan_vnos=dan_vnos, mesec_vnos=mesec_vnos, leto_vnos=leto_vnos)


bottle.run(reloader=True, debuger=True)
