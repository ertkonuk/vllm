#!/usr/bin/env
import json

def generate():
    from vllm import LLM, SamplingParams
    import os
    #prompt = open("input.hellaswag.txt").read().strip()
    f = "Context: After Washington had returned to Williamsburg, Dinwiddie ordered him to lead a larger force to assist Trent in his work. While en route, Washington learned of Trent's retreat. Since Tanaghrisson had promised support to the British, Washington continued toward Fort Duquesne and met with the Mingo leader. Learning of a French scouting party in the area, Washington, with Tanaghrisson and his party, surprised the Canadians on May 28 in what became known as the Battle of Jumonville Glen. They killed many of the Canadians, including their commanding officer, Joseph Coulon de Jumonville, whose head was reportedly split open by Tanaghrisson with a tomahawk. The historian Fred Anderson suggests that Tanaghrisson was acting to gain the support of the British and regain authority over his own people. They had been inclined to support the French, with whom they had long trading relationships. One of Tanaghrisson's men told Contrecoeur that Jumonville had been killed by British musket fire. Question: Upon learning of a French scounting party in the area, what did Washington do? Answer:"
    f2 = "Context: Washington continued toward Fort Duquesne and met with the Mingo leader. Question: Upon learning of a French scounting party in the area, what did Washington do? Answer:"
    prompts=[f, f]
    tasks=["TASK1", "TASK3"]
    sampling_params = SamplingParams(temperature=0.0, top_k=-1)

    # llm = LLM(model='/mnt/nvdl/datasets/inference-engines/projects/nemollm/checkpoints/nvgpt-2b-001/', lora_model_path='/mnt/nvdl/datasets/inference-engines/projects/nemollm/checkpoints/nvgpt-2b-001/lora_checkpoints/', tensor_parallel_size=1, dtype='float16')
    llm = LLM(model='/mnt/nvdl/datasets/inference-engines/projects/nemollm/checkpoints/llama2-7Bf/huggingface', lora_model_path='/mnt/nvdl/datasets/inference-engines/projects/nemollm/checkpoints/llama2-7Bf/lora_checkpoints', tensor_parallel_size=1, dtype='float16')
    #llm = LLM(model='bigscience/bloomz-3b', tensor_parallel_size=4)
    #os.system('clear')
    print('#'*100)
    print('#'*100)
    print('#'*100)
    outputs = llm.generate(prompts, sampling_params, tasks=tasks)

    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f'Prompt: {prompt!r}, Generated text: {generated_text!r}')

if __name__ == "__main__":
    generate()
