def summarize_args(*args, **kwargs):
    summary = []

    if args:
        summary.append("Positional arguments:")
        i = 1
        for arg in args:
            summary.append(f"  arg{i}: {arg}")
            i += 1
    else:
        summary.append("No positional arguments.")

    if kwargs:
        summary.append("Keyword arguments:")
        for key in kwargs:
            summary.append(f"  {key}: {kwargs[key]}")
    else:
        summary.append("No keyword arguments.")

    return "\n".join(summary)

print(summarize_args(1, 2, 3, name="Alice", city="NY"))