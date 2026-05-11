import argparse
import yaml
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    with open(args.input, "r") as f:
        data = yaml.safe_load(f)

    title = data.get("site_title", "Default Title")
    content = data.get("content", "Default Content")

    html = f"""
    <html>
    <head><title>{title}</title></head>
    <body>
        <h1>{title}</h1>
        <p>{content}</p>
        <hr>
        <small>Built by PodChain</small>
    </body>
    </html>
    """

    # Ensure artifacts directory exists relative to script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.join(script_dir, "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)
    
    output_path = os.path.join(artifacts_dir, "index.html")
    with open(output_path, "w") as f:
        f.write(html)
    
    print(f"Artifact created at {output_path}")

if __name__ == "__main__":
    main()
