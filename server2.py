from xmlrpc.server import SimpleXMLRPCServer

acervo = {
    1:{
        "titulo": "Sistemas Distribuidos",
        "Ano": 2007,
        "autor": "Coulouris",
        "edicao": 4,
        "exemplares_total": 5,
        "exemplares_emprestados": 2
    },
}

def listar_livros():
    lista = []
    
    for livro in acervo.values():
        disponivel = livro["exemplares_total"] > livro["exemplares_emprestados"]
        lista.append(
            {
                "titulo": livro["titulo"],
                "autor": livro["autor"],
                "edicao": livro["edicao"],
                "disponivel": disponivel
            })
    return lista

def buscar_autor(str_busca):
    resultado = []
    
    for l in acervo.values():
        if str_busca.lower() in l['autor'].lower():
            disponivel = l["exemplares_total"] > l["exemplares_emprestados"]
            resultado.append(
            {
                "titulo": l["titulo"],
                "autor": l["autor"],
                "edicao": l["edicao"],
                "disponivel": disponivel
            })
    
    return resultado

def parar_server():
    global running
    running = False
    return "Servidor Finalizado"

#Criar o processo
server = SimpleXMLRPCServer(("localhost", 9876))
print("Servidor criado na porta 9876")

server.register_function(listar_livros, "listar_livros")
server.register_function(buscar_autor, "buscar_autor")
server.register_function(parar_server, "parar_server")

running = True
while running:
    server.handle_request()