from olipy import corpora
import random

class Grammar(object):

    @property
    def an(self):
        if self.name[0] in 'aeio':
            return "an %s" % self.name
        else:
            return "a %s" % self.name

    def quote(self, text):
        if not text.startswith('"'):
            text = '"' + text
        if not text.endswith('"'):
            text = text + '"'
        return text
        
    def list(self, items):
        if len(items) == 0:
            import pdb; pdb.set_trace()
        if len(items) == 1:
            return items[0]
        first = items[:-1]
        final = items[-1]
        return ", ".join([str(x) for x in first]) + " and " + str(final)
        
class Character(Grammar):
    occupations = corpora.humans.occupations['occupations']
    animals = corpora.animals.common['animals']
    nationalities = corpora.geography.nationalities['nationalities']
    characters = corpora.archetypes.character['characters']
    descriptions = corpora.humans.descriptions['descriptions']
    adverbs = "quietly loudly impatiently hoarsely warmly coldly frantically".split(" ")
    adverbs.extend(["a bit too loudly", "in a hush", "in a whisper"])
    
    def __init__(self):
        r = random.randint(0, 2)
        if r == 0:
            self.his = "his"
            self.him = "him"
            self.he = "he"
        elif r == 0:
            self.his = "her"
            self.him = "her"
            self.he = "she"
        else:
            self.his = "their"
            self.him = "them"
            self.he = "they"

        if random.randint(0, 4) == 0:
            self.characterization = random.choice(self.nationalities)
        elif random.randint(0,3) == 0:
            self.characterization = random.choice(self.descriptions)
        else:
            self.characterization = None
        if random.randint(0, 6) == 0:
            self.occupation = random.choice(self.animals)
        else:
            self.occupation = random.choice(self.occupations)

        if self.characterization:
            self.name = "%s %s" % (self.characterization, self.occupation)
        else:
            self.name = self.occupation
            
        self.inventory = [Possession()]

    def say(self, text, target):
        if target is None:
            return 'The %s says: %s' % (self.name, self.quote(text))
        else:
            if target != 'you':
                target = 'the %s' % target.name
            template = random.choice([
                'The %(name)s nods and says: %(statement)s',
                'The %(name)s turns to %(you)s and says: %(statement)s',
                'The %(name)s mutters: %(statement)s',
                'The %(name)s looks around suspiciously and says: %(statement)s',
                'Leaning over to whisper to %(you)s, the %(name)s says: %(statement)s',]
                )
            return template % dict(you=target, name=self.name, statement=self.quote(text))

    def mention_clue(self, clue):
        template = random.choice([
            '"The %(noun)s!" says the %(person)s%(adverb)s... "That %(adjective)s, %(clue)s!"',
            '"The %(clue)s..." says the %(person)s%(adverb)s, "it\'s the cause of it all!"',
            '"The %(clue)s..." says the %(person)s%(adverb)s. "The %(clue)s..."',
            '"Who would have thought?" says the %(person)s%(adverb)s. "If it weren\'t for that %(clue)s..."',
            '"The %(clue)s..." says the %(person)s%(adverb)s. "Where is it? Where is it, detective?"',
            '"Where\'s that %(clue)s?" asks the %(person)s%(adverb)s. "Where did it go?"',
        ])
        if random.random() < 0.5:
            adverb=" " +random.choice(self.adverbs)
        else:
            adverb = ""
        args = dict(
            person=self.name,
            adverb=adverb,
            adjective=random.choice(Possession.adjectives),
            clue=clue.as_clue,
            noun=clue.name
        )
        return template % args
            
        
    def look_at_something(self, target):
        item = random.choice(self.inventory)
        if target is None:
            return "The %s looks at %s %s." % (self.name, self.his, item.name)
        else:
            if target != 'you':
                target = 'the %s' % target.name
            a = random.randint(1,10)
            if a < 5:
                return 'The %s shows %s %s %s.' % (self.name, target, self.his, item.name)
            elif a < 6:
                return "The %s casts a furtive glance at %s %s." % (self.name, self.his, item.name)
            else:
                return 'The %s seems to be hiding %s from %s. Could this be a clue?' % (self.name, item.an, target)
        
    def __str__(self):
        return self.an
        
class Location(Grammar):
    countries = corpora.geography.countries['countries']
    rooms = corpora.architecture.rooms['rooms']
    passages = corpora.architecture.passages['passages']
    venues = []
    for category in corpora.geography.venues['categories']:
        venues.extend([x['name'] for x in category['categories']])

    settings = [x['name'] for x in corpora.archetypes.setting['settings']]
    places = settings + venues + rooms + passages

    def __init__(self):
        
        self.name = random.choice(self.places)
        if random.randint(0,4) == 0:
            self.name += " in " + random.choice(self.countries)

        self.characters = [Character() for i in range(0,random.randint(2,3))]
        self.body = Character()
        self.prop = Possession()
        self.items = []
        for character in self.characters:
            for item in character.inventory:
                self.items.append(item)
        self.items.append(self.prop)
        self.clue = random.choice(self.items)
        
    def describe(self):
        return "You are in %s. The dead body of %s lies on the floor, clutching %s. You are here with %s." % (
            self.an, self.body.an, self.prop.an, self.list(self.characters)
        )

    @property
    def random_character(self):
        return random.choice(self.characters)
    
class Transition(Grammar):
    events = []
    for i in corpora.archetypes.event['events']:
        events.append(i['name'])
        events.extend(i['synonyms'])

    def __init__(self):
        self.name = random.choice(self.events)

    def __str__(self):
        return self.an
        
class Possession(Grammar):
    objects = corpora.objects.objects['objects']
    adjectives = corpora.words.adjs['adjs']
    def __init__(self):
        self.name = random.choice(self.objects)
        self.adjective = random.choice(self.adjectives)
        
    def __str__(self):
        return self.an

    @property
    def as_clue(self):
        return "%s %s" % (self.adjective, self.name)
    
class Scene(Grammar):

    def __init__(self):
        self.location = Location()
        case_template = random.choice([
            "The Mystery of the %s",
            "The Case of the %s",
            "The %s Affair",
            "The Adventure of the %s",
        ])
        self.case_name = case_template % self.location.clue.as_clue.title()
        
    def describe(self):
        return self.location.describe()
        
    def say(self, text):
        # Some number of things will happen, until someone says the given text.
        done = False
        self.mentioned_clue = False
        while not done:
            for i in self._say(text):
                yield i
                if text in i:
                    done = True
            
    def _say(self, text):
        #  who = self.location.random_character
        # target = "you"
        # other_characters = [x for x in self.location.characters if x != who]
        # if random.randint(0,1) == 0:
        #     if not other_characters or random.randint(0, 1) == 0:
        #         target = None
        #     else:
        #         target = random.choice(other_characters)
        #         if target == who:
        #             target = "you"
        target = "you"
        
        choice = random.randint(0,10)
                
        if choice < 7:
            # Time for someone to say something.
            yield self.location.random_character.say(text, target)
        elif choice < 8:
            # Character takes out an inventory item
            yield self.location.random_character.look_at_something(target)
        else:
            if not self.mentioned_clue:
                yield self.location.random_character.mention_clue(self.location.clue)
                self.mentioned_clue = True
        #elif choice < 9:
        #    self.location = Location()
        #    yield "All at once there is %s, and the scene changes..." % (str(Transition()))
        #    yield self.location.describe()
        #else:
        #    yield "A voice over a loudspeaker says: %s" % self.quote(text)

        
        
if __name__ == '__main__':
    scene = Scene()
    print(scene.case_name)
    print(Transition())
    print(scene.describe())
    for i in range(10):
        print(scene.location.random_character.mention_clue(scene.location.clue))
                   
    for i in range(10):
        for j in scene.say("hello"):
            print(j)
