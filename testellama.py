import ollama
import time

# Define o sistema de instruções para o modelo de forma direta na chamada do chat
sistema = '''
Você será responsável por classificar e resumir uma lista de atos, decretos e portarias em categorias predefinidas. 
Para cada item do texto fornecido, siga estes passos:
1. Classifique cada ato separadamente com um título, escolhendo entre uma das seguintes categorias: 
   Exoneração, Licitação, Afastamento ou Demissão.
2. Após classificar, forneça um resumo curto e direto abaixo do título, destacando informações essenciais.

Definições para cada classificação:
- **Exoneração**: Saída oficial de um servidor ou funcionário de um cargo ou função pública, sem indicação de substituição imediata.
- **Licitação**: Processos formais de contratação, compra de bens ou serviços, ou concursos promovidos por órgãos públicos.
- **Afastamento**: Afastamento temporário de um funcionário de suas funções, com previsão de retorno.
- **Demissão**: Saída definitiva de um servidor do serviço público, geralmente por motivos disciplinares.

Analise e classifique cada ato de forma individual, colocando o título da classificação diretamente acima do resumo correspondente.
'''

# Tempo de início
inicio_tempo = time.time()

# Conteúdo dos atos a serem classificados e resumidos
conteudo_usuario = '''
DECRETO Nº 1344-P, DE 29 DE OUTUBRO DE 2024
O GOVERNADOR DO ESTADO DE RORAIMA, no uso da atribuição que lhe confere o art. 62, inciso III, da Constituição Estadual.
RESOLVE:
Art. 1º Exonerar a servidora, a seguir relacionada, do Cargo Comissionado pertencente à estrutura organizacional da Procuradoria-Geral do Estado de
Roraima – PGE:
ORD NOME CPF CARGO CÓD.
1. LAÍS FONTINELE MATOS DE CARVALHO 946.024.252-91 GERENTE DE NÚCLEO DE RECURSOS HUMANOS CDS-I 

'''

# Executa o chat com as instruções e o conteúdo fornecido
response = ollama.chat(model='qwen2:0.5b', messages=[
    {
        'role': 'system',
        'content': sistema
    },
    {
        'role': 'user',
        'content': conteudo_usuario
    },
])

# Calcula o tempo de execução
fim_tempo = time.time()
tempo_execucao = fim_tempo - inicio_tempo
print(f'Tempo de execução: {tempo_execucao:.4f} segundos')

# Imprime a resposta formatada do modelo
if 'message' in response and 'content' in response['message']:
    print(response['message']['content'])
else:
    print("Erro: Resposta inesperada do modelo")
