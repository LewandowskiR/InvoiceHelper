from fpdf import FPDF


# =============================================================================
# def BasicInvoiceGenerate():
#     numer_faktury = 'Sprzedawca1'
#     nip_sprzedawcy = 'kupujacy1'
#     nip_nabywcy = '12345678'
#     
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font('Times', 'B', 16)
#     pdf.cell(40, 10, numer_faktury)
#     pdf.cell(0, 10, nip_sprzedawcy)
#     pdf.cell(0, 10, nip_nabywcy)
#     return pdf.output('website/static/tuto1.pdf', 'F')
# =============================================================================
     
    

def BasicInvoiceGenerate(formdata):
 
    pdf = FPDF()
    pdf.set_fill_color(228,g=231,b=231)
    
    page_width = pdf.w - 2*pdf.l_margin
    column_ratio = 0.4
    space_ratio = 0.15
    
    pdf.add_page()
    
    pdf.set_x(page_width*0.6)
    pdf.set_font('Times', '', 12)
    pdf.cell(page_width*column_ratio, 5, 'Data Wystawienia', border='T', align='C', fill=1, ln=2)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(page_width*column_ratio, 5, str(formdata.get("data_wystawienia")), align='C', ln=2)
    
    
    pdf.set_font('Times', '', 12)
    pdf.cell(page_width*column_ratio, 5, 'Data Sprzedazy', border='T', align='C', fill=1, ln=2)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(page_width*column_ratio, 5, str(formdata.get("data_sprzedazy")), align='C', ln=1)
    pdf.cell(page_width, 20,'',ln=1)
    
    pdf.cell(page_width*column_ratio, 5, 'Sprzedawca', border='T', align='C', fill=1, ln=0)
    pdf.cell(page_width*space_ratio, 5, '')
    pdf.cell(page_width*column_ratio, 5, 'Nabywca', border='T', align='C', fill=1, ln=1)
    
    pdf.set_font('Times', '', 12)
    pdf.cell(page_width*column_ratio, 5, str(formdata.get("sprzedawca")), align='L', ln=0)
    pdf.cell(page_width*space_ratio, 5, '')
    pdf.cell(page_width*column_ratio, 5, str(formdata.get("nabywca")), align='L', ln=1)
    
    pdf.cell(page_width*column_ratio, 5, str(formdata.get("nip_sprzedawcy")), align='L', ln=0)
    pdf.cell(page_width*space_ratio, 5, '')
    pdf.cell(page_width*column_ratio, 5, str(formdata.get("nip_nabywcy")), align='L', ln=1)
    
    pdf.cell(page_width*column_ratio, 5, str(formdata.get("ulica_sprzedawcy")), align='L', ln=0)
    pdf.cell(page_width*space_ratio, 5, '')
    pdf.cell(page_width*column_ratio, 5, str(formdata.get("ulica_nabywcy")), align='L', ln=1)
    
    pdf.cell(page_width*column_ratio, 5, f'{str(formdata.get("miejscowosc_sprzedawcy"))} {str(formdata.get("kod_sprzedawcy"))}', align='L', ln=0)
    pdf.cell(page_width*space_ratio, 5, '')
    pdf.cell(page_width*column_ratio, 5, f'{str(formdata.get("miejscowosc_nabywcy"))} {str(formdata.get("kod_nabywcy"))}', align='L', ln=1)
    
    pdf.cell(page_width, 20,'',ln=1)
    pdf.set_x(page_width*0.45)
    pdf.set_font('Times', 'B', 18)
    pdf.cell(page_width*column_ratio, 5, str(formdata.get("numer_faktury")), align='L', ln=1)
    
    pdf.cell(page_width, 20,'',ln=1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(page_width*0.1, 5, 'Lp.', border='LTR', align='C', fill=1, ln=0)
    pdf.cell(page_width*0.4, 5, 'Nazwa towaru lub uslugi', border='LTR', align='C', fill=1, ln=0)
    pdf.cell(page_width*0.1, 5, 'Jm.', border='LTR', align='C', fill=1, ln=0)
    pdf.cell(page_width*0.1, 5, 'Ilosc', border='LTR', align='C', fill=1, ln=0)
    pdf.cell(page_width*0.1, 5, 'Cena', border='LTR', align='C', fill=1, ln=0)
    pdf.cell(page_width*0.2, 5, 'Wartosc', border='LTR', align='C', fill=1, ln=1)
    
    pdf.set_font('Times', '', 12)
    pdf.cell(page_width*0.1, 5, '1', border='LBR', align='C', fill=0, ln=0)
    pdf.cell(page_width*0.4, 5, str(formdata.get("nazwa_uslugi")), border='LBR', align='L', fill=0, ln=0)
    pdf.cell(page_width*0.1, 5, str(formdata.get("jednostka")), border='LBR', align='C', fill=0, ln=0)
    pdf.cell(page_width*0.1, 5, str(formdata.get("ilosc")), border='LBR', align='C', fill=0, ln=0)
    pdf.cell(page_width*0.1, 5, str(formdata.get("cena")), border='LBR', align='C', fill=0, ln=0)
    pdf.cell(page_width*0.2, 5, str(formdata.get("cena")), border='LBR', align='C', fill=0, ln=1)   
    
    
    
    
    
    return pdf.output('website/static/tuto1.pdf', 'F')


     
    
