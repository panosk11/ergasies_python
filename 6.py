import sys, tweepy
key = "K9iNvrMKvXLuMkBodGyrCH1ZA"
secretkey = "cStr4kOz15Ay0fa7fG9SvlpxaNwmUbiDILnVYD5v4C7uZecFVW"
token = "796483476233011200-GP37CocDiR5ZRRh7VWazfFgTj8iTOWq"
secrettoken = "FoHVCBxJzx4oTOUvLrxFQ5uv8boWOw8DhlPGNTwMgE1gF"

auth = tweepy.OAuthHandler(key, secretkey)
auth.set_access_token(token, secrettoken)

api = tweepy.API(auth)                       

try:
    username = input("Δώσε μου το username του account που θες να ψάξεις: ")
    number_of_tweets= 10
    for i in range (9):
        timeline = api.user_timeline(screen_name=username, count=number_of_tweets, tweet_mode="extended")
        tweets = [tweet.full_text for tweet in timeline]
    a = tweets[0].split()
    b = tweets[1].split()
    c = tweets[2].split()
    d = tweets[3].split()
    e = tweets[4].split()
    f = tweets[5].split()
    g = tweets[6].split()
    h = tweets[7].split()
    i = tweets[8].split()
    j = tweets[9].split()

    k = a+b+c+d+e+f+g+h+i+j
    w = len(k)

    g=[0]*w
    for z in range (w):
        g[z]=len(k[z])

    temp=sorted(zip(k,g), key=lambda i:i[1], reverse=True)
    print ("Οι 5 μεγαλύτερες λέξεις των τελευταίων 10 tweets είναι οι : ")
    print (temp[0], temp[1], temp[2], temp[3], temp[4])
    print ("Οι 5 μικρότερες λέξεις των τελευταίων 10 tweets είναι οι : ")
    temp=sorted(zip(k,g), key=lambda i:i[1])
    print (temp[0], temp[1], temp[2], temp[3], temp[4])

except:
    print ("Δεν υπάρχει αυτό το username")