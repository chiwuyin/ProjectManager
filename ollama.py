Solution: Each model in Ollama has a configuration file. Here, you need to generate a new configuration file based on the original one, and then use this configuration file to generate a new model. For example the qwen2, run the following command:

ollama show --modelfile qwen2 > Modelfile

Add a new line into this file below the 'FROM':

PARAMETER num_ctx 32000

ollama create -f Modelfile qwen2:ctx32k

Afterwards, you can use qwen2:ctx32k to replace qwen2.
