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
#  <b>Module und Kommandozeile</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Module und Kommandozeile.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_150_modules_and_cli.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wir können Python-Module auch direkt von der Kommandozeile ausführen
# - Dazu verwenden wir das Kommando `python -m <modulname>`
# - Im Gegensatz zu `python <modulname>.py` wird das Modul auch gefunden, wenn
#   es nicht im aktuellen Verzeichnis liegt

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Dabei ist es zweckmäßig, wenn das Modul eine `main()` Funktion enthält, die
#   ausgeführt wird
# - Das sollte aber nur passieren, wenn das Modul direkt ausgeführt wird
# - Dazu können wir die Variable `__name__` verwenden:
#   - Der Wert von `__name__` ist der String `"__main__"`, wenn das Modul direkt
#     ausgeführt wird (also nicht importiert wird)
#   - `__name__` ist der Modulname, wenn das Modul importiert wird

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Um die `main()` Funktion nur auszuführen, wenn das Modul direkt ausgeführt
#   wird, können wir folgenden Code verwenden:

# %%

# %%


# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Modul und Kommandozeile
#
# - Schreiben Sie ein Modul `cli_module`, das eine Funktion `main()` enthält
# - Die Funktion `main()` soll `CLI Module is starting...` ausgeben
# - Das Modul soll direkt von der Kommandozeile ausführbar sein und dann die
#   Funktion `main()` ausführen
# - Die Funktion `main()` soll **nur** ausgeführt werden, wenn das Modul direkt
#   ausgeführt wird
# - Wenn das Modul importiert wird, soll die Funktion `main()` **nicht**
#   ausgeführt werden


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
