import json

class Expert:
    def __init__(self, kb_path, dialogue_path):
        self.kb_path = kb_path
        self.dialogue_path = dialogue_path
        with open(self.kb_path) as kb_file:
            self.kb = json.load(kb_file)
        with open(self.dialogue_path) as d_file:
            self.dialogue = json.load(d_file)

    def start(self):
        keep_going = True
        print(self.dialogue["intro"] )
        while keep_going:
            r1 = input(f'\n{self.dialogue["q1"]}\n').lower()
            r2 = 1 if input(f'\n{self.dialogue["q2"]}\n').lower()[0] == "y" else 0
            print(r2)
            print(r1)

            # create key from input

            # get fruit dictionary from key

            # if the key exists print the fruit name

            # else tell the user the fruit was not found and to ask for the name of the fruit

                # base on the user input create a dictionary and add it to the in memory dictionary with the fruit key

                # write the in memory dictionary to file.

                
            keep_going = input(f'{self.dialogue["repeat"]}\n').upper()[0] == "Y"

        print(f'\n{self.dialogue["farewell"]}')    



def main():
    pass

if __name__ == "__main__":
    main()