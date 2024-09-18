

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    prices = {'A': 50, 'B':30, 'C':20, 'D':15}
    special_offers = {'A': (3,130), 'B':(2,45)}

    total_cost, item_counts = 0, {}

    if not skus:
        return 0
    
    for item in skus:
        if item not in prices:
            return -1
        item_counts[item] = item_counts.get(item, 0) +1
    
    for item, count in item_counts.items():
        if item in special_offers:
            offer_count, offer_price = special_offers[item]
            total_cost += (count // offer_count) * offer_price
            total_cost += (count % offer_count) * prices[item]
        else:
            total_cost += count*prices[item]
    
    return total_cost
    
