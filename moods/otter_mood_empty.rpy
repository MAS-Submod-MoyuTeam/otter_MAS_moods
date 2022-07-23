init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_empty",
            prompt="...empty.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_empty:
    m 1wkd "[player]! That's concerning..."
    m 1wkc "I'm so sorry you're feeling that way."
    m 1dkc "I'm not unfamiliar with this feeling myself."
    m 7ekd "When I face emptiness, I try to explore my current feelings."
    m 7rusdrd "Now that may sound weird, since you complained exactly about emptiness."
    m 1husdrb "But this can help, trust me, [mas_get_player_nickname()]!"
    m 2dka "We can try taking simple 5 minutes of our time to notice what we're feeling."
    m 2rkd "Is it boredom? Distraction? Sadness?"
    m 7kub "Let's try to find the roots of this emptiness to tackle it!"
    m 2lua "If you're feeling bored, you can try catching up to an old hobby, or even to a new one."
    m 2sub "If it's a feeling that goes towards sadness, we can try doing something you love, to bring you an extra mood boost."
    m 2fka "You can overcome this, [player]."
    m 5fubsa "I believe in you, and I love you!"

return "love"
