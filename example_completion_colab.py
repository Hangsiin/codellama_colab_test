from typing import Optional

import fire

from llama import Llama


def main(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.2,
    top_p: float = 0.9,
    max_seq_len: int = 256,
    max_batch_size: int = 4,
    max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    while True:
        prompt = input("Enter a prompt (or type 'exit' to quit):\n>>> ")
        if prompt.lower() == "exit":
            break
        
        prompts = [prompt]
        print("Generating answer...")  # 상태 표시
        results = generator.text_completion(
            prompts,
            max_gen_len=max_gen_len,
            temperature=temperature,
            top_p=top_p,
        )
        for result in results:
            print(prompt)
            print(f"> {result['generation']}")
            print("\n==================================\n")


if __name__ == "__main__":
    fire.Fire(main)
