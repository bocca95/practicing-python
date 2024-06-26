import random

def choosing_word():

    with open(r"exercicios\dicionario.txt", "r", encoding="utf-8") as arquivo:
        dictionary = arquivo.readlines()

    dictionary = [line.strip() for line in dictionary]
    dictionary_size = len(dictionary)
    chosen_word = dictionary[random.randint(0, dictionary_size-1)]
    word_size = len(chosen_word)
    return chosen_word, int(word_size)

def game_logic():
    
    chosen_word, chosen_word_size = choosing_word()
    chosen_word = list(chosen_word)
    cloned_chosen_word = chosen_word[:]
    print(chosen_word)
    mistakes, attempts = 0,0
    players_word = [ '_' for i in range(chosen_word_size)]
    vowels = ['a', 'e', 'i', 'o', 'u']
    fh_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm']
    sh_consonants = ['n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']
    
    missing_vowels, missing_fhconsonants, missing_shconsonants, correct_letters = False, False, False, 0
    while True:
        
        players_input = input("Escolha uma letra para tentar adicionar a palavra: ")
        if players_input not in chosen_word:
            mistakes+=1
        if mistakes == 1:
            if correct_letters > 0:
                print(f'{players_word}')
            else: print(['_' for i in range(chosen_word_size)])
        if mistakes == 2:
            for i in range(len(vowels)):
                if vowels[i] in cloned_chosen_word:
                    missing_vowels = True
            for i in range(len(fh_consonants)):
                if fh_consonants[i] in cloned_chosen_word:
                    missing_fhconsonants = True
            for i in range(len(sh_consonants)):
                if sh_consonants[i] in cloned_chosen_word:
                    missing_shconsonants = True
            if missing_vowels and missing_shconsonants and missing_fhconsonants:
                print(f"Ainda faltam vogais e consoantes.")
            elif missing_vowels and missing_fhconsonants:
                print(f"Ainda faltam vogais e consoantes da primeira metade do alfabeto.")
            elif missing_vowels and missing_shconsonants:
                print(f"Ainda faltam vogais e consoantes da segunda metade do alfabeto.")
            elif missing_shconsonants and missing_fhconsonants:
                print(f"Faltam apenas consoantes")
            elif missing_fhconsonants:
                print(f"Faltam consoantes da primeira metade do alfabeto.")
            elif missing_shconsonants:
                print(f"Faltam consoantes da segunda metade do alfabeto.")
            elif missing_vowels:
                print(f"Faltam apenas vogais!")
        if mistakes == 3:
            print(f"Você perdeu! A palavra era: {''.join(chosen_word)}")
            break
        if players_input in chosen_word:
            for i in range(chosen_word_size):
                for char in chosen_word:
                    if chosen_word[i] == players_input:
                        players_word[i] = players_input
                        correct_letters +=1
                        cloned_chosen_word[i] = ''
            print(f"A letra: {players_input} está na palavra!")
        attempts+=1
        
        if players_word == chosen_word or players_input == '-':
            print(f"Você acertou em {attempts} tentaivas!\nTambém possuiu {mistakes} erros! Bom trabalho!")
            break
if __name__ == '__main__':
    game_logic()