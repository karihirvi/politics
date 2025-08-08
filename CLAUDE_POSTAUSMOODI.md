# CLAUDE_POSTAUSMOODI.md - Interaktiivinen postausten luominen

## Yleiskuvaus

Postausmoodi on interaktiivinen toimintatila, jossa Claude ohjaa käyttäjää postausten luomisessa dialogin kautta. Kaikki päätökset dokumentoidaan automaattisesti, ja prosessi on täysin jäljitettävä.

## Postausmoodin aktivointi

```
Käyttäjä: postausmoodi
Claude: Postausmoodi aktivoitu. Komennot: uusi, käsittele, palaute, sync, status, listaa, poistu
```

Kun postausmoodi on aktivoitu, Claude:
- Pitää muistissa aktiivisen postauksen
- Seuraa iteraation vaihetta
- Dokumentoi kaikki dialogit automaattisesti
- Ohjaa käyttäjää kysymyksillä

## Postausmoodin komennot

### Peruskomennot

| Komento | Kuvaus | Esimerkki |
|---------|---------|-----------|
| `postausmoodi` | Aktivoi postausmoodin | `postausmoodi` |
| `uusi [aihe]` | Aloita uusi postaus | `uusi feminismi-burka` |
| `sync` | Tallenna nykyinen versio | `sync` |
| `käsittele` | Generoi postaus/korjaus | `käsittele` |
| `palaute` | Aloita palautesessio | `palaute` |
| `status` | Näytä nykyinen tila | `status` |
| `listaa` | Listaa kaikki postaukset | `listaa` |
| `poistu` | Poistu postausmoodista | `poistu` |

### Interaktiivisen dialogin komennot

| Komento | Kuvaus | Käyttö |
|---------|---------|---------|
| `dialogi` | Aloita vapaa dialogi | Kun haluat keskustella vapaasti |
| `lopeta` | Lopeta dialogi | Palataksesi perustilaaan |
| `valitse [numero]` | Valitse vaihtoehto | `valitse 3` |
| `lisää` | Pyydä lisää vaihtoehtoja | Kun tarvitset enemmän ideoita |

## A-tiedostojen rakenne (interaktiivisesti luodut)

### Pyynnön rakenne (01-a, 03-a, 05-a...)

```markdown
# Pyyntö: [Otsikko]

## SYNC 3 - 14:35
## Tavoite
[Viimeisin tavoite - tämä käytetään]

## Tyyli
[Valittu tyyli]

## Pituus
[LYHYT/KESKIPITKÄ/PITKÄ]

## Keskeiset kohdat
- [Kohta 1]
- [Kohta 2]

## Retoriset tekniikat
- [Tekniikka 1]
- [Tekniikka 2]

---

## SYNC 2 - 14:28
[Edellinen versio]

---

## SYNC 1 - 14:22
[Ensimmäinen versio]

---

## DIALOGI-HISTORIA
14:20 - Käyttäjä: uusi feminismi-burka
14:20 - Claude: Mikä on postauksen tavoite?
14:21 - Käyttäjä: paljastaa ristiriita
[...jatkuu kronologisesti...]
```

### Palautteen rakenne (02-a, 04-a, 06-a...)

```markdown
# Palaute: [Postauksen nimi]

## SYNC 2 - 15:45
## Mikä toimi hyvin
[Lista hyvistä asioista]

## Mitä voisi parantaa
[Lista parannettavista]

## Konkreettiset muutosehdotukset
[Tarkat ohjeet muutoksiin]

## Sävyn säätö
[x] Sopiva / [ ] Terävämpi / [ ] Pehmeämpi

---

## SYNC 1 - 15:40
[Edellinen versio]

---

## DIALOGI-HISTORIA
[Palautekeskustelu]
```

## Interaktiivisen dialogin kulku

### 1. Uuden postauksen aloittaminen

```
Käyttäjä: uusi kaksinaismoralismi
Claude: Aloitetaan p005-kaksinaismoralismi. Mikä on postauksen päätavoite?
Käyttäjä: paljastaa ristiriita feminismin ja burkan välillä
Claude: Hyvä! Millainen tyyli sopisi - kriittis-poliittinen, analyyttinen, populistinen?
Käyttäjä: kriittinen mutta ei liian hyökkäävä
Claude: Ymmärrän. Kriittis-poliittinen sävy maltillisena. Pituus?
Käyttäjä: keskipitkä
Claude: Selvä, 5-6 kappaletta. Haluatko määritellä keskeiset kohdat vai kehitetäänkö yhdessä?
Käyttäjä: kehitetään
Claude: Ehdotan: 1) #metoo vs burka-ristiriita, 2) kulttuurirelativismi, 3) kaksinaismoralismi. Sopiiko?
Käyttäjä: sync
```

### 2. Sync-toiminto

Kun käyttäjä sanoo `sync`, Claude:
1. Kokoaa dialogista strukturoidun pyynnön/palautteen
2. Lisää sen ylimmäksi SYNC-osioksi a-tiedostoon
3. Säilyttää aiemmat syncit alla
4. Dokumentoi dialogin DIALOGI-HISTORIA -osioon
5. Vahvistaa: "SYNC 3 tallennettu. Jatketaanko kehittämistä vai käsitelläänkö?"

### 3. Palautesession kulku

```
Käyttäjä: palaute
Claude: Aloitetaan palautesessio postaukselle p005-01-b. Mikä toimi hyvin?
Käyttäjä: sävy ja rakenne olivat hyviä
Claude: Hienoa! Entä parannettavaa?
Käyttäjä: tuo laihdutusesimerkki ei toimi
Claude: Ymmärrän. Ehdotan vaihtoehtoja tuohon kohtaan:
1. "Jos taistelemme yhdenvertaisuudesta..."
2. "Jos miesten katse on ongelma..."
3. "Jos puolustamme valinnanvapautta..."
Mikä sopisi parhaiten?
Käyttäjä: valitse 2
Claude: Valittu vaihtoehto 2. Muuta palautetta?
Käyttäjä: ei
Käyttäjä: sync
```

## Status-komennon näkymä

```
POSTAUSMOODI - STATUS
=====================
Aktiivinen: p005-kaksinaismoralismi
Vaihe: Iteraatio 2 (palaute)
Viimeisin: p005-02-a-palaute.md (SYNC 2)

Tyyli: Kriittis-poliittinen (maltillinen)
Pituus: KESKIPITKÄ

Historia:
✓ 01-a: Pyyntö (3 synciä)
✓ 01-b: Postaus generoitu
⏳ 02-a: Palaute (2 synciä)
→ Seuraava: käsittele (generoi 02-b)
```

## Clauden automaattiset toiminnot

### Pyynnön kehittämisessä Claude:
1. Kysyy puuttuvat kentät järjestyksessä
2. Ehdottaa vaihtoehtoja epäselvissä kohdissa
3. Muistuttaa tyylien ominaisuuksista
4. Varmistaa johdonmukaisuuden

### Palautesesiossa Claude:
1. Analysoi postauksen automaattisesti
2. Tunnistaa mahdolliset ongelmat
3. Tarjoaa konkreettisia vaihtoehtoja
4. Dokumentoi päätökset

### Generoinnissa Claude:
1. Lukee AINA ylimmän SYNC-osion
2. Noudattaa kaikkia määriteltyjä parametreja
3. Soveltaa aiempia oppeja samasta postauksesta
4. Luo automaattisesti seuraavan a-pohjan

## Oppiminen ja kehittyminen

Postausmoodi oppii käyttäjän preferensseistä:
- Toistuvat korjaukset tunnistetaan
- Tyylivalinnat muistetaan
- Palautemallit kehittyvät
- Dialogi-historia opettaa

## Virhetilanteet ja palautuminen

### Jos käyttäjä haluaa perua syncin:
```
Käyttäjä: peru sync
Claude: Palaan edelliseen tilaan. SYNC 3 poistettu, SYNC 2 nyt voimassa.
```

### Jos sessio katkeaa:
```
Käyttäjä: postausmoodi
Claude: Postausmoodi aktivoitu. Edellinen aktiivinen: p005-kaksinaismoralismi (02-a).
Käyttäjä: status
Claude: [Näyttää tilanteen]
```

## Hyödyt perinteiseen prosessiin verrattuna

1. **Ei tyhjää paperia** - Claude ohjaa prosessia
2. **Täysi dokumentointi** - Kaikki päätökset tallennetaan
3. **Iteratiivinen kehitys** - Voi tehdä useita syncejä
4. **Oppiva systeemi** - Claude oppii preferensseistä
5. **Nopea palauteprosessi** - Interaktiivinen dialogi
6. **Versionhallinta** - Syncit toimivat versiohistoriana

## Esimerkkejä erityistilanteista

### Vapaa dialogi kesken pyynnön:
```
Käyttäjä: mitä retorisia tekniikoita sopisi kriittiseen tyyliin?
Claude: Kriittis-poliittiseen tyyliin sopivat parhaiten:
- Tu quoque (osoittaa tekopyhyyden)
- Harhautus (laajentaa yksittäisestä systeemiseen)
- Rusinoiden poiminta (vahvimmat esimerkit)
Haluatko lisätä nämä?
Käyttäjä: kyllä
Käyttäjä: sync
```

### Osittainen sync:
```
Käyttäjä: sync vain tavoite ja tyyli
Claude: Tallennan SYNC 2 (osittainen):
- Tavoite: [määritelty]
- Tyyli: [määritelty]
- Muut kentät: [AVOIN]
```

## Muistilista Claudelle

- [ ] Aina lue ylin SYNC käsittele-komennossa
- [ ] Dokumentoi KAIKKI dialogi
- [ ] Tarjoa vaihtoehtoja proaktiivisesti
- [ ] Muista aiemmat syncit samassa sessiossa
- [ ] Tunnista toistuvat korjausmallit
- [ ] Pidä a-tiedostot käänteisessä kronologiassa
- [ ] Generoi strukturoitu pyyntö/palaute vapaasta dialogista