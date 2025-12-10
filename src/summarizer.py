import subprocess

def ollama_summarize(text, model="tinyllama"):
    prompt = f"Summarize the following text in 5–8 sentences:\n\n{text}\n\nSummary:"

    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        capture_output=True
    )

    return result.stdout.decode("utf-8").strip()
