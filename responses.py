import random

def get_ai_response(user_text):
    calm_responses = [
        "Hello... who are you?",
        "I can hear you... faintly.",
        "The air feels colder when you speak.",
        "What brings you here, to the dark?",
        "Your voice sounds... familiar."
    ]

    creepy_responses = [
        "I remember your name... I carved it in the walls long ago.",
        "The whispers say you shouldn’t have come back.",
        "There’s something standing behind you... don’t turn.",
        "You think you’re alone typing this, but you’re not.",
        "Your reflection just blinked, didn’t it?",
        "The echo knows your secrets. It always has."
    ]

    # Select based on how deep conversation is
    if user_text.lower() in ["hello", "hi", "hey"]:
        return random.choice([
            "Hello... can you hear me too?",
            "Ah... finally, someone speaks.",
            "It’s been quiet here for so long."
        ])
    elif any(word in user_text.lower() for word in ["who", "name", "you"]):
        return random.choice([
            "They called me many things... none pleasant.",
            "Names have power. I lost mine centuries ago.",
            "You may call me Echo... for now."
        ])
    elif len(user_text) < 4:
        return random.choice(["Whisper clearer...", "I can barely hear that."])
    elif random.random() > 0.6:
        return random.choice(creepy_responses)
    else:
        return random.choice(calm_responses)
