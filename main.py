print("Приветствую вас, вы попали в программу - объяснялку")
for i in range(5):
    meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "Шутка",
            "ЩИЩ": "Одобрение или восторг",
            "КРИПОВЫЙ": "Страшный, пугающий",
            "АГРИТЬСЯ": "Злиться"
            }
    print("")
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print("")
        print(word, "-" , meme_dict[word])
    else:
        print("")
        print("К сожалению в базе данных такое слово не найдено")
