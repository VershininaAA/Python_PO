def task() -> float:
    summ = 0.0
    ch1 = 0.0
    ch2 = 0.0
    
    with open("input.json", "r", encoding='utf-8') as f:
        data = json.load(f)  
        
        if isinstance(data, list):  
            for item in data:
                if isinstance(item, dict):  
                    if 'score' in item:
                        ch1 = float(item['score'])
                    if 'weight' in item:
                        ch2 = float(item['weight'])
                    
                    if ch1 != 0 and ch2 != 0:
                        summ += ch1 * ch2
                        ch1, ch2 = 0.0, 0.0
    
    return round(summ, 3)

print(task())
