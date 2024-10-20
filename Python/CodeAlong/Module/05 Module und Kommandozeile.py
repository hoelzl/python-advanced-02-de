# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Module und Kommandozeile</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Module und Kommandozeile.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_150_modules_and_cli.py -->

# %% [markdown]
#
# - Wir können Python-Module auch direkt von der Kommandozeile ausführen
# - Dazu verwenden wir das Kommando `python -m <modulname>`
# - Im Gegensatz zu `python <modulname>.py` wird das Modul auch gefunden, wenn
#   es nicht im aktuellen Verzeichnis liegt

# %%

# %%

# %%

# %% [markdown]
#
# - Dabei ist es zweckmäßig, wenn das Modul eine `main()` Funktion enthält, die
#   ausgeführt wird
# - Das sollte aber nur passieren, wenn das Modul direkt ausgeführt wird
# - Dazu können wir die Variable `__name__` verwenden:
#   - Der Wert von `__name__` ist der String `"__main__"`, wenn das Modul direkt
#     ausgeführt wird (also nicht importiert wird)
#   - `__name__` ist der Modulname, wenn das Modul importiert wird

# %% [markdown]
#
# - Um die `main()` Funktion nur auszuführen, wenn das Modul direkt ausgeführt
#   wird, können wir folgenden Code verwenden:

# %%

# %%


# %%

# %%

# %% [markdown]
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


# %%

# %%
