
import requests
import deep_translator

opcao = 0
opcao2 = 0


def linha(tamanho=40, char='='):
    print(char * tamanho)

def titulo(texto, tamanho=40):
    linha(tamanho)
    print(f'{texto.center(tamanho)}')
    linha(tamanho)

def mensagem(texto, tamanho=40):
    print(f'{texto.center(tamanho)}')
    linha(tamanho)


def menu():
    titulo('🍹 Cachaçaria do Seu Zé 🍹')
    print('''
    [1] 📜 Receber Conselhos
    [2] 📂 Ler Conselhos Salvos
    [3] 🌎 Tradução de Conselhos
    [4] 🚪 Sair do Programa
    ''')
    escolher = int(input('Escolha uma das opções: '))
    return escolher

def menu_conselhos():
    titulo('💭 Conselhos para o Seu Zé 💭')
    print('''
    [1] Receber 1 Conselho
    [2] Receber 2 Conselhos
    [3] Receber 3 Conselhos
    [4] ↩️ Voltar ao Menu Principal
    ''')
    escolher2 = int(input('Escolha o número de conselhos: '))
    return escolher2

def menu_traduzir():
    titulo('🌍 Tradução de Conselhos 🌍')
    print('''
    [0] Traduzir Todos os Conselhos
    [1, 2, 3...] Traduzir Conselho Específico
    [4] Traduzir Conselhos no Arquivo
    [5] ↩️ Voltar ao Menu Principal
    ''')
    escolher4 = int(input('Escolha o que deseja: '))
    return escolher4


def conselhos():
    try:
        url = 'https://api.adviceslip.com/advice'
        api = requests.get(url)
        conselho = api.json()['slip']['advice']
        id_conselho = api.json()['slip']['id']
    except requests.RequestException as e:
        print(f"⚠️ Erro ao acessar a API: {e}")
    return conselho, id_conselho

def salvando_conselho(opcao2):
    titulo('📜 Recebendo Conselhos 📜')
    lista_conselhos = []
    lista_id = []
  
    for c in range(opcao2):
        advice, id = conselhos()
        lista_id.append(id)
        lista_conselhos.append(advice)
        print(f'    {c + 1}° Conselho: {lista_conselhos[c]} (ID: {lista_id[c]})')
    return lista_conselhos, lista_id

def txt_conselho(lista_conselhos, lista_id):
    titulo('💾 Salvar Conselhos 💾')
    print('''
    [0] Salvar Todos os Conselhos
    [1, 2, 3...] Salvar Conselho Específico
    [5] 🌍 Tradução
    [6] ↩️ Voltar ao Menu Principal
    [7] 🚪 Sair do Programa
    ''')
    escolher3 = int(input('Escolha: '))
    if escolher3 == 0:
        with open('Conselhos.txt', 'a') as arquivo:
            for i in range(len(lista_conselhos)):
                arquivo.write(f'\nID: {lista_id[i]} - Conselho: {lista_conselhos[i]}')
        mensagem('✅ Todos os conselhos foram salvos!', 40)
    elif 1 <= escolher3 <= len(lista_conselhos):
        with open('Conselhos.txt', 'a') as arquivo:
            arquivo.write(f'\nID: {lista_id[escolher3 - 1]} - Conselho: {lista_conselhos[escolher3 - 1]}')
        mensagem('✅ Conselho salvo!', 40)
    return escolher3

def ler_conselhos():
    try:
        with open('Conselhos.txt', 'r') as arquivo:
            leitura = arquivo.read()
            if leitura.strip():
                titulo('📂 Conselhos Salvos 📂')
                print(f'{leitura}\n')
            else:
                mensagem('📭 Ainda não há conselhos salvos...', 40)
    except FileNotFoundError:
        mensagem('📭 Arquivo não encontrado...', 40)
    traduz = input('Deseja traduzir? [S/N]: ').strip().upper()
    return traduz

def traduzirtxt():
    try:
        with open('Conselhos.txt', 'r') as arquivo:
            leitura = arquivo.read()
            traducao = deep_translator.GoogleTranslator(source='en', target='pt').translate(leitura)
            if leitura.strip():
                titulo('🌍 Conselhos Traduzidos 🌍')
                print(f'{traducao}\n')
            else:
                mensagem('📭 Nenhum conselho encontrado para traduzir.', 40)
    except FileNotFoundError:
        mensagem('📭 Arquivo não encontrado.', 40)
    escolher5 = input('Deseja continuar traduzindo? [S/N]: ').strip().upper()
    return escolher5

def traduzir(opcao4, lista1):
    try:
        if opcao4 > 0 and opcao4 <= len(lista1):
            texto = lista1[opcao4 - 1]
            traducao2 = deep_translator.GoogleTranslator(source='en', target='pt').translate(texto)
            titulo('🌍 Conselho Traduzido 🌍')
            print(f'{traducao2}\n')
        elif opcao4 == 0:
            for c in range(len(lista1)):
                texto = lista1[c - 1]
                traducao2 = deep_translator.GoogleTranslator(source='en', target='pt').translate(texto)
                if c == 0:
                    titulo('🌍 Conselhos Traduzidos 🌍')
                    print(f'{traducao2}\n')
    except:
            mensagem('⚠️ Conselho inválido ou inexistente.', 40)
    escolher5 = input('Deseja continuar traduzindo? [S/N]: ').strip().upper()
    return escolher5

if __name__ == '__main__':
    while True:
        opcao2 = 0
        if opcao == 0:
            opcao = menu()
            if opcao == 1:
                while True:
                    if opcao2 == 4:
                        opcao = 0
                        break
                    opcao2 = menu_conselhos()
                    if opcao2 == 4:
                        opcao = 0
                        break
                    lista1, lista2 = salvando_conselho(opcao2)
                    opcao3 = txt_conselho(lista1, lista2)
                    if opcao3 == 6:
                        opcao = 0
                        break
                    elif opcao3 == 7:
                        opcao = 4
                        break
                    elif opcao3 == 5:
                        while True:
                            opcao4 = menu_traduzir()
                            if opcao4 == 5:
                                opcao2 = 4
                                break
                            elif opcao4 == 0:
                                opcao5 = traduzir(opcao4, lista1)
                                if opcao5 in 'N':
                                    opcao2 = 4
                                    break
                            elif opcao4 > 0 and opcao4 < 4:
                                try:
                                    opcao5 = traduzir(opcao4, lista1)
                                    if opcao5 in 'N':
                                        opcao2 = 4
                                        opcao = 0
                                        break
                                except:
                                    mensagem('⚠️ Conselho inválido ou inexistente.', 40)
                                    opcao = 0
                                    break
                            
        elif opcao == 2:
            while True:
                traduz = ler_conselhos()
                if traduz == 'S':
                    opcao5 = traduzirtxt()
                    if opcao5 in 'N':
                            opcao = 0
                            break
                    elif opcao5 in 'S':
                        opcao = 3
                        break
        elif opcao == 3:
            while True:
                opcao4 = menu_traduzir()
                if opcao4 == 5:
                    opcao = 0
                    break
                elif opcao4 == 4:
                    opcao5 = traduzirtxt()
                    if opcao5 in 'N':
                                opcao = 0
                                break
                    elif opcao4 == 0:
                        try:
                            opcao5 = traduzir(opcao4, lista1)
                            if opcao5 in 'N':
                                opcao2 = 4
                                opcao = 0
                                break
                        except:
                            mensagem('⚠️ Conselho inválido ou inexistente.', 40)
                            opcao = 0
                            break
                elif opcao4 > 0 and opcao4 < 4:
                    try:
                            opcao5 = traduzir(opcao4, lista1)
                            if opcao5 in 'N':
                                opcao2 = 4
                                opcao = 0
                                break
                    except:
                            mensagem('⚠️ Conselho inválido ou inexistente.', 40)
                            opcao = 0
                            break
        elif opcao == 4:
            mensagem('👋 Até mais! Volte sempre!', 40)
            break
        else:
            mensagem('⚠️ Opção inválida! Tente novamente.', 40)
