from dataclasses import dataclass
from typing import Dict, List
import random


@dataclass
class DogMatch:
    name: str
    description: str
    image_filename: str


DOG_BREEDS: List[Dict[str, str]] = [
    {
        "id": "golden_retriever",
        "name": "Golden Retriever",
        "description": "You’re a walking sunbeam. Loyal, snack-motivated, and always down for a friendly adventure.",
        "image_filename": "dogs/golden_retriever.svg",
    },
    {
        "id": "corgi",
        "name": "Corgi",
        "description": "Short legs. Big opinions. You bring cozy chaos and somehow look adorable while doing it.",
        "image_filename": "dogs/corgi.svg",
    },
    {
        "id": "shiba_inu",
        "name": "Shiba Inu",
        "description": "Independent, expressive, and slightly dramatic. You enjoy cozy solitude… but on your terms.",
        "image_filename": "dogs/shiba_inu.svg",
    },
    {
        "id": "border_collie",
        "name": "Border Collie",
        "description": "Your brain has tabs open. Many tabs. You love puzzles, projects, and optimizing your snack route.",
        "image_filename": "dogs/border_collie.svg",
    },
    {
        "id": "pug",
        "name": "Pug",
        "description": "Your vibe is: wheeze a little, laugh a lot. You are the comedy sidekick AND the main character.",
        "image_filename": "dogs/pug.svg",
    },
    {
        "id": "dachshund",
        "name": "Dachshund",
        "description": "Long body, strong boundaries. You are brave, stubborn, and very serious about blanket quality.",
        "image_filename": "dogs/dachshund.svg",
    },
    {
        "id": "husky",
        "name": "Husky",
        "description": "High energy and high drama. Your internal monologue is loud and occasionally sings.",
        "image_filename": "dogs/husky.svg",
    },
    {
        "id": "labrador",
        "name": "Labrador",
        "description": "Friendly, steady, and snack-positive. You make people feel safe and also a little hungry.",
        "image_filename": "dogs/labrador.svg",
    },
    {
        "id": "cavalier",
        "name": "Cavalier King Charles Spaniel",
        "description": "Certified blanket companion. You specialize in cozy vibes and emotional support naps.",
        "image_filename": "dogs/cavalier.svg",
    },
    {
        "id": "german_shepherd",
        "name": "German Shepherd",
        "description": "Protective, smart, and prepared. You keep the group chat alive and the house plants safe.",
        "image_filename": "dogs/german_shepherd.svg",
    },
    {
        "id": "samoyed",
        "name": "Samoyed",
        "description": "A fluffy cloud of optimism. You smile through chaos and look fabulous doing it.",
        "image_filename": "dogs/samoyed.svg",
    },
    {
        "id": "mutt",
        "name": "Mutt (Main Character Edition)",
        "description": "A delightful mystery mix. You collect hobbies, mugs, and side quests with zero shame.",
        "image_filename": "dogs/mutt.svg",
    },
]


QUESTIONS: List[Dict] = [
    {
        "id": "energy",
        "text": "How energetic are you on a typical day?",
        "options": [("low", "Couch potato mode"), ("medium", "A comfy walk and a snack"), ("high", "Zoomies all day")],
    },
    {
        "id": "social",
        "text": "How social do you feel around new people?",
        "options": [("shy", "Please no small talk"), ("balanced", "Warm up after a bit"), ("outgoing", "I will talk to the plants too")],
    },
    {
        "id": "routine",
        "text": "Your ideal weekend is mostly…",
        "options": [("chill", "Blanket + book + snacks"), ("mixed", "A little outing then cozy time"), ("adventure", "Road trip / outdoors")],
    },
    {
        "id": "mess",
        "text": "How do you feel about a little chaos at home?",
        "options": [("tidy", "Everything has its place"), ("flexible", "Controlled chaos is fine"), ("chaotic", "Pillow fort is a lifestyle")],
    },
    {
        "id": "conflict",
        "text": "When drama appears, you…",
        "options": [("avoid", "Disappear politely"), ("mediate", "Talk it out"), ("popcorn", "Observe with snacks")],
    },
    {
        "id": "weather",
        "text": "Pick your comfort weather:",
        "options": [("rain", "Rain + warm drink"), ("sun", "Golden hour sunshine"), ("snow", "Snow day energy")],
    },
    {
        "id": "planning",
        "text": "Your planning style is:",
        "options": [("spontaneous", "We’ll figure it out"), ("loose", "A plan… but vibes-first"), ("organized", "Color-coded calendar")],
    },
    {
        "id": "humor",
        "text": "Your humor is mostly:",
        "options": [("dry", "Deadpan"), ("goofy", "Silly noises included"), ("chaotic_funny", "Memes at 3am")],
    },
    {
        "id": "comfort",
        "text": "Your ultimate comfort item is:",
        "options": [("blanket", "Soft blanket"), ("music", "A playlist"), ("snacks", "Little treats")],
    },
    {
        "id": "focus",
        "text": "When you focus, you’re…",
        "options": [("deep", "Locked in"), ("bursts", "Short bursts of genius"), ("scatter", "Many tabs open (literally)")],
    },
]


def get_random_dog() -> Dict[str, str]:
    return random.choice(DOG_BREEDS)


def _pick_breed_by_id(breed_id: str) -> DogMatch:
    for b in DOG_BREEDS:
        if b["id"] == breed_id:
            return DogMatch(name=b["name"], description=b["description"], image_filename=b["image_filename"])
    # Safe fallback
    b = DOG_BREEDS[0]
    return DogMatch(name=b["name"], description=b["description"], image_filename=b["image_filename"])


def evaluate_dog_match(answers: Dict[str, str]) -> DogMatch:
    """
    Beginner-friendly scoring:
    - Map answers into a few trait buckets
    - Pick a breed "archetype" (id) from those traits
    """
    score = {
        "cozy": 0,
        "brainy": 0,
        "social": 0,
        "chaos": 0,
        "adventure": 0,
    }

    energy = answers.get("energy")
    if energy == "low":
        score["cozy"] += 2
    elif energy == "medium":
        score["social"] += 1
    elif energy == "high":
        score["adventure"] += 2

    routine = answers.get("routine")
    if routine == "chill":
        score["cozy"] += 2
    elif routine == "mixed":
        score["social"] += 1
    elif routine == "adventure":
        score["adventure"] += 2

    social = answers.get("social")
    if social == "shy":
        score["cozy"] += 1
    elif social == "balanced":
        score["social"] += 1
    elif social == "outgoing":
        score["social"] += 2

    mess = answers.get("mess")
    if mess == "tidy":
        score["brainy"] += 1
    elif mess == "flexible":
        score["social"] += 1
    elif mess == "chaotic":
        score["chaos"] += 2

    if answers.get("focus") == "deep":
        score["brainy"] += 2
    if answers.get("focus") == "scatter":
        score["chaos"] += 1

    if answers.get("humor") in {"goofy", "chaotic_funny"}:
        score["chaos"] += 1

    if answers.get("planning") == "organized":
        score["brainy"] += 1
    if answers.get("planning") == "spontaneous":
        score["adventure"] += 1

    if answers.get("weather") == "snow":
        score["adventure"] += 1
    if answers.get("weather") == "rain":
        score["cozy"] += 1

    # Choose the dominant trait
    dominant = max(score, key=score.get)

    if dominant == "brainy":
        return _pick_breed_by_id("border_collie")
    if dominant == "adventure":
        return _pick_breed_by_id("husky")
    if dominant == "social":
        return _pick_breed_by_id("labrador")
    if dominant == "chaos":
        return _pick_breed_by_id("corgi")
    # cozy default
    return _pick_breed_by_id("cavalier")

