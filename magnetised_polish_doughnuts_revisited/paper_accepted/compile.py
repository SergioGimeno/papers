import os

os.system("pdflatex paper_accepted.tex")
os.system("bibtex paper_accepted")
os.system("pdflatex paper_accepted.tex")
os.system("pdflatex paper_accepted.tex")