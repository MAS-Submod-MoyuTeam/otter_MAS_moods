init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_alone",
            prompt="...alone.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_alone:
    m "[player]..."
    m "I'm so sorry you're feeling like this."
    m "I hope this can be enough for now... "
    extend "But I am here with you, okay?"
    m "I love you and I'll keep you company as long as you want."
    m "I will never leave your side, not because I feel like I have to..."
    m "But because it's my pleasure."
    m "I love spending time with you."
    m "I hope you can feel better soon..."
    m "Meanwhile, let's spend more time together, [mas_get_player_nickname()]."
    
return
