import tabula
pdf_path = "Bangalore Mobility Indicators_(22-12-2011).pdf"
dfs = tabula.read_pdf(pdf_path, pages=[15,16,17,21,63,67,68], multiple_tables=True, stream=True)
