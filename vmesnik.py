import model
import datetime

def datum_py(d, m, l):
    return datetime.date(l, m, d)

def datum_izpis(d, m, l):
    return '{0}. {1}. {2}'.format(d, m, l)

def datum_izpis_py(datum):
    dat = datum.timetuple()
    d = dat[2]
    m = dat[1]
    l = dat[0]
    return '{0}. {1}. {2}'.format(d, m, l)

def razlika_izpis(x):
    return x.days