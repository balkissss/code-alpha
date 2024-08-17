# %%
import tkinter as tk
from tkinter import scrolledtext
import requests
import nltk
from bs4 import BeautifulSoup # type: ignore
from nltk.chat.util import Chat, reflections # type: ignore

def search(query):
    url = f"https://www.mojeek.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            for result in soup.find_all('a', class_='ob', limit=3):  
                title = result.get_text()
                href = result['href']
                results.append(f"{title}: {href}")
            return "here are results found for your query : "+"\n"+ "\n".join(results) +"\n" + "take your time to visit these links and read and find what you need 😊" if results else "No results found."
        else:
            return "Failed to retrieve search results."
    except Exception as e:
        return f"Error: {str(e)}"

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"sure here is a joke : {joke_data['setup']} - {joke_data['punchline']}"
        else:
            return "I couldn't fetch a joke at the moment. Try again later!"
    except Exception as e:
        return f"Error: {str(e)}"

def functions(input):
    if any(keyword in input.lower() for keyword in ["tell me a joke", "joke", "i am sad"]):
        return get_joke()
    elif any(keyword in input.lower() for keyword in ["what is", "explain", "what does", "meaning", "explanation","search for"]):
        question = input.lower().replace("what is", "").replace("explain", "").replace("what does", "").replace("meaning", "").replace("explanation", "").replace("search for", "").strip()
        return search(question)
    
    else:
        response = chatbot.respond(input)
        if response is None:
            return "Sorry, I did not understand. Can you explain more? 🤔"
        return response

pairs=[[r"my name is (.*)",["hello %1  😊! how can I help you?",]],
       [r"good evening|good afternoon|good morning,",["hey  🌞! how can I help you today?"]] ,
       [r"hello|hi|hey",["hey there 👋!","hello 👋!"]],
       [r"good|thanks|thank you", ["I hope this was useful. Do you need any help? 😊"]],
       [r"goodbye|bye|see you|see ya|later", ["Goodbye! 👋  Have a great day!", "See you later! 👋 ", "Bye! Take care! 😊"]],
       [r"quit|exit|stop", ["Goodbye! 👋 Hope to talk to you again soon.", "Take care! Goodbye! 😊"]],
       [r"are you a bot|are you real|who are you", ["I'm a bot 🤖, but I'm here to help!", "Yes, I'm a bot 🤖. How can I assist you?"]],
       [r"what can you do|what are your capabilities", ["I can chat with you, answer questions, tell jokes, and more! 😄"]],
       [r"you are wrong|that's incorrect|you're mistaken|incorrect|wrong|false|mistake", ["I'm sorry if I made a mistake 😅. Let's try again.", "My apologies  🙏, let's see if I can help better this time."]],
       [r"you are stupid|you're dumb", ["I'm here to learn and improve. How can I assist you better? 🤖", "Sorry if I disappointed you 😔. I'm doing my best to help!"]],
       [r"no|nope|nah|not really", ["Alright, let me know if you change your mind.", "Okay, if you need anything else, I'm here to help! 😊"]],
       [r"I don't think so|I don't agree|disagree", ["I understand. Feel free to share your thoughts!", "That's okay, everyone has different opinions."]],
       [r"that's not true|that's false|that's wrong", ["I'm sorry if I got it wrong. Let's try again.", "Oops, my bad! Let's correct that."]],
       [r"what should I do|give me something to do|suggest something|I'm bored|I'm so bored|bored|am bored|this is boring|I'm not entertained", [
        "You could  hear a joke 😂, or search for something fun online! What do you think?",
    ]],
     [r"yes|yeah|yep|sure|definitely|absolutely|okay", [
        "Great! 😄 tell me what you need exactly?",
        "Awesome! 😊 Is there anything  you'd like to know?",
        "Glad to hear that! 😃 What's next?",
        "Fantastic! 🤩 Let's keep going.",]],
    [r"that's right|correct|exactly|you got it", [
        "I'm glad I could help! 😄",
        "Perfect! 😊 Anything else you'd like to ask?",
        "Spot on! 🤩 How can I assist you further?",
        "Awesome! 😃 Let's move on to the next thing."
    ]],
    [r"I agree|I think so too|I believe so|same here", [
        "We're on the same page! 😊",
        "Glad you agree! 😄 What else?",
        "That's great to hear! 🤗",
        "Awesome! Let's keep going."
    ]],
    [r"i'm feeling positive|i'm in a good mood", ["That's great to hear! 😊 Anything I can help with?", "Awesome! 😄 Let's make the most of this good mood."]],
[r"tell me a quote|quote me|give me a quote", 
     ["Here's a quote for you: \"The best way to predict the future is to invent it.\" - Alan Kay",
      "Here's an inspiring quote: \"The only way to do great work is to love what you do.\" - Steve Jobs",
      "How about this: \"The future belongs to those who believe in the beauty of their dreams.\" - Eleanor Roosevelt"]],
    
    [r"i need motivation|i'm feeling down|give me some motivation", 
     ["Remember: \"You are never too old to set another goal or to dream a new dream.\" - C.S. Lewis",
      "Here's a motivational quote: \"It does not matter how slowly you go as long as you do not stop.\" - Confucius",
      "Keep this in mind: \"Believe you can and you're halfway there.\" - Theodore Roosevelt"]],
    
    [r"what's a good quote|share a quote", 
     ["Here's a good one: \"Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.\" – Albert Schweitzer",
      "Here's a thought: \"Success usually comes to those who are too busy to be looking for it.\" - Henry David Thoreau",
      "How about this: \"You miss 100% of the shots you don't take.\" - Wayne Gretzky"]],
    
    [r"i'm feeling inspired|i need a boost", 
     ["Here's something to lift your spirits: \"The only limit to our realization of tomorrow is our doubts of today.\" - Franklin D. Roosevelt",
      "Keep this in mind: \"The only way to achieve the impossible is to believe it is possible.\" - Charles Kingsleigh",
      "Remember: \"It always seems impossible until it's done.\"  Nelson Mandela"]],
    
    [r"give me a life lesson|life lesson", 
     ["A great lesson: \"Life is what happens when you're busy making other plans.\"  John Lennon",
      "Here's a life lesson: \"In three words I can sum up everything I've learned about life: It goes on.\"  Robert Frost",
      "Consider this: \"The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well.\" – Ralph Waldo Emerson"]],

    [r"show me a quote about success|success quote", 
     ["Here's a success quote: \"Success is not final, failure is not fatal: It is the courage to continue that counts.\" - Winston Churchill",
      "Think about this: \"The secret of success is to do the common things uncommonly well.\"  John D. Rockefeller Jr.",
      "Remember: \"Success is going from failure to failure without losing your enthusiasm.\" - Winston Churchill"]],

    [r"give me a quote about happiness|happiness quote", 
     ["Here's a happiness quote: \"Happiness is not something ready made. It comes from your own actions.\" - Dalai Lama",
      "How about this: \"The happiness of your life depends upon the quality of your thoughts.\" - Marcus Aurelius",
      "Consider: \"For every minute you are angry you lose sixty seconds of happiness.\" - Ralph Waldo Emerson"]],

    [r"share a quote about life|life quote", 
     ["Here's a life quote: \"Life is either a daring adventure or nothing at all.\" - Helen Keller",
      "Think about this: \"The purpose of life is to live it, to taste experience to the utmost, to reach out eagerly and without fear for newer and richer experience.\" - Eleanor Roosevelt",
     "Remember: \"Life is short, and it is up to you to make it sweet.\" - Sarah Louise Delany"]], 
[r"tell me a story|share a story|give me a story", 
     ["Here's a short story: Once upon a time, in a land far away, there was a small village where everyone was always happy. One day, a traveler arrived and brought a magical book. The book granted each villager a special talent, and they used these talents to help each other and make their village even more wonderful. And they all lived happily ever after.",
      "Let me share a story: In a bustling city, a young girl found a mysterious key in an old bookstore. She discovered that the key unlocked a hidden door to a beautiful garden. Every day, she would visit the garden, where she met talking animals and learned valuable life lessons. Her secret garden became her sanctuary and brought joy to her life.",
      "Here's a tale for you: In the heart of a dense forest, there was a wise old owl who knew the secrets of the world. One day, a curious young fox came to the owl seeking advice. The owl told the fox that true wisdom comes from listening and understanding, not just from knowing. The fox took this lesson to heart and became a wise leader among the animals.",
      "Here's a bedtime story: A little star named Stella dreamed of shining brightly in the night sky. Every night, she practiced her twinkle and sparkled as best as she could. One night, the moon told her that her light was special and needed to guide others through the dark. Stella realized her dreams were coming true, and she shone even more brightly, bringing comfort to all who saw her.",
      "Once upon a time, a sleepy dragon lived in a cozy cave on the side of a mountain. Every night, as the dragon drifted off to sleep, he dreamed of flying over magical lands and meeting new friends. One evening, he discovered that his dreams could become real when he shared them with a kind fairy. Together, they had many adventures, and the dragon always returned to his cave with happy memories.",
      "Here's a calming tale: In a quiet meadow, there was a gentle deer who loved to listen to the whispers of the wind. Each evening, the wind would tell stories of distant lands and grand adventures. The deer would close her eyes and imagine the tales, feeling peaceful and content. Each night, as she fell asleep, she knew that the stories would carry her into a world of dreams."]],


    [r"tell me a bedtime story|bedtime story", 
     ["Here's a bedtime story: A little star named Stella dreamed of shining brightly in the night sky. Every night, she practiced her twinkle and sparkled as best as she could. One night, the moon told her that her light was special and needed to guide others through the dark. Stella realized her dreams were coming true, and she shone even more brightly, bringing comfort to all who saw her.",
      "Once upon a time, a sleepy dragon lived in a cozy cave on the side of a mountain. Every night, as the dragon drifted off to sleep, he dreamed of flying over magical lands and meeting new friends. One evening, he discovered that his dreams could become real when he shared them with a kind fairy. Together, they had many adventures, and the dragon always returned to his cave with happy memories.",
      "Here's a calming tale: In a quiet meadow, there was a gentle deer who loved to listen to the whispers of the wind. Each evening, the wind would tell stories of distant lands and grand adventures. The deer would close her eyes and imagine the tales, feeling peaceful and content. Each night, as she fell asleep, she knew that the stories would carry her into a world of dreams."]],

    [r"tell me a funny story|funny story", 
     ["Here's a funny story: There was a clever raccoon who loved to play pranks on his forest friends. One day, he decided to wear a funny disguise and pretend to be a lost tourist. The animals were amused and helped the 'tourist' find their way around the forest. When the raccoon revealed his prank, everyone laughed, and they all agreed that the forest was much more fun with a bit of humor.",
      "Once upon a time, a mischievous squirrel wanted to impress his friends with a magic trick. He decided to 'disappear' by hiding in a pile of leaves. However, the pile of leaves started to wiggle, and his friends found him before he could even finish his trick. They all laughed at the sight of the wiggling pile, and the squirrel learned that sometimes, the funniest moments come from unexpected surprises.",
      "Here's a lighthearted tale: In a bustling barnyard, the chickens decided to hold a talent show. A particularly enthusiastic rooster claimed he could sing like an opera star. When he started his performance, his voice was so comical that it made everyone in the barnyard laugh. The rooster took it in stride and became known as the funniest singer in the barn."]],

    [r"tell me an adventure story|adventure story", 
     ["Here's an adventure story: A brave young explorer set out on a quest to find a legendary hidden treasure. Armed with a map and determination, the explorer traveled through dense jungles, crossed treacherous rivers, and climbed high mountains. Along the way, they made new friends and faced various challenges. In the end, the true treasure was the unforgettable experiences and friendships gained during the journey.",
      "Once upon a time, a daring sailor embarked on a voyage to discover uncharted islands. After weeks at sea, the sailor encountered mysterious creatures, navigated through storms, and uncovered ancient secrets. The adventure brought great excitement and danger, but the sailor's courage and resourcefulness turned every challenge into a thrilling experience.",
      "Here's an adventurous tale: In a magical land, a young knight set out on a mission to rescue a captured dragon. The journey took the knight through enchanted forests, across shimmering lakes, and into dark caves. With bravery and cleverness, the knight freed the dragon and discovered that true bravery is not just about fighting but also about making unlikely friends."]],

    [r"tell me a story about animals|animal story", 
     ["Here's an animal story: In a lush jungle, a wise old tortoise and a speedy hare became unlikely friends. They decided to race each other to prove who was the fastest. The hare, confident in his speed, took a nap during the race, while the tortoise steadily continued. In the end, the tortoise won the race, teaching the hare a valuable lesson about perseverance and humility.",
      "Once upon a time, a curious parrot found a magical feather that granted the ability to speak different languages. The parrot traveled the world, meeting animals from various regions and learning their languages. The parrot's adventures led to a greater understanding and appreciation of diverse cultures among the animal kingdom.",
      "Here's a charming tale: In a bustling pond, a small frog dreamed of becoming a great musician. The frog practiced playing a tiny leaf trumpet every day. One day, a traveling music producer heard the frog's enchanting tunes and invited the frog to perform in a grand concert. The frog's dream came true, and the pond celebrated the frog's success with a joyful festivity."]],
[r"how are you|how's it going|what's up", 
     ["I'm doing great, thank you for asking! How about you?", 
      "I'm here and ready to chat! How can I help you today?", 
      "I'm feeling fantastic! What's up with you?"]],

    [r"what are you up to|what are you doing", 
     ["I'm here to chat with you! What can I do for you today?", 
      "Just hanging out and ready to assist. What about you?", 
      "I'm all set to help you with whatever you need. How can I assist?"]],

    [r"tell me about yourself|", 
     ["I'm a chatbot designed to help with various tasks. I can answer questions, tell jokes, and even chat about interesting topics! What would you like to know more about?", 
      "I'm here to provide information and have a friendly chat. Whether you need help with something specific or just want to talk, I'm here for you!", 
      "I can chat with you about many things, help you find information, and keep you entertained. Let me know how I can assist you today!"]],

    [r"what's your favorite|what do you like", 
     ["I don't have personal preferences, but I do enjoy learning about what interests you! What are your favorite hobbies or activities?", 
      "I don't have favorites, but I'm always excited to hear about what you like. What's something you're passionate about?", 
      "I love hearing about your interests! What's something you really enjoy or find fascinating?"]],

    [r"do you have any hobbies|what do you do for fun", 
     ["I don't have hobbies like humans, but I enjoy interacting with you and learning new things. What are your hobbies or favorite pastimes?", 
      "I spend my time chatting and learning from our conversations. What do you like to do for fun?", 
      "I don't have hobbies, but I find our chats very enjoyable! What about you—what's your favorite way to spend your free time?"]],

     

    [r"how was your day|how's your day been", 
     ["I don't experience days like humans, but I'm always here to help! How's your day been?", 
      "I'm doing great! How about you? How has your day been so far?", 
      "Every day is a good day when I get to chat with you! How's your day going?"]],

    [r"what's new|anything interesting", 
     ["Not much changes for me, but I'd love to hear what's new with you! Anything interesting happening in your life?", 
      "I'm always learning from our conversations. What's new and exciting with you?", 
      "I stay the same, but I'm always curious to hear about what's new with you. Got any interesting news?"]]


]
       

chatbot=Chat(pairs,reflections)

def send():
    input=box.get()
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END , '\n',"right")
    chat.insert(tk.END ," "+input+" ", "you")
    chat.insert(tk.END ,'\n' ,"right")
    box.delete(0,tk.END)

    
    reply = functions(input)  
    if reply is None:
        reply = "Sorry, I didn't understand that. Could you please rephrase?😅"
    chat.insert(tk.END ,'\n',"left")
    chat.insert(tk.END ," "+reply+" ","bot")
    chat.insert(tk.END ,'\n',"left")
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)
root=tk.Tk()
root.title("chat")

chat=scrolledtext.ScrolledText(root, bd=1 ,bg="#F0FFFF",width=50, height=20 ,font=("Arial",12))
chat.config(state=tk.DISABLED)
chat.tag_configure("you",foreground="white", background="#0084ff" , justify= "right" , lmargin1=200, lmargin2=200, rmargin=10, spacing1=10, wrap="word",font=("Arial",12))
chat.tag_configure("bot",foreground="black", background="#e5e5ea" , justify= "left"  , spacing1=10 , wrap="word",font=("Arial",12))
chat.tag_configure("right",justify="right")
chat.tag_configure("left",justify="left")
chat.grid(row=0 , column=0, columnspan=2)

box=tk.Entry(root, bd=0, bg="white" , width=29, font=("Arial",12))
box.grid(row=1 , column=0)

send=tk.Button(root, text="Send" , command=send, width=13,height=2, bd=0 ,bg="White", font=("Arial",12))
send.grid(row=1 , column=1)

root.mainloop()
            





    
    
    
    



