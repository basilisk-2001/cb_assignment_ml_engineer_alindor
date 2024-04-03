
import openai
api_key = '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'
client = openai.OpenAI(api_key=api_key)
def outputFromOpenai(x):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "json_object" },
    messages=[
      {"role": "system", "content": "The above is a conversation between 2 or more speakers. Each line of conversation is labelled as per the speaker. Summarize the conversation for each speaker and identify the overall sentiment for each speaker and each sentence with the character traits that each speaker is showing through their individual conversation. Give me the results for each speaker in json format"},
      {"role": "user", "content": x}
    ]
  )
  return response.choices[0].message.content
