# immune-multiomics-pipeline
A Python-based integrative multi-omics pipeline for biomarker discovery in immune-mediated adverse events.


# 🧬 Transcriptomic Analysis of Influenza A Infection (GSE68849)

Pipeline end-to-end em Python/Jupyter Notebook para análise de expressão diferencial e enriquecimento funcional de dados de microarray (Illumina HumanHT-12 v4).

## 📌 Highlights do Projeto
- **Pré-processamento & QC**: Controle de qualidade e normalização da matriz de expressão.
- **Expressão Diferencial (DEG)**: Identificação de genes super/sub-expressos em infecção por Influenza A vs. Controle.
- **Anotação de Genes**: Mapeamento de sondas Illumina (`ILMN_xxxx`) para HGNC Gene Symbols em memória.
- **Enriquecimento Funcional (GSEA)**: Análise de vias KEGG evidenciando a regulação da via *T cell receptor signaling*.

## 🧪 Principais Achados Biológicos
- **Vias Enriquecidas**: Forte representação da *T cell receptor signaling pathway*, refletindo o engajamento da resposta adaptativa celular.
- **Marcadores de Resposta Imune**: Elevação de efetores inflamatórios (*IFNG*, *CXCL10*, *TNF*, *IL6*) e fatores de transcrição antiviral (*STAT3*, *IRF1*).
- **Checkpoints Imunológicos**: Co-expressão de receptores coinibitórios (*PDCD1*, *CTLA4*, *LAG3*) juntamente com *CD8A*, indicando mecanismos de atenuação e controle de imunopatologia pulmonar.

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3.10
- **Análise de Dados**: `pandas`, `numpy`
- **Bioinformática**: `gseapy`, `mygene`
- **Visualização**: `matplotlib`, `seaborn`

## 📁 Estrutura do Repositório
