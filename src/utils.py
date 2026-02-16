def format_sources(docs):
    sources = []
    for d in docs:
        src = f"{d.metadata.get('source')} - Page {d.metadata.get('page')}"
        sources.append(src)
    return sources
