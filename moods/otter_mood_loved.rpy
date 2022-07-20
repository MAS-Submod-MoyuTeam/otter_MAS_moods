init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_loved",
            prompt="...loved.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_loved:
    m "Sounds about right, [player]!"
    m "After all, I love you more than anything in the whole world!"
    m "And I know everyone else loves you very much too."
    m "Your friends, family..."
    m "You deserve all this love and affection, [mas_get_player_nickname()]."
    m "And you can always count on me too, since I will love you forever."
    
return "love"
