def count_word_frequency(words):
    word_frequency={}
    for word in words:
        word_frequency[word]=word_frequency.get(word,0)+1
    return word_frequency   
def display_word_frequency(word_frequency):
    print("word frequency")
    for word,count in word_frequency.items():
        print(f"{word}:{count}")
if __name__=="__main__":
    try:
        file_path=input("Enter the path of the text file:")
        text= file_path
        if text:
            words=text
            word_frequency=count_word_frequency(words)
            display_word_frequency(word_frequency)
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    except Exception as e:
        print(f"An error occured:{e}")