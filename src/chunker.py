def chunk_text(text, chunk_size=1000, overlap=200):
    """
    Split document text into overlapping chunks.

    chunk_size: approximately 1000 characters per chunk
    overlap: 200 characters shared between consecutive chunks
    """

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks