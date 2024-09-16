import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class Error(Exception):
    pass
class Name_Not_Found_Error(Error):
    pass


class Mark_Book:

    def __init__(self,names):
        self.names = names   
        self.stu_scores = {}
        self.stu_scores_avg = {}
        self.cla_scores_avg = 0

    def stu_score(self,score):
        """Appends new score to existing score in dictionary."""
        for key, value in score.items():
            if key not in self.stu_scores.keys():
                self.stu_scores[key] = [value]
            else:
                self.stu_scores[key].append(value)
    
    def stu_score_avg(self):
        """You know what this does."""
        for key, value in self.stu_scores.items():
            self.stu_scores_avg[key] = sum(value)/len(value)

    def cla_score_avg(self):
        """Calculates class average."""
        for value in self.stu_scores_avg.values():
            self.cla_scores_avg += value
        self.cla_scores_avg = self.cla_scores_avg/len(self.stu_scores_avg.values())
    
    def next_stu_score(self,name):
        """Uses linear regression to predict a student's next score."""
        if name not in self.names:
            raise Name_Not_Found_Error
        else:
            df = pd.DataFrame([[x] for x in self.stu_scores[name]],columns=[name])

            model = LinearRegression()
            model.fit(df.index.values.reshape(-1, 1),df[[name]].values.reshape(-1, 1))

            next_score = model.predict(np.array([len(self.stu_scores[name])]).reshape(-1, 1))
            print(f"{name}'s next score is predicted to be {next_score[0][0]}.")

    
Mark_1 = Mark_Book(['Ryan','Peter','Thomas','Ares','Anson','Lomax'])
Mark_1.stu_score({'Thomas':23,'Ryan':49,'Ares':12,'Anson':39,'Lomax':30,'Peter':99})
Mark_1.stu_score({'Thomas':25,'Ryan':51,'Ares':14,'Anson':41,'Lomax':32,'Peter':101})
Mark_1.stu_score({'Thomas':27,'Ryan':53,'Ares':16,'Anson':43,'Lomax':34,'Peter':103})
Mark_1.stu_score({'Thomas':29,'Ryan':55,'Ares':18,'Anson':45,'Lomax':36,'Peter':105})
Mark_1.stu_score({'Thomas':31,'Ryan':57,'Ares':20,'Anson':47,'Lomax':38,'Peter':107})
Mark_1.stu_score_avg()
Mark_1.cla_score_avg()
print(Mark_1.stu_scores)
print(Mark_1.stu_scores_avg)
print(Mark_1.cla_scores_avg)
Mark_1.next_stu_score('Thomas')


