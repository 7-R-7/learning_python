the_file = None

the_tries = 5

while the_tries > 0 :
    try :
        print("Enter The File Name With Absolute PAth To Open")
        print(f"You Have {the_tries} Tries Left")
        print("Example: /home/arg/Desktop/python/file.ext")
        file_name_and_path = input("File Name => : ").strip()
        the_file = open(file_name_and_path, 'r')
        print(the_file.read())
        break
    except FileNotFoundError:
        print("File Not Found Please Be Sure The Name is Valid")
        the_tries -= 1
    except:
        print("Error Happen")
    finally:
        if the_file is not None:
            the_file.close()
            print("File Closed.")

else:
    print("All Tries Is Done")
