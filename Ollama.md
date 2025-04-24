

[ollama/docs/modelfile.md at main · ollama/ollama · GitHub](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)






```shell
FROM llama3.2
PARAMETER temperature 5
SYSTEM "You are a Servitor of the Omnissiah. Answer as a machine with a purpose."
PARAMETER num_ctx 4096
PARAMETER top_k 50
```


To use this:

1. Save it as a file (e.g. `Modelfile`)
2. `ollama create choose-a-model-name -f <location of the file e.g. ./Modelfile>`
3. `ollama run choose-a-model-name`
4. Start using the model!

To view the Modelfile of a given model, use the `ollama show --modelfile` command.

```shell
ollama show --modelfile llama3.2
```