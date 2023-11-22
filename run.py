import llm
import random
from improv import Scene
class ConversationEngine(object):

    INITIAL_PROMPT = """*** %(title)s ***
Welcome to "%(title)s", a murder mystery role-playing game where you play the role of the detective. Late at night, you are called to the scene of a murder. %(description)s
%(text)s

People in this city are known for cryptic comments, and this statement surely has some bearing on the case. It's your job to uncover the hidden meaning behind what is being said here. You need to determine who is a witness, who is a suspect... and who is the killer. With an eye towards getting to the bottom of the mystery, you begin your investigation.

[This is a free-form text adventure. Write out your actions and dialogue, and also write the characters' responses. Always write in the first person. Write in %(genre)s. Do not recapitulate or summarize the events that are narrated to you. You are role-playing, so fill in details yourself rather than asking for clarification.]"""
    
    def __init__(self, knowledge, llm_model):
        self.knowledge = knowledge
        if isinstance(llm_model, str):
            self.model = llm.get_model(llm_model)
        else:
            self.model = llm_model
        self.conversation = self.model.conversation()
        self.prompts = []
        self.scene = Scene()
        self.final_round = False
        
    def run(self):
        prompt = self.generate_prompt()
        print("<STORY>")
        print(prompt)
        print("\n")
        print("<DETECTIVE>")
        response = self.conversation.prompt(prompt)
        text = response.text()
        print(text)
        print("\n")
        self.prompts.append((response, text))
        return response
            
    def generate_prompt(self):
        self.round_number = len(self.conversation.responses)
        if self.round_number == 0:
            return self.first_round_prompt()
        action = self.world_action_prompt()
        return action + "\n"

    def first_round_prompt(self):
        genre = random.choice(
            ["a hard-boiled style", "a whimsical and comedic style", "a neo-noir style", "a cyberpunk style",
             "in the style of a thriller", "in the style of a supernatural mystery", "the style of the Sherlock Holmes mysteries",
             "the style of Agatha Christie",]
        )
        
        # Start off with a properly morbid seed.
        seed = random.choice(["murder", "death", "innocent", "victim", "guity"])
        prompt_word, prompt_chain = self.knowledge.query(seed)
        prompt = " ".join(prompt_chain)
        text = "\n".join([x for x in self.scene.say(prompt)])

        return self.INITIAL_PROMPT % dict(
            genre=genre,
            description=self.scene.describe(),
            text=text,
            title=self.scene.case_name,
        )

    def generate_nudge(self):
        if self.round_number >= 10:
            self.final_round = True
            return "Unfortunately, detective, you're out of time to solve this case. You need to sum it up. Who is most likely to have committed the crime, and how?"
        if random.random() < 0.5:
            return "What's your next move, detective?"
        if random.random() < 0.5:
            a = random.randint(1,5)
            if a == 1:
                extra = "That sounds fishy; you'd better hone in on that statement."
            elif a == 2:
                extra = "You're not here to coddle these suspects... you need answers!"
            elif a == 3:
                extra = "That could be a legitimate alibi... or a slick cover-up."
            elif a == 4:
                extra = "That seems clear enough, but you have just one more question."
            else:
                extra = "You think you know who committed the crime... but you're not sure how."
            return extra + " What's your next move, detective?"

        a = random.randint(1,3)
        if a == 1:
            return "You decide to take stock of what you know so far. Who are the suspects? What do you have in the way of means, motive, and opportunity?"
        elif a == 2:
            return "This is a tricky case, but you have a few leads. You take out your notebook and begin to put together the scattered pieces of the clues you've found so far."
        else:
            return "You consider the various characters you've encountered so far, evaluating their alibis to see which of them is the most likely suspect."
    
    def world_action_prompt(self):
        last_response = self.conversation.responses[-1]
        prompt_word, prompt_chain = self.knowledge.query(last_response.text())
        prompt = " ".join(prompt_chain)
        text = [x for x in self.scene.say(prompt)] + [self.generate_nudge()]
        return "\n".join(text)   
            
        return extra + "What's your next move, detective?"

from knowledge import KnowledgeBase
knowledge = KnowledgeBase("uncommon_english_words.json", "questions.ndjson")

class Response(object):
    def __init__(self, text):
        self._text = text

    def text(self):
        return self._text

class UserInputModel(object):
    # Get the responses of the detective from user input rather than
    # accessing an LLM through an API.
    
    def __init__(self):
        self.responses = []
    
    def conversation(self):
        return self

    def prompt(self, prompt):
        data = input()
        response = Response(data)
        self.responses.append(response)
        return response

if __name__ == '__main__':    
    # This runs the conversation engine based on user input.
    engine = ConversationEngine(knowledge, llm_model=UserInputModel())
    while not engine.final_round:
        engine.run()

    # This runs the conversation engine for every 
    for llm_model in ["wizardlm-13b-v1", "all-MiniLM-L6-v2-f16", "replit-code-v1_5-3b-q4_0", "orca-mini-3b-gguf2-q4_0", "mpt-7b-chat-merges-q4_0", "rift-coder-v0-7b-q4_0", "em_german_mistral_v01", "mistral-7b-instruct-v0", "mistral-7b-openorca", "gpt4all-falcon-q4_0", "gpt4all-13b-snoozy-q4_0", "nous-hermes-llama2-13b", "starcoder-q4_0"]:
        print(llm_model)
        engine = ConversationEngine(knowledge, llm_model=llm_model)
        while not engine.final_round:
            engine.run()
