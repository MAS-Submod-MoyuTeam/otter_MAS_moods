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
    m "Oh no [player]!"
    m "Hm... What could we do..."
    m "Oh! What about a breathing excercise?"
    m "Let's do it together, breathing in and out."
    m "Breathe in.{w=0.1}.{w=0.1}.{w=0.1}."
    m "And out.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}."
    m "Let's do it one more time."
    m "Breathe in.{w=0.1}.{w=0.1}.{w=0.1}."
    m "And out.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}."
    m "..."
    m "Do you feel better, [mas_get_player_nickname()]? "
    extend "I hope you do...!"
    m "Feel free to do this breathing exercise as many times as you need."
    m "I wish I could hold you right now..."
    m "But for now, know that I love you and that everything is going to be okay."
    
return "love"
