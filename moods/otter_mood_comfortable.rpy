init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_comfortable",
            prompt="...comfortable.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_comfortable:
    m "Oh, that's great!"
    m "Tell me more about this comfort!{nw}"
$ _history_list.pop()
menu:
    m "Tell me more about this comfort!{fast}"
    
    "I feel comfortable with you, [m_name].":
    m "..."
    m "Right back at you, [player]!"
    m "I know sometimes I don't have much to say..."
    m "But spending time with you is the high point of my day."
    m "I love you, so much!"
    m "I'm glad you feel the same."
    
    "I feel physically comfortable.":
    m "Yay!"
    m "Isn't it a great feeling, [player]?"
    m "I'm glad you are comfortable over there, [mas_get_player_nickname()]."
    m "Now we can spend more time together in the best way possible!"
    m "Ehehe~"
    
    "I feel mentally comfortable.":
    m "Aww, I'm so glad!"
    m "Hearing that makes me comfortable too!"
    m "Our little reality, when we're together, is my most comfortable place."
    m "You make me feel safe!"
    m "I'm happy that you're feeling that way too, [player]."
    
return
