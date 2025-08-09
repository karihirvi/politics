# Nyanssien opetussysteemi

Tämä järjestelmä opettaa Claudelle tekstin hienovaraisia vivahteita ja "kulmia", jotka tekevät tekstistä inhimillisen ja persoonallisen.

## Miksi tämä systeemi?

Claude pyrkii luonnostaan "siistimään" tekstiä ja poistamaan juuri ne elementit, jotka tekevät siitä aidon tuntuisen:
- Epätasainen rytmi
- Tunnepiikit odottamattomissa kohdissa  
- "Virheelliset" mutta tehokkaat rakenteet
- Persoonalliset kulmat ja ärtymys

## Miten systeemi toimii?

1. **Oppimateriaali**: Jokainen postaus tallennetaan kahtena versiona
   - Claude-generoitu alkuperäinen
   - Ihmisen korjaama versio "kulmilla"
   - Analyysi keskeisistä eroista

2. **Anti-patterns**: Lista vältettävistä generoitu-tekstin tunnusmerkeistä

3. **Opitut periaatteet**: Kootut opit kategorioituna tyyleittäin

## Käyttö käytännössä

### Uuden oppimateriaalin lisääminen

1. Kun postaus on valmis ja korjattu, luo uusi kansio:
   ```
   oppimateriaali/n###-aihe-tyyli/
   ```

2. Lisää tiedostot AINA tässä järjestyksessä:
   - `1-claude-generoitu.md` - Clauden alkuperäinen versio
   - `2-ihmisen-korjaama.md` - Ihmisen korjaama versio kulmilla
   - `3-analyysi.md` - Analyysi muutoksista ja opeista

**TÄRKEÄÄ**: Säilytä aina sama numerointi (1-2-3) ja nimeämiskäytäntö. Tämä johdonmukainen rakenne helpottaa vertailua ja oppimista.

### Oppien hyödyntäminen

Claude tarkistaa automaattisesti:
1. Onko vastaavan tyylin oppimateriaalia?
2. Mitä tyypillisiä korjauksia on tehty?
3. Soveltaa oppeja proaktiivisesti

## Kansiorakenne

```
nyanssit/
├── oppimateriaali/          # Generoitu vs korjattu vertailut
│   └── n001-esimerkki/
│       ├── 1-claude-generoitu.md
│       ├── 2-ihmisen-korjaama.md
│       └── 3-analyysi.md
├── opitut-periaatteet.md    # Kootut opit tyyleittäin
└── anti-patterns.md         # Vältettävät rakenteet
```

## Analyysit postausten toimivuudesta

- **p004-vs-p005-analyysi.md** - Vertailu miksi p004 toimi mutta p005 ei
  - P004: Konkreettinen, tunteellinen, selkeä
  - P005: Teoreettinen, abstrakti, sekava
  - Ydinopetus: Voima tulee konkretiasta ja tunteista, ei käsitteistä

## Tavoite

Opettaa Claudelle että:
- **Epätäydellisyys on ominaisuus**, ei bugi
- **Särmät tekevät tekstistä muistettavan**
- **Inhimillinen teksti ei ole symmetristä**
- **Tunteet näkyvät rakenteessa**, ei vain sanoissa
- **Konkretiaa yli teorian** - aina tunnistettavia esimerkkejä

## Vinkkejä korjaajalle

Kun korjaat Clauden tekstiä oppimateriaaliksi:
1. Älä pelkää rikkoa kielioppisääntöjä
2. Lisää epätasaisuutta rytmiin
3. Tuo mukaan henkilökohtaista äärtymystä/intohimoa
4. Käytä konkreettisia yksityiskohtia
5. Vältä tasapainoista 3-osaista rakennetta