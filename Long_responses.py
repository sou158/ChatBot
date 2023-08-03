import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = ["sucess is not final;failure is not fatal;it is the courage to continue that counts","Life is what happens when you're busy making other plans","if you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."][random.randrange(3)]
R_JOKE= ["i want to die peacefully in my sleep like my grandfather not  screaming like the passengers in his car","I was going to tell you a joke about boxing but I forgot the punch line.","I ordered a chicken and an egg from Amazon. I'll let you know."][random.randrange(3)]
R_PICKUP = "Feel my shirt you know what it's made of?..Husband Material"



def unknown():
    response = [
                "what do you mean?",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(3)]
    return response
