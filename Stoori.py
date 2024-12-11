def Stoori():
    # Aloitustilanne
    print("Löydät itsesi istumasta vanhan metsämökin keittiöstä. Et ole varma kuinka tähän päädyttiin, eilisen illan mielikuvat ovat hiukan hämäriä, mutta jostain tulee fiilis että poistuminen ripeästi saattaisi olla hyvä vaihtoehto.")
    
    # Tällä saattaa olla merkitystä
    kumpi = input("Oletko Hannu vai Kerttu? ").capitalize()

    # Ensimmäinen testi, helpoin reitti ulos
    voima = input("Yrität katsoa josko oven saisi auki. Riittääkö voimia? (Kyllä/Ei) ").capitalize()
    if voima == "Kyllä":
        print("Vapaa, vapaa vihdoin! Mä en enää vandalisoi tätä kioskia!")
        exit()
    else:
        print("Pitää etsiä toinen reitti.")
         
    # Toinen testi, kuinka monta pullaa houkuttelee
    print("Ikkunat ovat lukossa. Otat pullaa. Niitä on kymmenisen kappaletta, tuoksuvatkin mokomat aika hyvälle. Tuoreita?")
    try:
        pullat = int(input("Montako otat? (0-10): "))
    except ValueError:
        print("Et vastannut luvulla, joten et ota pullaa.")
        pullat = 0
		
    if pullat < 5:
        print("Pullat mukaan ja menoksi. Vapaa! Muista kuitenkin soittaa poliisit paikalle, noin anonyyminä vinkkinä.")
        exit()
    else:
        print("Liikaa pullia, ketuille meni, pitää jatkaa etsintöjä. Syöt kuitenkin pullan lohdutukseksi.")
        
    # Kolmas testi, pullaa hiirille vai ei pullaa hiirille
    print("Pullat on aika hyviä, mutta jumissa ollaan. Noita on krapuloissaan höpöttänyt lattialuukun reitistä, ehkä se toimii? Tosin et tiedä missä se on.")
    hiiri = input("Annatko hiirille pullaa että ehkä auttavat? (Kyllä/Ei) ").capitalize()
    if hiiri == "Kyllä":
        print("Reitti löytyy kivojen ja mukavien hiirten avulla. Vapaa!")
        exit()
    else:
        print("Etsintä jatkuu.")

    # Viimeinen testi, suuri moraalikysymys
    print("Noita saapastelee kotiin. Vaikuttaa olevan kännissä kuin käki.")
    kehu = input("Kehutko leivontakykyjä? (Kyllä/Ei) ").capitalize()
    if kehu == "Kyllä":
        print("Noita raivostuu ja päädyt itse uuniin seuraavan evään ainesosaksi. Bad end.")
        exit()
    else:
        print("Noita hämmentyy kun ei löydä pulliaan. Työnnät uuniin kun täti tarkistaa sitä, ja liukenet ovesta pihalle. Vapaa!")
        exit()

Stoori()
