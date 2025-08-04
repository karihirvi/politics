# Poliittisen viestinnän suunnittelujärjestelmä

Systemaattinen lähestymistapa tehokkaaseen poliittiseen viestintään Suomen kontekstissa.

## Viestintäsuunnittelun filosofia

Perinteistä poliittista viestintää on käsitelty taidemuotona—luottaen intuitioon, karismaan ja yrityksen ja erehdyksen menetelmään. Tämä repositorio edustaa paradigman muutosta: poliittisen viestinnän käsittelyä suunnittelutieteenä, jossa viestit voidaan systemaattisesti suunnitella, optimoida ja hioa mitattavien rajoitteiden ja todistettujen mallien perusteella.

Viestintäsuunnittelun ytimessä on optimointiongelma: ihmiset määrittelevät tavoitteet, koneet käyttävät optimointia luodakseen viestejä, jotka ihmisten lukemina tuottavat maksimaalisen vaikutuksen tavoitteiden edistämisessä. Vaikka ihmiset ovat paljon enemmän kuin reaktiivisia koneita, suostuttelun mallintamisen tarkoituksessa voimme approksimoida yleisön reaktioita toisena kielimallina—sellaisena, joka reagoi tilastollisesti tiettyihin kielellisiin ja emotionaalisiin malleihin. Tämä ei tarkoita deterministisiä reaktioita, vaan pikemminkin todennäköisyyksiä, joita voidaan mitata ja optimoida.

Aivan kuten ohjelmistosuunnittelu muutti ohjelmoinnin käsityöstä tieteenalaksi, viestintäsuunnittelu muuttaa poliittisen viestinnän arvailusta tieteeksi. Hajottamalla monimutkaisen suostutteluhaasteen hallittaviksi abstraktiotasoiksi voimme optimoida jokaista komponenttia itsenäisesti varmistaen samalla niiden harmonisen yhteistoiminnan.

## Ihmisesimerkkien kriittinen rooli

Mikään suunnittelujärjestelmä ei voi toimia ilman empiiristä dataa. Viestintäsuunnittelussa `tyyliesimerkit/`-kansio toimii koulutusdatanamme—todellisia viestejä, jotka ovat osoittautuneet tehokkaiksi suomalaisessa poliittisessa kontekstissa. Nämä esimerkit eivät ole pelkkää inspiraatiota; ne ovat perustottuus, joka rajoittaa ja ohjaa optimointijärjestelmää.

Esimerkit palvelevat useita tarkoituksia:
- **Validointi**: Todiste siitä, että tietyt lähestymistavat toimivat todellisten yleisöjen kanssa
- **Rajoitteet**: Määrittelevät hyväksyttävän ja tehokkaan viestinnän rajat
- **Mallit**: Paljastavat resonoivat kielelliset ja retoriset rakenteet
- **Mittarit**: Tarjoavat mitattavia menestyksen indikaattoreita (näkymät, sitoutuminen, vaikutus)

Ilman näitä ihmisten luomia esimerkkejä järjestelmä optimoisi sokeasti. Niiden avulla se voi oppia, mikä todella saa ihmiset toimimaan.

## Miksi abstraktiotasot ovat tärkeitä

Monimutkaiset järjestelmät vaativat hierarkkista organisointia. Aivan kuten rakennus tarvitsee arkkitehtuurin, rakenteen, materiaalit ja yksityiskohdat, tehokas poliittinen viestintä vaatii useita suunnittelun ja toteutuksen tasoja:

- **Ilman abstraktiota**: Kirjoittajat ylikuormittuvat yrittäessään jongleerata strategiaa, tyyliä, kielioppia ja sanavalintojai samanaikaisesti
- **Abstraktion kanssa**: Jokaista tasoa voidaan optimoida itsenäisesti, selkeiden rajapintojen kanssa tasojen välillä
- **Tulos**: Johdonmukaisempaa, tehokkaampaa ja skaalautuvampaa viestintää

Abstraktiohierarkia mahdollistaa "mitä sanoa" erottamisen "miten sanoa" -kysymyksestä ja "mitä sanoja käyttää" -kysymyksestä—mahdollistaen systemaattisen parantamisen jokaisella tasolla.

## Miten tämä järjestelmä toimii

Tämä repositorio tarjoaa monitasoisen rajoitejärjestelmän, joka mahdollistaa AI-työkalujen (erityisesti Clauden) toimimisen kehittyneinä optimointimoottoreina poliittiselle viestinnälle. Määrittelemällä rajoitteita eri abstraktiotasoilla järjestelmä ohjaa erittäin kohdennetun ja tehokkaan poliittisen sisällön tuottamista.

### Viisi abstraktiotasoa

#### Taso 1: Strategiset tavoitteet (Korkein abstraktio)
**Tiedostot:** `CLAUDE_TAVOITE.md`
- **Tarkoitus**: Määrittele mitä haluat saavuttaa
- **Sisältö**: Kampanjatavoitteet, psykologiset matkamallit, strategiset sekvenssit
- **Esimerkki**: "Muuta skeptikot kannattajiksi" tai "Mobilisoi kannattajakunta toimintaan"

#### Taso 2: Viestintätyylit
**Tiedostot:** `CLAUDE_TYYLI.md`
- **Tarkoitus**: Määrittele miten viestiä
- **Sisältö**: 7 erillistä poliittisen viestinnän tyyliä ainutlaatuisine ominaisuuksineen
- **Esimerkki**: Paasaustyyli kokoontumisiin, Analyyttinen tyyli intellektuellien suostutteluun

#### Taso 3: Retoriset rakenteet
**Tiedostot:** `CLAUDE_RETORIIKKA.md`
- **Tarkoitus**: Määrittele argumentaatiomallit
- **Sisältö**: Todistustyypit, kehystysmenetelmät, narratiivikaaret
- **Esimerkki**: Käytä emotionaalisia vetoomuksia 60%, loogisia argumentteja 40%

#### Taso 4: Syntaktiset mallit
**Tiedostot:** `CLAUDE_SYNTAKSI.md`
- **Tarkoitus**: Määrittele lauserakenteet
- **Sisältö**: Lausetyypit, pituudet, kieliopilliset mallit
- **Esimerkki**: 40-60% imperatiivisia lauseita Paasaustyylissä

#### Taso 5: Leksikaaliset valinnat
**Tiedostot:** `CLAUDE_SANASTO.md`
- **Tarkoitus**: Määrittele sanavalinta
- **Sisältö**: Sanasto, rekisterit, avainlauseet
- **Esimerkki**: Käytä "sisu" ja muita kulttuurisia avainsanoja Paasaustyylissä

## Repositorion rakenne

```
├── postaukset/        # Yksittäiset taktiset viestit  
├── puolueohjelmat/    # Lähdemateriaali ja kannat
├── kehystys/          # Viestintätekniikat
├── tyyliesimerkit/    # PERUSTA: Ihmisten luomat tehokkaat esimerkit
└── CLAUDE_*.md        # Suunnitteluspesifikaatiot
```

### Optimointivirta

1. **Ihmisen syöte**: Onnistuneet esimerkit osoittavat mikä toimii
2. **Mallien poiminta**: Järjestelmä analysoi esimerkkejä kielellisten mallien löytämiseksi
3. **Rajoitteiden määrittely**: Malleista tulee mitattavia rajoitteita
4. **Tavoitteen asettaminen**: Ihminen määrittelee halutun lopputuloksen
5. **Optimointi**: Järjestelmä generoi sisältöä maksimoiden tavoitteen saavuttamisen
6. **Ihmisen palaute**: Tulokset informoivat seuraavaa iteraatiota

## Aloittaminen

1. **Määrittele tavoitteesi**: Minkä poliittisen tavoitteen haluat saavuttaa?
2. **Konsultoi strategiaopasta**: `CLAUDE_TAVOITE.md` kartoittaa tavoitteesi kampanjarakenteeksi
3. **Tarkastele saatavilla olevia tyylejä**: `CLAUDE_TYYLI.md` näyttää työkalupakin työkalut
4. **Tutki esimerkkejä**: `tyyliesimerkit/`-kansio sisältää taistelussa testattua sisältöä
5. **Luo iteratiivisesti**: Käytä A-B tiedostokuviota viestisi hiomiseen
6. **Anna järjestelmän ohjata**: Jokainen abstraktiotaso tarjoaa erityisiä rajoitteita

## Keskeinen innovaatio

Tämä järjestelmä muuttaa poliittisen viestinnän intuitiivisesta taiteesta systemaattiseksi suunnitteluksi:
- Hajottamalla monimutkaisuuden hallittaviksi tasoiksi
- Tarjoamalla mitattavia rajoitteita jokaisella tasolla
- Mahdollistamalla systemaattisen optimoinnin
- Luomalla toistettavia tuloksia
- Sallimalla jatkuvan parantamisen iteraation kautta

## Järjestelmän rajoitukset

### Kampanjaluomisen haasteet

Vaikka tämä järjestelmä loistaa yksittäisten postausten luomisessa erityisillä tyyleillä, Claudella on osoitettu rajoituksia täysien monivaiheisten kampanjoiden luomisessa:

- **Lähteiden eheys**: Kampanjoita luotaessa Claude saattaa esittää lähteitä väärin, viitaten tutkimukseen, joka itse asiassa argumentoi kampanjan kantaa vastaan
- **Johdonmukaisuus**: Yhtenäisen poliittisen kannan ylläpitäminen useiden postausten ja vaiheiden yli osoittautuu haasteelliseksi
- **Psykologinen yhtenäisyys**: 5-vaiheinen matkamalli (HERÄTÄ → KIIHDYTÄ → KOULUTA → AKTIVOI → INTEGROI) vaatii hienovaraista psykologista etenemistä, joka ylittää nykyiset kyvyt

### Suositeltu lähestymistapa

Parhaisiin tuloksiin:
- Keskity luomaan voimakkaita yksittäisiä postauksia käyttäen 7 viestintätyyliä
- Käytä tyylinvalintaoppaita (CLAUDE_TAVOITE.md) valitaksesi tehokkaimman lähestymistavan
- Hyödynnä rajoitejärjestelmää yksittäisille viesteille monimutkaisten kampanjoiden sijaan
- Harkitse ihmisvetoista kampanjasuunnittelua AI-avusteisella yksittäisten postausten luomisella

Järjestelmä pysyy erittäin tehokkaana ydintarkoituksessaan: yksittäisten poliittisen viestinnän osien suunnittelussa ennennäkemättömällä tarkkuudella ja vaikutuksella.

## Kieli

- Suomi varsinaiselle poliittiselle sisällölle
- Englanti järjestelmädokumentaatioon tarvittaessa
- Esimerkit sisältävät molempia kieliä maksimaalisen oppimisen vuoksi

---

*Tämä repositorio edustaa uutta lähestymistapaa poliittiseen viestintään—sellaista, joka yhdistää ihmisen luovuuden systemaattiseen optimointiin saavuttaakseen ennennäkemätöntä tehokkuutta digitaalisella aikakaudella.*