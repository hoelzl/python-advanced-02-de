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
#  <b>Importieren von Modulen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Importieren von Modulen.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_130_loading_modules.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `import` Anweisung
# - `from`-`import` Anweisung
# - Umbenennen mit `as`

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Importieren mit `from`-`import`
#
# - Statt das gesamte Modul zu importieren, können wir auch einzelne Funktionen
#   importieren
# - Syntax: `from <modulname> import <funktionsname>`
# - Damit ist nur die importierte Funktion verfügbar
# - Ihr Name kann direkt verwendet werden, ohne den Modulnamen voranzustellen

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# import my_test_module

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wenn wir mehrere Funktionen aus einem Modul importieren, können wir sie
#   mit Kommas trennen

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Umbenennen mit `as`
#
# - Manchmal ist der Name eines Moduls zu lang oder nicht aussagekräftig
# - Dann können wir das Modul mit `as` umbenennen

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wir können auch Funktionen umbenennen

# %%


# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Importieren aller Namen mit `*`
#
# - Wir können alle Namen eines Moduls mit `*` importieren
# - Syntax: `from <modulname> import *`
# - Damit werden (fast) alle im Modul definierten Namen importiert
#   - Ausnahme: Namen, die mit `_` beginnen
# - Der Name des Moduls wird nicht importiert
# - Außer zum interaktiven Experimentieren sollten wir dies vermeiden

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}


# %%


# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Importieren von Modulen
#
# - Importieren Sie das Modul `workshop_module`, das Sie im vorherigen Workshop
#   erstellt haben unter dem Namen `wm`
# - Rufen Sie die Funktionen `say_hello()` und `say_bye()` auf

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Importieren Sie die Funktion `say_hello()` aus dem Modul `workshop_module`.
# - Importieren Sie die Funktion `say_bye()` aus dem Modul `workshop_module` unter
#   dem Namen `goodbye`.
# - Rufen Sie die Funktionen auf.
# - Was passiert, wenn Sie `say_bye()` aufrufen?

# %%

# %%

# %%

# %%

# %%
