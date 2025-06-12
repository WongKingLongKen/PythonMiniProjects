from art import logo

print(logo)

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def caesar(original_text, shift_amount, encode_or_decode):
    shift_amount %= len(alphabet)
    if encode_or_decode == "decode":
        shift_amount *= -1

    output_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' to go again. Otherwise type 'no':\n").lower()
    if restart != 'yes':
        should_continue = False
        print("Goodbye!")
