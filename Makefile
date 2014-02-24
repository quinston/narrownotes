folder = notes

$(folder): main.tex $(folder)-tex
	python dynamic.py $(folder)-tex > dynamic.tex
	xelatex main.tex

