import random

class Environment:
    def __init__(self):
        # Inicializa as salas aleatoriamente como sujas ou limpas
        self.rooms = {"left": random.choice(["clean", "dirty"]),
                      "right": random.choice(["clean", "dirty"])}

class TableDrivenVacuumAgent:
    def __init__(self, environment):
        # O agente começa na sala da esquerda
        self.position = "left"
        self.environment = environment
        self.perceptions = []  # Histórico de percepções
        
        # Definição da tabela de ações (baseada em percepções)
        self.action_table = {
            ("left", "clean"): "MoveRight",
            ("left", "dirty"): "Suck",
            ("right", "clean"): "MoveLeft",
            ("right", "dirty"): "Suck"
        }

    def perceive_environment(self):
        # O agente percebe se a sala em que está é suja ou limpa
        room_state = self.environment.rooms[self.position]
        current_perception = (self.position, room_state)
        self.perceptions.append(current_perception)
        return current_perception
    
    def act(self):
        current_perception = self.perceive_environment()
        action = self.action_table.get(current_perception, "NoAction")

        if action == "Suck":
            print(f"A sala {self.position} está suja. Limpando...")
            self.environment.rooms[self.position] = "clean"
        elif action == "MoveRight":
            print(f"A sala {self.position} está limpa. Movendo para a sala direita.")
            self.position = "right"
        elif action == "MoveLeft":
            print(f"A sala {self.position} está limpa. Movendo para a sala esquerda.")
            self.position = "left"
        
        return action

def run_agent(agent, steps=5):
    for step in range(steps):
        print(f"Passo {step + 1}:")
        agent.act()
        print(f"Estado do ambiente: {agent.environment.rooms}")
        print(f"Posição atual do agente: {agent.position}")
        print(f"Histórico de percepções: {agent.perceptions}\n")

# Criar o ambiente
environment = Environment()

# Criar o agente com tabela
agent = TableDrivenVacuumAgent(environment)

# Executar o agente
run_agent(agent)
