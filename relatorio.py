import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def processar_gastos():
    print("1. Lendo dados do arquivo CSV...")
    df = pd.read_csv('dados_gastos.csv')

    total_gasto = df['Valor'].sum()
    gastos_por_categoria = df.groupby('Categoria')['Valor'].sum()

    print("\n--- RESUMO DE GASTOS ---")
    print(f"Gasto Total: R$ {total_gasto:.2f}")
    print("\nGastos por Categoria:")
    print(gastos_por_categoria)

    # 2. Gerando Gráfico
    print("\n2. Gerando gráfico de pizza...")
    plt.figure(figsize=(6, 6))
    plt.pie(gastos_por_categoria, labels=gastos_por_categoria.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Gastos por Categoria')
    grafico_path = 'grafico_gastos.png'
    plt.savefig(grafico_path, bbox_inches='tight')
    plt.close()

    # 3. Gerando Relatório em PDF
    print("3. Gerando relatório PDF...")
    pdf_path = "Relatorio_Financeiro.pdf"
    pdf = canvas.Canvas(pdf_path, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(100, 750, "Relatório Automatizado de Despesas")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 710, f"Gasto Total Acumulado: R$ {total_gasto:.2f}")

    pdf.drawImage(grafico_path, 100, 350, width=400, height=300)
    pdf.save()

    if os.path.exists(grafico_path):
        os.remove(grafico_path)

    print(f"\n✅ Concluído! Relatório gerado com sucesso: {pdf_path}")

if __name__ == "__main__":
    processar_gastos()
