import openai, os, sys, time
from pygui import GUI
#TODO: "Do the comments and documentations"
def clear():
    os.system('cls')

def separator():
    print(120*'-')

class ChatGPT3:
    def __init__(self,mode) -> None:
        if(mode=='Application'):
            self.gui = 'yes'
        else:
            self.gui = 'no'
        self.grammar_checker = {'ENGLISH':'translate to english: "{}"'}
        self.translate = {'TRANSLATE':'translate to spanish: "{}"'}
        self.use = {'USES':'how to use the phrase "{}"'}
        self.synonyms = {'SYNONYMS':'synonyms of "{}"'}
        self.tenses = {'TENSES':'all tenses for verb "{}"'}
        self.examples_tenses = {'EXAMPLES TENSES':'all examples tenses for verb "{}"'}
        self.is_noun = {'TYPE':'is "{}" a noun?'}
        self.extended = [self.use,self.tenses,self.examples_tenses]
        self.types = [self.translate,self.synonyms]

    def askGPT3(self,text='',is_text=False,_print=None):
        _input = text.replace('translate to english:','')
        if(is_text):
            print('Your input: \n %s \n' %_input)
            separator()
        if(_print is not None):
            print(_print)
        response = openai.Completion.create(
        engine="text-davinci-003",
        temperature=0.5,
        prompt=text,
        max_tokens=250
        )
        return response.choices[0].text.strip()

    def translator(self):
        errors = ['This is not','Sorry,','is not a','No problem.']
        clear()
        while True:
            print('\n')
            separator()
            text = input('\nEnter your text: \n')
            if(text=='exit'):
                exit()
            elif(text=='menu'):
                self.start()
            elif(len(text.split(' '))==1):
                clear()
                out = str(self.askGPT3(self.is_noun['TYPE'].format(text)))
                is_word = str(self.askGPT3(self.grammar_checker['ENGLISH'].format(text))).strip()
                if(is_word in errors or is_word.__contains__(errors[0]) or is_word.__contains__(errors[1]) or is_word.__contains__(errors[2])):
                    print(is_word)
                    time.sleep(1.333)
                    self.translator()
                if(out.upper().__contains__('YES')):
                    noun = True
                    out = out.replace('Yes, ','')
                else:
                    noun = False
                    out = out.replace('No, ', '')
                    out = out.replace('is not a noun. It ', '')
                out = {'TYPE':out}
                print('     ** {} **'.format(list(out.keys())[0]))
                print(out['TYPE'])
                if(not noun):#TODO: what happends when not is an verb and not is a noun , like adjetive for instance. 
                    self.types.extend(self.extended)
                for _type in self.types:
                    separator()
                    print('     ** {} **'.format(list(_type.keys())[0]))
                    translation = list(_type.values())[0].format(text)
                    print(self.askGPT3(translation))
                if(not noun):
                    del self.types[-1], self.types[-1],self.types[-1]
            elif(len(text.split(' '))>1):
                clear()
                grammar = self.grammar_checker['ENGLISH'].format(text)
                msg=' ** ENGLISH CORRECTION **'
                print(self.askGPT3(grammar,is_text= True,_print=msg))
                msg=' ** SPANISH **'
                translate =  self.translate['TRANSLATE'].format(text)
                print(self.askGPT3(translate,_print=msg))

    def chat_gpt3(self):
        clear()
        while True:
            separator()
            text = input('Enter your text: \n')
            if(text=='exit'):
                exit()
            if(text=='menu'):
                self.start()
            clear()
            print(self.askGPT3(text,is_text=True))

    def check_grammar(self):
        clear()
        CHECK = 'is correct: "{}"'
        while True:
            separator()
            text = input('Enter your text: \n')
            if(text=='exit'):
                exit()
            elif(text=='menu'):
                self.start()
            clear()
            to_check = CHECK.format(text)
            print(self.askGPT3(to_check,is_text=True))

    def start(self):
        if(self.gui == 'yes'):
            self.gui = GUI('CHAT GPT3','What are you wanna do today?')
        else:
            clear()
            user_input = str(input("What are you gonna do to day?: \n        ** Options**  \n [1] translate \n [2] ask something to chatgpt 3 \n [3] check your grammar \n [4] exit \n [*] menu [write 'menu'] \n Answer: "))
            _input = user_input.upper()
            while(_input != '1' or _input != '2' or _input != '3' or _input != '4'):
                if(_input.__contains__('1')):
                    self.translator()
                elif(_input.__contains__('2')):
                    self.chat_gpt3()
                elif(_input.__contains__('3')):
                    self.check_grammar()
                elif(_input.__contains__('4')):
                    exit()
                elif(_input.__contains__('MENU')):
                    self.start()
                else:
                    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nPlease insert a valid option !!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    time.sleep(1.333333)
                    clear()
                    user_input = str(input("What are you gonna do to day?: \n        ** Options**  \n [1] translate \n [2] ask something to chatgpt 3 \n [3] check your grammar \n [4] exit \n [*] menu [write 'menu'] \n Answer: "))
                _input = user_input.upper()

if(__name__ == '__main__'):
    key = sys.argv[1]
    openai.api_key = key
    gui = GUI('Chat GPT3 mode','How would you like to work?','initial')
    mode = str(gui.event)
    del gui
    chat_gpt3 = ChatGPT3(mode)
    clear()
    chat_gpt3.start()
