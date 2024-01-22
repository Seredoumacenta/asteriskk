#!usr/bin/python
print("BIENVENUE DANS LA CONFIGURATION ASTERISK")
def programme():
    import sys
    contact = str("1234567890")
    pays = input("+224:")
    operater = input("622:")
    for a in contact:
        for b in contact:
            for c in contact:
                for d in contact:
                    for e in contact:
                        for f in contact:
                            with open('virtualphone.txt', 'a') as file:
                                sr = file.write(f'\n{pays}{operater}{a}{b}{c}{d}{e}{f}')
                                print(sr)
                            return sr
conf = programme()
print(conf)

def sip():
    print("Bienvenue dans la configuration sip")
    def general():
        print("1.general")
        print("0.Quitter")
    while True:
        general()
        choix = input("choix:")
        if choix =="1":
            general1 = str("[general]")
            with open('/etc/asterisk/sip.conf','w') as file:
                ghh = file.write(f'{general1}')
                print(ghh)

        if choix =="0":
            print("Retour")
            break
    language = str("language = fr")
    allow1 = str("allow = alaw")
    allow2 = str("allow = ulaw")
    context = str("context  = labo")
    with open('/etc/asterisk/sip.conf', 'a') as file:
        sip = file.write(f'\n{language}\n{allow1}\n{allow2}\n{context}')
        print(sip)
    def utilisateur():
        print("1.utilisateur")
        print("0.retour")
    while True:
        utilisateur()
        choix = input("choix:")
        if choix =="1":
            utilisateur1 = input('utilisateur:')
            util = str('\n['+(f'{utilisateur1}')+']')
            with open('/etc/asterisk/sip.conf', 'a') as file:
                kb = file.write(util)
                print(kb)
            
            
        if choix =="0":
            print("je me retourne au programme general")
            break
    type = str("type = friend")
    passeword = input("password:")
    identifiant = input("identifiant:")
    secret = str("secret = "+(f'{passeword}'))
    host = str("host = dynamic")
    contact = input("telephone")
    callerid = str("callerid = "+('"')+(f'{identifiant}')+('"') + "<"+str(f'{contact}')+">")
    with open('/etc/asterisk/sip.conf', 'a') as file:
        ui = file.write(f'\n{type}\n{secret}\n{host}\n{callerid}')
    return(ui)
config = sip()
print(config)

def extension():
    print("Nous voilà dans la config extensions")
    def general():
        print("1.general")
        print("0.Quitter")
    while True:
        general()
        choix = input("choix:")
        if choix =="1":
            general1 = str("[general]")
            with open('/etc/asterisk/extensions.conf','w') as file:
                ghh = file.write(f'{general1}')
                print(ghh)

        if choix =="0":
            print("Retour")
            break
    def labo():
        print("1.general")
        print("0.Quitter")
    while True:
        labo()
        choix = input("choix:")
        if choix =="1":
            context = input("context:")
            general1 = str('['+(f'{context}')+']')
            with open('/etc/asterisk/extensions.conf','a') as file:
                ghh = file.write(f'{general1}')
                print(ghh)

        if choix =="0":
            print("Retour")
            break
    telephone = input("telephone:")
    exten1 = str("exten =>"+(f'{telephone}')+'.1.'+'Answer')
    utilisateur = input('utilisateur:')
    exten2 = str("exten =>"+(f'{telephone}')+'.2.'+'Dial'+'(SIP/'+(f'{utilisateur}')+')')
    exten3 = str("exten =>"+(f'{telephone}')+'.3.'+'Hangup')
    with open('/etc/asterisk/extensions.conf', 'a') as file:
        e = file.write(f'\n{exten1}\n{exten2}\n{exten3}')
        print(e)
    return e
ension = extension()
print(ension)