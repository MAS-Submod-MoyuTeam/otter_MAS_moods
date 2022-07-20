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
    m 1sub "Oh! Is that so, [player]?"
    m 2sua "Just hearing that gets me all fired up too!"
    m 7sub "Did something great just happen?"
    m 7hua "I'm so happy for you."
    extend 4hub " Euphoria is such a great feeling to get!"
    m 4kub "Let's enjoy it, [mas_get_player_nickname()]!"
    m 5fkbsa "I love you sooooooooo much!"
    
return "love"
