#!usr/bin/python
import sqlite3
import os
import random
def sqlite():
    print("1.Creer table et database")
    print("2.Selectionner et inserer les données")
    print("3.Creer les contacts virtual")
    print("4.configuration appel local et international")
    print("5.simple configuration ast appel local et international")
    print("6.securiser le server contre les attacks ")
while True:
    sqlite()
    choix = input("choix:")
    if choix =="1":
        print("Bienvenue dans creations d'une table")
        ya = sqlite3.connect('arcenciel.db')
        y = ya.cursor()
        y.execute('''CREATE TABLE guinee(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prenom TEXT NOT NULL,
                nom TEXT NOT NULL,
                utilisateur TEXT NOT NULL,
                mot_de_passe TEXT NOT NULL,
                telephone_virtuel INTEGER,
                pays TEXT NOT NULL,
                abonnement INTEGER,
                horaire INTEGER,
                journalier INTEGER,
                semestriel INTEGER,
                mensuel INTEGER,
                prix INTEGER,
                expiration INTEGER)''')
        ya.commit()
    if choix =="2":
        print("selection et insertion des informations")
        ya = sqlite3.connect('arcenciel.db')
        y = ya.cursor()
        y.execute("SELECT * FROM guinee")
        ya.commit()
        def generate_phone_number():
            # Générer un numéro de téléphone aléatoire au format XXX-XXX-XXXX
            phone_random = '{}-{}-{}'.format(random.randint(100, 999), random.randint(100, 999), random.randint(1000, 9999))
            return phone_random

            # Utilisation de la fonction pour générer un numéro de téléphone aléatoire
        telephone_virtuel1 = str(generate_phone_number())
        choice = input("code indicatif:")
        telephone_virtuel = str(choice+telephone_virtuel1)
        os.system('clear')
        print(telephone_virtuel)
        prenom = input("prenom:")
        nom = input("nom:")
        utilisateur = input("utilisateur:")
        mot_de_passe = input("mot_de_passe:")
        #telephone_virtuel = input("telephone_virtuel:")
        pays = input("pays:")
        abonnement = input("abonnement:")
        horaire = input("horaire:")
        journalier = input("journalier:")
        semestriel = input("semestriel:")
        mensuel = input("mensuel:")
        prix = input("prix:")
        expiration = input("expiration:")
        y = ya.cursor()
        y.execute("INSERT INTO guinee (prenom, nom, utilisateur, mot_de_passe, telephone_virtuel, pays, abonnement, horaire, journalier, semestriel, mensuel, prix, expiration)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(prenom, nom, utilisateur, mot_de_passe, telephone_virtuel, pays, abonnement, horaire, journalier, semestriel, mensuel, prix, expiration))
        ya.commit()
        rows = y.fetchall()
        for row in rows:
            os.system('clear')
            prenom, nom, utilisateur, mot_de_passe, telephone_virtuel, pays, abonnement, horaire, journalier, semestriel, mensuel, prix, expiration = row
            print(f'{prenom}{nom}{utilisateur}{mot_de_passe}{telephone_virtuel}{pays}{abonnement}{horaire}{journalier}{semestriel}{mensuel}{prix}{expiration}')
       


    if choix =="3":
        print("bienvenue dans la creation des contact virtuel avec format EDGE")
        def sys():
            numero = "129875643"
            indicatif = input("+224:")
            operateur = input("code operateur:")
            for a in str(numero):
                for b in str(numero):
                    for c in str(numero):
                        for d in str(numero):
                            for e in str(numero):
                                for f in str(numero): 
                                    nim = str(indicatif+operateur+a+b+c+d+e+f)
                                    file= open('conta.conf', 'a')
                                    vk = file.write(nim+'\n')
                                    print(nim)
                                    os.system('clear')
                                    return nim
        telephone_virtuel = sys()
        print(telephone_virtuel)
        cnn = sqlite3.connect('arcenciel.db')
        c = cnn.cursor()
        expiration = input("date_expiration:")
        c.execute("SELECT * FROM guinee WHERE expiration")
        cnn.commit()
        c.fetchone()
        c = cnn.cursor()
        c.execute("DROP guinee SET expiration VALUES(?)", (expiration))
        cnn = cnn.commit()
        row = c.fetchall()
        for rows in row:
            expiration = rows
            vn = str(f'{expiration}')
            print(vn)
    if choix =="4":
        os.system('clear')
        print("Bienvenue dans la configuration des appels locaux et internationaux")
        def menu():
            print("parametre ODBC-DSN pour sqlite3 Base de donnée, asterisk")
            print("1.odbc-dsn.ini")
            print("2.odbcinst.ini")
            print("3.configurons les fichiers asterisk sur la base d'odbc-dsn")
            print("4.")
            print("0.Quitter")
        while True:
            menu()
            choix = input("choix:")
            if choix =="1":
                print("odbc.ini")
                sqlite = str("[sqlite3]")
                description = str("Description = "+ "enSQLite ODBC Driver DSN")
                Driver = str("Driver = "+"/usr/lib/x86_64-linux-gnu/odbc/libsqlite3odbc.so")
                database = str("database =" + "/usr/src/arcenciel.db")
                timeout = str("timeout = "+"200")
                with open('/etc/odbc.ini','w') as file:
                    wj = file.write(sqlite+'\n'+description+'\n'+Driver+'\n'+database+'\n'+timeout+'\n')
                    print(wj)
                    os.system('clear')
                file.close()
            if choix == "2":
                print("odbcinst.ini")
                sqlit = str("[sqlite]")
                description = str("Description = "+"SQLite3 ODBC Driver")
                driver = str("Driver = "+"libsqliteodbc.so")
                setup = str("Setup = "+"libsqlite3odbc.so")
                usagecount = input("usageCount(1 ou 2..etc...):")
                usageCount = str("usageCount = "+usagecount)
                with open('/etc/odbcinst.ini','w') as file:
                    wj = file.write(f'\n{sqlit}\n{description}\n{driver}\n{setup}\n{usageCount}')
                    print(wj)
                    os.system('clear')
                file.close()
            if choix =="3":
                print("Bienvenue dans asterisk sur la base d'ODBC-DSN")
                def programme():
                    print("1.res_odbc.conf")
                    print("2.modules.conf")
                    print("3.sip.conf")
                    print("4.extension.conf")
                    print("5.users.conf")
                    print("6.voicemail.conf")
                    print("7.creer un tableau s'il n'existe pas")
                    print("0.Quitter")
                while True:
                    programme()
                    choix = input("choix:")
                    if choix =="1":
                        print("Bienvenue dans res_odbc.conf sqlite3 et asterisk")
                        def res_odbc():
                            my = input("my-odbc-connection users:")
                            my_odbc = str(f'{[my]}')
                            enable = str("enabled =>"+"yes")
                            dsn = str("dsn => "+"sqlite-dsn")
                            user = input("utilisateur:")
                            username = str("username => "+(f'{user}'))
                            motdepasse = input("mot_de_passe:")
                            password = str("mot_de_passe => "+(f'{motdepasse}'))
                            pre = str("pre-connect =>"+"yes")
                            id = input("Id:")
                            telephone_virtuel = input("telephone_virtuel:")
                            expiration = str(input("date d'expiration:"))
                            sqlread = str("sqlread =>SELECT id, utilisateur, telephone_virtuel, expiration FROM guinee"+"WHERE"+"id:"+(f'{id},')+"utlilisateur:"+(f'{utilisateur},')+"telphone_virtuel:"+(f'{telephone_virtuel},')+"AND Expiration:"+(f'{expiration}')+">DATE('now')")
                            with open('/etc/asterisk/res_odbc.conf','w') as file:
                                vk = str(f'{my_odbc}\n{enable}\n{dsn}\n{username}\n{password}\n{pre}\n{sqlread}')
                                gang = file.write(vk+"\n")
                            return vk
                        gh = res_odbc()
                        os.system('clear')
                        print(gh)
                    if choix =="2":
                        print("Bienvenue dans la module.conf")
                        def module():
                            load = str("load =>"+"res_odbc.so")
                            with open('/etc/asterisk/modules.conf','w') as file:
                                mod = str(f'{load}')
                                gi = file.write(mod)
                            return mod
                        oba = module()
                        os.system('clear')
                        print(oba)
                    if choix =="3":
                        print("Bienvenue dans sip.conf")
                        def sip_odbc():
                            utilisateur = input("utilisateur sip:")
                            gen = str(f'{[utilisateur]}')
                            type = str("type="+"friend")
                            host = str("host="+"dynamic")
                            context = str("context="+"interne")
                            print("recuperation des information depuis la base de données")
                            id = input("id:")
                            utilisateur = input("utilisateur:")
                            phone = input("telephone_virtuel:")
                            date_expiration = input("date_expiration:")
                            dbq = str("dbq =" +"SELECT id, utilisateur, telephone_virtuel, expiration FROM guinee WHERE "+ (f'Id:{id}, Utilisateur:"{utilisateur}", Telphone_virtuel:{phone}, AND Expiration:{date_expiration}')+">DATE('now')")
                            with open('/etc/asterisk/sip.conf','w') as file:
                                dk = str(f'{gen}\n{type}\n{host}\n{context}\n{dbq}\n')
                                gt = file.write(dk)
                            return dk
                        yc = sip_odbc()
                        os.system('clear')
                        print(yc)
                    if choix =="4":
                        print("Bienvenue extension avec odbc-dsn sqlite3 et asterisk")
                        def extension_odbc():
                            plan = str('[outgoing]')
                            extern = str('exten => 622001839,GotoIf($["${ODBC_READ(date_expiration)}" < "${STRFTIME(${EPOCH},,%F %T)}"]?bloquer_appel_sortant')
                            same1 = str('same => n,Dial(SIP/127.0.0.1/${EXTEN})')
                            same2 = str('same => n(bloquer_appel_sortant),Playback(appel_interdit)')
                            same3 = str('same => n,Hangup()')
                            with open('/etc/asterisk/extensions.conf','w') as file:
                                apk = str(f'{plan}\n{extern}\n{same1}\n{same2}\n{same3}')
                                file.write(apk+'\n')
                            return apk
                        seredou = extension_odbc()
                        print(f'{seredou}')


                    if choix =="0":
                        print("quittons ce parametre")
                        break
        

    if choix =="5":
        os.system('clear')
        print("Bienvenue dans la conf simple avec lacalhost et port sans ODBC ET SQLITE")
        def aste():
            print("1.sip.conf")
            print("2.users.conf")
            print("3.extensions.conf")
            print("4.voicemail.conf")
            print("5.localhost")
            print("6.port")
            print("0.quitter")
        while True:
            aste()
            choix = str(input("choix:"))
            if choix =="1":
                print("Bienvenue dans la config sip")
                def simplesip():
                    general = str("[general]")
                    host = str("host = "+"127.0.0.1")
                    port = str("port = " + "5060")
                    externip = str("externip = "+input("externip:"))
                    localnet = str("localnet = "+input("localnet[127.0.0.1/255.255.255.0]:"))
                    nat = str("nat = "+"force_rport,comedia")
                    qualify = str("qualify = "+"yes")
                    canreinvite = str("canreinvite = "+"no")
                    sv = str(f'\n\n{general}\n{host}\n{port}\n{externip}\n{localnet}\n{nat}\n{qualify}\n{canreinvite}')
                    with open('/etc/asterisk/sip.conf','w') as file:
                        sg = file.write(sv)
                    return sv
                vps = simplesip()
                print(vps)


            if choix =="2":
                print("Bienvenue dans user.conf")
                def usersconf():
                    utilisateur = input("utilisateur:")
                    users = str([utilisateur])
                    type = str("type = "+input("exemple(amis or friends):"))
                    host = str("host = "+input("(host=dynamic):"))
                    secret = str("secret = "+input("mot_de_passe:"))
                    context = str("context = "+input("(local ou): "))
                    disallow = str("disallow ="+input("(disallow=all):"))
                    allow = str("allow = "+input("(allow=ullaw):"))
                    user = (f'{users}\n{type}\n{host}\n{secret}\n{context}\n{disallow}\n{allow}')
                    with open('/etc/asterisk/users.conf', 'w') as file:
                        vpk = file.write(user)
                    return user
                users = usersconf()
                print(users)
            if choix =="3":
                print("Bienvenue dans extension.conf")
                def extension():
                    glo = str(input("globals:"))
                    glob = str(f'{[glo]}')
                    utilisateur = input("utilisateur:")
                    exten1 = str("exten=> "+"+224622001839"+",Dial Sip/"+(f'{utilisateur}'))
                    exten2 = str("exten=> "+"622001839"+",Ringing()")
                    exten3 = str("exten=> "+ str("002246221839"))
                    exten4 = str("exten=> "+"622001839"+",Dial(SIP/"+(f'{utilisateur})'))
                    localcontext = str(input("(contextlocal(local)):"))
                    local = str(f'{[localcontext]}')
                    exten5 = str("exten => "+ "622001839")
                    exten6 = str("exten=> "+"622001839"+",Ringing()")
                    exten7 = str("exten=> "+"622001839"+",Dial(SIP/${EXTEN}@127.0.0.1)")
                    same1 = str("same => "+"n,Wait(7)")
                    same2 = str("same => "+"n,Playback(bonjour)")
                    same3 = str("same => "+"n,Hangup()")
                    with open('/etc/asterisk/extensions.conf','w') as file:
                        ext = (f'{glob}\n{exten1}\n{exten2}\n{exten3}\n{exten4}\n{local}\n{exten5}\n{exten6}\n{exten7}\n{same1}\n{same2}\n{same3}')
                        vpk = file.write(ext+'\n\n')
                    return ext
                ext = extension()
                print(ext)
            if choix =="4":
                print("Bienvenue dans le fichier voicemail")
                def voicemail():
                    general = str("[general]")
                    spool = str("spool => "+"/var/spool/asterisk/voicemail/defaut/")
                    format = str("format = "+"wav")
                    email = input("servermail:")
                    servermail = str("servermail = "+ (f'{email}'))
                    attach = str("attach = "+"yes")
                    skipms = str("skipms = "+"3000")
                    with open('voicemail.conf', 'a') as file:
                        voice = str(f'{general}\n\n{spool}\n{format}\n{servermail}\n{attach}\n{skipms}')
                        vcm = file.write(voice+'\n')      
                    return voice
                yaya = voicemail()
                print(yaya)

            if choix =="0":
               print("ByeBye")
               os.system('clear')
               break
    if choix =="6":
        print("Bienvenue dans le programme de securité server")
        def securite():
            print("1.installer les packets ou les commandes")
            print("2.Authentification du server")
            print("3.Authentification ssh")
            print("4.integration de VPN pour les clients normals")
            print("5.Etablissement des Ips autorisées")
            print("6.Interdiction d'accés sans autorisation das SIP")
            print("0.quitter")
        while True:
            securite()
            choix = input("fait votre choix:")
            if choix =="1":
                def subprocess():
                    import subprocess
                    packet = subprocess(['iptables -A INPUT -p udp --dport 5060 -j ACCEPT'],['iptables -A INPUT -p udp --dport 10000:20000 -j ACCEPT'])
                    subprocess.run(packet)
                    return packet
                pkt = subprocess()
                print(pkt)
            if choix =="2":
                print("Bienvenue dans la config TLS pour l'authenification du server")
                def authentif():
                    print("sip.configuration tls-auth")
                    tls = str('[transport-tls]')   
                    type = str('type=transport')
                    protocol = str('protocol=tls')
                    bind = str('bind=0.0.0.0')
                    cert = str('cert_file=/etc/sshd_config/votre/certificat.pem')
                    priv = str('priv_key_file=/chemin/vers/votre/cle_privee.pem')
                    method = str('method=tlsv1')
                    with open('/etc/asterisk/sip.conf','w') as file:
                        tlsv = str(f'\n{tls}\n{type}\n{protocol}\n{bind}\n{cert}\n{priv}\n{method}\n')
                        vk = file.write(tlsv+'\n')
                    return tlsv
                gans = authentif()
                print(gans)
                def clients():
                    client = str('[client1]')
                    type1 = str('type=endpoint')
                    transport = str('transport=transport-tls')
                    context = str('context=default')
                    auth = str('auth=auth-client1')
                    aors = str('aors=client1')
                    with open('/etc/asterisk/sip.conf','w') as file:
                        gh = str(f'{client}\n{type1}\n{transport}\n{context}\n{auth}\n{aors}\n')
                        gy = file.write(gh+'\n')
                    return gh
                guinee =  clients()
                print(guinee)
            if choix =="3":
                print("authentification ssh")
                def authentif():
                    authentification = str("#authentification:")
                    utilisateur = input("utilisateur ssh:")
                    nvuser = str("AllowUser "+(f'{utilisateur}'))
                    root = input('access root user(yes or no):')
                    yess = input("yes or no:")
                    login = str("LoginGraceTime 120")
                    permission = str("PermitRootLogin "+(f'{root}'))
                    StrictMode = str("StrictMode "+(f'{yess}'))
                    with open('/etc/ssh/sshd_config.d','w') as file:
                        ssh = str(f'\n{authentification}\n{nvuser}\n{login}\n{permission}\n{StrictMode}\n\n')
                        vs = file.write(ssh)
                    return ssh
                gsb = authentif()
                print(gsb)
            if choix =="4":
                print("integration de VPN pour les clients normals ast")

            if choix =="5":
                print("Etablissement des Ips autorisées")

            if choix =="6":
                print("Interdiction d'access sans authentication asterisk SIP")
                def asteriskaut():
                    voir = input("voir yes or no:")
                    server = str("srvlookup="+(f'{voir}'))
                    allo = input("yes or no")
                    guest = str("allowguest="+(f'{allo}'))
                    rejet = str("alwaysauthreject="+(f'{voir}'))
                    qualify = str("qualify="+(f'{voir}'))
                    with open('/etc/asterik/sip.conf','w') as file:
                        gha = str(f'\n{server}\n{guest}\n{rejet}\n{qualify}')
                        tg = file.write(gha+'\n')
                    return gha
                vb = asteriskaut()
                print(vb)    
            if choix =="0":
                print("Bye Bye")
                break

        


                   
                    
                    
      