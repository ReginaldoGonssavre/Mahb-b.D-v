import sys

def main():
    code = sys.argv[1]
    language = sys.argv[2]
    description = sys.argv[3]
    print(f"[Mimic] Corrigindo código em {language}:\n{code}\nDescricao: {description}")

if __name__ == "__main__":
    main()