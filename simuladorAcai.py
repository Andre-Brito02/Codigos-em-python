import unicodedata
import re
import time

class Evento:
    def __init__(self, caixas_acai, copos_300, copos_400, copos_500, copos_770, leite_condensado, leite_em_po, granola, banana, creme_de_avela, bombom, pacoca, morango, confete, colher_grande, colher_pequena, troco):
        self._caixas_acai = caixas_acai
        self._copos_300 = copos_300
        self._copos_400 = copos_400
        self._copos_500 = copos_500
        self._copos_770 = copos_770
        self._leite_condensado = leite_condensado 
        self._leite_em_po = leite_em_po
        self._granola = granola
        self._banana = banana
        self._creme_de_avela = creme_de_avela
        self._bombom = bombom
        self._pacoca = pacoca
        self._morango = morango
        self._confete = confete
        self._colher_grande = colher_grande
        self._colher_pequena = colher_pequena
        self._troco = troco
        self._receita = 0
    
    def pedido(self, tamanho_copo, lista_acompanhamentos, dinheiro_recebido = None):
        valor_total = 0

        match(tamanho_copo):
            case 300:
                valor_total += 20
                self._copos_300 -= 1
                valor_total += self._soma_valor_total(lista_acompanhamentos)
                self._colher_pequena -= 1
            
            case 400:
                valor_total += 23
                self._copos_400 -= 1
                valor_total += self._soma_valor_total(lista_acompanhamentos)
                self._colher_grande -= 1
            
            case 500:
                valor_total += 25
                self._copos_500 -= 1
                valor_total += self._soma_valor_total(lista_acompanhamentos)
                self._colher_grande -= 1

            case 770:
                valor_total += 32
                self._copos_770 -= 1
                valor_total += self._soma_valor_total(lista_acompanhamentos)
                self._colher_grande -= 1
        
        print(f"Valor total: {valor_total:.2f}")
        metodo_de_pagamento = input("Digite a forma de pagamento: ")
        if metodo_de_pagamento == "dinheiro":
            dinheiro_recebido = int(input("Digite o valor recebido pelo cliente: "))
            
        if dinheiro_recebido is not None:
            if dinheiro_recebido < valor_total:
                print(f"Dinheiro insuficiente! Valor total: R${valor_total:.2f}")
                return
            
            troco_cliente = dinheiro_recebido - valor_total
            
            if troco_cliente > self._troco:
                print(f"Não há troco suficiente! Troco disponível: R${self._troco:.2f}")
                return
            
            self._troco -= troco_cliente
            print(f"Pagamento recebido: R${dinheiro_recebido:.2f}")
            print(f"Troco ao cliente: R${troco_cliente:.2f}\n")
        else:
            print(f"Pagamento não em dinheiro. Valor total: R${valor_total:.2f}\n")
        
        self.set_receita(valor_total)

    def _soma_valor_total(self, lista_acompanhamentos):
            valor_total = 0
            for acompanhamento in lista_acompanhamentos:
                acompanhamento = normalizar_entrada_usuario(acompanhamento)
                
                nome_formalizado = normalizar(acompanhamento)
                if acompanhamento in ["leite condensado", "creme de avela"]:
                    setattr(self, nome_formalizado, getattr(self, nome_formalizado) - 5)
                elif acompanhamento.lower() == "morango":
                    setattr(self, nome_formalizado, getattr(self, nome_formalizado) - 3)
                else:
                    setattr(self, nome_formalizado, getattr(self, nome_formalizado) - 1)
                        
                if acompanhamento == "pacoca":
                    valor_total += 1
                elif acompanhamento in ["confete", "bombom"]:
                    valor_total += 2
                elif acompanhamento in ["morango", "creme de avela"]:
                    valor_total += 3
            return valor_total  
    
    def set_receita(self, valor_total):
        self._receita += valor_total        
        
    def __str__(self):
        return f"""
    Evento{{
            caixas de açaí = {self._caixas_acai},
            Copos de 300 = {self._copos_300},
            Copos de 400 = {self._copos_400},
            Copos de 500 = {self._copos_500},
            Copos de 770 = {self._copos_770},
            Leite condensado = {self._leite_condensado},
            Leite em pó = {self._leite_em_po},
            Banana = {self._banana},
            Granola = {self._granola},
            Paçoca = {self._pacoca},
            Bombom = {self._bombom},
            Confete = {self._confete},
            Morango = {self._morango},
            Creme de avelã = {self._creme_de_avela},
            Colher grande = {self._colher_grande},
            Colher pequena = {self._colher_pequena},
            Troco = {self._troco},
            Receita = {self._receita}
        }}
    """
        
def normalizar(texto: str) -> str:
    nfkd = unicodedata.normalize("NFD", texto)
    sem_acento = "".join([c for c in nfkd if unicodedata.category(c) != "Mn"])
    sem_espaco = re.sub(r"[\s\-]+", "_", sem_acento)
    return "_" + sem_espaco.lower()

def normalizar_entrada_usuario(texto: str)-> str:
    nfkd = unicodedata.normalize("NFD", texto)
    sem_acento = "".join([c for c in nfkd if unicodedata.category(c) != "Mn"])
    return sem_acento.lower()

def cardapio():
    formatador = " "
    print(f"\n{'=' * 9} CARDÁPIO {'=' * 10}")
    print(f"Copo 300ml{formatador*6}----- R$20,00")
    print(f"Copo 400ml{formatador*6}----- R$23,00")
    print(f"Copo 500ml{formatador*6}----- R$25,00")
    print(f"Copo 770ml{formatador*6}----- R$32,00")
    print(f"{'=' * 6} ACOMPANHAMENTOS {'=' * 6}")
    print(f"Leite em pó{formatador*6}----- R$0,00")
    print(f"Leite condensado{formatador}----- R$0,00")
    print(f"Banana{formatador*11}----- R$0,00")
    print(f"Granola{formatador*10}----- R$0,00")
    print(f"Paçoca{formatador*11}----- R$1,00")
    print(f"Bombom{formatador*11}----- R$2,00")
    print(f"Confete{formatador*10}----- R$2,00")
    print(f"Morango{formatador*10}----- R$3,00")
    print(f"Creme de avelã{formatador*3}----- R$3,00\n")
    time.sleep(5)

caixas_acai = 20
copos_300 = 150
copos_400 = 150
copos_500 = 150
copos_770 = 100
bisnaga_leite_condensado = 500
leite_em_po = 1000
granola = 1000
banana = 50
sache_creme_de_avela = 500
bombom = 200
pacoca = 200
morango = 200
confete = 1000
colher_grande = 300
colher_pequena = 300
troco = 350

cardapio()
novo_evento = Evento(caixas_acai, copos_300, copos_400, copos_500, copos_770, bisnaga_leite_condensado, leite_em_po, granola, banana, sache_creme_de_avela, bombom, pacoca, morango, confete, colher_grande, colher_pequena, troco)
novo_evento.pedido(770, ["leite em pó", "leite condensado", "creme de avelã", "morango", "confete"])
novo_evento.pedido(500, ["leite em pó", "leite condensado", "pacoca"])
novo_evento.pedido(300, ["leite em pó", "leite condensado", "granola", "banana"]) 
print(novo_evento.__str__())