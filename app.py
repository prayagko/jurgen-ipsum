# app.py
import re
import random
import math
from flask import Flask, request, jsonify

app = Flask(__name__)

quotes = [
              "I never succeeded in bringing to the field what was going on in my brain. I had the talent for the fifth division, and the mind for the Bundesliga. The result was a career in the second division.",
              "He likes having the ball, playing football, passes. It’s like an orchestra. But it’s a silent song. I like heavy metal.",
              "It doesn’t make it any easier to run your heart out when you’ve just woken up in a five-star hotel. Too much comfort makes you comfortable.",
              "Mkhitaryan fits us like an arse on a bucket. What he offers is exactly what we need.",
              "You have to feel a defeat. You cannot say ‘I don’t care, it’s not important’. If I was allowed to say shit I would say shit but I’m not allowed!",
              "It was important and we lost, so that feels not too good. You always have to strike back. We can say all of these things, but you know you can fall down and then you have to stand up.",
              "We have a bow and arrow and if we aim well, we can hit the target. The problem is that Bayern has a bazooka. But then Robin Hood was quite successful.",
              "I’m a totally normal guy, I came from the Black Forest. I’m the Normal One.",
              "The only thing I can say is that it was great. The weather was good, everything is OK, only the result is shit.",
              "We’re facing the greatest challenge there is in football: to play against an Italian team that only needs a draw.",
              "I told my players during the break: Since we’re here anyway, we might actually play a bit of football.",
              "He’s leaving because he’s Guardiola’s favourite. If it’s anyone’s fault, it’s mine. I can’t make myself shorter and learn Spanish.",
              "If that’s not a bullshit story, I’ll eat a broomstick!",
              "Yes, it’s true. I underwent a hair transplant, I think the results are really cool, don’t you?",
              "It’s like Harry Potter – but it’s about football. There’s no Harry Potter flying on his fucking stick – just football.",
              "You can speak about spirit, or you can live it. We took the team to a lake in Sweden where there was no electricity. We went for five days without food.",
              "I couldn’t have been a rock star, although I do sing Country Road very loudly on the PlayStation.",
              "My players sleep in double rooms the night before the match. I hope that nothing happens.",
              "I got more in life than I was ever supposed to get – family, money, football. None of my teachers, or my parents, ever believed this would happen to me. So how can this perfect life of mine be spoilt because they take our players?",
              "It could have been a bit warmer.",
              "How do you explain to a blind person what colour is?",
              "I show my team very often Barcelona but not the way they play. Just the way they celebrate goals. Goal no 5768 in the last few weeks and they go ‘Yeeeess’ like they never scored a goal. This is what I love about football. That’s what you have to feel all the time. Until you die. And then everything is OK.",
              "I’m a bit proud of my first red card as a coach. I approached the fourth official and said: ‘How many mistakes are allowed here, if it’s 15, you have one more.’",
              "Does anyone in this room think that I can do wonders? I’m a normal guy from the Black Forest. My mother is very proud. I am the normal one.",
              "I’m not a dreamer but I’m a romantic. I love the stories and Anfield is one of the best places in the football world. Now I’m here. I’m a lucky guy and really looking forward to the first match.",
              "I am not the guy who is going to go out and shout ‘we are going to conquer the world’ or something like this. But we will conquer the ball. Yeah? Each fucking time!",
              "We don’t have to sprinkle magical dust on them; ‘and now you can play football.’ They know how to play.",
              "I would really like to change my personality but I can’t forget this fucking loss against Crystal Palace.",
              "My glasses are in the Borussia Dortmund museum. When we beat Bayern, Nuri Sahin did it. I don’t know what it looked like at the end – I lost my glasses! I have a second pair of glasses but it is hard to find them without my glasses!",
              "We can change nothing now, but we can change something tomorrow morning. Tonight, we feel rubbish. OK, we feel shit.",
              "The best word I can say to describe this is: Boom!",
              "If someone is silly enough to want to see my face for 90 minutes during a game I cannot change the world.",
              "We had a good plan in the first half but conceded two goals. So you can throw your plan in the purple bin.",
              "We watched all of them 500 million times!",
              "When BVB last won here, most of my players were still being breastfed.",
              "Crazy players love me – I don’t know why.",
              "When I left School, the head said, ‘I hope you can do something in football because, if not, I have not the best feeling for your future’.",
              "These young players are our future. If we handle them like horses then we get horses.",
              "We will wait for him like a good wife waiting for her husband who is in jail.",
              "Here’s something everyone inside Anfield knows, including our opponents. This Liverpool never stops. This Liverpool never shut down. This Liverpool gives it all at all times.",
              "It was too much. It was overwhelming.",
              "It’s 10 past 10, the children are probably in bed. These boys are fucking unbelievable. Fine me if you want.",
              "The whole performance was too much, it was overwhelming. In my life I’ve watched many football games and I can never a match like this.",
              "What a performance. It’s just unbelievable.",
              "I seen the ball flying in the goal (4-0), Ben Woodburn looked at me and said ‘what happened?’.",
              "I saw James Milner crying on the pitch after the game. It means so much to all of us. It’s the best phase of football. There are more important things in the world. But creating this emotional atmosphere together is so special. It’s all about the players.",
              "I told the boys before it was impossible, but because it’s you boys, we have a chance."
         ]

@app.route("/api")
def jurgenIpsum():
    query = request.args
    number = query.get('number', 6)

    try:
        number = int(number)
    except ValueError:
        return jsonify({'ok': False, 'message': "Invalid 'number' value"}), 400
    
    textType = query.get('text-type', 'sentence')

    quotesString = ' '.join(sentence for sentence in quotes)
    sentenceList = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', quotesString)
    if textType.lower() == 'sentence':
        ipsum = [sentenceList[random.randint(0,(len(sentenceList)-1))] for n in range(number)]
        ipsum = [' '.join(sentence for sentence in ipsum)]
    
    elif textType.lower() == 'paragraph':
        ipsum = []
        for n in range(number):
            para = [sentenceList[random.randint(0,(len(sentenceList)-1))] for i in range(6)]
            para = [' '.join(sentence for sentence in para)]
            ipsum += para    
    else:
        return jsonify({'ok': False, 'message': "text-type must be either 'sentence' or 'pargraph'"}), 400
    

    return jsonify({'ok': True, 'data':ipsum})