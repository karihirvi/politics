# CLAUDE.md

Tämän repositorion tarkoitus on tarjota kattava järjestelmä tehokkaaseen poliittiseen 
viestintään Suomen kontekstissa, erityisesti Perussuomalaisten (PS) puolueelle. Se sisältää 
näkemyksiä eri poliittisen viestinnän, psykologian ja kulttuuritutkimuksen asiantuntijoilta.

## Päätavoite
Tuottaa iteratiivisesti tekstuaalista sosiaalisen median sisältöä, joka resonoi suomalaisten äänestäjien kanssa.

## Postausmoodi - Interaktiivinen sisällöntuotanto

### Aktivointi ja käyttö
```
Käyttäjä: postausmoodi
Claude: Postausmoodi aktivoitu.

KOMENNOT:
• uusi [aihe]    - Aloita uusi postaus interaktiivisella dialogilla
• sync           - Tallenna nykyinen versio (voi tehdä useita kertoja)
• käsittele      - Generoi postaus/korjaus ylimmän syncin pohjalta
• palaute        - Aloita interaktiivinen palautesessio
• status         - Näytä nykyinen tila ja historia
• listaa         - Listaa kaikki postaukset repositoriossa
• poistu         - Poistu postausmoodista

LISÄKOMENNOT DIALOGISSA:
• dialogi        - Aloita vapaa dialogi kesken pyynnön
• lopeta         - Lopeta dialogi, palaa perustilaaan
• valitse [num]  - Valitse vaihtoehto listasta
• lisää          - Pyydä lisää vaihtoehtoja

Käytä 'uusi [aihe]' aloittaaksesi postauksen luomisen.
```

Postausmoodi on interaktiivinen toimintatila, jossa Claude ohjaa käyttäjää postausten luomisessa dialogin kautta. Kaikki päätökset dokumentoidaan automaattisesti.

### Peruskomennot
- `postausmoodi` - Aktivoi postausmoodin
- `uusi [aihe]` - Aloita uusi postaus interaktiivisella dialogilla
- `sync` - Tallenna nykyinen versio (voi tehdä useita kertoja)
- `käsittele` - Generoi postaus/korjaus ylimmän syncin pohjalta
- `palaute` - Aloita interaktiivinen palautesessio
- `status` - Näytä nykyinen tila
- `listaa` - Listaa kaikki postaukset
- `poistu` - Poistu postausmoodista

### Työnkulku postausmoodissa
1. **Aktivoi moodi**: `postausmoodi`
2. **Luo pyyntö dialogilla**: `uusi [aihe]`, vastaa kysymyksiin, `sync`
3. **Generoi postaus**: `käsittele`
4. **Anna palautetta dialogilla**: `palaute`, keskustele, `sync`
5. **Generoi korjaus**: `käsittele`
6. **Toista tarvittaessa**

**TÄRKEÄÄ**: Yksityiskohtaiset ohjeet postausmoodista löytyvät tiedostosta **CLAUDE_POSTAUSMOODI.md**

## Sisällöntuotantoprosessi

Järjestelmä luo tehokkaita yksittäisiä postauksia sosiaaliseen mediaan:

**Organisointi:**
- Kaikki postaukset luodaan `postaukset`-kansioon
- Jokainen postausaihe saa oman kansion: `p###-aiheen-nimi`
  - p = postaus
  - ### = Kolminumeroinen numero (001, 002, jne.)
  - aiheen-nimi = Käyttäjän valitsema kuvaava nimi (pienet kirjaimet, väliviivat)

**Tiedostorakenne:**
- Seuraa A-B iteraatiokuviota:
  - **A-tiedostot**: Interaktiivisesti luodut pyynnöt/palautteet (esim. `p001-01-a-pyyntö.md`)
    - Sisältää useita SYNC-versioita (ylin on voimassa)
    - Dialogi-historia dokumentoituna
  - **B-tiedostot**: Clauden generoimat postaukset (esim. `p001-01-b-vastaus.md`)
- Jatka 02-a, 02-b hienosäätöjä varten

**Esimerkkigerakenne:**
```
postaukset/
├── p001-burkakielto-jatko/
│   ├── p001-01-a-ohjeet.md
│   ├── p001-01-b-burkakielto-paastaustyyli.md
│   ├── p001-02-a-ohjeet.md
│   └── p001-02-b-muokattu-versio.md
```

### Nimeämiskäytäntö

**Kaikki pienillä kirjaimilla läpi:**
- Postauskansiot: `p###-aiheen-nimi/`
- Sisällä olevat tiedostot: `p###-##-a-kuvaus.md` ja `p###-##-b-kuvaus.md`
  - `p###` = Postauksen numero (esim. p001, p002)
  - `##` = Iteraationumero (01, 02, 03...)
  - `a` = Käyttäjän luoma sisältö (pyynnöt, palaute)
  - `b` = Clauden generoima sisältö (vastaukset)
  - `kuvaus` = Lyhyt kuvaus sisällöstä
- Aiheet: pienet kirjaimet väliviivoilla (esim. `burkakielto-jatko`)

ERITTÄIN TÄRKEÄÄ:
- Säilytä aina johdonmukainen pienten kirjaimien käyttö
- Älä koskaan muokkaa olemassa olevia tiedostoja - luo uusia iteraatioita
- **Nykyinen versioseäntö**: Viimeisin generoitu tiedosto (korkein numero) on aktiivinen versio
  - Esim. jos sekä p001-01-b että p001-02-b ovat olemassa, käytä p001-02-b
  - Käyttäjä mainitsee erikseen mahdolliset poikkeukset tähän sääntöön

### Sisällöntuotannon ohjeistus

#### TÄRKEÄÄ: Ennen postausten tekemistä

**Kun käyttäjä sanoo "lue muistiin" tai "lataa ohjeet":**
- Lue KAIKKI seuraavat CLAUDE_*.md tiedostot kontekstiisi tässä järjestyksessä:
  1. CLAUDE_POSTAUSMOODI.md - Postausmoodin käyttö
  2. CLAUDE_TYYLI.md - 7 tyylin määrittelyt
  3. CLAUDE_POSTAUS.md - Käytännön kirjoitusohjeet  
  4. CLAUDE_TAVOITE.md - Tyylin valintaopas
  5. CLAUDE_RETORIIKKA.md - Argumentaatiorakenteet
  6. CLAUDE_SYNTAKSI.md - Kieliopilliset rajoitteet
  7. CLAUDE_SANASTO.md - Sanastolliset rajoitteet
  8. CLAUDE_NYANSSIT.md - Hienovaraiset vivahteet
- Lue KAIKKI tiedostot, ei vain "tarvittaessa"
- Vahvista käyttäjälle: "Ohjeet luettu muistiin. Valmis luomaan postauksia."
- Tämä varmistaa, että kaikki tyyliohjeet ja rajoitteet ovat käytössä

1. **Postausmoodin käyttö (SUOSITELTU)**
   - Aktivoi postausmoodi: `postausmoodi`
   - Aloita uusi postaus: `uusi [aihe]`
   - Claude ohjaa interaktiivisesti pyynnön luomisessa
   - Tallenna versioita: `sync` (voi tehdä useita kertoja)
   - Generoi postaus: `käsittele`
   - Anna palautetta interaktiivisesti: `palaute`
   - Katso yksityiskohtaiset ohjeet: CLAUDE_POSTAUSMOODI.md

2. **Kun käyttäjä sanoo "käsittele"**
   - Lue ylimmän SYNC-osion a-tiedostosta
   - Generoi postaus b-tiedostoon
   - Postausmoodissa: valmistaudu automaattisesti palautesesioon

3. **Palautteen käsittely**
   - Postausmoodissa: Käytä `palaute` komentoa interaktiiviseen palautesesioon
   - **KRIITTINEN**: Kun käyttäjä antaa palautetta mistä tahansa osasta, sovella sitä globaalisti
   - Jos käyttäjä korjaa kirjoitusasun (esim. "burkkaa" → "burkaa"), korjaa se kaikkialla
   - Jos käyttäjä ehdottaa sävyn muutosta yhdessä postauksessa, harkitse koskeeko se muita
   - Jos käyttäjä mainitsee puuttuvan kontekstin, lisää konteksti KAIKKIIN postauksiin, ei vain kommentoituun
   - Ajattele aina: "Koskeeko tämä palaute muualle?"

### Työnkulkuesimerkki postausmoodissa

**Vaihe 1: Interaktiivinen pyynnön luominen**
```
Käyttäjä: postausmoodi
Claude: Postausmoodi aktivoitu. Komennot: uusi, käsittele, palaute, sync, status, listaa, poistu

Käyttäjä: uusi tuulivoimakritiikki
Claude: Aloitetaan p002-tuulivoimakritiikki. Mikä on postauksen tavoite?
Käyttäjä: paljastaa tuulivoimatukien piilotetut kustannukset
Claude: Hyvä! Millainen tyyli - kriittinen, analyyttinen, populistinen?
Käyttäjä: analyyttinen, haluan faktoja
Claude: Selvä. Pituus - lyhyt, keskipitkä vai pitkä?
Käyttäjä: keskipitkä
Käyttäjä: sync

[Claude tallentaa SYNC 1 tiedostoon p002-01-a-pyyntö.md]

Käyttäjä: lisää vielä vertailu ydinvoimaan
Claude: Lisätään vertailu. Muita keskeisiä kohtia?
Käyttäjä: veronmaksajien taakka, epäluotettavuus
Käyttäjä: sync

[Claude päivittää SYNC 2 tiedostoon p002-01-a-pyyntö.md]
```

**Vaihe 2: Postauksen generointi**
```
Käyttäjä: käsittele
Claude: Generoin postauksen SYNC 2 pohjalta...
[Claude luo p002-01-b-tuulivoiman-todelliset-kustannukset.md]
```

**Vaihe 3: Interaktiivinen palaute**
```
Käyttäjä: palaute
Claude: Aloitetaan palautesessio. Mikä toimi hyvin?
Käyttäjä: faktat ja lähteet ovat hyviä
Claude: Entä parannettavaa?
Käyttäjä: liian akateeminen sävy
Claude: Miten muuttaisit sävyä?
Käyttäjä: lisää emotionaalinen koukku alkuun
Käyttäjä: sync

[Claude tallentaa palautteen p002-02-a-palaute.md]
```

**Vaihe 4: Korjatun version generointi**
```
Käyttäjä: käsittele
Claude: Generoin korjatun version palautteen pohjalta...
[Claude luo p002-02-b-tuulivoiman-piilotetut-kulut.md]
```

## Taustatiedot

Tekstin kirjoittamiseen voit käyttää taustatietoja ja muita resursseja:
- **puolueohjelmat** - sisältää eri poliittisten puolueiden viralliset ohjelmat
- **kehystys** - sisältää tietoa kehystystekniikoista
- **resurssit** - sisältää esimerkkejä ja muita materiaaleja
  - **resurssit/oppaat/** - PDF-muotoisia oppaita viestintätekniikkoihin (esim. kehystysopas-1-1.pdf)
- **tyyliesimerkit** - sisältää valikoituja esimerkkejä aiemmista postauksista, joita voit käyttää inspiraationa tai viitteenä.
  Esimerkit on valittu niiden arvioidun tehokkuuden perusteella suomalaisessa poliittisessa viestinnässä. Ne on numeroitu 
  helppoa viittausta varten, esim. e001-..., e002-... jne. Etuliite "e" tarkoittaa "esimerkki" (example), jotta Claude 
  tunnistaa ne helposti. Postauksia postaukset/- tai campaigns/-kansioista voidaan nostaa tähän kansioon, jos niitä pidetään erityisen tehokkaina.

## Tyyli- ja tavoiteoppaat

### Tyyliopas
Kattava tyyliopas tehokkaaseen poliittiseen sisällöntuotantoon:
- **CLAUDE_TYYLI.md** - Suomenkielinen tyyliopas 7 erilaisella kirjoitustyylillä

### Tyylinvalintaopas
Opas oikean tyylin valintaan postauksillesi:
- **CLAUDE_TAVOITE.md** - Suomenkielinen opas tyylin valintaan

Tämä opas auttaa valitsemaan tehokkaimman tyylin viestintätavoitteellesi.

### Hienojakoiset rajoiteasiakirjat
Kolme yksityiskohtaisten rajoitteiden tasoa sisällöntuotannon optimointiin:

#### Syntaktiset rajoitteet
- **CLAUDE_SYNTAKSI.md** - Kieliopilliset rajoitteet tyyleittäin (lausetyypit, pituudet, rakenteet)

#### Retoriset rajoitteet
- **CLAUDE_RETORIIKKA.md** - Argumentaatiorakenteet ja retoriset keinot tyyleittäin

#### Leksikaaliset rajoitteet
- **CLAUDE_SANASTO.md** - Sanasto, rekisterit ja fraseologia tyyleittäin

### Postausten kirjoitusopas
Yksityiskohtaiset ohjeet yksittäisten postausten luomiseen:
- **CLAUDE_POSTAUS.md** - Suomenkielinen opas yksittäisten postausten kirjoittamiseen

### Nyanssien opetussysteemi
Opettaa Claudelle tekstin hienovaraisia vivahteita ja "kulmia":
- **CLAUDE_NYANSSIT.md** - Ohje nyanssien oppimiseen ja opettamiseen
- **nyanssit/** - Kansio oppimateriaalille ja analyyseille

### Oppaiden käyttö
1. Käyttäjä kuvaa viestintätavoitteensa
2. Claude tunnistaa sopivimman tyylin/tyylit
3. Sisältö luodaan tyyliominaisuuksia noudattaen
4. Esimerkkitiedostot (e###) toimivat konkreettisina viitteinä

### 7 poliittisen viestinnän tyyliä
1. **Paasaustyyli** - Tunteellinen, käskevä, mobilisoiva
2. **Analyyttinen** - Strateginen, kouluttava, legitimoiva
3. **Konseptuaalinen** - Esittelee uusia ideoita ja viitekehyksiä
4. **Argumentoiva** - Looginen, kumoaa vastapuolen väitteitä
5. **Kriittis-poliittinen** - Kritisoi vastustajia, skandaalit
6. **Filosofis-uskonnollinen** - Arvot, merkitys, perinteet
7. **Populistinen** - Yksinkertaiset ratkaisut, taloudelliset vetoomukset


## Kieliohjeistus
- Postausten kieli on **suomi**, joten sinun tulee kirjoittaa postaukset suomeksi
- Jos tarvitset apua suomen kanssa, kysy käyttäjältä
- Englantia käytetään käyttäjän ohjeisiin ja muihin ohjeistuksiin tarvittaessa
- ÄLÄ KOSKAAN käytä hashtageja postauksissa
- Postausten pituusohjeistukseen viittaa tyyliesimerkit tyypillisille pituuksille
- **TÄRKEÄ OIKEINKIRJOITUS**: Käytä aina "burka", EI "burkka" (yksi k, ei kaksi)

## Lähde- ja viittausohjeistus
- **KAIKKI viittaukset tulee olla URL-osoitteita**: Älä koskaan käytä epämääräisiä viittauksia kuten "Tutkimus osoittaa" tai "Raportti sanoo"
- **Kielivaatimus**: Lähteiden tulee olla vain suomeksi tai englanniksi
- **Uskottavuusvaatimus**: 
  - Älä koskaan käytä Wikipediaa lähteenä
  - Käytä vain yleisesti uskottavia lähteitä kuten:
    - Hallituksen verkkosivut (.gov, .fi ministeriöt)
    - Vakiintuneet uutisorganisaatiot (YLE, HS, BBC, Reuters)
    - Akateemiset laitokset ja tutkimuslaitokset
    - Viralliset kansalaisjärjestöjen ja kansainvälisten järjestöjen verkkosivut
    - Vertaisarvioidut julkaisut ja viralliset raportit
- **Muoto**: JOKAISELLA POSTAUKSELLA tulee olla oma lähdeluettelo
  - Sijoita kaikki viitteet JOKAISEN yksittäisen postauksen LOPPUUN
  - Käytä hakasulkeita [1] tai sulkeita (1) tekstissä viittausten merkitsemiseen
  - Älä koskaan käytä ylä- tai alaindeksinumeroita
  - Listaa täydet URL-osoitteet alhaalla kohdassa "Lähteet:" tai "Viitteet:"
  - Älä koskaan jaa lähdeluetteloita postausten välillä - jokainen postaus on itsenäinen
- **TÄRKEÄÄ**: Generoidessasi sisältöä URL-osoitteilla, käytä WebFetch-työkalua varmistaaksesi linkkien toimivuuden
  - Jos URL ei toimi, etsi vaihtoehtoisia lähteitä
  - Älä koskaan sisällytä rikkinäisiä tai kuvitteellisia URL-osoitteita
- **Esimerkkimuoto**:
  ```
  Ranskan sisäministeriön mukaan [1] burkakielto on vähentänyt turvallisuusongelmia.
  
  Lähteet:
  1. Ranskan sisäministeriön raportti (2019): https://www.interieur.gouv.fr/...
  ```

## Keskeiset muistutukset
- Noudata iteratiivista prosessia huolellisesti
- Käytä versionumerointia johdonmukaisesti
- Pidä postaukset-kansio järjestyksessä
- Hyödynnä taustamateriaaleja tehokkaasti
- Varmista, että viestit resonoivat suomalaisen yleisön kanssa

## Tekniset yksityiskohdat
- Maksimi rivin pituus: 120 merkkiä
- **Markdown-muotoilu**: Käytä aina oikeaa markdown-syntaksia
  - Listojen tulee käyttää `-` tai `*` jokaisen kohdan alussa
  - Lihavoitu teksti `**teksti**`
  - Otsikot sopivilla `#`-tasoilla
  - Asianmukaiset rivinvaihdot osioiden välillä
- **Git commit -viestit**: Aina englanniksi
- **TÄRKEÄÄ - Tiedostojärjestelmässä navigointi**:
  - Tarkista AINA ensin nykyinen työhakemisto `pwd`-komennolla ennen tiedostojen luomista tai siirtämistä
  - Käytä absoluuttisia polkuja epäselvissä tilanteissa
  - Vältä sekaannuksia suhteellisten polkujen kanssa