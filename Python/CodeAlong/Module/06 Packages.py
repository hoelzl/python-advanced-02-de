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
# Packages (Pakete) erlauben es uns, verwandte Module zu organisieren

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


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Struktur von Packages
#
# - Packages sind Ordner im Dateisystem
# - Sie können Module und andere Packages enthalten
# - Um zu kennzeichnen, dass ein Ordner ein Package ist, enthält er typischerweise eine
#   `__init__.py` Datei
# - Die `__init__.py` Datei kann leer sein (und ist oft leer)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from dirtree import dir_tree

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Struktur des `greetings` Packages
#
# - Dateien für Module:
#   - [`formal.py`](greetings/formal.py)
#   - [`informal.py`](greetings/informal.py)
#   - [`generic.py`](greetings/generic.py)
# - Ordner für Sub-Packages:
#   - `intl` mit Datei [`generic.py`](greetings/intl/generic.py)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Namen von Packages
#
# - Namenskomponenten werden durch Punkte getrennt
#   - z.B. `<package>.<sub-package>.<sub-sub-package>.<module>`
# - Namenskonventionen:
#   - Namen sollten mit einem Kleinbuchstaben beginnen
#   - Namen sollten keine Unterstriche enthalten

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Namen des `greetings` Packages
#
# - Dateien für Module:
#   - [`greetings.formal`](greetings/formal.py)
#   - [`greetings.generic`](greetings/generic.py)
#   - [`greetings.informal`](greetings/informal.py)
# - Ordner für Sub-Packages:
#   - `intl` mit Modul [`greetings.intl.generic`](greetings/intl/generic.py)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

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

# %% tags=["keep"]
# %pycat greetings/generic.py

# %% tags=["keep"]
# %pycat greetings/intl/generic.py

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Persönlicher Finanz-Tracker
#
# ### Übersicht
#
# In diesem Workshop werden Sie einen einfachen persönlichen Finanz-Tracker
# entwickeln. Dieses Programm hilft den Benutzern, ihre persönlichen Finanzen,
# einschließlich Ausgaben und Einkommen, zu verfolgen und zu analysieren. Ihre Aufgabe
# wird es sein, diese Anwendung in Pakete und Module zu strukturieren, um eine
# ordnungsgemäße Funktionalität zu gewährleisten und Ihr Verständnis von
# Python-Paketverwaltung und Modulreferenzen zu demonstrieren.


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Problem- und Funktionsdomäne
#
# Der persönliche Finanz-Tracker besteht aus zwei Hauptkomponenten: Ausgabenverfolgung
# und Einkommensverfolgung. Zusätzlich wird er Funktionen für das Generieren von
# Finanzberichten und das Erstellen von Budgets haben.
#
# **Schlüsselfunktionalitäten:**
#
# 1. **Ausgaben verfolgen:** Einzelne Ausgaben aufzeichnen und kategorisieren.
# 2. **Einkommen verfolgen:** Verschiedene Einkommensquellen aufzeichnen und
#    kategorisieren.
# 3. **Berichte generieren:** Zusammenfassungen von Finanzaktivitäten erstellen.
# 4. **Budgetanalyse:** Ausgaben und Einkommen vergleichen, um Budgets zu setzen und
#    zu analysieren.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Paket- und Modulstruktur
#
# Ihr Programm wird in zwei Hauptpakete unterteilt: `finance` und `analytics`. Jedes
# Paket enthält spezifische Module, die mit ihren Funktionalitäten verbunden sind.
#
# 1. **Paket: `finance`**
#    - **Modul: `expenses.py`**
#      - Funktionen zum Hinzufügen, Kategorisieren und Zusammenfassen von Ausgaben.
#    - **Modul: `income.py`**
#      - Funktionen zum Aufzeichnen und Kategorisieren von Einkommensquellen.
#
# 2. **Paket: `analytics`** (ein Unter-Paket innerhalb von `finance`)
#    - **Modul: `reports.py`**
#      - Funktionen zum Erstellen von Finanzberichten basierend auf Einkommen und
#        Ausgaben.
#    - **Modul: `budget.py`**
#      - Funktionen zum Erstellen und Analysieren von Budgets.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Spezifikationen von Funktionen und Klassen
#
# - `expenses.py`:
#   - `add_expense()`
#   - `categorize_expense()`
#   - `summarize_expenses()`
#
# - `income.py`:
#   - `record_income()`
#   - `categorize_income()`
#
# - `reports.py`:
#   - `generate_financial_report()`
#
# - `budget.py`:
#   - `create_budget()`
#   - `compare_budget_to_actual()`

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Paketreferenzen und Abhängigkeiten
#
# Realisieren Sie die folgenden Abhängigkeiten zwischen den Paketen und Modulen:
#
# - `budget.py` sollte sowohl auf `expenses.py` als auch auf `income.py` zugreifen
#   können, um alle Daten für die Budgetanalyse zu erhalten.
# - `reports.py` sollte auf `budget.py` zugreifen können, um Budgetanalysen in
#   Finanzberichte aufzunehmen.
# - `reports.py` sollte auf die Funktion `summarize_expenses()` in `expenses.py`
#   zugreifen können, um Ausgaben in Finanzberichten zu berücksichtigen.
#
# *Hinweis:* Die Abhängigkeiten zwischen den Modulen dienen dazu, die verschiedenen
# Import-Möglichkeiten zu demonstrieren. Sie sind nicht unbedingt das beste Beispiel för
# die Organisation von Funktionalität


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Programm
#
# Legen Sie eine Datei `main.py` an, die folgendes Budget erzeugt:
#
# ```python
# incomes = [
#     record_income(5000, "Salary"),
#     record_income(200, "Interest"),
# ]
# expenses = [
#     add_expense(100, "Groceries"),
#     add_expense(150, "Utilities"),
#     add_expense(200, "Rent"),
# ]
# ```
#
# Verwenden Sie die Funktionen `generate_financial_report()` und
# `compare_budget_to_actual()` um einen Finanzbericht zu erstellen und das Budget zu
# analysieren.
#
# Stellen Sie sicher, dass die Funktionalität nur ausgeführt wird, wenn `main.py` direkt
# ausgeführt wird (d.h. nicht, wenn das Modul `main` importiert wird).

# %% tags=["keep"]
# !python -m finance.main

# %% tags=["keep"]
# import finance.main

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Workshop-Ziel
#
# Ihre Aufgabe ist es, diese Module und Funktionen zu implementieren und dabei die
# angegebene Struktur einzuhalten. Dabei sollten Sie sicherstellen, dass:
#
# - Jedes Modul die angegebenen Funktionen oder Klassen enthält.
# - Richtige Verweise zwischen den Modulen verwendet werden, um auf notwendige
#   Funktionen anderer Module zuzugreifen.
# - Zyklische Abhängigkeiten vermieden werden, um eine klare und effiziente
#   Code-Struktur zu erhalten.
#
# **Hinweis:** Da der Fokus dieses Workshops auf der Strukturierung von Paketen und
# Modulen liegt, müssen Sie die Funktionen nicht vollständig implementieren. Sie
# können stattdessen Platzhalter verwenden, um die Funktionalität zu simulieren.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Erwartetes Ergebnis
#
# Am Ende dieses Workshops werden Sie einen grundlegenden, aber funktionalen
# Persönlichen Finanz-Tracker haben. Dieses Projekt wird Ihre Fähigkeit demonstrieren,
# eine Python-Anwendung in logische Pakete und Module zu strukturieren,
# Inter-Modul-Abhängigkeiten zu verwalten und Kernfunktionalitäten zu implementieren.
