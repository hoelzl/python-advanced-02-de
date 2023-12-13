# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# <div style="text-align:center; font-size:200%;">
#  <b>Module und Packages</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Module und Packages.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_110_modules.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  - Der Python Interpreter bietet nur einen kleinen Teil der für die meisten
#    Programme benötigten Funktionalität
#    - Keine Interaktion mit dem Betriebssystem
#    - Kein Netzwerkfunktionalität
#    - Keine GUI
#    - ...
#  - Durch *Module* und *Packages* kann diese Funktionalität bei Bedarf geladen
#    werden.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Module und Pakete
#
# - Ein *Modul* ist eine Datei mit Python-Code
#   - Name des Moduls: Dateiname ohne `.py`-Endung
#   - Enthält Funktionen, Klassen, Variablen, ...
# - Ein *Paket* ist ein Verzeichnis mit Python-Code
#   - Name des Pakets: Name des Verzeichnisses

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Hinweis
#
# - Der Begriff *Paket* oder *Package* wird in Python noch für einen
#   anderen Zweck verwendet, nämlich für *Distributionspakete*.
# - Ein Distributionspaket ist eine Sammlung von Modulen oder Paketen, die
#   zusammen installiert werden können.
# - Wenn wir die Pakete im Sinne dieses Kapitels meinen, können wir auch von
#   *Import-Paketen* sprechen.
# - Das wird aber typischerweise nicht gemacht.
# - Sie müssen aus dem Kontext erkennen, welche Art von Paket gemeint ist.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Module und Pakete:
#
# - Müssen im Suchpfad des Python-Interpreters liegen
# - Sind Namensräume
# - Zugriff auf Elemente mit `.`-Operator

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Importieren eines Moduls/Pakets
#
# - `import`-Anweisung
# - Sowohl für Module als auch Pakete
# - Für eingebaute und benutzerdefinierte Module/Pakete
# - Beispiel: Importieren des `os`-Moduls
#   - Dieses Modul bietet Funktionen für den Zugriff auf das Betriebssystem

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Verwenden der Funktionalität
#
# - Abfragen des aktuellen Verzeichnisses

# %%

# %% [markdown] lang="de"
#
# - Auflisten des aktuellen Verzeichnisses:

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Ausgabe aller Namen im Modul
#
# - `Tab`-Vervollständigung
# - `dir`-Funktion

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  Python bietet viele Standardmodule an, die mit dem Interpreter installiert
#  werden:
#
#  - abc: Abstract base classes
#  - argparse: Kommandozeilenargumente
#  - asyncio: Asynchrone Programmierung
#  - collections: Container-Datentypen
#  - ...
#
#  [Hier](https://docs.python.org/3/py-modindex.html) ist eine vollständigere Liste.

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Interne Darstellung von Code im Python-Interpreter:

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Laden von eingebauten Modulen
#
# Importieren Sie das `math`-Modul
# - Verwenden Sie die `sqrt`-Funktion aus diesem Modul, um die Quadratwurzel
#   von 2 zu berechnen
# - Verwenden Sie die `pi`-Variable aus diesem Modul, um den Umfang eines
#   Kreises mit Radius 1 zu berechnen (Formel: $2 \pi r$)

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Importieren Sie das `random`-Modul
# - Verwenden Sie die `random`-Funktion aus diesem Modul, um eine Zufallszahl
#   zwischen 0 und 1 zu erzeugen
#   - *Hinweis*: Sie können die `random`-Funktion ohne Argument aufrufen
# - Verwenden Sie die `randint`-Funktion aus diesem Modul, um eine Zufallszahl
#   zwischen 1 und 6 zu erzeugen (Würfel)
#   - *Hinweis*: Sie müssen die `randint`-Funktion mit zwei Argumenten aufrufen,
#     dem unteren und dem oberen Wertebereich
#   - Evaluieren Sie die folgende Zelle mehrmals, um zu sehen, dass sich die
#     Zufallszahl ändert
#   - Ist die Zufallszahl inklusive 1 und 6?

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%
