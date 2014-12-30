
epclist={
    "75484660544.983622.1.onsserver.com" : "http://www.foodtrace.com/upload",
    "75484660546.983623.1.onsserver.com" : "http://www.foodtrace.com/qurey"
}


def shift_epc(urn):
    prefix = 'urn.epc:'
    if urn.__contains__(prefix):
        raw_epc = urn[ len(prefix) : ]
        print raw_epc
        return (True,raw_epc)
    else:
        return (False,)

def reverse(raw):
    print 'now splitting the raw epc'
    raw = raw.split('.')
    if len(raw) < 4:
        return (False,)
    else:
        raw.reverse()
        return (True,reduce(lambda x,y: x+'.'+y,raw[1:4]))

def match(key):
    if epclist.has_key(key):
        return (True,epclist.get(key))
    else:
        return (False,)
