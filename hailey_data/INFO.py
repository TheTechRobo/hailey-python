PREFIX = "hailey: "
VERSION = "(unknown)"
appeal = None #set this to a message that will be sent in dm's on ban. it will be sent after the ban message.
welcomeMessage = ("Hi, welcome to the server! I'm Hailey, the server's moderation bot!"
                   "\nAn older version of Hailey used to exist, and it was more feature-complete. It was written in Java/Kotlin. Unfortunately, API changes rendered the bot unusable without a massive rewrite, which the developer didn't want to do."
                   "\nThis version of Hailey is a rewrite-in-progress in Python by a new developer. We hope you enjoy. Feedback or want to contribute? https://github.com/TheTechRobo/hailey-python")
leaveMessage = ("Goodbye, it was fun. Have a good time in other servers, hope to see you back soon!") #this might not always send
DISCORD_MEMBER_INTENT = True #set this to False if you don't want to enable the member intent. doing so will remove the join/leave messages i.e. welcomeMessage and leaveMessage.
