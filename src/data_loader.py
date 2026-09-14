import gzip
import os
import pandas as pd

def parse_geo_series_matrix(filepath):
    """
    Realiza o parse do arquivo GEO Series Matrix (.txt.gz).
    
    Retorna:
    --------
    expression_df : pd.DataFrame
        Matriz de expressão gênica (Genes/Probes em linhas, Amostras em colunas).
    metadata_df : pd.DataFrame
        Metadados associados às amostras clínicas.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

    metadata_dict = {}
    matrix_lines = []
    in_matrix = False

    with gzip.open(filepath, 'rt', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line_str = line.strip()

            # Captura metadados das amostras
            if line_str.startswith("!Sample_geo_accession"):
                sample_ids = [x.replace('"', '') for x in line_str.split('\t')[1:]]
                metadata_dict['sample_id'] = sample_ids
            elif line_str.startswith("!Sample_characteristics_ch1"):
                characteristics = [x.replace('"', '') for x in line_str.split('\t')[1:]]
                # Adiciona cada linha de caracteristica aos metadados
                key = characteristics[0].split(':')[0] if ':' in characteristics[0] else 'characteristic'
                metadata_dict[key] = characteristics

            # Identifica início da tabela de expressão
            if line_str.startswith("!series_matrix_table_begin"):
                in_matrix = True
                continue
            elif line_str.startswith("!series_matrix_table_end"):
                in_matrix = False
                break

            if in_matrix:
                matrix_lines.append(line_str.split('\t'))

    # Converte matriz de expressão em DataFrame
    if matrix_lines:
        header = [x.replace('"', '') for x in matrix_lines[0]]
        data = matrix_lines[1:]
        expression_df = pd.DataFrame(data, columns=header)
        expression_df.rename(columns={expression_df.columns[0]: 'ID_REF'}, inplace=True)
        
        # Define ID_REF (Gene/Probe) como índice e converte valores para float
        expression_df.set_index('ID_REF', inplace=True)
        expression_df = expression_df.apply(pd.to_numeric, errors='coerce')
    else:
        expression_df = pd.DataFrame()

    # Converte metadados em DataFrame
    metadata_df = pd.DataFrame(metadata_dict)
    if 'sample_id' in metadata_df.columns:
        metadata_df.set_index('sample_id', inplace=True)

    return expression_df, metadata_df

if __name__ == "__main__":
    raw_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "GSE68849_series_matrix.txt.gz")
    print(f"Lendo dados de {raw_path}...")
    
    expr, meta = parse_geo_series_matrix(raw_path)
    
    print("\n--- Matriz de Expressão Gênica ---")
    print(f"Dimensões (Genes x Amostras): {expr.shape}")
    print(expr.head())
    
    print("\n--- Metadados Clinicos ---")
    print(f"Dimensões (Amostras x Atributos): {meta.shape}")
    print(meta.head())

