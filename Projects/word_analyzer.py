def analyze_text(*bits, **opts):
    raw_text = " ".join(bits).lower()
    pieces = raw_text.split()

    skip_words = {"is", "the", "a", "an", "and", "or", "in", "on", "of", "to"}
    if opts.get("ignore_stopwords"):
        pieces = [w for w in pieces if w not in skip_words]

    word_map = {}
    for w in pieces:
        if w in word_map:
            word_map[w] += 1
        else:
            word_map[w] = 1

    try:
        longest = max(pieces, key=len)
        shortest = min(pieces, key=len)
    except ValueError:
        longest = shortest = ""

    total = len(pieces)
    unique = len(set(pieces))

    if opts.get("reverse"):
        word_map = dict(sorted(word_map.items(), key=lambda x: x[1], reverse=True))

    if "min_len" in opts:
        threshold = opts["min_len"]
        word_map = {k: v for k, v in word_map.items() if len(k) >= threshold}

    print("\nAnalysis Result")
    print(f"Total Words: {total}")
    print(f"Unique Words: {unique}")
    print(f"Longest Word: {longest}")
    print(f"Shortest Word: {shortest}\n")

    print("Word Frequency:")
    for w, c in word_map.items():
        print(f"{w}: {c}")

analyze_text("My name is Anthony Gonzalves. I am alone in this world.", ignore_stopwords=False, reverse=True)
