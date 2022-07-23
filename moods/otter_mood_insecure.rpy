init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_insecure",
            prompt="...insecure.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_insecure:
    m 1wkd "[player]..."
    m 4dua "There's this quote from a certain anime that says..."
    m 2fka "'Believe in me, who believes in you.'"
    m 2fkb "And that's exactly what I want to tell you right now."
    m 2hua "If you can't believe in yourself right now, believe in me."
    m 4kuu "Because I, for sure, trust you can do this!"

return
