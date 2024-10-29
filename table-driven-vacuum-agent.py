import random
from tabulate import tabulate

class Environment:
    def __init__(self):
        # Inicializa as salas aleatoriamente como limpas ou sujas
        self.rooms = {
            "a": random.choice(["limpo", "sujo"]),
            "b": random.choice(["limpo", "sujo"]),
            "c": random.choice(["limpo", "sujo"]),
            "d": random.choice(["limpo", "sujo"]),
            "e": random.choice(["limpo", "sujo"])
        }

    def is_clean(self):
        # Verifica se todas as salas estão limpas
        return all(state == "limpo" for state in self.rooms.values())

class TableDrivenVacuumAgent:
    def __init__(self, environment):
        # O agente começa na sala 'a'
        self.position = "a"
        self.environment = environment
        self.perceptions = []  # Histórico de percepções do agente
        
        # Definição da tabela de ações (baseada nas percepções)
        self.action_table = {
            ("a", "limpo"): "Move-se à direita",
            ("a", "sujo"): "Limpa",
            ("b", "limpo"): "Move-se à direita",
            ("b", "sujo"): "Limpa",
            ("c", "limpo"): "Move-se à direita",
            ("c", "sujo"): "Limpa",
            ("d", "limpo"): "Move-se à direita",
            ("d", "sujo"): "Limpa",
            ("e", "limpo"): "Move-se à esquerda",
            ("e", "sujo"): "Limpa"
        }

    def perceive_environment(self):
        # O agente percebe se a sala em que está é suja ou limpa
        room_state = self.environment.rooms[self.position]
        current_perception = (self.position, room_state)
        self.perceptions.append(current_perception)
        return current_perception
    
    def act(self):
        # Agente age com base na percepção atual e na tabela de ações
        current_perception = self.perceive_environment()
        action = self.action_table.get(current_perception, "NoAction")

        if action == "Limpa":
            print(f"A sala {self.position} está suja. Limpando...")
            self.environment.rooms[self.position] = "limpo"
        elif action == "Move-se à direita":
            next_position = chr(ord(self.position) + 1)  # Move para a sala à direita
            print(f"A sala {self.position} está limpa. Movendo para a sala {next_position}.")
            self.position = next_position
        elif action == "Move-se à esquerda":
            next_position = chr(ord(self.position) - 1)  # Move para a sala à esquerda
            print(f"A sala {self.position} está limpa. Movendo para a sala {next_position}.")
            self.position = next_position
        
        return action

def run_agent(agent, max_steps=10):
    # Tabela de resultados para armazenar as ações realizadas e o estado do ambiente
    result_table = []

    for step in range(max_steps):
        # Verifica se todas as salas estão limpas
        if agent.environment.is_clean():
            print("Todas as salas estão limpas. Finalizando a execução.")
            break

        action = agent.act()
        environment_state = agent.environment.rooms.copy()  # Copia o estado atual do ambiente
        current_position = agent.position
        current_perception = agent.perceptions[-1]  # Última percepção

        # Adiciona as informações à tabela de resultados
        result_table.append([
            step + 1,          # Passo
            current_perception[0],  # Posição
            current_perception[1],  # Estado
            action,            # Ação realizada
            environment_state  # Estado do ambiente
        ])
    
    # Exibe a tabela de resultados usando a biblioteca tabulate
    print("\nAgent Execution Results:")
    print(tabulate(result_table, headers=["Step", "Position", "State", "Action", "Environment State"], tablefmt="grid"))

# Cria o ambiente
environment = Environment()

# Cria o agente baseado em tabela
agent = TableDrivenVacuumAgent(environment)

# Executa o agente
run_agent(agent)
