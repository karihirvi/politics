# KAYTTOOHJE.md - Järjestelmän käyttöohjeet

Tämä dokumentti opastaa järjestelmän käytössä Claude Coden kanssa.

## Pikaopas

1. **Lataa ohjeet muistiin:** `lue muistiin` tai `lataa ohjeet`
2. **Luo postaus:** `luo postaus aiheesta X tyylillä Y`
3. **Käsittele:** `käsittele` tai `käsittely` (prosessoi A-tiedoston)
4. **Iteroi:** Kirjoita palaute A-tiedostoon → `käsittele`
5. **Opi:** `analysoi mikä toimi`

**A-B tiedostot:**
- **A** = Käyttäjän kirjoittamat pyynnöt ja palautteet
- **B** = Clauden luomat vastaukset
- Numerot = Iteraatiokierrokset (01, 02, 03...)

## Sisällysluettelo

1. [Postauksen luominen ja iterointi](#1-postauksen-luominen-ja-iterointi)
2. [Nyanssien oppiminen](#2-nyanssien-oppiminen)
3. [CLAUDE_*.md tiedostojen päivittäminen](#3-claude_md-tiedostojen-päivittäminen)
4. [Yleisten .md tiedostojen päivittäminen](#4-yleisten-md-tiedostojen-päivittäminen)
5. [Viestintä Clauden kanssa](#5-viestintä-clauden-kanssa)

## 1. Postauksen luominen ja iterointi

### Ennen aloittamista

**TÄRKEÄÄ: Lataa ohjeet muistiin**
```
lue muistiin
```
Claude lukee kaikki CLAUDE_*.md tiedostot kontekstiinsa ja vahvistaa: "Ohjeet luettu muistiin. Valmis luomaan postauksia."

### Uuden postauksen aloittaminen

**Vaihe 1: Kerro Claudelle mitä haluat**
```
luo postaus burkakiellosta populistisella tyylillä
```

**Vaihe 2: Claude luo kansiorakenteen**
Claude luo automaattisesti:
- `postaukset/p###-aihe-nimi/` (esim. p004-burkakielto-jatko)
- `p###-01-a-pyyntö.md` pyyntötiedoston

**Vaihe 3: Täydennä pyyntötiedosto**
Muokkaa luotua pyyntötiedostoa tarvittaessa. Claude luo pohjan:
```markdown
# Pyyntö: [Aihe]

Tavoite: [Mitä haluat saavuttaa]
Tyyli: [Valittu tyyli]
Pituus: [LYHYT/KESKIPITKÄ/PITKÄ/ERIKOISPITKÄ]
Keskeiset kohdat:
- [Pääviesti 1]
- [Pääviesti 2]
- [Pääviesti 3]
```

**Vaihe 4: Käsittele pyyntö**
```
käsittele
```
Claude:
1. Luo vastauksen B-tiedostoon (esim. `p004-01-b-burkakielto-populistinen.md`)
2. Luo AUTOMAATTISESTI seuraavan iteraation palautepohjan (esim. `p004-02-a-palaute.md`)

### Postauksen iterointi

**Kirjoita palautteesi A-tiedostoon** (esim. `p004-02-a-palaute.md`):

```markdown
# Palaute edelliseen versioon

- Lisää enemmän tunnetta alkuun, erityisesti huolta tulevaisuudesta
- Tämä on liian pitkä keskiosaltaan, lyhennä analyyttistä osuutta  
- Konkretisoi esimerkeillä suomalaisesta arjesta
```

**Sitten käsittele palaute:**
```
käsittele
```

**Vaihtoehtoisesti pyydä variaatioita A-tiedostossa:**

```markdown
# Pyyntö: Variaatiot

Luo 3 erilaista versiota tästä viestistä:
- Versio 1: Korostetusti emotionaalinen
- Versio 2: Faktapainotteinen  
- Versio 3: Henkilökohtainen tarina -lähestyminen
```

**Viimeistelyvaihe A-tiedostossa:**

```markdown
# Viimeistely

Hyvä pohja, mutta:
- Lopetus jää vaisuksi. Tee iskevämmäksi.
- Lisää toimintakehotus
```

### Hyödyllisiä komentoja postauksille

```
käsittele
```
```
Luo 3 erilaista versiota tästä viestistä
```
```
Yhdistä version 1 emotionaalinen alku version 3 analyyttiseen loppuun
```
```
Lyhennä tämä puoleen alkuperäisestä pituudesta
```
```
Lisää 2-3 uskottavaa lähdettä väitteiden tueksi
```

## 2. Nyanssien oppiminen

### Nyanssit syntyvät iteraatioista

Nyanssit ovat hienovaraisia vivahteita, jotka Claude oppii analysoimalla iteraatioita.

**Vaihe 1: Iteroi postaus valmiiksi**
```
Luo postaus energiapolitiikasta populistisella tyylillä
```
[iteroi kunnes tyytyväinen]
```
Tämä on juuri oikea sävy! Tallenna tämä.
```

**Vaihe 2: Pyydä nyanssianalyysia**
```
Analysoi mikä muuttui iteraatioiden aikana ja miksi lopullinen versio toimii
```

**Vaihe 3: Claude tunnistaa opitun**
```
"Huomasin että:
- Lisäsimme 'arkijärki' -termin 3 kertaa
- Vaihdoimme 'kansalaiset' → 'tavalliset ihmiset'
- Lyhensimme lauseita 40%
Luon tästä nyanssi-ohjeen."
```

**Vaihe 4: Dokumentointi**
Claude luo `nyanssit/energia-arkijarki.md` tiedoston opituista nyansseista.

### Nyanssien kerääminen useista postauksista

```
Analysoi postaukset p001-p005 ja tunnista yhteiset onnistumisen elementit populistisessa tyylissä
```

```
Vertaa kaikkia burka-aiheisia postauksia ja tunnista mikä tekee niistä tehokkaita
```

### Anti-patternien tunnistaminen

**Kun tunnistat ei-toivottuja elementtejä:**
```
Analysoi mitkä elementit eivät sovi suomalaiseen poliittiseen viestintään
```

**Dokumentoi havaitut anti-patternit:**
```
Huomasin että käytit "toisaalta...toisaalta" -rakennetta. Lisää tämä anti-patterns.md tiedostoon.
```

## 3. CLAUDE_*.md tiedostojen päivittäminen

### Perussääntö
CLAUDE_*.md tiedostot ovat järjestelmän ydindokumentaatiota. Ne päivittyvät orgaanisesti käytön myötä.

### Konsistenssin tarkistaminen

**Pyydä kokonaistarkistus:**
```
Tarkista ovatko kaikki CLAUDE_*.md tiedostot keskenään konsistentteja ja ajan tasalla
```

**Tarkista käytännön vastaavuus:**
```
Tarkista vastaako nykyinen tyyliopas todellista käytäntöä postaukset-kansiossa
```

**Vertaa ohjeita toteutukseen:**
```
Vertaa järjestelmän ohjeita viimeisimpiin postauksiin. Ovatko ne vielä päteviä?
```

### Oppimisen dokumentointi

**Kun löydät uuden toimivan käytännön:**
```
Tämä burka-postaus toimi erityisen hyvin. Päivitä CLAUDE_*.md tiedostot heijastamaan tätä käytäntöä.
```

**Kun huomaat puutteen järjestelmässä:**
```
Lisää puuttuva ohje lähteiden käytöstä perustuen viimeisimpiin postauksiin
```

## 4. Yleisten .md tiedostojen päivittäminen

### README.md päivitykset

```
Päivitä README.md kuvaamaan uusi nyanssien oppimisjärjestelmä
```
```
README on liian tekninen tavalliselle käyttäjälle. Tee siitä konkreettisempi.
```

### Resurssitiedostojen päivittäminen

```
Lisää resurssit/fraasit.md tiedostoon uusia tehokkaita ilmaisuja viimeisimmistä postauksista
```
```
Lisää uusi retorinen tekniikka "henkilökohtainen tarina" retoriset-tekniikat.md tiedostoon
```

### Dokumentaation luominen

```
Luo uusi tiedosto resurssit/somekanavat.md joka kuvaa eri somekanavien erityisvaatimukset
```

## 5. Viestintä Clauden kanssa

### Yleiset periaatteet

**Ole konkreettinen:**
- ❌ "Tee parempi"
- ✅ "Lisää emotionaalinen koukku alkuun"

**Anna kontekstia:**
- ❌ "Korjaa tämä"
- ✅ "Tämä postaus on liian akateeminen PS:n tyyliin, tee kansanomaisemmaksi"

**Käytä esimerkkejä:**
- ❌ "Kirjoita eri tavalla"
- ✅ "Kirjoita tyylillä kuten e011-halpa-energia.txt"

### Hyödylliset fraasit

**Aloittaminen:**
```
Luo uusi postaus maahanmuutosta kriittis-poliittisella tyylillä
```

**Iterointi:**
```
Tämä on hyvä pohja, mutta tarvitsee enemmän konkreettisia esimerkkejä
```

**Oppiminen:**
```
Analysoi miksi tämä burka-postaus resonoi niin hyvin
```

**Metatason ohjaus:**
```
Tarkista noudattaako tämä postaus populistisen tyylin ohjeita
```

### Ongelmatilanteet

**Jos Claude ei ymmärrä:**
```
Tarkoitan että lisää enemmän tunteita, kuten e005-sisu.txt esimerkissä
```

**Jos tulos ei ole haluttu:**
```
Hyvä yritys, mutta haen enemmän e011-halpa-energia.txt kaltaista konkreettista populismia
```

**Jos Claude tekee liikaa:**
```
Älä muuta faktoja tai argumenttien rakennetta, vain emotionaalista sävyä
```

## Vinkit tehokkaaseen käyttöön

1. **Käytä referenssejä**: `Kirjoita tämä uudestaan e001-vaestonvaihto.txt tyylillä`
2. **Ole iteratiivinen**: Älä yritä saada täydellistä ensimmäisellä kerralla
3. **Dokumentoi oppimasi**: `Luo uusi nyanssi-tiedosto tästä onnistuneesta iteraatiosta`
4. **Testaa variaatioita**: `Luo 5 erilaista versiota eri näkökulmista`
5. **Säilytä hyvät osat**: `Säilytä kappaleet 1 ja 3, mutta kirjoita muut uudestaan`

## Muistilista aloittelijalle

- [ ] Lue ensin README.md ymmärtääksesi järjestelmän
- [ ] Lataa ohjeet muistiin komennolla `lue muistiin`
- [ ] Tutustu tyyliesimerkit-kansioon
- [ ] Kokeile luoda ensimmäinen postaus
- [ ] Harjoittele antamaan palautetta ja iteroimaan
- [ ] Pyydä Claudea analysoimaan mikä toimi hyvin

---

*Muista: Claude oppii jokaisesta iteraatiosta. Mitä tarkempaa palautetta annat, sitä parempia tuloksia saat.*