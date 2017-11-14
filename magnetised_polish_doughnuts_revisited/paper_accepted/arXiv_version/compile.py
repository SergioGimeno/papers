import os

os.system("pdflatex paper_final.tex")
os.system("bibtex paper_final")
os.system("pdflatex paper_final.tex")
os.system("pdflatex paper_final.tex")