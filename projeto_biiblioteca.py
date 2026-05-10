class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor 
        self.disponibilidade = "disponível"
  
lista_livros = []

# função para adicionar livros 
def adiciona_livro():
    t = input("\nTítulo do Livro: ")
    a = input("\nAutor do Livro: ")
    novoLivro = Livro(t, a)
    lista_livros.append(novoLivro)
    print(f"\nO livro '{t}' de {a} foi adicionado com sucesso!")
        
# função para listar os livros
def listar_livro():
    if not lista_livros:
        print("\nNenhum livro cadastrado.")
        return
    for livro in lista_livros:
        print(f"\nTítulo: {livro.titulo}\nAutor: {livro.autor}\nDisponilidade: {livro.disponibilidade}")

# função para emprestar um livro
def empresta_livro():
    nome = input("\nNome do Livro para empréstimo: ")
    for livro in lista_livros:
        # usando .lower() por conta sensibilidade do python, para ignorar maiúsculas e minúsculas
        if livro.titulo.lower() == nome.lower() and livro.disponibilidade == "disponível":
            livro.disponibilidade = "emprestado"
            print(f"Livro '{livro.titulo}' emprestado com sucesso!")
            return
    print("Livro não disponível ou não existe")

# função para devolver um livro 
def devolver_livro():
    nome = input("\nNome do Livro para devolução: ")
    for livro in lista_livros:
        if livro.titulo.lower() == nome.lower() and livro.disponibilidade == "emprestado":
            livro.disponibilidade = "disponível"
            print(f"O livro '{livro.titulo}' foi devolvido e agora está [disponível].")
            return
    print("Livro não encontrado ou não está emprestado.")

# função da disponibilidade do livro específico
def consultar_disponibilidade():
    nome = input("\nDigite o título para consultar: ")
    for livro in lista_livros:
        if livro.titulo.lower() == nome.lower():
            print(f"O livro '{livro.titulo}' está: {livro.disponibilidade}")
            return
    print("Livro não encontrado no acervo.")

# menu 
while True:
    print("\n1 - Adicionar Livro")
    print("2 - Listar Livros")
    print("3 - Emprestar Livro")
    print("4 - De\nvolver Livro")
    print("5 - Consultar Disponibilidade")
    print("6 - Sair")
    
    menu = input("\nEscolha uma opção: ")
    
    if menu == "1":
        adiciona_livro()
    elif menu == "2":
        listar_livro()
    elif menu == "3":
        empresta_livro()
    elif menu == "4":
        devolver_livro()
    elif menu == "5":
        consultar_disponibilidade()
    elif menu == "6":
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida!")