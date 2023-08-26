STRING = input("string: ").strip().lower()
VOWELS_IN_STRING = (
    STRING.count("a")
    + STRING.count("e")
    + STRING.count("i")
    + STRING.count("o")
    + STRING.count("u")
    + STRING.count("á")
    + STRING.count("é")
    + STRING.count("í")
    + STRING.count("ó")
    + STRING.count("ú")
)

print(len(STRING)*VOWELS_IN_STRING)

# Alternative for counting vowels: sum(map(STRING.count, "aeiouáéíóú"))
