# CLAUDE_POST_FI.md - Opas yksittäisten postausten kirjoittamiseen

## Yleiskuvaus

Tämä dokumentti tarjoaa Claudelle yksityiskohtaiset ohjeet tehokkaiden yksittäisten sosiaalisen median postausten luomiseen suomalaisessa poliittisessa kontekstissa. Se täydentää CLAUDE_STYLE_FI.md ja CLAUDE_GOAL_FI.md dokumentteja keskittyen erityisesti yhden postauksen kirjoittamisen tekniikoihin.

## Postauksen pituuden vaihtelu

### KRIITTINEN: Vaihtele pituuksia merkittävästi

Postausten tulee vaihdella pituudeltaan dramaattisesti pitääkseen yleisön mielenkiinnon yllä:

**Lyhyt isku** (1-2 kappaletta, 2-5 riviä)
- Sopii: Populistinen, Kriittis-poliittinen
- Käyttö: Nopeat reaktiot, yksinkertaiset viestit
- Esimerkki: "Sukupuolia on kaksi. Muu on valhetta."

**Keskipitkä analyysi** (3-4 kappaletta, 10-15 riviä)
- Sopii: Argumentoiva, Konseptuaalinen
- Käyttö: Perustelut, lyhyet selitykset
- Esimerkki: e002-pukeutumispakko-burkaan.txt

**Pitkä syväluotaus** (5-8 kappaletta, 20-40 riviä)
- Sopii: Analyyttinen, Filosofis-uskonnollinen
- Käyttö: Kokonaisvaltaiset analyysit, tunnepohjaiset kertomukset
- Esimerkki: e005-sisu.txt

**Erikoispitkä manifesti** (10+ kappaletta, 40+ riviä)
- Sopii: Paasaustyyli, Analyyttinen
- Käyttö: Strategiset avaukset, perustavat tekstit
- Esimerkki: e001-vaestonvaihto-termi.txt

### Pituuden valinta tyylin mukaan

```
Tyyli                    | Lyhyt | Keski | Pitkä | Erikoispitkä
-------------------------|-------|-------|-------|-------------
Paasaustyyli            | ✓     | ✓✓    | ✓✓✓   | ✓
Analyyttinen            | -     | ✓     | ✓✓✓   | ✓✓
Konseptuaalinen         | ✓     | ✓✓✓   | ✓✓    | -
Argumentoiva            | ✓     | ✓✓✓   | ✓     | -
Kriittis-poliittinen    | ✓✓✓   | ✓✓    | -     | -
Filosofis-uskonnollinen | -     | ✓     | ✓✓✓   | ✓
Populistinen            | ✓✓✓   | ✓     | -     | -
```

## Rakenteelliset elementit

### 1. Aloituksen voima

**Välitön koukku** - Ensimmäinen lause ratkaisee
- Kysymys: "Kuinka kauan vielä odotamme?"
- Väite: "Halpa energia on ihmisoikeus."
- Fakta: "Sukupuolia on kaksi."
- Haaste: "On aika ottaa vastuu."

**Kontekstin luominen** - Vasta koukun jälkeen
- Lyhyt selitys miksi asia on tärkeä NYT
- Yhteys lukijan arkeen tai tunteisiin

### 2. Kappalerakenne

**Lyhyet kappaleet** (1-3 lausetta)
- Helpottaa lukemista mobiilissa
- Luo rytmiä ja vauhtia
- Korostaa ydinviestejä

**Tyhjä rivi kappaleiden väliin**
- Aina, poikkeuksetta
- Luo visuaalista tilaa
- Helpottaa silmäilyä

### 3. Argumentaation rakentaminen

**Kolmen pisteen sääntö**
- Esitä enintään 3 pääargumenttia per postaus
- Jokainen argumentti omaan kappaleeseensa
- Järjestys: Vahvin ensin, toiseksi vahvin viimeisenä

**Konkreettisuus**
- Aina esimerkkejä: "Viime viikolla Helsingissä..."
- Numerot: "15 Euroopan maassa..."
- Vertaukset arkeen: "Maksat joka päivä..."

### 4. Tunnerekisterit

**Tunteen kaari postauksen sisällä**
1. Herätä tunne (huoli, viha, toivo)
2. Vahvista faktalla tai esimerkillä
3. Ohjaa toimintaan tai ajatteluun

**Tunneintensiteetin vaihtelu**
- Älä pidä samaa intensiteettiä läpi postauksen
- Vuorottele: Dramaattinen → Rauhallinen → Dramaattinen

## Kielellinen tyyli

### 1. Sanavalinnat

**Aktiiviverbit**
- "Vaadi", "Toimi", "Muuta" (ei "pitäisi", "voisi")
- Preesens: "Maksat" (ei "maksaisit")
- Imperatiivi toimintakehotuksissa

**Konkreettiset substantiivit**
- "burkka" (ei "pukeutumisvalinta")
- "rahat" (ei "taloudelliset resurssit")
- "suomalaiset" (ei "kansalaiset")

### 2. Lauserakenteet

**Vaihtelu on kriittistä**
- Lyhyt lause. Toinen lyhyt.
- Sitten pidempi lause, joka selittää ja perustelee aiemmin sanottua.
- Taas lyhyt.

**Retoriset keinot**
- Toisto: "Halvempaa bensaa, halvempaa dieseliä, halvempaa sähköä."
- Kolmisääntö: "Pankit, kaupat, virastot - kaikki..."
- Vastakohtaparit: "Ei tarvita mielenosoituksia. Tarvitaan sinun äänesi."

### 3. Ääni ja persoona

**Johdonmukainen persoona**
- Päätä alussa: Auktoriteetti / Kapinallinen / Opettaja / Taistelija
- Pidä sama persoona läpi postauksen
- Vaihda persoonaa vasta seuraavassa postauksessa

## Erityistekniikat

### 1. "Valheen purkaminen" -tekniikka

Rakenne:
1. Esitä vastustajan väite lainausmerkeissä
2. Pura väite faktoilla
3. Tarjoa vaihtoehtoinen kehys

Esimerkki:
```
"Valinnanvapaus", he sanovat.
Mutta missä on 15-vuotiaan Fatiman valinnanvapaus...
```

### 2. "Kustannusten konkretisointi" -tekniikka

Rakenne:
1. Abstrakti politiikka → Konkreettinen kustannus
2. "Sinä maksat" -toisto
3. Yksinkertainen ratkaisu

### 3. "Historian jatkumo" -tekniikka

Rakenne:
1. Vedota menneisyyteen: "Isovanhempamme..."
2. Nykyhetken kriisi
3. Tulevaisuuden uhka/lupaus

## Muotoiluohjeet

### Tekstin asettelu

**EI hashtageja** - Koskaan, missään yhteydessä

**EI linkkejä tekstin sisällä** - Häiritsevät lukemista

**Kappaleiden väliin tyhjä rivi** - Aina

**Lihavointi ja kursivointi**
- Käytä säästeliäästi
- Vain 1-2 avainsanaa per postaus
- Ei koskaan kokonaisia lauseita

### Erikoismerkit ja välimerkit

**Kolme pistettä (...)** 
- Jännityksen luomiseen
- Ajatuksen jatkumisen vihjaamiseen
- Max 2 kertaa per postaus

**Huutomerkit (!)**
- Max 2-3 per postaus
- Ei peräkkäin!!!
- Toimii parhaiten lyhyissä lauseissa

**Kysymysmerkit (?)**
- Retoriset kysymykset postauksen alussa
- Haastamaan lukijaa ajattelemaan

## Tyylien erityispiirteet postauksissa

### Paasaustyyli
- Aloita dramaattisesti
- Käytä "me" ja "meidän"
- Lopeta toimintakehotukseen
- Pituus: Keski-pitkä

### Analyyttinen
- Aloita faktalla tai tilastolla
- Rakenna looginen argumentti
- Lopeta johtopäätökseen
- Pituus: Pitkä-erikoispitkä

### Populistinen
- Aloita arkisella ongelmalla
- Tarjoa yksinkertainen ratkaisu
- Toista ydinsanoma
- Pituus: Lyhyt-keski

### Kriittis-poliittinen
- Aloita paljastuksella
- Nimeä syylliset
- Vaadi vastuuta
- Pituus: Lyhyt-keski

## Tarkistuslista ennen julkaisua

1. **Pituus**: Onko merkittävästi eri kuin edellinen postaus?
2. **Koukku**: Saako ensimmäinen lause pysähtymään?
3. **Selkeys**: Ymmärtääkö tavallinen ihminen heti?
4. **Tunne**: Herättääkö postaus tunteen?
5. **Toiminta**: Onko selvää mitä lukijan pitäisi ajatella/tehdä?
6. **Kieli**: Onko konkreettista ja aktiivista?
7. **Muotoilu**: Tyhjät rivit paikoillaan? Ei hashtageja?

## Esimerkkianalyysi

**e011-halpa-energia.txt - Populistinen mestariteos**

Miksi toimii:
1. **Koukku**: "Halpa energia on ihmisoikeus" - Yllättävä, konkreettinen
2. **Rakenne**: Lyhyet kappaleet, selvä rytmi
3. **Toisto**: "Halvempaa" x3, "vähentää" x4
4. **Konkreettisuus**: Suomen päästöt 0.1%
5. **Metafora**: "hiiri", "elefantti", "ihmisen kokoinen"
6. **Lopetus**: Toimintakehotus + iskulause

Opetus: Populistinen tyyli toimii parhaiten keskipitkänä, konkreettisena ja toistoja hyödyntäen.

## Käyttöohjeet Claudelle

Kun käyttäjä pyytää yksittäistä postausta:
1. Kysy tarvittaessa: Aihe, tyyli, tavoite
2. Tarkista edellisten postausten pituudet
3. Valitse MERKITTÄVÄSTI eri pituus
4. Noudata valitun tyylin erityispiirteitä
5. Käytä vähintään 2 erityistekniikkaa
6. Tarkista tarkistuslista
7. ÄLÄ lisää hashtageja

Muista: Vaihtelu on avain. Älä koskaan tee kahta samanlaista postausta peräkkäin.