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
#  <b>Reload von Modulen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Reload von Modulen.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_140_reloading_modules.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Module werden nur einmal geladen und dann im Speicher gehalten
# - Änderungen an der Datei werden nicht automatisch erkannt
# - Das ist beim Entwickeln vom Modulen etwas unpaktisch

# %% tags=["keep"]
# %load_ext autoreload
# %autoreload 0


# %% tags=["keep"]
import my_test_module

# %% tags=["keep"]
my_test_module.my_function()

# %% tags=["keep"]
my_test_module.my_variable

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Was passiert, wenn wir die Datei `my_test_module.py` ändern?

# %%

# %%

# %%

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Automatischer Reload von Modulen mit `importlib.reload`
#
# - Das Modul `importlib` bietet die Funktion `reload`
# - Damit kann ein Modul neu geladen werden

# %% tags=["keep"]
import importlib

# %% tags=["keep"]
import my_test_module

# %% tags=["keep"]
importlib.reload(my_test_module)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Automatischer Reload von Modulen
#
# In IPython (und damit Jupyter Notebooks) ist es möglich das automatische Laden
# von modifizierten Modulen zu aktivieren:

# %% tags=["keep"]
# %load_ext autoreload
# %autoreload 2

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Was passiert jetzt, wenn wir die Datei `my_test_module.py` ändern?

# %%

# %%

# %%

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# In Startup-Skripten kann man syntaktische Warnungen vermeiden, wenn man statt dessen
# schreibt:

# %% tags=["keep"]
try:
    get_ipython().run_line_magic("load_ext", "autoreload")  # noqa
    get_ipython().run_line_magic("autoreload", "2")  # noqa
except NameError:
    pass
