DICE_ROLL_REGEX = '[\\w|\\s|!-/|:-@]*?[\\s]' \
                  '([0-9]*[\\s]*)d[\\s]*([0-9]+)' \
                  '[\\s]*([\\+|\\-][\\s]*[0-9]*)*[\\s]*(.*)[\\s]*$'

SPONGEBOB_CLEANER_REGEX = '\\/spongebob|\\/spongerep|\\/spr|\\/sp'

ZALGO_CLEANER_REGEX = '\\/zalgo|\\/z'

HELP_MESSAGE = ('I can roll dice and do funny stuff!\n\n'
                'You can control me by sending these commands:\n\n'
                '/help - sends this help message\n'
                '/start - sends this help message\n\n'
                'To roll dice and other things (each command has a long and short version):\n\n'
                '/roll - roll dice as indicated using dice notation\n'
                '/r - short version\n\n'
                '/ability_scores - rolls six ability scores for use in D&D style game systems\n'
                '/as - short version\n\n'
                '/alive - returns the emotional state of the bot\n\n'
                '/spongebob - takes your sentence and returns a saltier one\n'
                '/sp - short version\n\n'
                '/spongerep - reply to a message writing this, it will mock the first message\n'
                '/spr - short version\n\n'
                '/zalgo - takes your message to glitch it\n'
                '/z - short version\n\n'
                '/edgelord - give your character a reason to brood\n'
                'this command is the only one to just have a long version, for added edginess\n\n'
                '/character - creates a fully fledged character\n'
                '/char - short version\n\n'
                '/fabula - create your identity for a Fabula Ultima character\n'
                '/f - short version')

ALIVE_SERVICE = [
    'Alive and kicking',
    'Lock \'n loaded',
    'My life for DnD',
    'Stop poking me',
    'I like when you try to reach me',
    'I\'m alive, not by my choice',
    'What does "alive" even means?',
    'I\'m alive, be grateful to Pelor',
    'Who\'s summoning me?',
    '(/^▽^)/',
    '(つ ͡° ͜ʖ ͡°)つ',
    '(╯°□°）╯︵ ┻━┻',
    'ಠ_ಠ',
    'Pelor sucks'
]

SALTY_ANSWER = [
    'eh?',
    'Yeah, sure',
    'try writing something that makes sense, next time',
    'I\'m sure you can do better',
    'Wait. Are you sure about that?',
    'You may wanna think this over',
    'Did you really drink that much?',
    'Why do you people keep not reading the instructions?',
    'Well, fuck you too',
    'ಠ_ಠ',
    '...',
    'boooring'
]

EDGELORD_PARTS = [
    # Edgy antagonist
    [
        'An evil wizard',
        'A dragon',
        'The drow',
        'Goblins',
        'Kobolds',
        'A mind flayer',
        'Evil cultists',
        'Orcs',
        'Trolls',
        'A banshee',
        'A demon lord',
        'An archdevil',
        'Giants',
        'Vampires',
        'Gnolls',
        'A werefolf',
        'A Djinni',
        'A mimic',
        'A tarrasque',
        'A beholder',
        'A hag coven',
        'A lich',
        'Barbarians',
        'An aboleth',
        'A succubus',
        'A criminal organizations',
        'A gelatinous cube',
        'A necromancer',
        'Corrupt nobles',
        'A death knight',
        'The BBEG',
        'The bard',
        'Natural selection',
        'The DM',
    ],
    # Edgy action
    [
        'killed',
        'murdered',
        'slaughtered',
        'massacred',
        'assassinated',
        'brainwashed',
        'captured',
        'banished',
        'enslaved',
        'betrayed',
        'sacrificed',
        'mauled',
        'stole',
        'blackmailed',
        'conned',
        'framed',
        'humiliated',
        'pillaged',
        'ruined',
        'ate',
        'cursed',
        'befriended',
        'seduced'
    ],
    # Edgy victim
    [
        'my family',
        'my hometown',
        'my parents',
        'my clan',
        'my sibling',
        'my mentors',
        'my significant other',
        'my master',
        'my side squeeze',
        'my apprentice',
        'my friends',
        'my previous adventuring party',
        'everyone I knew',
        'my crew of sailors',
        'my crew of pirates',
        'my crew of noble outlaws',
        'my crew of thieves',
        'the tavern I basically lived in',
        'my military unit',
        'my social status',
        'my treasure',
        'my aspirations',
        'my honour',
        'my confidence',
        'my imaginary friends'
    ],
    # Edgy outcome
    [
        'and it will have no effect on how i roleplay my character',
        'and now I\'m a murder hobo',
        'and now I\'m a lawful good stick in the mud',
        'and now I seek vengeance',
        'and now I trust no one',
        'and now I have a bleak outlook of the world',
        'and now I strive to live by their ideals',
        'and now I must become stronger',
        'and now I seek to bring back what I have lost',
        'and now I vow to prevent that from happening to anyone else',
        'and now I am haunted by their memory',
        'and now I seek to uncover the truth about what happened',
        'and now I fear it will happen again',
        'and now I am stronger because of it',
        'and now I\'m and alcoholic',
        'and now I have multiclassed into warlock',
        'and now I\'m Batman'
    ]
]

PG_CREATION_PARTS = {
    'Sex': [
        'Male',
        'Female',
        'You choose'
    ],
    'Sexual orientation': [
        'Heterosexual',
        'Homosexual',
        'Bisexual',
        'Pansexual',
        'Asexual',
        'you choose'
    ],
    'Race': [
        'Aarakocra',
        'Aasimar (Fallen)',
        'Aasimar (Protector)',
        'Aasimar (Scourge)',
        'Bugbear',
        'Centaur',
        'Changeling',
        'Dragonborn (Base)',
        'Dragonborn (Draconblood)',
        'Dragonborn (Ravenite)',
        'Dwarf',
        'Dwarf (Duergar)',
        'Dwarf (Hill)',
        'Dwarf (Mark of Warding)',
        'Dwarf (Mountain)',
        'Elf (Drow)',
        'Elf (Eladrin)',
        'Elf (High)',
        'Elf (Mark of Shadow)',
        'Elf (Pallid)',
        'Elf (Sea)',
        'Elf (Shadar-kai)',
        'Elf (Wood)',
        'Firbolg',
        'Genasi (Air)',
        'Genasi (Earth)',
        'Genasi (Fire)',
        'Genasi (Water)',
        'Gith (Githyanki)',
        'Gith (Githzerai)',
        'Gnome (Deep)',
        'Gnome (Deep/Svirfneblin)',
        'Gnome (Forest)',
        'Gnome (Mark of Scribing)',
        'Gnome (Rock)',
        'Goblin',
        'Goliath',
        'Half-Elf',
        'Half-Elf (Variant)',
        'Half-Elf (Variant; Aquatic Elf Descent)',
        'Half-Elf (Variant; Drow Descent)',
        'Half-Elf (Variant; Mark of Detection)',
        'Half-Elf (Variant; Mark of Storm)',
        'Half-Elf (Variant; Moon Elf or Sun Elf Descent)',
        'Half-Elf (Variant; Wood Elf Descent)',
        'Half-Orc',
        'Half-Orc (Mark of Finding)',
        'Halfling (Ghostwise)',
        'Halfling (Lightfoot)',
        'Halfling (Lotusden)',
        'Halfling (Mark of Healing)',
        'Halfling (Mark of Hospitality)',
        'Halfling (Stout)',
        'Hobgoblin',
        'Human (Base)',
        'Human (Mark of Finding)',
        'Human (Mark of Handling)',
        'Human (Mark of Making)',
        'Human (Mark of Passage)',
        'Human (Mark of Sentinel)',
        'Human (Variant)',
        'Kalashtar',
        'Kenku',
        'Kobold',
        'Leonin',
        'Lizardfolk',
        'Loxodon',
        'Minotaur',
        'Orc',
        'Satyr',
        'Shifter (Beasthide)',
        'Shifter (Longtooth)',
        'Shifter (Swiftstride)',
        'Shifter (Wildhunt)',
        'Simic Hybrid',
        'Tabaxi',
        'Tiefling (Asmodeus)',
        'Tiefling (Baalzebul)',
        'Tiefling (Base)',
        'Tiefling (Dispater)',
        'Tiefling (Fierna)',
        'Tiefling (Glasya)',
        'Tiefling (Levistus)',
        'Tiefling (Mammon)',
        'Tiefling (Mephistopheles)',
        'Tiefling (Variant; Devil\'s Tongue)',
        'Tiefling (Variant; Hellfire)',
        'Tiefling (Variant; Infernal Legacy)',
        'Tiefling (Variant; Winged)',
        'Tiefling (Zariel)',
        'Triton',
        'Vedalken',
        'Verdan',
        'Warforged',
        'Yuan-ti Pureblood',
        'You choose'
    ],
    'Class': [
        'Artificer',
        'Barbarian',
        'Bard',
        'Cleric',
        'Druid',
        'Fighter',
        'Monk',
        'Paladin',
        'Ranger',
        'Rogue',
        'Sorcerer',
        'Warlock',
        'Wizard',
        'You choose'
    ],
    'Background': [
        'Acolyte',
        'Anthropologist',
        'Archaeologist',
        'Athlete',
        'Augen Trust (Spy)',
        'Azorius Functionary',
        'Boros Legionnaire',
        'Celebrity Adventurer\'s Scion',
        'Charlatan',
        'City Watch',
        'Variant City Watch (Investigator)',
        'Clan Crafter',
        'Cloistered Scholar',
        'Cobalt Scholar (Sage)',
        'Courtier',
        'Criminal',
        'Variant Criminal (Spy)',
        'Dimir Operative',
        'Entertainer',
        'Variant Entertainer (Gladiator)',
        'Faceless',
        'Faction Agent',
        'Failed Merchant',
        'Far Traveler',
        'Fisher',
        'Folk Hero',
        'Gambler',
        'Golgari Agent',
        'Grinner',
        'Gruul Anarch',
        'Guild Artisan',
        'Variant Guild Artisan (Guild Merchant)',
        'Haunted One',
        'Hermit',
        'House Agent',
        'Inheritor',
        'Izzet Engineer',
        'Knight of the Order',
        'Luxonborn (Acolyte)',
        'Marine',
        'Mercenary Veteran',
        'Myriad Operative (Criminal)',
        'Noble',
        'Variant Noble (Knight)',
        'Orzhov Representative',
        'Outlander',
        'Plaintiff',
        'Rakdos Cultist',
        'Revelry Pirate (Sailor)',
        'Rival Intern',
        'Sage',
        'Sailor',
        'Variant Sailor (Pirate)',
        'Selesnya Initiate',
        'Shipwright',
        'Simic Scientist',
        'Smuggler',
        'Soldier',
        'Urban Bounty Hunter',
        'Urchin',
        'Uthgardt Tribe Member',
        'Volstrucker Agent',
        'Waterdhavian Noble',
        'You choose'
    ]
}

HEIGHT_TABLE = {
    'Aarakocra': [140, 160],
    'Aasimar (Fallen)': [150, 190],
    'Aasimar (Protector)': [150, 190],
    'Aasimar (Scourge)': [150, 190],
    'Bugbear': [180, 245],
    'Centaur': [180, 210],
    'Changeling': [150, 185],
    'Dragonborn (Base)': [185],
    'Dragonborn (Draconblood)': [185],
    'Dragonborn (Ravenite)': [185],
    'Dwarf': [120, 150],
    'Dwarf (Duergar)': [120, 150],
    'Dwarf (Hill)': [120, 150],
    'Dwarf (Mark of Warding)': [120, 150],
    'Dwarf (Mountain)': [120, 150],
    'Elf (Drow)': [140, 185],
    'Elf (Eladrin)': [140, 185],
    'Elf (High)': [140, 185],
    'Elf (Mark of Shadow)': [140, 185],
    'Elf (Pallid)': [140, 185],
    'Elf (Sea)': [140, 185],
    'Elf (Shadar-kai)': [140, 185],
    'Elf (Wood)': [140, 185],
    'Firbolg': [210, 245],
    'Genasi (Air)': [150, 190],
    'Genasi (Earth)': [150, 190],
    'Genasi (Fire)': [150, 190],
    'Genasi (Water)': [150, 190],
    'Gith (Githyanki)': [160],
    'Gith (Githzerai)': [160],
    'Gnome (Deep)': [90, 120],
    'Gnome (Deep/Svirfneblin)': [90, 120],
    'Gnome (Forest)': [90, 120],
    'Gnome (Mark of Scribing)': [90, 120],
    'Gnome (Rock)': [90, 120],
    'Goblin': [90, 120],
    'Goliath': [210, 245],
    'Half-Elf': [150, 185],
    'Half-Elf (Variant)': [150, 185],
    'Half-Elf (Variant; Aquatic Elf Descent)': [150, 185],
    'Half-Elf (Variant; Drow Descent)': [150, 185],
    'Half-Elf (Variant; Mark of Detection)': [150, 185],
    'Half-Elf (Variant; Mark of Storm)': [150, 185],
    'Half-Elf (Variant; Moon Elf or Sun Elf Descent)': [150, 185],
    'Half-Elf (Variant; Wood Elf Descent)': [150, 185],
    'Half-Orc': [155, 195],
    'Half-Orc (Mark of Finding)': [155, 195],
    'Halfling (Ghostwise)': [75, 105],
    'Halfling (Lightfoot)': [75, 105],
    'Halfling (Lotusden)': [75, 105],
    'Halfling (Mark of Healing)': [75, 105],
    'Halfling (Mark of Hospitality)': [75, 105],
    'Halfling (Stout)': [75, 105],
    'Hobgoblin': [150, 190],
    'Human (Base)': [150, 190],
    'Human (Mark of Finding)': [150, 190],
    'Human (Mark of Handling)': [150, 190],
    'Human (Mark of Making)': [150, 190],
    'Human (Mark of Passage)': [150, 190],
    'Human (Mark of Sentinel)': [150, 190],
    'Human (Variant)': [150, 190],
    'Kalashtar': [150, 190],
    'Kenku': [135, 165],
    'Kobold': [60, 90],
    'Leonin': [175, 210],
    'Lizardfolk': [150, 190],
    'Loxodon': [210, 240],
    'Minotaur': [175, 195],
    'Orc': [175, 215],
    'Satyr': [145, 185],
    'Shifter (Beasthide)': [150, 190],
    'Shifter (Longtooth)': [150, 190],
    'Shifter (Swiftstride)': [150, 190],
    'Shifter (Wildhunt)': [150, 190],
    'Simic Hybrid': ['You choose'],
    'Tabaxi': [160, 200],
    'Tiefling (Asmodeus)': [150, 190],
    'Tiefling (Baalzebul)': [150, 190],
    'Tiefling (Base)': [150, 190],
    'Tiefling (Dispater)': [150, 190],
    'Tiefling (Fierna)': [150, 190],
    'Tiefling (Glasya)': [150, 190],
    'Tiefling (Levistus)': [150, 190],
    'Tiefling (Mammon)': [150, 190],
    'Tiefling (Mephistopheles)': [150, 190],
    'Tiefling (Variant; Devil\'s Tongue)': [150, 190],
    'Tiefling (Variant; Hellfire)': [150, 190],
    'Tiefling (Variant; Infernal Legacy)': [150, 190],
    'Tiefling (Variant; Winged)': [150, 190],
    'Tiefling (Zariel)': [150, 190],
    'Triton': [140, 180],
    'Vedalken': [175, 195],
    'Verdan': [90, 120],
    'Warforged': ['You choose'],
    'Yuan-ti Pureblood': [150, 190],
    'You choose': ['You choose']
}

WEIGHT_TABLE = {
    'Aarakocra': [80, 100],
    'Aasimar (Fallen)': [110, 200],
    'Aasimar (Protector)': [110, 200],
    'Aasimar (Scourge)': [110, 200],
    'Bugbear': [250, 350],
    'Centaur': [600, 700],
    'Changeling': [110, 190],
    'Dragonborn (Base)': [200, 300],
    'Dragonborn (Draconblood)': [200, 300],
    'Dragonborn (Ravenite)': [200, 300],
    'Dwarf': [130, 170],
    'Dwarf (Duergar)': [130, 170],
    'Dwarf (Hill)': [125, 165],
    'Dwarf (Mark of Warding)': [130, 170],
    'Dwarf (Mountain)': [130, 170],
    'Elf (Drow)': [80, 160],
    'Elf (Eladrin)': [80, 160],
    'Elf (High)': [80, 160],
    'Elf (Mark of Shadow)': [80, 160],
    'Elf (Pallid)': [80, 160],
    'Elf (Sea)': [80, 160],
    'Elf (Shadar-kai)': [80, 160],
    'Elf (Wood)': [80, 160],
    'Firbolg': [240, 300],
    'Genasi (Air)': [110, 200],
    'Genasi (Earth)': [110, 200],
    'Genasi (Fire)': [110, 200],
    'Genasi (Water)': [110, 200],
    'Gith (Githyanki)': [100, 180],
    'Gith (Githzerai)': [90, 140],
    'Gnome (Deep)': [80, 120],
    'Gnome (Deep/Svirfneblin)': [80, 120],
    'Gnome (Forest)': [30, 50],
    'Gnome (Mark of Scribing)': [30, 50],
    'Gnome (Rock)': [30, 50],
    'Goblin': [35, 50],
    'Goliath': [280, 340],
    'Half-Elf': [110, 190],
    'Half-Elf (Variant)': [110, 190],
    'Half-Elf (Variant; Aquatic Elf Descent)': [110, 190],
    'Half-Elf (Variant; Drow Descent)': [110, 190],
    'Half-Elf (Variant; Mark of Detection)': [110, 190],
    'Half-Elf (Variant; Mark of Storm)': [110, 190],
    'Half-Elf (Variant; Moon Elf or Sun Elf Descent)': [110, 190],
    'Half-Elf (Variant; Wood Elf Descent)': [110, 190],
    'Half-Orc': [140, 240],
    'Half-Orc (Mark of Finding)': [140, 240],
    'Halfling (Ghostwise)': [140, 240],
    'Halfling (Lightfoot)': [30, 50],
    'Halfling (Lotusden)': [30, 50],
    'Halfling (Mark of Healing)': [30, 50],
    'Halfling (Mark of Hospitality)': [30, 50],
    'Halfling (Stout)': [30, 50],
    'Hobgoblin': [110, 200],
    'Human (Base)': [110, 200],
    'Human (Mark of Finding)': [110, 200],
    'Human (Mark of Handling)': [110, 200],
    'Human (Mark of Making)': [110, 200],
    'Human (Mark of Passage)': [110, 200],
    'Human (Mark of Sentinel)': [110, 200],
    'Human (Variant)': [110, 200],
    'Kalashtar': [110, 180],
    'Kenku': [90, 120],
    'Kobold': [25, 35],
    'Leonin': [180, 240],
    'Lizardfolk': [120, 220],
    'Loxodon': [300, 400],
    'Minotaur': [180, 240],
    'Orc': [230, 280],
    'Satyr': [100, 180],
    'Shifter (Beasthide)': [90, 160],
    'Shifter (Longtooth)': [90, 160],
    'Shifter (Swiftstride)': [90, 160],
    'Shifter (Wildhunt)': [90, 160],
    'Simic Hybrid': ['You choose'],
    'Tabaxi': [90, 160],
    'Tiefling (Asmodeus)': [110, 200],
    'Tiefling (Baalzebul)': [110, 200],
    'Tiefling (Base)': [110, 200],
    'Tiefling (Dispater)': [110, 200],
    'Tiefling (Fierna)': [110, 200],
    'Tiefling (Glasya)': [110, 200],
    'Tiefling (Levistus)': [110, 200],
    'Tiefling (Mammon)': [110, 200],
    'Tiefling (Mephistopheles)': [110, 200],
    'Tiefling (Variant; Devil\'s Tongue)': [110, 200],
    'Tiefling (Variant; Hellfire)': [110, 200],
    'Tiefling (Variant; Infernal Legacy)': [110, 200],
    'Tiefling (Variant; Winged)': [110, 200],
    'Tiefling (Zariel)': [110, 200],
    'Triton': [90, 160],
    'Vedalken': [140, 200],
    'Verdan': [35, 50],
    'Warforged': ['You choose'],
    'Yuan-ti Pureblood': [110, 200],
    'You choose': ['You choose']
}

FABULA_CONCEPT = [
    'knight',
    'bodyguard',
    'animated puppet',
    'bounty hunter',
    'bandit',
    'scavenger',
    'martial artist',
    'factory worker',
    'rebel agent',
    'treasure hunter',
    'student',
    'warrior mage',
    'alien',
    'painter',
    'noble',
    'priest/ess',
    'magitech engineer',
    'duelist',
    'professor',
    'archer',
    'monster hunter',
    'samurai',
    'occultist',
    'medic',
    'bard',
    'paladin',
    'shapeshifter',
    'soldier',
    'monk',
    'pirate',
    'inventor',
    'gunslinger',
    'gambler',
    'smuggler',
    'black knight',
    'rōnin',
    'automaton',
    'alchemist',
    'mercenary',
    'ninja',
    'airship pilot',
    'cook',
    'diplomat',
    'spy',
    'commander',
    'thief',
    'templar',
    'sniper',
    'king/queen',
    'mechanic',
    'athlete',
    'mage',
    'dancer',
    'healer',
    'gladiator',
    'cannoneer',
    'demon hunter',
    'prince/ss',
    'merchant',
    'abomination'
]

FABULA_ADJECTIVES = [
    'charming',
    'devout',
    'oathbreaker',
    'last',
    'chosen',
    'distant',
    'former imperial',
    'proud',
    'troubled',
    'wanted',
    'brave',
    'fearful',
    'animal-loving',
    'kind',
    'respectable',
    'amnesiac',
    'dashing',
    'tainted',
    'imperial',
    'young',
    'free-spirited',
    'eccentric',
    'loyal',
    'well-connected',
    'elderly',
    'naive',
    'chivalrous',
    'spoiled',
    'smiling',
    'gifted',
    'no-nonsense',
    'royal',
    'apprentice',
    'reckless',
    'influent',
    'furtive',
    'ill-tempered',
    'famous',
    'tough',
    'non-human'
]

FABULA_DETAIL = [
    'from an Ancient Bloodline',
    'on the run',
    'of the Old Faith',
    'seeking justice',
    'in disgrace',
    'of the Crimson Wings',
    'from the High Academy',
    'from the Moon',
    'of the seven seas',
    'from the future',
    'looking for answers',
    'without a homeland',
    'of the Royal Army',
    'from another dimension',
    'of the Desert Clans',
    'of the Storm Knights',
    'with a heart of gold',
    'from the ancient forest',
    'from the past',
    'of the Sacred Flame'
]

FABULA_THEME = [
    'ambition',
    'anger',
    'doubt',
    'duty',
    'guilt',
    'hope',
    'justice',
    'belonging',
    'mercy',
    'vengeance'
]
