# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Module und Packages</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Module und Packages.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_110_modules.py -->

# %% [markdown]
#
#  - Der Python Interpreter bietet nur einen kleinen Teil der für die meisten
#    Programme benötigten Funktionalität
#    - Keine Interaktion mit dem Betriebssystem
#    - Kein Netzwerkfunktionalität
#    - Keine GUI
#    - ...
#  - Durch *Module* und *Packages* kann diese Funktionalität bei Bedarf geladen
#    werden.

# %% [markdown]
#
# ## Module und Pakete
#
# - Ein *Modul* ist eine Datei mit Python-Code
#   - Name des Moduls: Dateiname ohne `.py`-Endung
#   - Enthält Funktionen, Klassen, Variablen, ...
# - Ein *Paket* ist ein Verzeichnis mit Python-Code
#   - Name des Pakets: Name des Verzeichnisses

# %% [markdown]
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

# %% [markdown]
#
# ## Module und Pakete:
#
# - Müssen im Suchpfad des Python-Interpreters liegen
# - Sind Namensräume
# - Zugriff auf Elemente mit `.`-Operator

# %% [markdown]
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

# %% [markdown]
#
# ### Verwenden der Funktionalität
#
# - Abfragen des aktuellen Verzeichnisses

# %%

# %% [markdown]
#
# - Auflisten des aktuellen Verzeichnisses:

# %%

# %% [markdown]
#
# ### Ausgabe aller Namen im Modul
#
# - `Tab`-Vervollständigung
# - `dir`-Funktion

# %%

# %%

# %%

# %%

# %% [markdown]
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

# %% [markdown]
#
# Interne Darstellung von Code im Python-Interpreter:

# %%

# %%

# %% [markdown]
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

# %% [markdown]
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

# %%

# %%

# %%

# %%
