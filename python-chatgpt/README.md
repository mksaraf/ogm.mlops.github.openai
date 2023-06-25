<!-- @format -->

## This is an accompanying project of YouTube video about Python automation with ChatGPT

https://platform.openai.com/docs/introduction/key-concepts
https://platform.openai.com/account/api-keys
https://www.youtube.com/watch?v=w-X_EQ2Xva4
key_pythonscript : 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

#### set environment variable OPENAI_API_KEY before executing python-chatgpt script

    # export OPENAI_API_KEY=your-key-here
    export OPENAI_API_KEY=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

#### execute the main python-chatgpt script to generate python code from Open AI

    python3 python-chatgpt.py "extract all html headers from a web page, translate to Spanish and save the result into an html file" "extract-translate.py"

    python3 python-chatgpt.py "print hello world" "hello-world.py"

####

OPENAI_API_KEY == "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"

## Making request

curl https://api.openai.com/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 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" \
 -d '{
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content": "Say this is a test!"}],
"temperature": 0.7
}'

## List models

curl https://api.openai.com/v1/models \
-H "Authorization: Bearer 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"

## Retrieve Model

curl https://api.openai.com/v1/models/text-davinci-003 \
 -H "Authorization: Bearer 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"

## Create chat completion

curl https://api.openai.com/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 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" \
 -d '{
"model": "gpt-3.5-turbo",
"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}]
}'

curl https://api.openai.com/v1/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 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" \
 -d '{
"model": "text-davinci-003",
"prompt": "Say this is a test",
"max_tokens": 7,
"temperature": 0
}'

## Create Edit

curl https://api.openai.com/v1/edits \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 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" \
 -d '{
"model": "text-davinci-edit-001",
"input": "What day of the wek is it?",
"instruction": "Fix the spelling mistakes"
}'

## Create Image

curl https://api.openai.com/v1/images/generations \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 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" \
 -d '{
"prompt": "A cute baby 2 year old",
"n": 2,
"size": "1024x1024"
}'

## Edit Image

curl https://api.openai.com/v1/images/generations \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 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" \
 -d '{
"prompt": "Old man wearing T shirt and pant",
"n": 2,
"size": "1024x1024"
}'

## Create Image Variation

curl https://api.openai.com/v1/images/variations \
 -H "Authorization: Bearer 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" \
 -F image="@otter.png" \
 -F n=2 \
 -F size="1024x1024"

## Create embeddings
