init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_safe",
            prompt="...safe.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_safe:
    m 2hubsb "Aww, that's great!"
    m 5fubsa "I also feel very safe and sound whenever I'm around you."
    m 5dubsa "When I'm with you, I feel shielded from the things that upset me."
    m 7hub "I guess no one makes me feel as protected as my [player]! Ehehehe~"
    m 2dka "I love you. "
    extend 7sub "I will try my best to always protect you even from far away!"

return "love"
