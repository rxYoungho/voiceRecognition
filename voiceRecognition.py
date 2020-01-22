import speech_recognition as sr
import webbrowser

repeat = 1

while repeat != 0: 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        text = r.recognize_google(audio)
    
        print("You said : {}".format(text))
            
        if text == "Google": 
            url = "http://www.google.com"
            webbrowser.open(url) #This opens without any condition!!!! error!!
            text = ""
            repeat = 0
        
        if text == "webtoon":
            url = "https://comic.naver.com/webtoon/list.nhn?titleId=670143&weekday=wed"
            webbrowser.open(url) #This opens without any condition!!!! error!!
            text = ""
            repeat = 0


        else:
            repeat = 1
            text = ""
    
# with sr.Microphone() as source:
#     print("Speak Anything :")
#     audio = r1.listen(source)
#     text = r1.recognize_google(audio)
#     print("You said : {}".format(text))
#     if 'webtoon' or 'web toon' or 'Webtoon' in text:
#         url = "https://comic.naver.com/webtoon/list.nhn?titleId=670143&weekday=wed"
#         webbrowser.open(url)
    
    
    # if 'Naver' or 'naver' in text:
    #     url = "http://www.naver.com"
    #     webbrowser.open(url, new=new)
    # if 'helper' or 'Helper' in text:
    #     url = "https://comic.naver.com/webtoon/list.nhn?titleId=670143&weekday=wed"
    #     webbrowser.open(url, new=new)
    # if 'youtube' or 'Youtube' in text:
    #     url = "http://www.youtube.com"
    #     webbrowser.open(url, new=new)
    # if 'github' or 'Github' in text:
    #     url = "https://github.com/RelaxDanny?tab=repositories"
    #     webbrowser.open(url, new=new)
    # 