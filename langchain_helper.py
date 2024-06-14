from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()


def generate_pet_names(animal_type, color, size, number):
    llm = OpenAI(temperature=0.7)
    prompt_template_pet_names = PromptTemplate(input_variables=['animal_type', 'color', 'size', 'number'],
                                               template=f"I have a {size} {color} colored pet {animal_type} and I want "
                                                        f"a cute name for it. Suggest {number} cute names for my {animal_type}")
    # names = llm.invoke("I have a pet cat and I want a cute name for it. Suggest 5 cute names for my cat")

    # names_chain = LLMChain(llm = llm, prompt = prompt_template_pet_names)
    # names = names_chain.invoke({'animal_type': animal_type, 'color': color})
    # return names['text']

    formatted_prompt = prompt_template_pet_names.format(animal_type=animal_type, color=color, size=size, number=number)
    names = llm.invoke(formatted_prompt)
    return names


# if __name__ == "__main__":
#     print(generate_pet_names("cat", "orange", "fat", 10))
