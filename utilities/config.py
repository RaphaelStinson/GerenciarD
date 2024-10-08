# utilities/config.py

import os
import json

# Caminho do arquivo de configuração
CAMINHO_CONFIG = 'config_pastas.json'

# Função para carregar pastas observadas do arquivo de configuração
def carregar_pastas_observadas():
    if os.path.exists(CAMINHO_CONFIG):
        with open(CAMINHO_CONFIG, 'r') as f:
            dados = json.load(f)
            return dados.get('pastas_observadas', [])
    else:
        # Se o arquivo não existir, cria um com um formato padrão
        salvar_pastas_observadas([])
        return []

# Função para salvar pastas observadas no arquivo de configuração
def salvar_pastas_observadas(pastas_observadas):
    dados = {
        'pastas_observadas': pastas_observadas
    }
    with open(CAMINHO_CONFIG, 'w') as f:
        json.dump(dados, f, indent=4)

# Função para criar uma nova pasta se não existir
def criar_pasta(pasta):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

# Pastas a serem observadas

pasta_destino = '/storage/emulated/0/Download'