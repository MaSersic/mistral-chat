A chat app using a locally deployed LLM - specifically the OpenHermes 2.5 fine tune of the Mistral 7B model.  
The app is capable of remembering the conversation context with the help of the langchain ConversationChain and ConversationBufferMemory

Links to the models:

[Mistral 7B](https://github.com/mistralai/mistral-src) / [OpenHermes 2.5](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) / [GGUF](https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF)

Install:

Install the requirements

Download the [quantized model](https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF/blob/main/openhermes-2.5-mistral-7b.Q8_0.gguf) into the LLMs folder

TODO:

PDF ingestion

Store vectorized conversation data.

Automate the model download, docker container creation, github actions

Create a login system.

Multiple different coversations?

Store previous conversations with each user, enable continuing the stored conversations.

Setting the max tokens and context size in the ui

Optimisations

Multiple user selectable models?

Nicer ui?

Templates for the prompts?
