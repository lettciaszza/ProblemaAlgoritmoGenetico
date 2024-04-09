import random

# Função de fitness para o algoritmo genético
def fitness(solution, wt, val, W):
    total_weight = sum(wt[i] for i in range(len(solution)) if solution[i] == 1)
    total_value = sum(val[i] for i in range(len(solution)) if solution[i] == 1)

    # Retorna 0 para soluções inviáveis
    if total_weight > W:
        return 0
    else:
        return total_value

# Algoritmo Genético
def genetic_algorithm(wt, val, W, population_size=100, generations=100):
    population = []

    # Inicialização da população
    for _ in range(population_size):
        individual = [random.randint(0, 1) for _ in range(len(wt))]
        population.append(individual)

    # Execução das gerações
    for generation in range(generations):
        # Avaliação da aptidão (fitness) de cada indivíduo
        fitness_values = [fitness(ind, wt, val, W) for ind in population]

        # Impressão de informações
        print(f"Geração {generation + 1} - Melhor Fitness: {max(fitness_values)}")

        # Seleção de pais com base na aptidão
        parents = []
        for _ in range(population_size // 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            parents.append((parent1, parent2))

        # Crossover
        children = []
        for parent1, parent2 in parents:
            crossover_point = random.randint(1, len(wt) - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            children.extend([child1, child2])

        # Mutação
        mutation_rate = 0.1
        for i in range(population_size):
            for j in range(len(wt)):
                if random.random() < mutation_rate:
                    children[i][j] = 1 - children[i][j]

        # Combinação de pais e filhos para formar a próxima geração
        combined_population = population + children

        # Seleção dos melhores indivíduos para formar a próxima população
        population = sorted(combined_population, key=lambda x: fitness(x, wt, val, W), reverse=True)[:population_size]

    # Retorno da melhor solução encontrada
    best_solution = max(population, key=lambda x: fitness(x, wt, val, W))
    return best_solution, fitness(best_solution, wt, val, W)

# Itens disponíveis para a missão espacial da NASA (Com 30 itens)
W = 30  # Capacidade da mochila
wt = [3, 2, 5, 4, 6, 1, 7, 8, 10, 12, 15, 18, 20, 22, 25, 28, 30, 1, 4, 9, 13, 16, 19, 21, 24, 26]  # Peso dos itens
val = [10, 8, 15, 12, 20, 5, 25, 30, 18, 22, 35, 40, 28, 32, 45, 50, 38, 8, 12, 20, 28, 36, 42, 48, 55, 60]  # Valores dos itens

best_solution, best_value = genetic_algorithm(wt, val, W)
print("Melhor solução encontrada:", best_solution)
print("Valor total na mochila:", best_value)
