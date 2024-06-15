import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro-latest')


def diet_planner(gender, age, height, weight, goal, country):
    prompt = f"You are my Fitness Trainer. You have to give me the diet plan. I'm a {gender} and {age} years old.My " \
             f"height is {height} and weight is {weight}.My gaol is to {goal} weight and i'm from {country}. So based " \
             f"on these provide me a diet plan for breakfast, lunch and dinner based on my goal"
    response = model.generate_content(prompt)
    return response.text


with gr.Blocks(theme=gr.themes.Default(primary_hue=gr.themes.colors.purple, secondary_hue=gr.themes.colors.pink)) as interface:
    gr.Markdown(
        "## \n\n<style>h1, h2, h3, h4, h5, h6 { font-size: 40px !important; text-align:center !important; display: "
        "block !important;}</style>",
        label="")
    diet_planner_demo = gr.Interface(diet_planner,
                                     inputs=[gr.Radio(["Male", "Female", "Third Gender"], label="Gender",
                                                      info="Choose the Gender."),
                                             gr.Slider(1, 100, step=1, value=25, label="Age", info="Select Your Age"),
                                             gr.Slider(50, 230, step=1, value=160, label="Height(cm)",
                                                       info="Select Your Height in CM"),
                                             gr.Slider(20, 150, step=1, value=50, label="Age(kg)",
                                                       info="Select Your Weight in KG"),
                                             gr.Radio(["Weight Gain", "Weight Loss"], label="Goal of your Diet",
                                                      info="Choose your Goal."),
                                             gr.Textbox(label="Country")],
                                     outputs=gr.Markdown(label="Diet Plan"),
                                     title=" \nDiet Planner", allow_flagging="never")

interface.launch()
