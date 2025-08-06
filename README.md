# AI-pohjainen poliittisen viestinnän suunnittelujärjestelmä

Käytännöllisiä työkaluja tehokkaaseen poliittiseen viestintään suomalaisessa kontekstissa.

## Mikä tämä on?

Tämä on AI-pohjainen **optimointijärjestelmä** poliittiseen viestintään. Sen sijaan että luottaisimme pelkkään vaistoon, järjestelmä optimoi viestejä systemaattisesti kohti määriteltyjä tavoitteita. Kyse on viestinnän muuttamisesta intuitiosta mitattavaksi prosessiksi.

### Tieteellinen perusta

Optimointiprosessi hyödyntää tutkimustietoa usealta alalta, esimerkiksi:
- **Kognitiivinen kielitiede**: Miten kieli muokkaa ajatteluamme
- **Kehystysteoria**: Miten metaforat ja kehykset ohjaavat ymmärrystämme
- **Priming-ilmiö**: Miten toistuvat käsitteet muuttavat maailmankuvaamme
- **Tunnepsykologia**: Miten tunteet vaikuttavat päätöksentekoon

Järjestelmä yhdistää nämä tutkimustulokset AI-optimointiin ja kehittyy jatkuvasti käytön myötä.

### Optimointiprosessi

Järjestelmä toimii näin:

```
1. Ihminen kertoo mitä haluaa saavuttaa
2. AI luo ensimmäisen version viestistä
3. Ihminen lukee viestin
4. Jos ihminen on tyytyväinen → mene kohtaan 8
5. Jos ihminen ei ole tyytyväinen → anna palautetta
6. AI luo uuden version palautteen pohjalta
7. Palaa kohtaan 3
8. Viesti on valmis ja julkaistaan
```

Lyhyesti: Ihminen ja AI työstävät viestiä yhdessä kierros kierrokselta, kunnes lopputulos on tyydyttävä. Jokainen kierros parantaa viestiä edelliseen verrattuna. Ihminen päättää milloin viesti on valmis.



## Miten se toimii?

### 1. Esimerkeistä oppiminen - järjestelmän perusta
**TÄRKEÄÄ**: Järjestelmä tarvitsee ihmisten luomia esimerkkejä toimiakseen hyvin. 

Oppimateriaali löytyy:
- `tyyliesimerkit/` - Toimiviksi todistetut poliittiset viestit
- `resurssit/oppaat/` - Viestintäoppaat ja teoriamateriaalit

Ilman näitä esimerkkejä järjestelmä ei voi oppia:
- Mitkä sanavalinnat toimivat suomalaisessa kontekstissa
- Millainen rytmi ja rakenne vetoaa kohderyhmään
- Mitkä argumentit vakuuttavat oikeasti

**Mitä enemmän laadukkaita esimerkkejä, sitä paremmin järjestelmä toimii.**

Lähdemateriaalin ja käyttäjäpalautteen perusteella Claude luo uusia .md-tiedostoja, jotka toimivat lisäoppaina ja -sääntöinä.

### 2. Seitsemän erilaista tyyliä
Eri tilanteet vaativat erilaista viestintää:
- **Paasaustyyli** - Tunteellinen, käskevä, mobilisoiva
- **Analyyttinen** - Strateginen, kouluttava, legitimoiva
- **Konseptuaalinen** - Esittelee uusia ideoita ja viitekehyksiä
- **Argumentoiva** - Looginen, kumoaa vastapuolen väitteitä
- **Kriittis-poliittinen** - Kritisoi vastustajia, skandaalit
- **Filosofis-uskonnollinen** - Arvot, merkitys, perinteet
- **Populistinen** - Yksinkertaiset ratkaisut, taloudelliset vetoomukset

### 3. Vaiheittainen hiominen
Viestit luodaan vaiheittain:
1. Ensimmäinen versio
2. Palaute ja parannukset
3. Hiottu lopputulos

## Käytännön esimerkki

**Tavoite:** Haluat kritisoida energiapolitiikkaa

**Prosessi:**
1. Valitse tyyli (esim. populistinen)
2. Järjestelmä luo ensimmäisen version
3. Annat palautetta ("lisää konkretiaa")
4. Saat hiotun version

**Tulos:** Viesti, joka puhuttelee kohderyhmääsi tehokkaasti

## Repositorion rakenne

```
postaukset/        # Valmiit viestit aiheittain
tyyliesimerkit/    # Toimiviksi todistetut esimerkit  
resurssit/         # Apumateriaalit (fraasit, narratiivit, kehystys)
  oppaat/          # PDF-oppaat ja teoriamateriaalit
nyanssit/          # Hienovaraisten vivahteiden oppimateriaali
puolueohjelmat/    # Eri puolueiden viralliset ohjelmat
CLAUDE_*.md        # Järjestelmän yksityiskohtaiset ohjeet
```

## Aloittaminen

1. **Määrittele tavoite** - Mitä haluat saavuttaa?
2. **Valitse tyyli** - Mikä sopii tilanteeseen?
3. **Luo ensimmäinen versio** - Järjestelmä auttaa
4. **Hio vaiheittain** - Paranna palautteen perusteella

## Järjestelmän vahvuudet

✅ **Toimii hyvin:**
- Yksittäisten viestien luominen
- Eri tyylien hallinta
- Sanavalintojen optimointi
- Argumenttien rakentaminen

❌ **Rajoitukset:**
- Pitkät kampanjat vaativat ihmisohjausta
- Johdonmukaisuus useiden viestien välillä on haastavaa

## Miksi tämä on tärkeää?

Poliittinen viestintä ei ole enää pelkkää intuitiota. Ymmärtämällä miten kieli vaikuttaa ajatteluun, voimme:
- Luoda tehokkaampia viestejä
- Tavoittaa ihmiset paremmin
- Edistää poliittisia tavoitteita

## Tekninen toteutus

Järjestelmä käyttää Claude AI:ta apuna viestien luomisessa. 

Keskeiset ohjeet:
- **CLAUDE.md** - Järjestelmän yleiskuvaus ja työnkulku
- **CLAUDE_TYYLI.md** - 7 erilaista kirjoitustyyliä
- **CLAUDE_POSTAUS.md** - Yksittäisten postausten kirjoitusopas
- **CLAUDE_TAVOITE.md** - Opas oikean tyylin valintaan
- **CLAUDE_SYNTAKSI.md**, **CLAUDE_RETORIIKKA.md**, **CLAUDE_SANASTO.md** - Hienojakoiset rajoitteet

**Huom:** Järjestelmän käyttö vaatii Claude Coden.

---

*Tämä työkalu yhdistää ihmisen luovuuden ja koneen tehokkuuden luodakseen vaikuttavaa poliittista viestintää.*