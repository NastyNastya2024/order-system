import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_english_words():
    url = "https://randomword.com/"
    translator = Translator()
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an error for bad responses
        soup = BeautifulSoup(response.content, "html.parser")

        # Fetching the random English word and its definition
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Translating the word and its definition to Russian
        translated_word = translator.translate(english_word, dest="ru").text
        translated_definition = translator.translate(word_definition, dest="ru").text

        return {
            "english_word": english_word,
            "translated_word": translated_word,
            "word_definition": word_definition,
            "translated_definition": translated_definition
        }

    except requests.exceptions.RequestException as e:
        print("Произошла ошибка при получении данных:", e)
        return None


def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            break  # Exit if there's an error fetching words

        word = word_dict.get("english_word")
        translated_word = word_dict.get("translated_word")
        word_definition = word_dict.get("word_definition")
        translated_definition = word_dict.get("translated_definition")

        print(f"Значение слова (англ): {word_definition}")
        print(f"Значение слова (рус): {translated_definition}")
        user = input("Что это за слово? ")

        if user.lower() == word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово: {word} ({translated_word})")

        play_again = input("Хотите сыграть еще раз? (y/n): ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    word_game()


