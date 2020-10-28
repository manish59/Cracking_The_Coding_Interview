import os

path=r"C:\Users\mbobbili\Desktop"
def list_all_pdf_files(path):
    try:
        total_files=os.listdir(path)
        folders=[i for i in total_files if i.find(".")<0]
        pdf_files=[i for i in total_files if i[-4:]==".pdf"]
        print(pdf_files)
        for i in folders:
            list_all_pdf_files(os.path.join(path,i))
    except:
        pass
list_all_pdf_files(path)