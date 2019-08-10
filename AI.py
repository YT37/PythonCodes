import pyttsx3, speech_recognition as sr, pyaudio, wikipedia, webbrowser,random
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def sub(a, b):
    return "".join(a.rsplit(b))
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("how can i help you")
        print("How can I help you?")
        print("Listening.....")
        r.energy_threshold = 200
        r.pause_threshold = 4
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said:{query}\n")
    except Exception:
        speak("Sorry , Please Type Your Query")
        query = str(input("Command: "))
        return query
    return query
def search():
    var1 = query
    var2 = "search"
    speak("What do you want to search")
    s = sub(var1, var2)
    webbrowser.open(f"https://www.google.com/search?q={s}")
def youtube():
    var1 = myCommand()
    var2 = "youtube"
    y = sub(var1, var2)
    webbrowser.open(f"https://www.youtube.com/search?q={y}")
def dictionary():
    var1 = query
    var2 = "tell me the meaning of"
    d = sub(var1, var2)
    webbrowser.open(f"https://www.collinsdictionary.com/dictionary/english/{d}")
def jokes():
    call = random.randint(0, 7)
    jokes = (
        "Martin Luther said that if u cannot fly, then run, if you cannot run, then walk, if you cant walk , then crawl , but keep moving . A guy responded o ta theek but where we have to go",
        "Teacher: What I ask give its answer quickly  ,  Sanju: ok, Sir,  Teacher: Tell the capital of India?  , Sanju: quickly",
        "Teacher (from Student): What is the use of semester system, tell?   , Student: The advantage is not known, but one thing is that insult happens only twice in a year.",
        "Engineering students - Sir, we have made such a thing in college ... with the help of which you can see across the wall ...  , Sir (happy) - Wow! Whats the matter ... What have you made?   ,   Student - Hole ... ??????????    Sir - Give slap ... give slap ...",
        'A teenage girl had been talking on the phone for about half an hour, and then she hung up."Wow!  ,   " said her father, "That was short. You usually talk for two hours. What happened?""Wrong number," replied the girl',
        "Teacher: - Money aside, on the other hand, choose the common sense, what will you choose? , Student: Money  ,  Teacher: - False, I choose common sense  ,  Student: - You are right, Madame, who has the shortage of things, he chooses the same ...............",
        'PUPIL: "Would you punish me for something I didn`t do?"  , TEACHER: Of course not  , PUPIL: Good, because I haven`t done my homework.',
        "Teacher: What are some products of the West Indies? , Student: I dont know. ,Teacher: Of course, you do. Where do you get sugar from?  , Student: We borrow it from our neighbor",
    )
    speak("ok! let me tell you a joke")
    speak(jokes[call])
def facts():
    facts = (
        "Mawsynram, a village on the Khasi Hills, Meghalaya, receives the highest recorded average rainfall in the world.",
        "Bandra Worli Sealink has steel wires equal to the earths circumference",
        "In September 2009, Indias ISRO Chandrayaan- 1 using its Moon Mineralogy Mapper detected water on the moon for the first time.",
        "India never invaded any country in her last 10000 years of history.",
        "The Worlds first university was established in Takshila in 700BC. ...",
        "The value of pi was first calculated by Budhayana, and he explained the concept of what is known as the Pythagorean Theorem. He discovered this in the 6th century long before the European mathematicians.",
        "Algebra, trigonometry and calculus came from India; Quadratic equations were by Sridharacharya in the 11th Century;The largest numbers the Greeks and the Romans used were 10^6(10 to the power of 6) whereas Hindus used numbers as big as 10^53(10 to the power of 53) with specific names as early as 5000 BCE during the Vedic period. Even today, the largest used number is Tera 10^12(10 to the power of 12).",
        "The second largest pool of engineers and scientists is from India.",
        "A cockroach can live a few weeks without its head. It will eventually die of hunger.",
        "Galileo Galilei’s middle finger is stored in The Museum of Science in Florence.",
        "The iPhone, the Harry Potter books, and the Rubik’s Cube are the top 3 most sold products in human history.",
        "THE RIG VEDA IS THE OLDEST KNOWN BOOK IN THE WORLD",
        "The original name in Sanskrit for Hinduism is Sanatana Dharma. The word Hindu or Indu was used by Greeks to describe the people living around the Indus River.",
    )
    speak("ok let me tell you some facts ")
    for i in range(3):
        call = random.randint(i, 13)
        speak(facts[call])
def maps():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Where Do You Want To Go")
        print("Listening.....")
        r.energy_threshold = 200
        r.pause_threshold = 4
        audio = r.listen(source)
    try:
        location = r.recognize_google(audio, language="en-in")
        speak("Showing The Route")
        return location
    except Exception:
        speak("Sorry, Please Type")
        location = str(input("Command: "))
        return location
    webbrowser.open(f"https://www.googlemaps.com/search?q={location}")
if __name__ == "__main__":
    while True:
        query = myCommand().lower()
        if "youtube" in query:
            webbrowser.open("youtube.com")

        elif "google" in query:
            webbrowser.open("google.com")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "news" in query:
            webbrowser.open("https://timesofindia.indiatimes.com")

        elif "shop" in query:
            webbrowser.open("https://www.amazon.in")

        elif "search" in query:
            search()

        elif "tell me the meaning" in query:
            dictionary()

        elif " bore" in query:
            jokes()

        elif "facts" in query:
            facts()

        elif "go to" in query:
            maps()

        elif "exit" in query:
            print("Exited")
            speak("Exiting")
            exit()