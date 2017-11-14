import os

os.system("pdflatex paper_revised.tex")
os.system("bibtex paper_revised")
os.system("pdflatex paper_revised.tex")
os.system("pdflatex paper_revised.tex")