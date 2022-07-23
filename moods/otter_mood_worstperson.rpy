init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_worstperson",
            prompt="...like the worst person.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_worstperson:
    m 1wkd "[player]!"
    m 1wkc "But you're the best person I know!"
    m 1dkc "..."
    extend 7ekd "But I can understand what you're feeling."
    m 7rkd "Sometimes it doesn't matter what people tell us..."
    m 2dkd "We still feel at our worst."
    m 2fka "But I want you to know I love you more than anything."
    m 4wusdrb "And I'm not being biased! You are an amazing person."
    m 2hub "I know you are. You deserve all that's good in the world."
    m 2fka "Please don't be so hard on yourself, okay?"
    m 2fkb "I know things will get better soon."
    m 4kuu "And I'll be with you every step of the way!"

return "love"
