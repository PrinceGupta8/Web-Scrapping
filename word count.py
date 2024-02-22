def count_word_in_file(file_path):
    try:
        with open(file_path,'r') as file:
            content=file.read()
            word_count=len(content.split())
            return word_count
    except FileNotFoundError:
      print("file not found")
    return -1
if __name__=="__main__":
    try:
        file_path=input("Enter the path of the file:")
        num_words=count_word_in_file(file_path)
        if num_words >=0:
            print(f"Number of words in the file:{num_words}")
    except KeyboardInterrupt:
        print('prograqm interruption')
    except Exception as e:
        print(f"an error occured:{e}")
                  
               

  

        

    










