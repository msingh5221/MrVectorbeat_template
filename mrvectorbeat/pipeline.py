# mrvectorbeat/pipeline.py
#
# SABLON. Ovde su samo IMENA funkcija i opis sta svaka treba da radi -
# tela su prazna (pass), pa se svaka funkcija moze pozvati bez greske,
# ali jos nista ne radi.
#
# VAZNO: ovo NISU fiksne funkcije. Imena, parametri i ono sto funkcija
# vraca su samo PREDLOG - slobodno ih menjajte, dodajte nove ili
# izbacite one koje vam ne trebaju, kako vam odgovara.
#
# Ideja ovog fajla: za svaki model postoji par funkcija
#   napravi_X() - gradi model JEDNOM i cuva ga u artifacts/
#                 (poziva je scripts/pripremi.py)
#   ucitaj_X()  - cita vec sacuvan model iz artifacts/
#                 (poziva je app.py)
# Tako aplikacija nikad ne gradi nista iznova pri svakom kliku.

# OVDE IDU importi vasih modula, npr.:
#   from mrvectorbeat import tekst, trie, indeks, ...


# Kolone koje zadrzavamo u katalogu. Sve ostalo iz CSV-a nam ne treba.
# Kartice u prikaz.py ocekuju bar: track_name, track_artist, godina,
# playlist_genre, tempo.
KOLONE = [
    "track_id",           # jedinstveni ID pesme, kljuc za sve kasnije
    "track_name",
    "track_artist",
    "lyrics",
    "track_album_name",
    "godina",             # ovu kolonu pravimo mi
    "playlist_genre",
    "playlist_subgenre",
    "track_popularity",
    "duration_ms",
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo",
    "porodica",           # ovu kolonu pravimo mi - isti kljuc za razlicite
                          # verzije iste pesme
]


def napravi_katalog():
    """Cita data/spotify_songs.csv, cisti ga i snima katalog u artifacts/.
    Vraca: tabelu kataloga."""
    pass


def ucitaj_katalog():
    """Cita gotov katalog iz artifacts/."""
    pass


def napravi_tokene():
    """Obradjuje stihove svake pesme i snima tokene u artifacts/."""
    pass


def ucitaj_tokene():
    """Cita gotove tokene iz artifacts/."""
    pass


def napravi_trie():
    """Gradi trie nad imenima pesama i izvodjaca i snima ga u artifacts/."""
    pass


def ucitaj_trie():
    """Cita gotov trie iz artifacts/."""
    pass


def ucitaj_porodice():
    """Vraca recnik track_id -> porodica."""
    pass


def ucitaj_popularnost():
    """Vraca recnik ime (pesma ili izvodjac) -> popularnost."""
    pass


def napravi_kgram():
    """Gradi k-gramski indeks nad imenima pesama i izvodjaca i snima ga u
    artifacts/."""
    pass


def ucitaj_kgram():
    """Cita gotov k-gramski indeks iz artifacts/."""
    pass


def napravi_indeks():
    """Gradi invertovani indeks iz tokena i snima ga u artifacts/."""
    pass


def ucitaj_indeks():
    """Cita gotov indeks iz artifacts/."""
    pass


def napravi_tfidf():
    """Gradi TF-IDF model i snima ga u artifacts/."""
    pass


def ucitaj_tfidf():
    """Cita gotov TF-IDF model iz artifacts/."""
    pass


def napravi_bm25():
    """Gradi BM25 model i snima ga u artifacts/."""
    pass


def ucitaj_bm25():
    """Cita gotov BM25 model iz artifacts/."""
    pass


def ucitaj_qrels(skup=None):
    """Cita test upite iz data/qrels.csv.

    skup - "poznata_stavka", "tema", ili None za oba.
    Vraca: tabelu (skup, upit, track_id, ocena, tipfeler)."""
    pass


def napravi_evaluaciju():
    """Racuna metrike za TF-IDF i BM25 nad qrels i snima tabelu u
    artifacts/."""
    pass


def ucitaj_evaluaciju():
    """Cita gotovu tabelu metrika iz artifacts/."""
    pass


def napravi_jezicki(mu=1000.0):
    """Gradi jezicki model i snima ga u artifacts/."""
    pass


def ucitaj_jezicki():
    """Cita gotov jezicki model iz artifacts/."""
    pass


def ucitaj_graf():
    """Cita graf izvodjaca koji je napravio vas crawler."""
    pass


def napravi_rangove():
    """Racuna PageRank nad grafom izvodjaca i snima rang-listu u
    artifacts/."""
    pass


def ucitaj_rangove():
    """Cita gotovu rang-listu iz artifacts/."""
    pass


def napravi_kdrvo():
    """Gradi k-d stablo nad audio-osobinama kataloga i snima ga u
    artifacts/."""
    pass


def ucitaj_kdrvo():
    """Cita gotovo k-d stablo iz artifacts/."""
    pass


def napravi_semantiku():
    """Gradi semanticki model nad katalogom i snima ga u artifacts/."""
    pass


def ucitaj_semantiku():
    """Cita gotov semanticki model iz artifacts/."""
    pass


def napravi_rag_korpus():
    """Gradi korpus za AI DJ Bot-a i snima ga u artifacts/."""
    pass


def ucitaj_rag_korpus():
    """Cita gotov RAG korpus iz artifacts/."""
    pass


def napravi_hibrid_evaluaciju():
    """Racuna metrike hibridne pretrage nad qrels i snima tabelu u
    artifacts/."""
    pass


def ucitaj_hibrid_evaluaciju():
    """Cita gotovu tabelu metrika hibridne pretrage iz artifacts/."""
    pass


def napravi_autoplay():
    """Gradi Autoplay nad data/music4all_istorija.csv i snima ga u
    artifacts/."""
    pass


def ucitaj_autoplay():
    """Cita gotov Autoplay iz artifacts/."""
    pass
