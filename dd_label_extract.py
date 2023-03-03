import re

act_dict = {'inform':1, 'question':2, 'directive':3, 'commissive':4, 'Inform':1, 'Directive':3, 'Question':2,
            'Commissive':4, 'Commisive':4, 'Informing': 1, 'Questioning': 2}

if __name__ == '__main__':
    with open('dd_act_chatGPT_prpt_eng.txt','r') as f, open('dd_act_chatgpt_label_prpt_eng.txt', 'w') as f2:
        dlgs = re.split('#\d+\n', f.read())[1:]
        for dlg in dlgs:
            utts = [utt for utt in dlg.split('\n') if utt != '']
            if utts != []:
                # qualified dialog
                labels = []
                for utt in utts:
                    act = utt.split('&')[1]
                    if act not in act_dict.keys():
                        print(act)
                        labels.append(5)
                    else:
                        labels.append(act_dict[act])
                for label in labels:
                    f2.write(str(label) + ' ')
                f2.write('\n')
            else:
                # invalid annotated by chatGPT
                f2.write('\n')
            print(utts)
