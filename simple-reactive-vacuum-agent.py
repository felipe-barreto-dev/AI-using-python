import random

class Environment:
    def __init__(self):
        # Inicializa as salas aleatoriamente como limpas ou sujas
        self.rooms = {"esquerda": random.choice(["limpo", "sujo"]),
                      "direita": random.choice(["limpo", "sujo"])}

class SimpleReactiveVacuumAgent:
    def __init__(self, environment):
        # O agente começa na sala da esquerda
        self.position = "esquerda"
        self.environment = environment
    
    def perceive_environment(self):
        # O agente percebe se a sala atual está limpa ou suja
        return self.environment.rooms[self.position]
    
    def act(self):
        perception = self.perceive_environment()
        
        if perception == "sujo":
            # Se a sala estiver suja, o agente limpa
            print(f"A sala {self.position} está suja. Limpando...")
            self.environment.rooms[self.position] = "limpo"
        else:
            # Se a sala estiver limpa, o agente se move para a próxima sala
            print(f"A sala {self.position} está limpa. Movendo para a próxima sala...")
            self.move_to_next_room()
    
    def move_to_next_room(self):
        # Move o agente para a sala oposta
        if self.position == "esquerda":
            self.position = "direita"
        else:
            self.position = "esquerda"

def run_agent(agent, steps=5):
    for step in range(steps):
        print(f"Passo {step + 1}:")
        agent.act()
        print(f"Estado do ambiente: {agent.environment.rooms}")
        print(f"Posição atual do agente: {agent.position}\n")

# Criar o ambiente
environment = Environment()
# Criar o agente
agent = SimpleReactiveVacuumAgent(environment)
# Executar o agente
run_agent(agent)
