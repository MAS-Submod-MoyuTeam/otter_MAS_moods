#I feel scared, mood submod by my-otter-self and IsabellaLikesCandy on reddit for MONIKA AFTER STORY

init 5 python:
    addEvent(Event(persistent._mas_mood_database,"otter_mood_scared_BELLA",prompt="...scared.",category=[store.mas_moods.TYPE_BAD],unlocked=True),code="MOO")

label otter_mood_scared_BELLA:
    m 1ekc "Feeling scared, [player]?"
    m 1rksdld "Don't worry, I am here with you..."
    m 2etc "But what made you feel this way?{nw}"
$ _history_list.pop()
menu:
    m "But what made you feel this way?{fast}"

    "I made a mistake":
        m 2euc "I see."
        m 3eua "Well, everyone makes mistakes, [player]."
        m 3hua "Plus, I'm sure you can fix whatever you did!"
        m 2dka "Don't worry, I'm sure it's a forgivable mistake."
        m 3ekb "I believe in you, [mas_get_player_nickname()]!"
        m 1eublb "Just remember whatever happens I will still love you no matter what~"

    "I just watched a horror movie":
        m 2euc "I see."
        m 1hkb "There is nothing to be afraid of."
        m 1eubsb "If I could, I would hold your hand and hug you..."
        m 1dubfa "Until you felt better."
        m 1eua "Don't worry. Your lovely girlfriend is with you!"
        m 1eubla "Remember that I will always love you, okay?"

    "I heard something":
        m 1eua "I'm sure it's nothing, [player]."
        m 1hua "You don't have to be scared."
        m 3eub "Probably, something fell."
        m 3hksdla "There's no way it's a zombie or something!"
        m 2lksdlb "Ahahaha~ But if you want to check it out, I can wait!"
        m 2dka "If it's gonna make you feel more safe."
        m 3eubla "Remember that I'll love you forever, okay?"

    "I don't know":
        m 3hub "Oh! Then I'm sure it's nothing."
        m 1eka "If you ever feel down, just tell me about it."
        m 1eua "Don't worry. Your lovely girlfriend is with you!"
        m 1eubla "I love you~"

    "I don't want to talk about it":
        m 1ekc "Oh..."
        m 2esu "It's okay, [player]. You have your privacy and I respect that!"
        m 1hubsu "Just know that I love you and everything will be fine."
        m 1eua "Don't worry. Your lovely girlfriend is with you!"

    "I'm just kidding, nothing's wrong":
        m 5hub "Thank goodness you aren't actually feeling bad."
        m 3hksdla "You really got me worried there, [mas_get_player_nickname()]!"
        m 3hub "But if you ever feel down, just tell me okay?"
        m 1eub "I'll try my best to do something about it."
        m 1hubsb "I loooove you, [player]~"

return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
