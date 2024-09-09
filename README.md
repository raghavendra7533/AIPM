# AIPM
## Dev Notes
- Run `pip install -r requirements.txt` to install the dependencies
- Run `python app.py` to start the server
- Run `python test.py` to test the server
- Run `python test_chat.py` to test the chat functionality
- Run `python test_chat_async.py` to test the chat functionality asynchronously
- Run `python test_chat_async_fastapi.py` to test the chat functionality asynchronously with FastAPI
- Run `python test_chat_async_fastapi.py` to test the chat functionality asynchronously with FastAPI
- Run `python test_chat_async_fastapi.py` to test the chat functionality asynchronously with FastAPI

## Domain name Ideas:
- .ai
- Surview.ai (Survey + Interview) 
- VoxAI Combines "vox" (voice) with AI
- Insytful.ai
- Insyght.ai
- SurvAI: Survey + AI
- ConvAI: Conversation + AI
 
## Team level pointers
- Where do we position the product -> Where does the product stand?
- Create the prompt, define constraints
- Try the prompt we create, in all the GPT models to test efficacy -> dependency → whole team
- Approx time it would take to complete the interview (5 to 7 mins) - let the company decide.
- I felt anything above 10-12 questions was becoming too much.
- Create wireframe or figma design of the product (optional) 
- Incentive (we define the workflow - is it in MVP)
- Explore GPT models on data analysis

## Attributes of model:
- Human feel -
- Engaging 
- Non-biased/Fail check -> constraints -> level of probing
- Simulate a test chat just to verify if the response may be in order. 

## Pages:
- Homepage/Landing page:  https://claude.site/artifacts/68678fea-8986-491d-9905-4654a351fcf7 
- Can we add a video - may be a recorded product walkthrough
- Pricing Page: 
What’s the pricing model
Login -> default access -> 
User access link for the interview


3 pages 
Company dashboard
Create interview/Set interview
Analysis
User end 
Chat interface for the interview

## Technical Specs
- Database -> MySQL
- Frontend -> Bootstrap, chart.js
- Use a SAAS boilerplate (makes the work easy for creating the rest pages)
- Routing -> {www.ourwebsitename}.ai/{id}/ 
- If invalid we throw 404, soft 302
- AI model -
- Anthropic -> reasoning -> creative 
- Voice -> OpenAI whisper (Elevation labs) -> Can you research (difficult but let’s try doing it)

- AI model prompting -> Mom test + the best practices for conducting user interview
- Some engagement so that it can do some small talks.
- Constraints -> 
		       

## AI model training prerequisites: 
- How will we train the model
- Can team members get access to run the prompts from the backend? To cut down dependency on the dev.
- Unblocker: Is claud prompts same as Anthropic prompts. Dedency on Raghav.
- Define guard rails

## How will the company or the person set the interview questions:
- The PM sets the interview context and gives some background. Maybe they include questions. 
- Multi prompt - Industry, upload existing interview questions
- AI models suggest some non-leading questions based on the context given.
- The PM can choose the questions suggested by the AI, edit the questions if needed.
- The final outcome is 10-12 questions. [Best practices to use the platform]
- Filters: Tone of interview, language, qualifying questions???? 
- Then they can share the link with the user -> send a mail with the link, whatsapp link, (maybe a phone number), or a shareable direct link [work refine it more - how is he sharing the link].


## Analysis
- The analysis of all the responses from the participants or tabular view. 
- CSV format raw data
- Condensed insights for each questions -> charts or % 
- AI prompts to interact with the data collected

## User end
When the user open the link, we ask to enter their name, email, phone number, few other attributes
Chatbot interface (if qualifying question selected then ask the question)


Whatsapp model for students to get better math for lower order kids
Backend -> question -> question explanation -> audio/video -> do you want to attempt the question -> loop of 3 steps -> hint Q&A -> 
Design a question loop/flow chart??
Progressive disclosure 
