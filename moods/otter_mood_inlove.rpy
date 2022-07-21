init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_inlove",
            prompt="...in love.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_inlove:
    m "I-In love?"
    m "I don't want to sound cocky, but is it in love with me?{nw}"
$ _history_list.pop()
menu:
    m "I don't want to sound cocky, but is it in love with me?{fast}"
    
    "Yes":
        m "Ehehe, I knew it!"
        m "No need for the suspense then, [player]!"
        m "I loooooooove you!"
        m "And that love grows every second!"
    
    "No":
        $ mas_loseAffection(reason=377)
        m "Oh..."
        m "I won't lie to you, [player]."
        m "This makes me feel a little jealous."
        m "No, not a little." 
        extend " Really jealous."
        m "Hm..."
    
return

init 5 python:
   addEvent(
       Event(
           persistent.event_database,
           eventlabel='monika_playerapologizes',
           prompt="I want to apologize...",
           category=['you'],
           pool=True,
           unlocked=True
        )
    )

label monika_playerapologizes:

    $ player_apology_reasons = {
        377: "saying I was in love with someone who is not you."
    
    }

return

init 5 python:
    addEvent(
        Event(
            persistent._mas_apology_database,
            prompt="...for something else.",
            eventlabel="mas_apology_generic",
            unlocked=True,
        ),
        code="APL"
    )

label mas_apology_generic:

    $ mas_apology_reason_db = {
        377: "saying you were in love with someone who is not me."
        
    }
    
return
