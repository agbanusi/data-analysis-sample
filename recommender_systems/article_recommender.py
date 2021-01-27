import pandas as pd
import os

def article_recommendation():
    dir_ ='./json_data/'
    json_data = [i for i in os.listdir(dir_)]
    
    # for content based recomender system, I'll use notification,thoughts, following, contact
    json_data =[ json_data[2],json_data[4],json_data[5],json_data[6]]
    jn =[]
    #create a list of the dataframes
    for i in range(len(json_data)):
        jsn= pd.read_json(dir_+ json_data[i])
        jn.append(jsn)

    jj = jn[2].copy()
    #jn[2].dropna(axis=1,inplace = True)
    jn[3]['tags'] = jj['tags']
    #jn[1].dropna(axis=1,inplace = True)
    df1 = pd.merge_ordered(jn[1],jn[2],on='id')    
    df1['action'] = jn[1]['action']

    features = ['title', 'content', 'tags']
    for feature in features:
        df1[feature] = df1[feature].fillna('')


    df1['titler'] = [str.lower(i) for i in df1['title']]    
    df1['features'] = df1['title']+' '+df1['content']+' '+df1['tags']
    df1['combine_features'] =  [str.lower(i) for i in df1['features']]

    # get the title of an article
    def get_title_from_id(id_):
        titles = df1[df1.id==id_].title
        return titles.values[0]

    # get the title of the index
    def get_title_from_index(index):
        titles = df1[df1.index == index].title
        return titles.values[0]
    
    # Get the actions
    def check_action(id_):
        action = df1[df1.id==id_].action
        return action.values[0]
    
    #Get content title and return similar articles
    def content_recommender(titles,df1=df1):
        try:
            titles = str.lower(titles)
            from sklearn.feature_extraction.text import CountVectorizer
            count = CountVectorizer(stop_words='english')
            count_matrix = count.fit_transform(df1['combine_features'])
            from sklearn.metrics.pairwise import cosine_similarity
            cosine_sim= cosine_similarity(count_matrix)
            ind = pd.Series(df1.index, index=df1['title'])
        
            idx = ind[titles] 
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, reverse=True)
            sim_scores = sim_scores[1:50]
            reco = [i[0] for i in sim_scores]
            gg = df1['title'].iloc[reco]
            cg = df1['action'].iloc[reco]
            ggg = pd.DataFrame([gg,cg],).transpose()
            cgg = ggg.groupby('title')['action'].count().sort_values(ascending = False)
            cb = []
            for i in range(1,11):
                cb.append(cgg.index[i])
            x = pd.Series(cb)
            return x
        except KeyError:
            cc = df1.groupby('title')['action'].count().sort_values(ascending = False) 
            ce = []
            for i in range(1,11):
                ce.append(cc.index[i])
                y = pd.Series(ce)
            return y
    
    # Get the most popular articles
    def action_recommender(id_):
        action = check_action(id_)
        if (action=='Liked' or action=='Loved' or action=='commented' or action == 'Followed'):
            title = get_title_from_id(id_)
            return content_recommender(title,df1)
        else:
            return None
    
    article = input('Input the article title: ')
    #simple Test for a already known title  
    test = content_recommender(article)

    print('\t',"Top 10 Recommended Articles",'\n',test)

if __name__=='__main__':
    article_recommendation()

