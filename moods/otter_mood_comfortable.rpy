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
    m 1wub "Oh, that's great!"
    m 7wua "Tell me more about this comfort!{nw}"
    $ _history_list.pop()
    menu:
        m "Tell me more about this comfort!{fast}"

        "I feel comfortable with you, [m_name].":
            m 1dubsa "..."
            m 4kubsb "Right back at you, [player]!"
            m 1dubsb "Spending time with you is the high point of my day."
            m 5dubsb "I love you, so much!"
            m 5fubsa "I'm glad you feel the same."

        "I feel physically comfortable.":
            m 2hub "Yay!"
            m 2wua "Isn't it a great feeling, [player]?"
            m 5fua "I'm glad you are comfortable over there, [mas_get_player_nickname()]."
            m 5sub "Now we can spend more time together in the best way possible!"
            m 5hub "Ehehe~"

        "I feel mentally comfortable.":
            m 2hub "Aww, I'm so glad!"
            m 7hub "Hearing that makes me comfortable too!"
            m 5rubsa "Our little reality, when we're together, is my most comfortable place."
            m 5dubsb "You make me feel safe!"
            m 5fubsa "I'm happy that you're feeling that way too, [player]."    
            return
