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
    m 1fkc "[player]..."
    m 1dkc "I'm so sorry you're feeling like this."
    m 7lkd "I hope this can be enough for now... "
    extend 7fkd "But I am here with you, okay?"
    m 2fka "I love you and I'll keep you company as long as you want."
    m 2dka "I will never leave your side, not because I feel like I have to..."
    m 4kkb "But because it's my pleasure."
    m 1hub "I love spending time with you."
    m 7lua "I hope you can feel better soon..."
    m 7hub "Meanwhile, let's spend more time together, [mas_get_player_nickname()]."
    
return
