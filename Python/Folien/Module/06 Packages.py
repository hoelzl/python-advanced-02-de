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
#  <b>Packages</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 Packages.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_200_packages.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Pakete sind eine Methode, um verwandte Module zu organisieren

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Beispiel: `html` Paket
#
# - `html` enthält Module, die für die Verarbeitung von HTML Dokumenten benötigt
#   werden
# - `html.entities` enthält eine Liste von HTML Entities
# - `html.parser` enthält einen HTML-Parser
# - `html` selber enthält nur Funktionen `escape()` und `unescape()`

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import html

# %% tags=["keep"]
html.escape("<a href='test'>Test</a>")

# %% tags=["keep"]
html.unescape("&lt;a href=&#x27;test&#x27;&gt;Test&lt;/a&gt;")

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import html.entities

# %% tags=["keep"]
html.entities.entitydefs["Psi"]

# %% tags=["keep"]
html.entities.html5["Psi;"]

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from html.parser import HTMLParser


# %% tags=["keep"]
class PrintingHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag:  ", tag)

    def handle_data(self, data):
        print("Data:     ", data)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
parser = PrintingHTMLParser()

# %% tags=["keep"]
parser.feed('<div class="my-class"><a href="test">Test</a></div>')

# %%
import html.entities
from html.parser import HTMLParser

# %%
html.entities.entitydefs["Psi"]

# %%
HTMLParser()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Namen von Packages
#
# - Packages führen zu hierarchische Namen
# - Namensbestandteile sind durch Punkte getrennt
#   - z.B. `<package>.<sub-package>.<sub-sub-package>.<module>`
# - Namenskonventionen:
#   - Namen sollten mit einem kleinen Buchstaben beginnen
#   - Namen sollten keine Unterstriche enthalten

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Struktur von Packages
#
#  - Hierarchie durch Verzeichnisse und Python Dateien
#  - Typischerweise `__init__.py` Datei in jedem Verzeichnis, aus dem Code importiert
#    werden soll
#  - Die `__init__.py` Datei kann leer sein (und ist oft leer)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from dirtree import dir_tree

# %%
dir_tree("greetings")


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Finden von Packages
#
#  - Python sucht in `sys.path` nach dem Package-Verzeichnis.
#  - Dieser kann durch die Environment-Variable `PYTHONPATH` oder direkt von
#    Python aus beeinflusst werden.
#  - In den meisten Fällen ist es besser, keine komplizierten Operationen an
#    `sys.path` vorzunehmen.

# %% tags=["keep"]
import sys

# %%
sys.path

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Das `import` statement
#
#  `import a.b.c`:
#
#  - `a` und `b` müssen Packages (Verzeichnisse) sein
#  - `c` kann ein Modul oder ein Package sein
#
#  `from a.b.c import d`
#  - `a` und `b` müssen Packages sein
#  - `c` kann ein Modul oder ein Package sein
#  - `d` kann ein Modul, ein Package oder ein Name (d.h. eine Variable, eine Funktion,
#    eine Klasse, usw.) sein

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Referenzen innerhalb eines Packages
#
#  - `from . import a` importiert `a` aus dem aktuellen Package
#  - `from .. import a` importiert `a` aus dem übergeordneten Package
#  - `from .foo import a` importiert `a` aus dem "Geschwistermodul" `foo`

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Beispiel: `greetings` Package

# %% tags=["keep"]
# %pycat greetings/formal.py

# %% tags=["keep"]
# %pycat greetings/informal.py

# %% tags=["keep"]
# %pycat greetings/generic.py

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
import greetings.generic

# %% tags=["keep"]
greetings.generic.say_hello()

# %% tags=["keep"]
greetings.generic.say_hello("John")

# %% tags=["keep"]
greetings.generic.say_hello("John")

# %% tags=["keep"]
# %pycat greetings/intl/generic.py
