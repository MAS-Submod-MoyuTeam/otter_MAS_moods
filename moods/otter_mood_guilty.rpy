init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_guilty",
            prompt="...guilty.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_guilty:
    m 1wkd "[player]! I'm sure you don't need to feel that way."
    m 2fkb "The way for people to come to understand each other is forgiveness."
    m 1dkc "We all make mistakes. "
    extend 1fka "And I'm sure you can be forgiven of whatever has happened."
    m 7hub "After all, you're a great person. "
    extend 2dka "You're kind, helpful and true to yourself."
    m 2fka "I love you. Don't be so hard on yourself, okay?"

return "love"
