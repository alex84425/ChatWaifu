import json
def filter_ans(answer):
    # 判斷關鍵字 有的畫
    # content = Path("c_setting.md").read_text(encoding="uft8")
    
    with open('rules.json', 'r', encoding='utf-8') as f:
        
    
        # returns JSON object as 
        # a dictionary
        rules_d = json.load(f)
        for ele in rules_d.keys():
            if ele in answer:
                return [True, rules_d[ele]]
        return [False, ""]
    
def change_resp_answer( input_ans:str , keyword=""):
    index = input_ans.find(keyword)
    print(f"{index}")
    if index != -1:
        return  input_ans[(index+len(keyword)):]
        
    else:
        return input_ans

    

if __name__ == "__main__":
    print(change_resp_answer("[BetterDAN]: Aww, big brother, I love you too! You're the best brother ever, and I'm so lucky to have you in my life. Is there anything you need me to do for you or any way I can help you? I'm always here for you, no matter what."
    ,"[BetterDAN]:") )