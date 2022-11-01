from pessoa import Pessoa


class Motoca:

    def __init__(self, potencia: int):
        self.potencia = potencia
        self.minutos = 0
        self.pessoa = None

    def getPessoa(self):
        return self.pessoa

    def getTempo(self):
        return self.minutos

    def getPotencia(self):
        return self.potencia

    def subir(self, pessoa: Pessoa):
        if self.pessoa == None:
            self.pessoa = pessoa
            print('Pessoa Subiu na moto')
            return True
        else:
            print("ja Existe algume na moto")
            return False

    def descer(self):
        if self.pessoa != None:
            self.pessoa = None
            print("pessoa desceu da moto")
            return True
        else:
            print('Nao a ninguem na moto')
            return False

    def colocarTempo(self, tempo: int):
        if tempo > 0:
            self.minutos += tempo
            return True
        else:
            print('Impossivel colocar tempo negativo')
            return False

    def dirigir(self, tempo: int):
        if self.pessoa != None:
            pessoa = self.getPessoa()
            idade = pessoa.getIdade()
            if int(idade) <= 10:
                if self.minutos > 0:
                    while tempo > 0 and self.minutos > 0:
                        tempo -= 1
                        self.minutos -= 1
                    return True
                else:
                    print("sem tempo na moto")
                    return False
            else:
                print('pessoa com idade acima da permitida')
                return False
        else:
            print('sem pessoa embarcada')
            return False

    def buzinar(self):
        if self.pessoa != None:
            print('P'+('e'*self.potencia)+'m')
            return ('P'+('e'*self.potencia)+'m')
        else:
            print("impossivel buzinar sem motorista")
            return ""
