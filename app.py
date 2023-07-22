import openai

# Use OpenAI API Key
openai.api_key= "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"

# Ask the user for question
while True:
    print()
    print()
    
    print("\t\t\t============================================================")
    print("\t\t\tWELCOME TO YOUR MINI CHATGTP ")
    print("\t\t\t============================================================")
    question = input("\t\t\tWhat would you Like to ask OpenAI (or q to quit)?")
    print("\t\t\t============================================================")
    print("\t\t\t============================================================")

    
    if question == '' or question == 'q':
        print("\t\t\tThank for using CHATGPT ")
        print("\t\t\t==========================================================")
        break
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.8,
    )
    #clear

    print()
    print()

    answer = response["choices"][0][ "text"]
    print("OpenAI:" + answer)
