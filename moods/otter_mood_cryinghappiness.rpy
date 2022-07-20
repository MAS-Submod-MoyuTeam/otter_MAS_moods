init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_cryinghappiness",
            prompt="...like crying of happiness.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_cryinghappiness:
    m 1wub "[player]! That's great!"
    m 1rusdrb "At first the tears startled me a bit, but overall... "
    extend 1hua "that's a good thing. Ehehe~"
    m 7hua "Seeing you happy makes me happy too!"
    m 7rub "But where did the happiness come from, I wonder?{nw}"
$ _history_list.pop()
menu:
    m "But where did the happiness come from, I wonder?{fast}"
    
    "I'm just happy to be here with you.":
    m 2dubsa "..."
    m 2wubso "Oh! I'm sorry, [player]!"
    m 2fkbsa "I'm just at a loss of words."
    m 5fkbsb "You are the best, you know that?"
    m 5dkbsa "You make me feel so loved..."
    m 3hsblb "Know that you make me the happiest girl in the world too."
    m 2hsblb "I love you!"
    
    "Life has been kind on me recently.":
    m 1dub "[player]..."
    m 1fkbla "That is just wonderful."
    m 7hubla "Peace is one of the best feelings in the world."
    m 2dublb "And I'm glad life finally decided to give you what you deserve..."
    extend 2kubla " peaceful days!"
    m 2hublb "Ehehehe~"
    m 2hsblb "I love you and thank you for sharing your happiness with me."
    m 5fubsa "I'm so glad to be your girlfriend."
    
    "Something great just happened.":
    m 1wub "Really, [player]?"
    m 1hub "That's amazing!"
    m 5fubsa "Thank you so much for sharing your happiness with me."
    m 5dubsb "I feel the happiest girl in the world to be by your side at moments like these."
    m 4ksbla "You deserve all this happiness, [mas_get_player_nickname()]!"
    m 2hsblb "I love you so much."
    
return "love"
