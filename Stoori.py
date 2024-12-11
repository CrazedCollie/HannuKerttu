def Stoori():
    print("Löydät itsesi istumasta vanhan metsämökin keittiöstä. Et ole varma kuinka tähän päädyttiin, mutta jostain tulee fiilis että poistuminen ripeästi saattaisi olla hyvä vaihtoehto.")

    kumpi = input("Oletko Hannu vai Kerttu?").capitalize()

    voima = input("Yrität katsoa josko oven saisi auki. Riittääkö voimia?(Kyllä/Ei)")
    if voima == "Kyllä":
	    print("Vapaa, vapaa vihdoin! Mä en enää vandalisoi tätä kioskia!")
    else:
	    print("Pitää etsiä toinen reitti.")

    print("Ikkunat ovat lukossa. Otat pullaa. Niitä on kymmenisen kappaletta, tuoksuvatkin mokomat aika hyvälle. Tuoreita?")
    try:
        pullat = int(input("Montako otat? (0-10) "))
    except ValueError:
        print("Et vastannut luvulla, joten et ota pullaa.")
    pullat = 0
		
    if pullat <5:
        print("Pullat mukaan ja menoksi. Vapaa!")
    else:
	    print("Liikaa pullia, ketuille meni, pitää jatkaa etsintöjä.")

    print("Pullat on aika hyviä, mutta jumissa ollaan. Noita on krapuloissaan höpöttänyt lattialuukun reitistä, ehkä se toimii?")
    hiiri = input("Annatko hiirille pullaa että ehkä auttavat?(Kyllä/Ei)").capitalize()
    if hiiri == "Kyllä":
        print("Reitti löytyy kivojen ja mukavien hiirten avulla. Vapaa!")
    else:
        print("Etsintä jatkuu.")

    print("Noita saapastelee kotiin. Vaikuttaa olevan kännissä kuin käki.")
    kehu = input("Kehutko leivontakykyjä?(Kyllä/Ei)").capitalize()
    if kehu == "Kyllä":
        print("Noita raivostuu ja päädyt itse uuniin seuraavan evään ainesosaksi. Bad end.")
    else:
        print("Noita hämmentyy kun ei löydä pulliaan. Työnnät uuniin kun täti tarkistaa sitä, ja liukenet ovesta pihalle. Vapaa!")

Stoori()