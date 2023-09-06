# Teksten aanpassen

De volgende sectie geeft meer informatie over hoe je de bestanden in `/content` kunt bewerken om de teksten op de website aan te passen. Voor informatie over hoe je de bestanden kunt bewerken en committen, zie de sectie "Bijdragen aan de website".

1. Zoek het `.json` bestand dat de tekst bevat die je wilt bewerken. Elke pagina op de website komt overeen met een gelijknamig `.json` bestand (bv `musilene.be/concerten` komt overeen met `concerten.json`). Ook is er een `common.json` bestand dat teksten bevat die op alle pagina's gebruikt worden.
2. Zoek naar de tekst die je wilt aanpassen. De tekst is opgeslagen als een waarde van een sleutel in het `.json` bestand. De sleutel is meestal een korte beschrijving van de tekst die het bevat (bv `concerten` of `titel`). De waarde is de tekst die op de website wordt weergegeven. De sleuten en waarde zijn steeds gescheiden door een dubbele punt (`:`). Zie het voorbeeld hieronder.
   ```json
   {
     "sleutel": {
       "sub-sleutel": "waarde"
     }
   }
   ```
   Pas enkel de waarde aan en verander de sleutel niet. Indien je dit wel doet, zal de website de tekst niet meer kunnen vinden en zal de standaardtekst worden weergegeven. Voor meer informatie over de structuur van de `.json` bestanden, zie de sectie ["Simpele teksten aanpassen"](#simpele-teksten-aanpassen) en ["Lijsten aanpassen"](#lijsten-aanpassen).
3. Nadat je de tekst hebt aangepast, sla je het bestand op en commit je de wijzigingen. Zie de sectie "Bijdragen aan de website" voor meer informatie over hoe je de wijzigingen kunt committen.

## Simpele teksten aanpassen

De meeste van de `.json` bestanden hebben een structuur als volgt:

```json
{
  "sleutel": {
    "sub-sleutel": "waarde"
  }
}
```

Hierbij mag je enkel de **waardes aanpassen**. Als je de sleutels aanpast kan het dat de website kapot gaat (geen zorgen, je kan altijd de aanpassingen ongedaan maken).

> Note: zorg er steeds voor dat alle speciale tekens zoals `{ } [ ] : ",` enz. correct blijven staan. Als je niet zeker bent of je de tekst correct hebt aangepast, kan je altijd de aanpassingen ongedaan maken en opnieuw proberen. Kijk vooral uit voor kommas, deze moeten steeds staan op het einde van een nieuwe lijn behalve op de laatste lijn van een _blok_ of in het begin van een blok.

```json
{ <- geen komma want dit is het begin van het blok
  "sleutel": { <- geen komma want dit is het begin van een blok
    "sub-sleutel": "waarde", <- hier staat een komma
    "sub-sleutel-2": "waarde 2" <- geen komma want dit is de laatste lijn van deze blok
  }, <- een komma
  "andere sleutel": [ <- geen komma want dit is het begin van een blok
    { <- geen komma want dit is het begin van een blok
        "sleutel": "waarde" <- geen komma want dit is de laatste lijn van deze blok
    } <- geen komma want dit is de laatste lijn van deze blok
} <- geen komma want dit is de laatste lijn van deze blok
```

## Lijsten aanpassen

In sommige van de `.json` bestanden zie je de volgende structuur

```json
{
  "sleutel": [
    {
      "sub_sleutel": "waarde 1",
      "sub_sleutel_2": "waarde 2"
    },
    {
      "sub_sleutel": "waarde 3",
      "sub_sleutel_2": "waarde 4"
    }
  ]
}
```

Dit zijn **lijsten**. Deze lijsten worden op de webiste ook getoond als een lijst van items die er elk ongeveer hetzelfde uitzien (bv. de agenda op [musilene.be/concerten](musilene.be/concerten)). Hierbij mag je vrij items toevoegen of verwijderen maar pas er wel op dat de structuur van elk item identiek is aan hoe die nu gedefinieerd is. Het voorbeeld kan je dus bijvoorbeeld aanpassen naar

```json
{
  "sleutel": [
    {
      "sub_sleutel": "waarde 1",
      "sub_sleutel_2": "waarde 2"
    }
  ]
}
```

of

```json
{
  "sleutel": [
    {
      "sub_sleutel": "waarde 1",
      "sub_sleutel_2": "waarde 2"
    },
    {
      "sub_sleutel": "waarde 3",
      "sub_sleutel_2": "waarde 4"
    },
    {
      "sub_sleutel": "waarde 5",
      "sub_sleutel_2": "waarde 6"
    }
  ]
}
```

maar **niet** naar

```json
{
  "sleutel": [
    {
      "sub_sleutel": "waarde 1",
      "sub_sleutel_2": "waarde 2"
    },
    {
      "sub_sleutel_2": "waarde 4" <- `sub_sleutel` ontbreekt
    },
    {
      "sub_sleutel": "waarde 5",
      "andere_sleutel": "waarde 6" <- dit zou `sub_sleutel_2` moeten zijn
    }
  ]
}
```

# Bijdragen aan de website

## Deel 1: Voorbereiding

1. Installeer [Visual Studio Code](https://code.visualstudio.com/), een populaire en gebruiksvriendelijke teksteditor. Je kunt het downloaden van hun officiële website en de installatie-instructies volgen.

## Deel 2: Verbinding maken met de externe GitHub-repository

1. Open Visual Studio Code.

2. Klik in de zijbalk op het pictogram met de "source control" (versiebeheer) omgeving.

3. Klik op het pictogram met de tekst "Clone Repository" en selecteer "GitHub".

4. Log in op je GitHub-account als daarom wordt gevraagd.

5. Selecteer de `musilene` repository uit de lijst met beschikbare repositories, of gebruik de URL [https://github.com/Musilene/musilene](https://github.com/Musilene/musilene).

6. Kies de lokale map op je computer waar je de repository wilt clonen en klik op "Select as Repository Destination" (of gelijkaardig).

## Deel 3: Aanpassen van de teksten en committen

1. In de zijbalk van Visual Studio Code zie je de gekloonde repository. Klik op het pijlpictogram naast de repositorynaam om de bestanden en mappen weer te geven.

2. Navigeer naar de map genaamd `/content` en open het gewenste tekstbestand dat je wilt bewerken.

3. Bewerk de tekst in het geopende bestand naar wens. Zie sectie ["Teksten aanpassen"](#teksten-aanpassen) voor meer informatie over het bewerken van de teksten.

4. Ga terug naar het "source control" (versiebeheer) paneel in de zijbalk van Visual Studio Code. Je zou de wijzigingen in het gewijzigde tekstbestand moeten zien.

5. Klik op het pluspictogram naast de bestanden die je hebt aangepast om ze klaar te maken voor gecommit te worden.

6. Voer een beschrijving in van de wijzigingen in het tekstvak "Message" boven aan het "source control" paneel.

7. Klik op de knop met `Commit` (of iets gelijkaardig) om de wijzigingen te committen.

## Deel 4: Pushen van de wijzigingen naar GitHub

1. Nadat je hebt gecommit, klik je nogmaals op de blauwe knop om de wijzigingen te pushen.

2. Log in op je GitHub-account als daarom wordt gevraagd.

3. Wacht tot de push-operatie is voltooid. Je kunt de voortgang volgen in het "output" paneel onderaan Visual Studio Code.

Na het volgen van deze stappen worden de aangepaste teksten in de gekloonde repository gecommit en gepusht naar de externe GitHub-repository. Het kan enkele minuten duren voordat de wijzigingen zichtbaar zijn op de website. Je kan de _deploy_ volgen op het tabblad [Actions](https://github.com/Musilene/musilene/actions) op Github.
