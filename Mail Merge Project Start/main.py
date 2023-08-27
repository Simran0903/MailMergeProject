PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_start:
    content=letter_start.read()
for name in names:
    stripped_letter = name.strip()
    letter=content.replace(PLACEHOLDER,stripped_letter)
    with open(f"./Output/ReadyToSend/Letter_for_{stripped_letter}.txt","w") as new_letter:
        new_letter.write(letter)
