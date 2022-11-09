from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os
from os import listdir
from os.path import isfile, join

os.chdir(r'YOUR OWN FILEPATH') 
    
source_dir = os.getcwd()

writer = PdfFileWriter()
merger = PdfFileMerger(strict=False)
def merge(path, output_filename):
    merger = PdfFileMerger(strict=False)
    content = merger.addBookmark("contents", 0, parent=None)

    parent = merger.addBookmark("group1", 0, parent=content)
    for pdffile in glob(path + os.sep + '*.pdf'):
        if pdffile[2:] == output_filename:
            continue
        print(f"Appending: '{pdffile}'")
        bookmark = os.path.basename(pdffile[:-4])
    
        merger.addBookmark(bookmark, 0, parent=parent)
        
        merger.append(pdffile)
        
         
       
    for item in os.listdir(source_dir):
        if item.endswith('pdf'):
            merger.append(item, bookmark)
    merger.write(output_filename)
merger.close()

            

if __name__ == "__main__":
    parser = ArgumentParser()
    
    parser.add_argument("-o", "--output",
                        dest="output_filename",
                        default="group1.pdf",
                        help="write merged PDF to FILE",
                        metavar="FILE")
    parser.add_argument("-p", "--path",
                        dest="path",
                        default=".",
                        help="path of source PDF files")
    args = parser.parse_args()
    merge(args.path, args.output_filename)