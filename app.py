from flask import Flask,render_template,request
# EDA
import random


app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():    
    return render_template('index.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():  
    

    # ratingsfile = os.path.join(app.static_folder, 'test_ratings.csv')
    # ratings = pd.read_csv(ratingsfile)    
   
    userid = int(request.form.get("userid"))    
  
   
    # Dict of all songs that are interacted with by each user
    # user_interacted_songs = ratings.groupby('User ID')['Song ID'].apply(list).to_dict()
    # user_interacted_songs = random.randint(10, 100)
   

    top10_songs = []
    for a in range(0,10): 
        top10_songs.append(random.randint(userid, 50000))

    songid = [userid]
    for a in range(0,10): 
        songid.append(random.randint(400, 90000))
  

    return render_template('recommendation.html', recommendations= top10_songs, songs=songid)

if __name__=="__main__":
    app.run(debug=True)



