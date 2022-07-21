init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_hyperfixation",
            prompt="...a hyperfixation.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_hyperfixation:
    m 1wub "Oh, really [player]?"
    m "What are you currently hyperfixated on?{nw}"
$ _history_list.pop()
menu:
    m "What are you currently hyperfixated on?{fast}"
    
    "A franchise":
        pass
    
    "A TV show":
        pass
    
    "A videogame":
        pass
    
    "A movie":
        pass
    
    "A book":
        pass
    
    "A band/artist":
        pass
    
        m 2hub "Aww, that's wonderful!"
        m 3hub "I would love to hear more about your current obsession."
        m 5sua "What do you like about it? Tell me everything!"
        m 5kua "I don't want to interrupt you, so let me know when you're done speaking.{nw}"
        menu:
            m "I don't want to interrupt you, so let me know when you're done speaking.{fast}"

            "I'm done, [m_name].":
                pass

                m 7hub "That was wonderful to hear!"
                m 7dua "Being excited by something is such a wonderful feeling."
                m 2wub "I hope you can have tons of fun with it, [player]!"
                m 2tsbsu "I love listening to the person I love the most talk about what they love the most."
                m 2hsbfb "Ehehehe~"
        
return "love"
