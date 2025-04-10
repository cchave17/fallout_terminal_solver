def calculate_likeness(word1, word2):
    """
    Calculate the likeness between two words, defined as the number of positions where the letters are identical.
    """
    if len(word1) != len(word2):
        return 0
    
    return sum(1 for a, b in zip(word1, word2) if a == b)

def update_possible_words(possible_words, guessed_word, likeness):
    """
    Update the list of possible words by keeping only those with the same likeness score to the guessed word.
    """
    return [word for word in possible_words if calculate_likeness(word, guessed_word) == likeness]

def main(test_mode=False):
    print("\n===== FALLOUT 4 TERMINAL HACKING SOLVER =====\n")
    print("Instructions:")
    print("1. Enter all possible passwords from the game as a comma-separated list.")
    print("2. For each guess, enter the word you tried and the likeness score received.")
    print("3. The program will narrow down the possible passwords until the solution is found.\n")
    
    # Test mode with predefined inputs for non-interactive environments
    if test_mode:
        print("RUNNING IN TEST MODE WITH SAMPLE DATA")
        possible_words = ["APPLE", "MAPLE", "AMPLE", "TABLE"]
        print(f"Sample passwords: {', '.join(possible_words)}")
        
        # Simulate first guess
        guessed_word = "APPLE"
        likeness = 2  # Let's say the likeness is 2
        print(f"\nGuessed: {guessed_word}, Likeness: {likeness}")
        
        possible_words = update_possible_words(possible_words, guessed_word, likeness)
        print(f"Updated possible words: {', '.join(possible_words)}")
        
        # Simulate second guess if needed
        if len(possible_words) > 1:
            guessed_word = possible_words[0]
            likeness = 3  # Let's say the likeness is 3
            print(f"\nGuessed: {guessed_word}, Likeness: {likeness}")
            
            possible_words = update_possible_words(possible_words, guessed_word, likeness)
            print(f"Updated possible words: {', '.join(possible_words)}")
        
        # Final result
        if len(possible_words) == 0:
            print("\nNo possible solution exists. This may be due to inconsistent input.")
        elif len(possible_words) == 1:
            print(f"\nSolution found: {possible_words[0]}")
        else:
            print(f"\nRemaining possible words: {', '.join(possible_words)}")
            
        return
    
    # Interactive mode
    # Get initial list of possible passwords
    while True:
        try:
            passwords_input = input("Enter all possible passwords (comma-separated): ").strip().upper()
            possible_words = [word.strip() for word in passwords_input.split(",")]
            
            # Validate input: check all words have same length and contain only letters
            if not possible_words:
                print("Error: No passwords entered. Please try again.")
                continue
                
            word_length = len(possible_words[0])
            invalid_words = [word for word in possible_words if len(word) != word_length or not word.isalpha()]
            
            if invalid_words:
                print(f"Error: All passwords must have the same length and contain only letters.")
                print(f"Invalid words: {', '.join(invalid_words)}")
                continue
            
            break
        except Exception as e:
            print(f"Error: {e}. Please try again.")
    
    # Main loop for guessing
    while len(possible_words) > 1:
        print(f"\nPossible passwords ({len(possible_words)}):")
        for i, word in enumerate(possible_words, 1):
            print(f"{i}. {word}", end="\t")
            if i % 5 == 0:
                print()  # New line after every 5 words
        print("\n")
        
        # Get guessed word and likeness score
        while True:
            try:
                guessed_word = input("Enter word you guessed: ").strip().upper()
                
                if guessed_word not in possible_words:
                    print(f"Error: '{guessed_word}' is not in the list of possible passwords.")
                    continue
                
                likeness = int(input("Enter likeness score received: "))
                
                if likeness < 0 or likeness > len(guessed_word):
                    print(f"Error: Likeness score must be between 0 and {len(guessed_word)}.")
                    continue
                
                break
            except ValueError:
                print("Error: Likeness score must be a number. Please try again.")
        
        # Update list of possible words
        possible_words = update_possible_words(possible_words, guessed_word, likeness)
        
        # Check if solution is found or no solutions remain
        if len(possible_words) == 0:
            print("\nNo possible solution exists. This may be due to inconsistent input.")
            break
        elif len(possible_words) == 1:
            print(f"\nSolution found: {possible_words[0]}")
            break
 
# FROST,GRASP,TRUST,CRUST,BLAST,FRESH,GRIND,BRUSH,TRASH,FLUSH 


if __name__ == "__main__":
    main(test_mode=False)
    
    