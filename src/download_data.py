import os
import urllib.request

def download_dataset():
    raw_dir = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    
    url = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE68nnn/GSE68849/matrix/GSE68849_series_matrix.txt.gz"
    dest_path = os.path.join(raw_dir, "GSE68849_series_matrix.txt.gz")
    
    if not os.path.exists(dest_path):
        print(f"Baixando dataset de {url}...")
        urllib.request.urlretrieve(url, dest_path)
        print(f"Download concluído! Salvo em: {dest_path}")
    else:
        print("Arquivo de dados já existe em data/raw/.")

if __name__ == "__main__":
    download_dataset()
