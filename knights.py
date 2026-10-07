from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Every person is exactly one of knight / knave
def kind(K, N):
    return And(Or(K, N), Not(And(K, N)))

# Puzzle 0: A says "I am both a knight and a knave."
s0 = And(AKnight, AKnave)
knowledge0 = And(
    kind(AKnight, AKnave),
    Implication(AKnight, s0),
    Implication(AKnave, Not(s0))
)

# Puzzle 1: A says "We are both knaves."
s1 = And(AKnave, BKnave)
knowledge1 = And(
    kind(AKnight, AKnave),
    kind(BKnight, BKnave),
    Implication(AKnight, s1),
    Implication(AKnave, Not(s1))
)

# Puzzle 2: A says "We are the same kind." B says "We are of different kinds."
same = Or(And(AKnight, BKnight), And(AKnave, BKnave))
diff = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    kind(AKnight, AKnave),
    kind(BKnight, BKnave),
    Implication(AKnight, same),
    Implication(AKnave, Not(same)),
    Implication(BKnight, diff),
    Implication(BKnave, Not(diff))
)

# Puzzle 3 (bonus)
# A's actual statement depends on their identity: 
# If A is a Knight, they say "I am a knight" (True). If A is a Knave, they still say "I am a knight" (False).
# Therefore, what A actually says is always equivalent to: Implication(AKnight, AKnight) and Implication(AKnave, Not(AKnight))
a_said_knight = Biconditional(AKnight, AKnight)
a_said_knave = Biconditional(AKnight, AKnave)

knowledge3 = And(
    kind(AKnight, AKnave),
    kind(BKnight, BKnave),
    kind(CKnight, CKnave),
    
    # B says "A said 'I am a knave'."
    Biconditional(BKnight, a_said_knave),
    
    # B says "C is a knave."
    Biconditional(BKnight, CKnave),
    
    # C says "A is a knight."
    Biconditional(CKnight, AKnight)
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3 (bonus)", knowledge3),
    ]
    for name, knowledge in puzzles:
        print(name)
        if len(knowledge.conjuncts) == 0:
            print("  Not yet implemented.")
            continue
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"  {symbol}")

if __name__ == "__main__":
    main()
