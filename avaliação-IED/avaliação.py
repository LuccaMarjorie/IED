import json  # importa o módulo json para salvar e carregar tarefas de um arquivo

ARQUIVO = "tarefas.txt"  # define o nome do arquivo onde as tarefas serão salvas

def salvar_tarefas():  # função que salva as tarefas no arquivo
    with open(ARQUIVO, "w") as f:  # abre o arquivo no modo escrita
        json.dump(tarefas, f, indent=4)  # salva a lista de tarefas em formato JSON no arquivo

def carregar_tarefas():  # função que carrega as tarefas do arquivo
    try:  # tenta abrir o arquivo
        with open(ARQUIVO, "r") as f:  # abre o arquivo no modo leitura
            return json.load(f)  # carrega os dados do arquivo e retorna como lista
    except FileNotFoundError:  # se o arquivo não for encontrado
        return []  # retorna uma lista vazia

def adicionar_tarefa(descricao):  # função que adiciona uma nova tarefa
    prioridade = input("Digite a prioridade (baixa, média, alta): ")  # lê a prioridade da tarefa informada pelo usuário
    tarefa = {  # cria um dicionário com os dados da tarefa
        "descricao": descricao,  # descrição da tarefa
        "prioridade": prioridade.lower()  # prioridade em letras minúsculas
    }
    tarefas.append(tarefa)  # adiciona a tarefa na lista principal
    historico.append(tarefa)  # adiciona a tarefa na pilha de histórico
    fila_execucao.append(tarefa)  # adiciona a tarefa na fila de execução
    salvar_tarefas()  # salva as tarefas no arquivo
    print(f"Tarefa '{descricao}' adicionada!\n")  # mostra para o usuário que a tarefa foi adicionada

def desfazer_ultima_tarefa():  # função para desfazer a última tarefa adicionada (Pilha)
    if historico:  # se houver tarefas no histórico
        ultima = historico.pop()  # remove a última tarefa da pilha
        tarefas.remove(ultima)  # remove a tarefa da lista principal
        fila_execucao.remove(ultima)  # remove a tarefa da fila de execução
        salvar_tarefas()  # salva as tarefas atualizadas no arquivo
        print(f"Tarefa '{ultima['descricao']}' desfeita!\n")  # mostra para o usuário qual tarefa foi desfeita
    else:  # se não
        print("Nenhuma tarefa para desfazer.\n")  # comando printa para o usuário que não existe nenhuma tarefa para ser removida

def atender_tarefa():  # comando de concluir tarefas (Fila)
    if fila_execucao:  # se fila_execução tiver:
        feita = fila_execucao.pop(0)  # remove e retorna a primeira tarefa (Fila)
        tarefas.remove(feita)  # remove a tarefa da fila de execução
        salvar_tarefas()  # salva as tarefas atualizadas no arquivo
        print(f"Tarefa '{feita['descricao']}' atendida!\n")  # comando printa para o usuário que a tarefa foi feita
    else:  # se não
        print("Nenhuma tarefa para atender.\n")  # comando printa para o usuário que não existe tarefas a serem concluidas

def mostrar_tarefas():  # comando para mostrar todas as tarefas adicionadas
    print("\n📋 Lista de Tarefas:")  # comando printa para o usuário a lista de tarefas
    for i, t in enumerate(tarefas):  # percorre a lista de tarefas com índice (i) e valor (t)
        print(f"{i + 1}. {t['descricao']} | Prioridade: {t['prioridade']}")  # comando printa a descrição e prioridade de cada tarefa
    print()  # comando printa para o usuário o espaço entre numeração e tarefa

# Inicializa estruturas com dados do arquivo
tarefas = carregar_tarefas()  # carrega as tarefas salvas no arquivo
historico = tarefas.copy()  # copia as tarefas para o histórico (simulando uma pilha)
fila_execucao = tarefas.copy()  # copia as tarefas para a fila de execução (simulando uma fila)

while True:  # comando de loop que só termina quando o usuário escolhe sair
    print("1. Adicionar Tarefa")  # comando printa para o usuário a opção de adicionar tarefa
    print("2. Desfazer Última Tarefa")  # comando printa para o usuário a opção de remover a ultima tarefa adicionada
    print("3. Atender Tarefa (modo fila)")  # comando printa para o usuário a opção de concluir tarefa
    print("4. Mostrar Tarefas")  # comando printa para o usuário a opção de mostrar tarefas
    print("5. Sair")  # comando printa para o usuário a opção de sair

    opcao = input("Escolha uma opção: ")  # comando que lê a opção escolhida pelo usuário

    if opcao == '1':  # se o usuário digitar "1":
        descricao = input("Digite a tarefa: ")  # printa para o usuário a opção de digitar uma tarefa
        adicionar_tarefa(descricao)  # comando executa a função "adicionar_tarefa"
    elif opcao == '2':  # se o usuário digitar "2":
        desfazer_ultima_tarefa()  # comando remove a última tarefa que foi adicionada
    elif opcao == '3':  # se o usuário digitar "3":
        atender_tarefa()  # comando executa a função "atender_tarefa"
    elif opcao == '4':  # se o usuário digitar "4":
        mostrar_tarefas()  # comando executa a função "mostrar_tarefas"
    elif opcao == '5':  # se o usuário digitar "5":
        print("Saindo do programa...")  # comando printa para o usuário que ele está saindo do programa
        break  # o loop para
    else:  # se não
        print("Opção inválida!\n")  # comando printa para o usuário que a opção escolhida é inválida
