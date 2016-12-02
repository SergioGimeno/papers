import os

os.system("pdflatex paper.tex")
os.system("bibtex paper")
os.system("pdflatex paper.tex")
os.system("pdflatex paper.tex")