import sys
import os
import numpy as np
from sklearn.metrics import mean_absolute_error
from scipy.stats import pearsonr
import json
import pandas as pd
import re
import logging
import argparse


def write_file(file,cores):
    with open(file, 'w', encoding="utf-8") as f:
        f.write(cores)
def f1_score(tp,fp,fn):
    precision=tp/fp
    recall=tp/fn
    f1=(2*precision*recall)/(precision+recall)
    return precision,recall,f1
def task1_score(pred_data,ans_data,scores):
    ans_v=[]
    ans_a=[]
    pred_v=[]
    pred_a=[]
    for i in range(len(ans_data)):

        sentence_id = ans_data.iloc[i]['ID']
        ans=ans_data.iloc[i]['Intensity'].split(')')
        del ans[-1]
        ans_aspect=[p.replace('(','').split(',')[0] for p in ans]
        ans_va=[p.replace('(','').split(',')[1] for p in ans]
        id=pred_data.index[pred_data["ID"] == sentence_id].tolist()[0]
        pred=pred_data.iloc[id]['Intensity'].split(')')
        del pred[-1]
        pred_aspect=[p.replace('(','').split(',')[0] for p in pred]
        pred_va=[p.replace('(','').split(',')[1] for p in pred]
        for i in range(len(pred_aspect)):
            ans_index=ans_aspect.index(pred_aspect[i])
            ans_v.append(float(ans_va[ans_index].split('#')[0]))
            ans_a.append(float(ans_va[ans_index].split('#')[1]))
            pred_v.append(float(pred_va[i].split('#')[0]))
            pred_a.append(float(pred_va[i].split('#')[1]))

    mae_v=mean_absolute_error(pred_v,ans_v)
    mae_a=mean_absolute_error(pred_a,ans_a)
    pearson_v=pearsonr(pred_v,ans_v)[0]
    pearson_a=pearsonr(pred_a,ans_a)[0]
    scores['Valance MAE']=mae_v
    scores['Valance PCC']=pearson_v
    scores['Arousal MAE']=mae_a
    scores['Arousal PCC']=pearson_a
    return scores
    
def task2_score(pred_data,ans_data,scores):
    ans_v=[]
    ans_a=[]
    pred_v=[]
    pred_a=[]
    tp_va,tp_v,tp_a,fp,fn=0,0,0,0,0
    for i in range(len(ans_data)):
        sentence_id = ans_data.iloc[i]['ID']
        ans=ans_data.iloc[i]['Triplets'].split(')')
        del ans[-1]
        ans_va=[p.replace('(','').split(',')[3].upper() for p in ans]
        ans_aspect=[p.replace('(','').split(',')[0].upper() for p in ans]
        ans_opinion = [p.replace('(','').split(',')[2].upper() for p in ans]
        id=pred_data.index[pred_data["ID"] == sentence_id].tolist()[0]
        if pd.isna(pred_data.iloc[id]['Triplets']):
            fp+=0
            fn+=len(ans_aspect)
        else:
            pred=pred_data.iloc[id]['Triplets'].split(')')
            del pred[-1]
            pred_aspect=[p.replace('(','').split(',')[0].upper() for p in pred]
            pred_opinion=[p.replace('(','').split(',')[1].upper() for p in pred]
            pred_va=[p.replace('(','').split(',')[2].upper() for p in pred]
            for i in range(len(pred_aspect)):
                for k in range(len(ans_aspect)):
                    ans_v=(int(round(float(ans_va[k].split('#')[0]),0)))
                    ans_a=(int(round(float(ans_va[k].split('#')[1]),0)))
                    pred_v=(int(round(float(pred_va[i].split('#')[0]),0)))
                    pred_a=(int(round(float(pred_va[i].split('#')[1]),0)))
                    if ans_v == pred_v and pred_aspect[i] == ans_aspect[k] and pred_opinion[i] ==ans_opinion[k]:
                        tp_v+=1
                    if ans_a == pred_a and pred_aspect[i] == ans_aspect[k] and pred_opinion[i] ==ans_opinion[k]:
                        tp_a+=1
                    if ans_v == pred_v and ans_a == pred_a and pred_aspect[i] == ans_aspect[k] and pred_opinion[i] ==ans_opinion[k]:
                        tp_va+=1
            fp+=len(pred_aspect)
            fn+=len(ans_aspect)

    precision_v,recall_v,f1_v=f1_score(tp_v,fp,fn)
    scores['V_Tri-Pre']=precision_v
    scores['V_Tri-Rec']=recall_v
    scores['V_Tri-F1']=f1_v
    precision_a,recall_a,f1_a=f1_score(tp_a,fp,fn)
    scores['A_Tri-Pre']=precision_a
    scores['A_Tri-Rec']=recall_a
    scores['A_Tri-F1']=f1_a
    precision_va,recall_va,f1_va=f1_score(tp_va,fp,fn)
    scores['VA_Tri-Pre']=precision_va
    scores['VA_Tri-Rec']=recall_va
    scores['VA_Tri-F1']=f1_va
    return scores

def task3_score(pred_data,ans_data,scores):
    ans_v,ans_a,pred_v,pred_a=[],[],[],[]
    tp_va,tp_v,tp_a,fp,fn=0,0,0,0,0
    total=0
    # print(ans_data)
    for i in range(len(ans_data)):
        sentence_id = ans_data.iloc[i]['ID']
        ans=ans_data.iloc[i]['Quadruples'].split(')')
        del ans[-1]
        ans_va=[p.replace('(','').split(',')[3].upper() for p in ans]
        ans_aspect=[p.replace('(','').split(',')[0].upper() for p in ans]
        ans_cat=[p.replace('(','').split(',')[1].upper() for p in ans]
        ans_opinion = [p.replace('(','').split(',')[2].upper() for p in ans]
        id=pred_data.index[pred_data["ID"] == sentence_id].tolist()[0]
        if pd.isna(pred_data.iloc[id]['Quadruples']):
            fp+=0
            fn+=len(ans_aspect)
        else:
            pred=pred_data.iloc[id]['Quadruples'].split(')')
            del pred[-1]
            pred_aspect=[p.replace('(','').split(',')[0].upper() for p in pred]
            pred_cat=[p.replace('(','').split(',')[1].upper() for p in pred]
            pred_opinion=[p.replace('(','').split(',')[2].upper() for p in pred]
            pred_va=[p.replace('(','').split(',')[3].upper() for p in pred]
            for i in range(len(pred_aspect)):
                for k in range(len(ans_aspect)):
                    ans_v=(int(round(float(ans_va[k].split('#')[0]),0)))
                    ans_a=(int(round(float(ans_va[k].split('#')[1]),0)))
                    pred_v=(int(round(float(pred_va[i].split('#')[0]),0)))
                    pred_a=(int(round(float(pred_va[i].split('#')[1]),0)))
                    if ans_v == pred_v and pred_aspect[i] == ans_aspect[k] and ans_cat[k]==pred_cat[i] and pred_opinion[i] ==ans_opinion[k]:
                        tp_v+=1
                    if ans_a == pred_a and pred_aspect[i] == ans_aspect[k] and ans_cat[k]==pred_cat[i] and pred_opinion[i] ==ans_opinion[k]:
                        tp_a+=1
                    if ans_v == pred_v and ans_a == pred_a and pred_aspect[i] == ans_aspect[k] and ans_cat[k]==pred_cat[i] and pred_opinion[i] ==ans_opinion[k]:
                        tp_va+=1
            total+=len(pred_aspect)
            
            fp+=len(pred_aspect)
            fn+=len(ans_aspect)

    precision_v,recall_v,f1_v=f1_score(tp_v,fp,fn)
    scores['V_Quat-Pre']=precision_v
    scores['V_Quat-Rec']=recall_v
    scores['V_Quat-F1']=f1_v
    precision_a,recall_a,f1_a=f1_score(tp_a,fp,fn)
    scores['A_Quat-Pre']=precision_a
    scores['A_Quat-Rec']=recall_a
    scores['A_Quat-F1']=f1_a
    precision_va,recall_va,f1_va=f1_score(tp_va,fp,fn)
    scores['VA_Quat-Pre']=precision_va
    scores['VA_Quat-Rec']=recall_va
    scores['VA_Quat-F1']=f1_va
    return scores

def main():
    """main entry"""
    scores={}
    if args['task'] == '1':
        print('task1')
        task1_pred_data=pd.read_csv(args['predict_data'],sep=' ')
        task1_ans =  pd.read_csv(args['reference_data'],sep=' ')
        try:
            scores=task1_score(task1_pred_data,task1_ans,scores)
        except KeyError:
            print('Data format error')
            pass

    if args['task'] == '2':
        print('task2')
        with open(args['predict_data'], 'r', encoding='utf-8') as file:
            data = file.readlines()
        data = data[1:]
        data_list = []

        for line in data:
            match = re.match(r'(\S+)\s+(.+)', line.strip())
            if match:
                id_value = match.group(1)
                triplet_value = match.group(2)
                data_list.append({'ID': id_value, 'Triplets': triplet_value})
        task2_pred_data = pd.DataFrame(data_list)
        with open(args['reference_data'], 'r', encoding='utf-8') as file:
            data = file.readlines()
        data = data[1:]
        data_list = []
        for line in data:
            match = re.match(r'(\S+)\s+(.+)', line.strip())
            if match:
                id_value = match.group(1)
                triplet_value = match.group(2)
                data_list.append({'ID': id_value, 'Triplets': triplet_value})
        task2_ans = pd.DataFrame(data_list)
        try:
            scores=task2_score(task2_pred_data,task2_ans,scores)
        except KeyError:
            print('Data format error')
            pass  

    elif args['task'] == '3':
        print('task3')
        with open(args['predict_data'], 'r', encoding='utf-8') as file:
            data = file.readlines()
        data = data[1:]
        data_list = []
        for line in data:
            match = re.match(r'(\S+)\s+(.+)', line.strip())
            if match:
                id_value = match.group(1)
                triplet_value = match.group(2)
                data_list.append({'ID': id_value, 'Quadruples': triplet_value})
        task3_pred_data = pd.DataFrame(data_list)
        with open(args['reference_data'], 'r', encoding='utf-8') as file:
            data = file.readlines()
        data = data[1:]
        data_list = []
        for line in data:
            match = re.match(r'(\S+)\s+(.+)', line.strip())
            if match:
                id_value = match.group(1)
                triplet_value = match.group(2)
                data_list.append({'ID': id_value, 'Quadruples': triplet_value})
        task3_ans = pd.DataFrame(data_list)
        try:
            scores=task3_score(task3_pred_data,task3_ans,scores)
        except KeyError:
            print('Data format error')
            pass
    write_file(os.path.join(args['output_data_path'], 'scores.json'), json.dumps(scores))

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--task",default='1',type=str,help='task:1,2,3')
    parser.add_argument("--predict_data",default='Input/res/task1s_example.txt',type=str,help='input data path')
    parser.add_argument("--reference_data",default='Input/ref/SIGHAN2024_dimABSA_Validation_Task1_Simplified_truth.txt',type=str,help='reference data path')
    parser.add_argument("--output_data_path",default='output/',type=str,help='output data path')
    args = parser.parse_args()
    args = vars(args)
    main()
