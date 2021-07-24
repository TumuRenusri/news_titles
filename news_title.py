import requests
api_key ="93f81dee4b6d4bd09274e6e9aaa46a22"
country=input("enter country name like India as in\n")
def news():
    print("--------------------------------News Headlines----------------------------------------")
    main_url ="https://newsapi.org/v2/top-headlines?country={}&apiKey={}".format(country,api_key)
    news=requests.get(main_url).json()
    article=news['articles']
    for arti in article:
        print(arti['title'],end="\n")
        print("-------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------")
news() 
