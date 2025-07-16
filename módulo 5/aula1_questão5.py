import emoji

print("\nEmojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

frase = input("\nDigite uma frase e ela será emojizada: ")
frase_emojizada = emoji.emojize(frase, language='alias')

print("Frase emojizada:")
print(frase_emojizada)