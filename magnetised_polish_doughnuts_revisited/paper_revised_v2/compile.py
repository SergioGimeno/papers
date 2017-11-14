import os

os.system("pdflatex paper_revised_v2.tex")
os.system("bibtex paper_revised_v2")
os.system("pdflatex paper_revised_v2.tex")
os.system("pdflatex paper_revised_v2.tex")