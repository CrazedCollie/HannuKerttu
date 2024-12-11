def Stoori():
    print("Löydät itsesi istumasta vanhan metsämökin keittiöstä. Et ole varma kuinka tähän päädyttiin, mutta jostain tulee fiilis että poistuminen ripeästi saattaisi olla hyvä vaihtoehto.")

    kumpi = input("Oletko Hannu vai Kerttu?")

    voima = input("Yrität katsoa josko oven saisi auki. Riittääkö voimia?(Kyllä/Ei)")
    If voima == "Kyllä":
	    print("Vapaa, vapaa vihdoin! Mä en enää vandalisoi tätä kioskia!")
    If voima == "Ei":
	    print("Pitää etsiä toinen reitti.")

    print("Ikkunat ovat lukossa. Otat pullaa. Niitä on kymmenisen kappaletta, tuoksuvatkin mokomat aika hyvälle. Tuoreita?")
    pullat = int(input("Montako otat? (0-10)"))
    If pullat <5 AND kumpi = "Hannu":
	print("Pullat mukaan ja menoksi. Vapaa!")
	If pullat 5>= OR kumpi = "Kerttu":
		print("Ketuille meni, pitää jatkaa etsintöjä.")

    print("Pullat on aika hyviä, mutta jumissa ollaan. Noita on krapuloissaan höpöttänyt lattialuukun reitistä, ehkä se toimii?")
    hiiri = input("Annatko hiirille pullaa että ehkä auttavat?(Kyllä/Ei)")
	If hiiri = "Kyllä":
		print("Reitti löytyy hiirten avulla. Vapaa!")
	If hiiri = "Ei":
		print("Etsintä jatkuu.")

    print("Noita saapastelee kotiin. Vaikuttaa olevan kännissä kuin käki.")
    kehu = input("Kehutko leivontakykyjä?(Kyllä/Ei)")
	If kehu = "Kyllä":
		print("Noita raivostuu ja päädyt itse uuniin seuraavan evään ainesosaksi. Bad end.")
	If kehu = "Ei":
		print("Noita hämmentyy kun ei löydä pulliaan. Työnnät uuniin kun täti tarkistaa sitä, ja liukenet ovesta pihalle. Vapaa!")

Stoori()