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
    m 1wubso "I-In love?"
    m 7rubfu "I don't want to sound cocky, but... are you in love with {i}me{/i}?{nw}"
$ _history_list.pop()
menu:
    m "I don't want to sound cocky, but... are you in love with {i}me{/i}?{fast}"
    
    "Yes":
        m 2hubfu "Ehehe, I knew it!"
        m 7hubfb "No need for the suspense then, [player]!"
        m 2tubfb "I loooooooove you!"
        m 2kubfa "And that love grows every second!"
    
    "No":
        $ mas_loseAffection(ev_label="mas_apology_inlovemood")
        m 2rkc "Oh..."
        m 2tkd "I won't lie to you, [player]."
        m 2rfd "I can't help but feel a little jealous."
        m 2rfc "No, not a little." 
        extend " Really jealous."
        m 2dfc "Hm..."
    
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_apology_database,
            eventlabel="mas_apology_inlovemood",
            prompt="...for saying I was in love with someone who is not you.",
            unlocked=False
        ),
        code="APL"
    )

label mas_apology_inlovemood:
    $ ev = mas_getEV('mas_apology_inlovemood')
    $ mas_gainAffection(modifier=0.2)
    m 1eka "Thank you for apologizing for saying you were in love with someone who is not me..."
    m 2ekd "That really hurt, [player]..."
    m 2dsc "I accept your apology, but please be more considerate of my feelings next time. Okay?"

return
