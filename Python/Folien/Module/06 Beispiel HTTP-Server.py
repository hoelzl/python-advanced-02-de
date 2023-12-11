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
#  <b>Beispiel: HTTP-Server</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 Beispiel HTTP-Server.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_160_example_http_server.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Der Python Interpreter hat keinen eingebauten HTTP Server. Mittels der
# Standardbibliothek ist es aber nicht schwer einen zu schreiben.

# %%
from http.server import HTTPServer, SimpleHTTPRequestHandler


# %%
def run_http_server():
    httpd = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()


# %%
run_http_server()

# %%
from python_server import run_http_server

# %%
run_http_server()
