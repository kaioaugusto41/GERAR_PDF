from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
#A4 = (Largura=565, Altura=833)
#cnv.line(inicio_esquerda=10, inicio_inferior=10, inicio_direita=580, inicio_superior=10)

cnv = canvas.Canvas('meu_pdf.pdf')
topo = 841.5
canto_direito = 595
meio_largura = 565/2
meio_altura = 833/2


cnv.drawImage('logo.png', 0, 710, width=130, height=130)          # Logo
cnv.setFontSize(12)
cnv.rect(canto_direito-220, topo-95, 200, 60)
cnv.drawString(canto_direito-210, topo-50, 'Emitido: 13/05/2022 às 11:45')
cnv.drawString(canto_direito-210, topo-70, 'Data inicial: 26/04/2022 às 09:48')
cnv.drawString(canto_direito-210, topo-90, 'Data final: 13/05/2022 às 11:45')
cnv.setFontSize(16)
cnv.drawCentredString(canto_direito/2, 700, 'RELATÓRIO DE PRODUÇÃO MENSAL')
cnv.line(20, topo-160, canto_direito-20, topo-160)                # Linha horizontal superior
cnv.line(20, 20, canto_direito-20, 20)                            # Linha horizontal inferior
#cnv.line(20, topo-160, 20, 20)                                    # Linha vertical esquerda
#cnv.line(canto_direito-20, topo-160, canto_direito-20, 20)        # Linha vertical direita
cnv.rect(20, topo-250, 555, 60)


cnv.save()