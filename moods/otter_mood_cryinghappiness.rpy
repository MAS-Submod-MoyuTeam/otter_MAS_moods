init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_cryinghappiness",
            prompt="...crying of happiness.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_cryinghappiness:
    m "[player]! That's great!"
    m "At first the tears startled me a bit, but overall... "
    extend "that's a good thing. Ehehe~"
    m "Seeing you happy makes me happy too!"
    m "But where did the happiness come from, I wonder?{nw}"
$ _history_list.pop()
menu:
    m "But where did the happiness come from, I wonder?{fast}"
    
    "I'm just happy to be here with you.":
    m "..."
    m "Oh! I'm sorry, [player]!"
    m "I'm just at a loss of words."
    m "You are the best, you know that?"
    m "You make me feel so loved..."
    m "Know that you make me the happiest girl in the world too."
    m "I love you!"
    
    "Life has been kind on me recently.":
    m "[player]..."
    m "That is just wonderful."
    m "Peace is one of the best feelings in the world."
    m "And I'm glad life finally decided to give you what you deserve..."
    extend " peaceful days!"
    m "Ehehehe~"
    m "I love you and thank you for sharing your happiness with me."
    m "I'm so glad to be your girlfriend."
    
    "Something great just happened.":
    m "Really, [player]?"
    m "That's amazing!"
    m "Thank you so much for sharing your happiness with me."
    m "I feel the happiest girl in the world to be by your side at moments like these."
    m "You deserve all this happiness, [mas_get_player_nickname()]!"
    m "I love you so much."
    
return "love"
