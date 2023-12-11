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
#  <b>Benutzerdefinierte Module</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 Benutzerdefinierte Module.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_120_user_defined_modules.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Benutzerdefinierte Module
#
# Ein benutzerdefiniertes Modul ist eine Datei mit Python-Code.
#
# - Wenn sich ein Python-Modul im Suchpfad befindet, kann es mit `import`
#   geladen werden.
# - Standardmäßig ist das aktuelle Verzeichnis im Suchpfad enthalten.
#  - Jupyter Notebooks lassen sich nicht (ohne zusätzliche Pakete) als Module laden.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import os

# %% [markdown] lang="de"
#
# Aktuelles Verzeichnis:

# %% tags=["keep"]
os.getcwd()

# %% [markdown] lang="de"
#
# Welche Dateien befinden sich im aktuellen Verzeichnis?

# %% tags=["keep"]
for filename in os.listdir(os.getcwd()):
    if filename[-3:] == ".py":
        print(filename)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Anzeigen des Quellcodes von `my_test_module.py`

# %% tags=["keep"]
# # %pycat my_test_module.py

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Laden von Modulen
#
# - Die `import`-Anweisung lädt die zum Modul gehörige Datei
# - Top-Level Code wird ausgeführt
# - Das Modul wird in einem Cache gespeichert

# %% tags=["keep"]
import my_test_module

# %%
my_test_module.add1(2)


# %%
# add1

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Top-Level Code
#
# - Der Top-Level Code wird beim Laden des Moduls ausgeführt
# - In der Regel werden hier Funktionen, Klassen und Variablen definiert
#   - Python definiert einige Variablen automatisch, z.B. `__name__` mit dem
#     Namen des Moduls
# - Der Top-Level Code wird nur einmal ausgeführt
#   - Beim erneuten Import des Moduls verwendet der Interpreter die Version aus dem
#     Cache
# - Die Funktionen, Klassen und Variablen werden in den Namespace des Moduls
#   eingefügt

# %%
__name__

# %%
import my_test_module

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Modul
#
# Definieren Sie ein Modul `workshop_module`, das folgende Funktionen enthält:
#
# - `say_hello()`: Gibt `"Hello"` aus
# - `say_bye()`: Gibt `"Bye"` aus
#
# Importieren Sie das Modul und rufen Sie die Funktionen auf.


# %%
import workshop_module_solution

# %%
workshop_module.say_hello()

# %%
workshop_module.say_bye()
