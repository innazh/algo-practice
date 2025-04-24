def rank_products(interactions, WEIGHTS):
    product_scores = {}

    for interaction in interactions:
        product_id = interaction['product_id']
        interaction_type = interaction['interaction_type']
        weight = WEIGHTS[interaction_type]

        if product_id not in product_scores:
            product_scores[product_id] = 0
        product_scores[product_id] += weight

    sorted_products = sorted(product_scores.items(), key=lambda x: (-x[1], x[0]))
    return [id for id, score in sorted_products]

def main():
    interactions = [
    {"product_id": 101, "interaction_type": "view"},
    {"product_id": 102, "interaction_type": "add_to_cart"},
    {"product_id": 101, "interaction_type": "wishlist"},
    {"product_id": 103, "interaction_type": "review_read"},
    {"product_id": 101, "interaction_type": "view"},
    ]

    WEIGHTS = {
        "view": 0.5,
        "add_to_cart": 1.0,
        "wishlist": 0.7,
        "review_read": 0.3
    }

    result = rank_products(interactions, WEIGHTS)
    print(result)   

if __name__=="__main__":
    main()