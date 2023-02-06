def dfs(users, origin_emoticons, dfs_emoticons, discount_list, discount_map, depth, answer):
    if depth == len(dfs_emoticons):
        user_count = 0
        user_sale_amount = 0
        for user in users:
            user_sum = 0
            for i in range(0, len(discount_map)):
                if discount_map[i] >= user[0]:
                    user_sum += dfs_emoticons[i]
                    
            if user_sum >= user[1]:
                user_count += 1
            else:
                user_sale_amount += user_sum
    
        if user_count > answer[0]:
            answer[0] = user_count
            answer[1] = user_sale_amount
        elif user_count == answer[0] and user_sale_amount > answer[1]:
            answer[0] = user_count
            answer[1] = user_sale_amount
        return
    
    for discount in discount_list:
        dfs_emoticons[depth] = origin_emoticons[depth] * ((100 - discount)/100)
        discount_map[depth] = discount
        dfs(users, origin_emoticons, dfs_emoticons, discount_list, discount_map, depth + 1, answer)
        
def solution(users, emoticons):
    answer = [0, 0]
    discount_list = [10, 20, 30, 40]
    discount_map = [0] * len(emoticons)
    origin_emoticons = emoticons.copy()
    depth = 0
    
    dfs(users ,origin_emoticons, emoticons, discount_list, discount_map, depth, answer)
    
    return answer