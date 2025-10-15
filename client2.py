import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:9876")

def listar_livros():
    lista = proxy.listar_livros()
    print("titulo | autor | Edicao | Disponível?")
    for l in lista:
        disponivel = "Sim" if l["disponivel"] else "Não"
        print(f"{l['titulo']} | {l['autor']} | {l['edicao']} | {disponivel}")
    
    input("Digite uma tecla para continuar...")
    
def buscar_autor():
    str_busca = input("Digite o nome do autor: ")
    resultado = proxy.buscar_autor(str_busca)
    
    if len(resultado) == 0:
        print('Não foi encontrado nenhum livro com esse autor')
    else:
        for r in resultado:
            disponivel = "Sim" if r["disponivel"] else "Não"
            print(f"{r['titulo']} | {r['autor']} | {r['edicao']} | {disponivel}")
        input("Digite uma tecla para continuar...")
        
def parar_server():
    valor = proxy.parar_server()
    print(valor)

while True:
    print("\n\n=== BIBLIOTECA UNESPAR ===")
    print("[1] Listar livros")
    print("[2] Buscar Autor")
    print("[4] Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    match(opcao):
        case 1:
            listar_livros()
        case 2:
            buscar_autor()
        case 3:
            pass
        case 4:
            print("Saindo...")
            parar_server()
            break
        case _:
            print("Digite uma opção válida")