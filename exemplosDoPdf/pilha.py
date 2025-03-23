class Pilha:
    def __init__(self):
        self.items = []  # Armazena os elementos da pilha
    
    def push(self, item):
        """Empilha um elemento"""
        self.items.append(item)
    
    def pop(self):
        """Desempilha um elemento"""
        if not self.is_empty():
            return self.items.pop()
        return None  # Evita erro se a pilha estiver vazia
    
    def peek(self):
        """Mostra o topo da pilha"""
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        """Verifica se a pilha está vazia"""
        return len(self.items) == 0

# Criando um objeto Pilha
minha_pilha = Pilha()

# Agora precisamos usar o objeto para acessar os métodos
minha_pilha.push(10)
minha_pilha.push(20)
print(minha_pilha.pop())  # Remove 20
print(minha_pilha.peek())  # Mostra 10
