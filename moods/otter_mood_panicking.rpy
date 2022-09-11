init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_panicking",
            prompt="...like panicking.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_panicking:
    m 1wkd "Oh no [player]!"
    m 1rkc "Hm... What could we do..."
    m 1wub "Oh! What about a breathing excercise?"
    m 7wua "Let's do it together, breathing in and out."
    m 2dud "Breathe in.{w=1.0}.{w=1.0}.{w=1.0}."
    m "And out.{w=0.1}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m 2fua "Let's do it one more time."
    m 2dud "Breathe in.{w=1.0}.{w=1.0}.{w=1.0}."
    m "And out.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
    m 2dua "..."
    m 7ekb "Do you feel better, [mas_get_player_nickname()]? "
    extend 7hkb "I hope you do...!"
    m 3kua "Feel free to do this breathing exercise as many times as you need."
    m 1duc "I wish I could hold you right now..."
    m 5fkbsa "But for now, know that I love you and that everything is going to be okay."
    return "love"
