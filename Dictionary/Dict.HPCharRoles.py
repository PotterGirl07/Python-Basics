characters = {
    "James": "Harry's father + member of the Order",
    "Lily": "Harry's mother who protects him through her sacrifice",
    "Sirius": "Harry's brave + loyal godfather, who is misunderstood + wrongly imprisoned",
    "Harry": "The main brave hero who faces many challenges + fights Voldemort",
    "Hermione": "Harry's intelligent + hardworking best friend",
    "Ron": "Harry's funny + brave best friend",
    
    "Dumbledore": "Hogwarts' wise headmaster + the only wizard Voldemort fears",
    "McGonagall": "Strict but fair Transfiguration professor + head of Gryffindor",
    "Hagrid": "Hogwarts groundskeeper who introduces Harry to the wizarding world",
    "Lupin": "3rd + best Defense Against the Dark Arts(DADA) professor",
    "Slughorn": "6th year Potions professor who favors students with connections to famous/influential people",
    "Snape": "Potions then 6th DADA professor with a complicated past + head of Slytherin", 
    "Quirrell": "1st DADA professor who secretly lets Voldemort use hsi body to live",
    "Umbridge": "5th + worst DADA professor, a Ministry official who interferes with Hogwarts",

    "Ginny": "Ron's younger sister + a talented, confident, + sassy witch",
    "Neville": "A shy/clumsy student later a brave/skilled wizard who helps defeat Voldemort",
    "Luna": "An unusual Ravenclaw student + a loyal friend to Harry",
    "Dobby": "House-elf who repeatedly helps Harry",
    "Kreacher": "House-elf who serves the Black family",

    
    "Voldemort": "Main dark villain who seeks power + immortality",
    "Bellatrix": "Devoted follower of Voldemort who enjoys using dark magic",
    "Peter": "Coward, Betrays Harry's parents to Voldemort + later helps to rise to power",
    "Lucius": "A wealthy + influential Death Eater who is Draco's father + supports Voldemort",
    "Draco": "Harry's rival who is later forced to be Death Eater"
}
print("Harry Potter Main Characters Roles")
for i in range (30):
    print("James, Lily, Sirius, Harry, Hermione, Ron")
    print("Dumbledore, McGonagall, Hagrid, Lupin, Slughorn, Snape, Quirrell, Umbridge")
    print("Ginny, Neville, Luna, Dobby, Kreacher")
    print("Voldemort, Bellatrix, Peter, Lucius, Draco")
    name = input("Enter a character's name to see their role: ").title()
    print("~" *50)

    if name in characters:
        print(f"You chose: {name}")
        print("Here is a short summary about them: ")
        print(f"{characters[name]}")
        print("~" *50)
    else:
        print("Character not found, try again.")