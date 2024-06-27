def calculate_lengths(text, summarization_len):
    token_quantity = len(text.split())
    reduction_factor = 1 - (summarization_len / 100)
    target_length = int(token_quantity * reduction_factor)

    min_length = int(target_length * 0.8)
    max_length = int(target_length * 1.2)

    return min_length, max_length
