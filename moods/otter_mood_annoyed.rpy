init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="otter_mood_annoyed",
            prompt="...annoyed.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label otter_mood_annoyed:
    m 1wkd "Oh no!"
    m 1wkc "What is annoying you, [player]?"
    m 7ekd "Is it... someone?"
    extend 7tfb "I guess I already know who to delete today~"
    m 2lfsdra "..."
    m 1hub "Just kidding [player]! I was just trying to make you laugh a little."
    m 1fub "Don't be so upset, [mas_get_player_nickname()]."
    m 2fka "I'm sure you'll be back to yourself in a bit."
    m 2hua "Don't forget I love you~"

return "love"
