from my_stegano import encode_text_to_image, decode_text_from_image

def make_a_picture():
    image_path = input("Enter image path (F:/sadra/image_code/homer.png) :")
    text = input("Enter image text: ")
    output = input("Enter the filename to save the output image (e.g. output): ")
    output_path = 'F:/sadra/image_code/' + output + '.png'
    encode_text_to_image(image_path, text, output_path)

def see_a_picture():
    img_path = input("Enter image name (its in: F:/sadra/image_code):  ")
    decoded = decode_text_from_image('F:/sadra/image_code/' + img_path + '.png')
    print("text decoded: ")
    print(decoded)


def main():
    while True:
        print("------image program------")
        print("Make a picture: 1")
        print("see a picture: 2")
        print("------------------------")
        choice = input("Enter your choice:  ")
        
        try:
            if choice == "1":
                make_a_picture()
                
            elif choice == "2":
                see_a_picture()
                
            else:
                print('')
                print("You stupid. 1 or 2 idiot.")
                print('')
                continue
                
        except Exception as e:
            print(f"Error: {e}")
            break
        
        while True: 
            print("--------------------------------")
            print('Do you wanna do again? (Yes/No)')
            answer = input().strip().upper()
            
            if answer == "YES" or answer == "Y":
                break
            elif answer == "NO" or answer == "N":
                print("Bye. I hope you have a great day!")
                return
            else:
                print("Unknown word. try again")

    
if __name__ == "__main__":
    main()
