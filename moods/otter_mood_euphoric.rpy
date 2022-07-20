init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_euphoric",
            prompt="...euphoric.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_euphoric:
    m "Oh! Is that so, [player]?"
    m "Just hearing that gets me all fired up too!"
    m "Did something great just happen?"
    m "I'm so happy for you."
    extend " Euphoria is such a great feeling to get!"
    m "Let's enjoy it, [mas_get_player_nickname()]!"
    m "I love you sooooooooo much!"
    
return "love"
