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
    mistakes, attempts = 0, 0
    players_word = ['_' for _ in range(chosen_word_size)]
    vowels = ['a', 'e', 'i', 'o', 'u']
    fh_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm']
    sh_consonants = ['n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']
    
    correct_letters = 0
    while True:
        player_input = input("Escolha uma letra para tentar adicionar a palavra: ").lower()
        
        if len(player_input) != 1 or not player_input.isalpha():
            print("Entrada inválida! Por favor, insira uma única letra.")
            continue
        
        if player_input not in chosen_word:
            mistakes += 1
        if mistakes == 1:
            print(players_word if correct_letters > 0 else ['_' for _ in range(chosen_word_size)])
        if mistakes == 2:
            missing_vowels = any(vowel in cloned_chosen_word for vowel in vowels)
            missing_fhconsonants = any(consonant in cloned_chosen_word for consonant in fh_consonants)
            missing_shconsonants = any(consonant in cloned_chosen_word for consonant in sh_consonants)
            
            if missing_vowels and missing_shconsonants and missing_fhconsonants:
                print("Ainda faltam vogais e consoantes.")
            elif missing_vowels and missing_fhconsonants:
                print("Ainda faltam vogais e consoantes da primeira metade do alfabeto.")
            elif missing_vowels and missing_shconsonants:
                print("Ainda faltam vogais e consoantes da segunda metade do alfabeto.")
            elif missing_shconsonants and missing_fhconsonants:
                print("Faltam apenas consoantes.")
            elif missing_fhconsonants:
                print("Faltam consoantes da primeira metade do alfabeto.")
            elif missing_shconsonants:
                print("Faltam consoantes da segunda metade do alfabeto.")
            elif missing_vowels:
                print("Faltam apenas vogais!")
        if mistakes == 3:
            print(f"Você perdeu! A palavra era: {''.join(chosen_word)}")
            break
        if player_input in chosen_word:
            for i in range(chosen_word_size):
                if chosen_word[i] == player_input:
                    players_word[i] = player_input
                    correct_letters += 1
                    cloned_chosen_word[i] = ''
            print(f"A letra: {player_input} está na palavra!")
        attempts += 1
        
        if players_word == chosen_word or player_input == '-':
            print(f"Você acertou em {attempts} tentativas!\nTambém teve {mistakes} erros! Bom trabalho!")
            break

if __name__ == '__main__':
    game_logic()
