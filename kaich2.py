#!usr/bin/python
print("BIENVENUE DANS LA CONFIGURATION ASTERISK")
def programme_gene():
    print("1.programme asterisk 1")
    print("2.programme asterisk 2")
    print("0.retour")
while True:
    programme_gene()
    choix = input("choix:")
    if choix =="1":
        print("hello world")
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
                    with open('sip.conf','w') as file:
                        ghh = file.write(f'{general1}')
                        print(ghh)

                if choix =="0":
                    print("Retour")
                    break
            language = str("language = fr")
            allow1 = str("allow = alaw")
            allow2 = str("allow = ulaw")
            context = str("context  = labo")
            with open('sip.conf', 'a') as file:
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
                    with open('sip.conf', 'a') as file:
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
            with open('sip.conf', 'a') as file:
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
                    with open('extensions.conf','w') as file:
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
                    with open('extensions.conf','a') as file:
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
            with open('extensions.conf', 'a') as file:
                e = file.write(f'\n{exten1}\n{exten2}\n{exten3}')
                print(e)
            return e
        ension = extension()
        print(ension)
    if choix =="0":
        break
    if choix=="2":
        print("NOUVELLE METHODE DE CONFIGURATION")
        def asterisk():
            print("1. Création des utilisateurs(Users.conf)") 
            print("2. Configuration du Dialplan(Extensions.conf)")
            print("3. Configuration général d’Asterisk (Sip.conf)")
            print("4. Mise en place des boîtes vocales")
            print("5. Configuration et mise en place du transfert d’appel")
        while True:
            asterisk()
            choix = input("choix:")
            if choix =="1":
                print("programme de configuration asterisk 2e partie")
                def sip_config():
                    print("bienvenue dans general")
                    def general():
                        print("1.general")
                        print("0.exit")
                    while True:
                        general()
                        choix = input("choix:")
                        if choix =="1":
                            def sip():
                                general = str("["+"general"+"]")
                                with open('user.conf','a') as file:
                                    vb = file.write(f'{general}')
                                return vb
                            hect = sip()
                            print(hect)
                        if choix=="0":
                            print("Bye Bye")
                            break
                    def suivant():
                        print("1.suite de general")
                        print("2.suite3(template)")
                        print("3.utilisateur")
                        print("0.exit")
                    while True:
                        suivant()
                        choix = input("choix:")
                        if choix=="1":
                            def suitec():
                                jk = input("voicemail(yes or no)?:")
                                email= str('hasvoicemail='+(f'{jk}'))
                                has = str('hassip ='+(f'{jk}'))
                                iax = str('hasiax ='+(f'{jk}'))
                                waiting = str('callwaiting='+(f'{jk}'))
                                three = str('threewaitcalling ='+(f'{jk}'))
                                call = str('callwaitingcallerid='+(f'{jk}'))
                                transfer= str('transfer='+(f'{jk}'))
                                can = str('canpark='+(f'{jk}'))
                                forward = str('cancallforward='+(f'{jk}'))
                                cal = str('callreturn='+(f'{jk}'))
                                callgr = input('groupe numbers(0 à 9999):')
                                callin = str('callgroup='+(f'{callgr}'))
                                pik = str('pickupgrup='+(f'{callgr}'))
                                nat = str('nat='+(f'{jk}'))
                                with open('user.conf','a') as file:
                                    files = file.write(f'\n{email}\n{has}\n{iax}\n{waiting}\n{three}\n{call}\n{transfer}\n{can}\n{forward}\n{cal}\n{callin}\n{pik}\n{nat}')
                                return files
                            conf=suitec()
                            print(conf)
                        if choix =="2":
                            def suitec2():
                                template = str('['+'template'+']'+'('+'!'+')')
                                type = str("type="+"friend")
                                host = str("host="+"dynamic")
                                dtmfmode = str("dtmfmode="+"rfc2833")
                                disable = str("disallow="+"all")
                                allow = str("allow ="+"ullaw")
                                context = str("context="+"work")
                                with open('user.conf','a') as file:
                                    fille = file.write(f'\n{template}\n{type}\n{host}\n{dtmfmode}\n{disable}\n{allow}\n{context}\n')
                                return fille
                            kallos = suitec2()
                            print(kallos)
                        if choix=="3":
                            def users():
                                print("je suis un nouvel utilisateur")
                                def generate_phone_number():
                                    import random
                                    # Générer un numéro de téléphone aléatoire au format XXX-XXX-XXXX
                                    phone_random = '{}-{}-{}'.format(random.randint(100, 999), random.randint(100, 999), random.randint(1000, 9999))
                                    return phone_random
                                telephone_virtuel1 = str(generate_phone_number())
                                choice = input("code indicatif:")
                                telephone_virtuel = str(choice+telephone_virtuel1)
                                print(telephone_virtuel)
                                telephone = str("["+(f'{telephone_virtuel}')+"]"+"("+"template"+")")
                                name = input("nom complet:")
                                fullname = str("fullname="+(f'{name}'))
                                utilisateur = input("nom d'utilisateur:")
                                username = str("username="+(f'{utilisateur}'))
                                secret = input("mode de passe:")
                                password = str("secret="+(f'{secret}'))
                                with open('user.conf','a') as file:
                                    ghana = file.write(f'\n{telephone}\n{fullname}\n{username}\n{password}\n')
                                return ghana
                            gps = users()
                            print(gps)

                        if choix=="0":
                            print("retour")
                            break
                sipp=sip_config()
                print(sipp)
            if choix =="2":
                def extensions():
                    print("bienvenue dans extensions.conf")
                    print("1.general")
                    print("2.general seconde etape")
                    print("3.derniere etape")
                    print("0.pour quitter")
                while True:
                    extensions()
                    choix = input("choix:")
                    if choix=="1":
                        def etape():
                            general = str("["+"general"+"]")
                            with open('extension.conf','a')as file:
                                balla = file.write(f'{general}')
                            return balla
                        gui = etape()
                        print(gui)
                    if choix=="0":
                        print("retour")
                        break
                    if choix=="2":
                        def seconf():
                            print("etape2")
                            static = str("static="+"yes")
                            write = str("writeprotect="+"no")
                            clear = str("clearglobalvars="+"no")
                            glogbal = str("["+"globals"+"]")
                            console = str("CONSOLE=console/dsp")
                            IAXINFO = str("iaxinfo=guest")
                            TRUNK = str("DAHDI/G2")
                            TRUNKMS = str("TRUNKMSD=1")
                            with open('extension.conf','a') as file:
                                jhk = file.write(f'\n{static}\n{write}\n{clear}\n{glogbal}\n{console}\n{IAXINFO}\n{TRUNK}\n{TRUNKMS}\n')
                            return jhk
                        key = seconf()
                        print(key)
                    if choix == "3":
                       def second():
                           print("etape 3")
                           context = input("context:")
                           work = str("["+(f'{context}')+"]")
                           phone = input("tel:")
                           username = input("utilisateur:")
                           exten=str("exten =>"+(f'{phone}')+","+"("+"SIP/"+(f'{username}')+")")
                           am = input("nombre(1,9999):")
                           exten2 = str("exten =>"+(f'{phone}')+","+"1"+"Dial"+(f'{am}')+"(SIP/"+('${EXTEN}')+",1"+")")
                           exten3 = str("exten=>"+(f'{phone}')+",1"+ "Hangout()")
                           with open('extension.conf', 'a') as file:
                               angle = file.write(f'\n{work}\n{exten}\n{exten2}\n{exten3}\n')
                           return angle
                       hector = second()
                       print(hector)
                    if choix=="4":
                        def sipc():
                            language = str("language=f")
                            with open('sip.conf','a') as file:
                                pe = file.write(f'\n{language}\n')
                            return pe
                        fara = sipc()
                        print(fara)
                            






                    