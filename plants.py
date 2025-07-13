import random

def probability_tree(max_levels, decrement=0.0001):
    prob = 1.0
    for level in range(1, max_levels + 1):
        roll = random.random()
        if roll > prob:
            return level
        prob -= decrement
    return max_levels

def normalize_value(x, min_val, max_val, a, b):
    if min_val == max_val:
        return a
    return a + ((x - min_val) / (max_val - min_val)) * (b - a)

def run_randomization(a, b, decrement=0.0001):
    max_levels = round(1 / decrement)
    level_reached = probability_tree(max_levels, decrement=decrement)
    normalized_value = normalize_value(level_reached, 1, max_levels, a, b)
    return level_reached, normalized_value

def random_used_value(a, b, decrement=0.0001, increment=5):
    _, normalized = run_randomization(a, b, decrement)
    return normalized * increment

class Plant:
    def __init__(self):
        self.name = ''
        self.species = ''
        self.plant_type = ''
        
        # Numeric attributes
        self.hp = 0
        self.attack = 0
        self.armor = 0
        self.smart = 0
        self.speed = 0
        self.luck = 0

    def build_name(self, length=6):
        vowels = list('aeiou')
        consonants = list('bcdfgjklmnpqrstv')
        name = []

        for _ in range(length // 2):
            name.append(random.choice(consonants))
            name.append(random.choice(vowels))
        
        self.name = ''.join(name).capitalize()
    
    def build_names(self):
        self.species = random.choice([
    "Acacia dealbata", "Acer palmatum", "Achillea millefolium", "Adiantum raddianum", "Agave americana",
    "Albizia julibrissin", "Allium schoenoprasum", "Aloe vera", "Amaranthus caudatus", "Ananas comosus",
    "Antirrhinum majus", "Aphelandra squarrosa", "Aquilegia vulgaris", "Arabidopsis thaliana", "Artemisia absinthium",
    "Asparagus officinalis", "Aster novi-belgii", "Azadirachta indica", "Azalea indica", "Bambusa vulgaris",
    "Begonia semperflorens", "Bellis perennis", "Berberis vulgaris", "Beta vulgaris", "Bixa orellana",
    "Brassica oleracea", "Calendula officinalis", "Calla palustris", "Camellia japonica", "Capsicum annuum",
    "Carica papaya", "Cassia fistula", "Catharanthus roseus", "Cattleya labiata", "Ceiba pentandra",
    "Centaurea cyanus", "Chamaedorea elegans", "Chamomilla recutita", "Chrysanthemum morifolium", "Citrus sinensis",
    "Clematis vitalba", "Clivia miniata", "Cocos nucifera", "Coffea arabica", "Colocasia esculenta",
    "Convallaria majalis", "Coreopsis tinctoria", "Cornus florida", "Crocus sativus", "Cucurbita pepo",
    "Cyclamen persicum", "Cymbidium hybrid", "Dahlia pinnata", "Datura stramonium", "Delphinium elatum",
    "Dianthus caryophyllus", "Digitalis purpurea", "Dionaea muscipula", "Dracaena fragrans", "Drosera capensis",
    "Echinacea purpurea", "Eichhornia crassipes", "Epipremnum aureum", "Equisetum arvense", "Eryngium planum",
    "Eucalyptus globulus", "Euphorbia pulcherrima", "Fagus sylvatica", "Ficus benjamina", "Foeniculum vulgare",
    "Fuchsia hybrida", "Gardenia jasminoides", "Ginkgo biloba", "Gleditsia triacanthos", "Glycine max",
    "Helianthus annuus", "Helleborus niger", "Hibiscus rosa-sinensis", "Hosta sieboldiana", "Hoya carnosa",
    "Hyacinthus orientalis", "Hydrangea macrophylla", "Hypericum perforatum", "Ilex aquifolium", "Impatiens walleriana",
    "Ipomoea purpurea", "Iris germanica", "Jasminum officinale", "Kalanchoe blossfeldiana", "Lactuca sativa",
    "Lantana camara", "Lavandula angustifolia", "Lilium candidum", "Liriodendron tulipifera", "Lonicera japonica",
    "Lotus corniculatus", "Magnolia grandiflora", "Malus domestica", "Mentha spicata", "Monstera deliciosa"
])
        self.plant_type = random.choice(["Tropical", "Desert", "Aquatic", "Mountain", "Cave"])
        self.build_name()

    def build_numbers_attributs(self, max_bounds, inc):
        self.hp = 100
        self.armor = random_used_value(1, self.hp)
        self.smart = random_used_value(1, max_bounds, inc)
        self.speed = random_used_value(1, max_bounds, inc)
        self.luck = random.uniform(0, max_bounds)
        self.attack = (2*self.armor + self.speed*1.5 + self.luck*0.3 + self.hp*0.4 + self.smart) / (2+1.5+0.3+0.4+1)

    def overall(self):
        total = self.hp + self.armor + self.smart + self.speed + self.luck + self.attack
        return total / 6


    def display(self):
        print("🌿 === PLANT MONSTER CARD === 🌿")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Plant Type: {self.plant_type}")
        print('')
        print("💥 Attributes:")
        print(f"HP     : {self.hp}")
        print(f"Armor  : {self.armor:.2f}")
        print(f"Smart  : {self.smart:.2f}")
        print(f"Speed  : {self.speed:.2f}")
        print(f"Luck   : {self.luck:.2f}")
        print(f"Attack : {self.attack:.2f}")
        print(f'Overall: {self.overall()}')

class Battle:
    def __init__(self, plant1, plant2,
                 max_turns=100,                # Número máximo de turnos antes de declarar empate
                 luck_factor=10,               # Quanto maior, menor o impacto da sorte na esquiva
                 miss_cap=0.9,                 # Limite máximo de chance de esquiva (ex: 90%)
                 attack_scale=1,               # Escala de dano com base no valor de ataque
                 damage_variation=(1-0.15, 1+0.15) # Variação aleatória do dano (mínimo, máximo)
                ):
        
        self.p1 = plant1              # Primeira planta combatente
        self.p2 = plant2              # Segunda planta combatente
        self.hp1 = plant1.hp          # Vida inicial baseada no atributo da planta
        self.hp2 = plant2.hp          # Vida inicial baseada no atributo da planta
        self.max_turns = max_turns    # Limite de turnos antes de empate
        self.luck_factor = luck_factor# Fator que define como a sorte afeta a esquiva
        self.miss_cap = miss_cap      # Chance máxima de esquiva
        self.attack_scale = attack_scale  # Escala que define o peso do atributo 'attack'
        self.damage_variation = damage_variation  # Faixa de variação aleatória do dano
        self.turn_log = []            # Log de eventos por turno
        self.winner = None            # Planta vencedora (definida após a batalha)

    def attack_success(self, defender_luck):
        dodge_chance = min(defender_luck / self.luck_factor, self.miss_cap)
        return random.random() > dodge_chance

    def calculate_damage(self, attack_value):
        variation = random.uniform(*self.damage_variation)
        return attack_value * variation * self.attack_scale

    def fight(self):
        print("⚔️ The Battle Begins!\n")
        attacker, defender = self.p1, self.p2
        hp_a, hp_d = self.hp1, self.hp2
        turn = 1

        while self.hp1 > 0 and self.hp2 > 0 and turn <= self.max_turns:
            print(f"--- Turn {turn} ---")
            if self.attack_success(defender.luck):
                dmg = self.calculate_damage(attacker.attack)
                hp_d -= dmg
                hp_d = max(0, hp_d)
                self.turn_log.append(f"{attacker.name} hit {defender.name} for {dmg:.2f} damage!")
                print(f"{attacker.name} hit {defender.name} for {dmg:.2f} damage!")
            else:
                self.turn_log.append(f"{attacker.name} missed the attack!")
                print(f"{attacker.name} missed the attack!")

            # Swap roles for next turn
            attacker, defender = defender, attacker
            hp_a, hp_d = hp_d, hp_a
            turn += 1

            # Update global HP values
            if attacker == self.p1:
                self.hp1 = hp_a
                self.hp2 = hp_d
            else:
                self.hp2 = hp_a
                self.hp1 = hp_d

            print(f"HP: {self.p1.name} = {self.hp1:.1f}, {self.p2.name} = {self.hp2:.1f}\n")

        # Determine winner
        if self.hp1 <= 0 and self.hp2 <= 0:
            self.winner = None
            print("💀 Both plants fainted! It's a draw!")
        elif self.hp1 <= 0:
            self.winner = self.p2
            print(f"🏆 {self.p2.name} wins!")
        elif self.hp2 <= 0:
            self.winner = self.p1
            print(f"🏆 {self.p1.name} wins!")
        else:
            print("⏳ Max turns reached!")
            if self.hp1 > self.hp2:
                self.winner = self.p1
                print(f"🏆 {self.p1.name} wins by HP!")
            elif self.hp2 > self.hp1:
                self.winner = self.p2
                print(f"🏆 {self.p2.name} wins by HP!")
            else:
                self.winner = None
                print("⚖️ It's a draw by HP!")