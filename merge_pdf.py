#plotting
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import plotly.express as px
plt.style.use("seaborn")
import seaborn as sns
import numpy as np
from PyPDF2 import PdfMerger
from glob import glob

def merge_pdf(in_pdf ,  out_pdf):
    merger = PdfMerger()

    for pdf_file in in_pdf:
        merger.append(pdf_file)

    merger.write(out_pdf)
    print(f'created merged pdf file {out_pdf}')
    merger.close()


merge_pdf(glob("*pdf") , 'sujeet_lta_merge.pdf')
