<p align="center">
  <h1>🚢 Projeto Titanic: Análise de Dados e Detecção de Outliers 🧪</h1>
</p>

<p align="center">
  <img src="https://miro.medium.com/0*CTJNRzvl8UDyyJ9V" width="500"/>
</p>

---

## 📌 Descrição

Este projeto utiliza a base de dados do Titanic para explorar e limpar dados, além de identificar **outliers** usando o algoritmo **Isolation Forest**. O objetivo é demonstrar técnicas de **análise exploratória, tratamento de inconsistências, redundâncias, dados incompletos e ruídos**.

---

## 🛠 Tecnologias e Bibliotecas

- Python 🐍
- pandas 📊
- scikit-learn 🧠
- matplotlib 🎨

---

## 🔍 Funcionalidades

1. Identificação de **dados inconsistentes** (ex.: idades negativas ou acima do esperado).  
2. Detecção de **dados incompletos** (`NaN`) e redundantes.  
3. Identificação de **dados ruidosos** (valores estranhos em `Fare`, `Cabin`, `Ticket`).  
4. **Detecção de outliers** com Isolation Forest.  
5. Visualização gráfica dos outliers em `Age x Fare`.

---

## 📖 Como Usar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/projeto-titanic.git
```
Instale as dependências:

Copiar código
```bash
pip install pandas scikit-learn matplotlib
```
Rode o script principal:

```bash
python main.py
```

📈 Resultado
Após executar, o script identifica os passageiros com dados fora do padrão e exibe gráficos destacando os outliers.

📚 Referências
Kaggle Titanic Dataset

Isolation Forest - scikit-learn

✨ Projeto criado para aprendizado em análise de dados e machine learning básico.
