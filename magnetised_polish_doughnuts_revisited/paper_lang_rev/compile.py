import os

os.system("pdflatex to_send.tex")
os.system("bibtex to_send")
os.system("pdflatex to_send.tex")
os.system("pdflatex to_send.tex")