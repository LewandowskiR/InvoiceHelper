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
def Slownie (Liczba):   
    Liczby = [
    [''         ,''               ,''                 ,''            ],
    ['jeden '   ,'jedenascie '    ,'dziesiec '        ,'sto '        ],
    ['dwa '     ,'dwanascie '     ,'dwadziescia '     ,'dwiescie '   ],
    ['trzy '    ,'trzynascie '    ,'trzydziesci '     ,'trzysta '    ],
    ['cztery '  ,'czternascie '   ,'czterdziesci '    ,'czterysta '  ],
    ['piec '    ,'pietnascie '    ,'piecdziesiat '    ,'piecset '    ],
    ['szesc '   ,'szesnascie '    ,'szescdziesiat '   ,'szescset '   ],
    ['siedem '  ,'siedemnascie '  ,'siedemdziesiat '  ,'siedemset '  ],
    ['osiem '   ,'osiemnascie '   ,'osiemdziesiat '   ,'osiemset '   ],
    ['dziewiec ','dziewietnascie ','dziewiecdziesiat ','dziewiecset ']]
     
    Grupy = [
    [''        ,''         ,''          ],
    ['tysiac ' ,'tysiace ' ,'tysiecy '  ],
    ['milion ' ,'miliony ' ,'milionow ' ],
    ['miliard ','miliardy ','miliardow '],
    ['bilion ' ,'biliony ' ,'bilionow ' ],
    ['biliard ','biliardy ','biliardow '],
    ['trylion ','tryliony ','trylionow ']]
     
    J, N, D, S, G, K = 0, 0, 0, 0, 0, 0     #Jednostki,Nastki,Dziesiatki,Setki,Grupy,Koncowki
    Ciag, Znak = "", ""
     
    if Liczba < 0:
        Znak = "minus "
        Liczba = -Liczba
    if Liczba == 0:
        Ciag = "zero "
    while not Liczba == 0:
        S = Liczba % 1000 // 100
        D = Liczba % 100 // 10
        J = Liczba % 10
        if D == 1 and J > 0:                #Warunek do obsługi nastek
            N = J
            D = 0
            J = 0
        else:
            N = 0
        if J == 1:                          #Tu zawiera sie cała gramatyka, wybór końcówki
            if S + D + N > 0:
                K = 2
            else:
                K = 0;
        elif J in [2,3,4]:
            K = 1
        else:
            K = 2       
        if S + D + N + J > 0:
            Ciag = Liczby[S][3] + Liczby[D][2] + Liczby[N][1] + Liczby[J][0] + Grupy[G][K] + Ciag
        G = G + 1
        Liczba = Liczba // 1000;
    return Znak + Ciag 
    

def BasicInvoiceGenerate(formdata, image):
 
    pdf = FPDF()
    pdf.set_fill_color(228,g=231,b=231)
    
    page_width = pdf.w - 2*pdf.l_margin
    column_ratio = 0.4
    space_ratio = 0.15
    
    pdf.add_page()
    
    pdf.set_x(page_width*0.15)
    
    if(image):
        pdf.image(image, x = None, y = None, w = 35, h = 35)
        
    pdf.set_xy(page_width*0.6,pdf.h-(pdf.h-30))
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
    pdf.cell(page_width*0.5, 5, 'Nazwa towaru lub uslugi', border='LTR', align='C', fill=1, ln=0)
    pdf.cell(page_width*0.08, 5, 'Jm.', border='LTR', align='C', fill=1, ln=0)
    pdf.cell(page_width*0.08, 5, 'Ilosc', border='LTR', align='C', fill=1, ln=0)
    pdf.cell(page_width*0.14, 5, 'Cena', border='LTR', align='C', fill=1, ln=0)
    pdf.cell(page_width*0.1, 5, 'Wartosc', border='LTR', align='C', fill=1, ln=1)
    
    pdf.set_font('Times', '', 12)
    pdf.cell(page_width*0.1, 5, '1', border='LBR', align='C', fill=0, ln=0)
    pdf.cell(page_width*0.5, 5, str(formdata.get("nazwa_uslugi")), border='LBR', align='L', fill=0, ln=0)
    pdf.cell(page_width*0.08, 5, str(formdata.get("jednostka")), border='LBR', align='C', fill=0, ln=0)
    pdf.cell(page_width*0.08, 5, str(formdata.get("ilosc")), border='LBR', align='C', fill=0, ln=0)
    pdf.cell(page_width*0.14, 5, str(formdata.get("cena")), border='LBR', align='R', fill=0, ln=0)
    pdf.cell(page_width*0.1, 5, str(formdata.get("cena")), border='LBR', align='R', fill=0, ln=1)
    
    pdf.cell(page_width*0.80, 5, '', ln=0)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(page_width*0.1, 5, 'Razem', align='R', ln=0)
    pdf.set_font('Times', '', 12)
    pdf.cell(page_width*0.1, 5, str(formdata.get("cena")), border='LBR', align='R', fill=0, ln=1)
    
    pdf.cell(page_width, 10,'',ln=1)
    pdf.cell(page_width*0.20, 8, 'Sposob platnosci', border='TB', align='L', fill=0, ln=0)
    pdf.cell(page_width*0.25, 8, str(formdata.get("platnosc")), border='TB', align='L', fill=0, ln=0)
    pdf.cell(page_width*0.05, 8, '', ln=0)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(page_width*0.5, 8, f'Do zaplaty:   {str(formdata.get("cena"))} PLN', border='TB', align='L', fill=0, ln=1)
    
    pdf.set_font('Times', '', 12)
    pdf.cell(page_width*0.20, 8, 'Numer konta', border='T', align='L', fill=0, ln=0)
    pdf.cell(page_width*0.25, 8, str(formdata.get("nr_konta")), border='', align='L', fill=0, ln=0)
    pdf.cell(page_width*0.05, 8, '', ln=0)
    #pdf.cell(page_width*0.5, 8, f'Slownie:   {str(Slownie(formdata.get("cena")))} PLN', border='T', align='L', fill=0, ln=1)
    
    pdf.cell(page_width, 40,'',ln=1)
    pdf.set_font('Times', '', 10)
    
    pdf.cell(page_width*0.05, 8, '', ln=0)
    pdf.cell(page_width*0.40, 8, 'Podpis osoby upowaznionej do wystawienia', border='T', align='C', fill=0, ln=0)
    pdf.cell(page_width*0.1, 8, '', ln=0)
    pdf.cell(page_width*0.40, 8, 'Podpis osoby upowaznionej do odbioru', border='T', align='C', fill=0, ln=1)
    

    
    return pdf.output('website/static/invoice1.pdf', 'F')


     
    
