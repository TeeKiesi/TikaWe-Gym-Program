# TikaWe-Gym-Program

Sovelluksen testaaminen (hävyttömästi ai:lta lainattu)

  Asenna [uv](https://docs.astral.sh/uv/getting-started/installation/) [OhTu:n uv asennusohje](https://studies.cs.helsinki.fi/ohtu/uv#asennus) ja python 3.14 tai uudempi
  
  Käynnistä ohjelma juurihakemistosta
  
  ```
  $ uv sync
  $ uv run flask --app sovellus.app run
  $ sqlite3 database.db < schema.sql
  ```

  Avaa selaimessa `http://127.0.0.1:5000`.

  Sovelluksessa käyttäjät pystyvät jakamaan saliohjelmia. Ohjelmassa on siihen tarvittavat päivät sekä päivien liikkeet.
  
  Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
  
  Käyttäjä pystyy lisäämään ohjelmia ja muokkaamaan ja poistamaan niitä.
  
  Käyttäjä näkee sovellukseen lisätyt ohjelmat.
  
  Käyttäjä pystyy etsimään ohjelmia hakusanalla.
  
  Käyttäjäsivu näyttää, montako ohjelmaa käyttäjä on lisännyt ja listan käyttäjän lisäämistä ohjelmista.
  
  Käyttäjä pystyy valitsemaan esimerkiksi seuraavia luokitteluja:
  
      Ohjelman volyymi: alhainen, keski tai korkea
      
      Ohjelmaan tarvittavat päivät. yhdestä seitsemään
      
      Ohjelmaan tarvittavat välineet: kehopaino, painot tai salilaitteet
      
  Käyttäjä pystyy antamaan ohjelmalle kommentin ja arvostelun. Ohjelmasta näytetään kommentit ja keskimääräinen arvostelu.

Tässä pääasiallinen tietokohde on saliohjelma ja toissijainen tietokohde on kommentti ohjelmaan.


Linkkejä 

https://google.github.io/styleguide/htmlcssguide.html