import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-udemy!")
    hot_news = """
        The current conflict between Iran and the United States (and its ally Israel) is being referred to as the 2026 Iran War, which began on February 28, 2026. As of April 19, 2026, the war has reached its 51st day, characterized by a series of heavy airstrikes, naval blockades, and a fragile, frequently broken ceasefire. 
        Current Status of the War (as of April 19, 2026)
        Fragile Ceasefire: A temporary ceasefire was brokered in early April, but tensions remain extremely high. BBC in Iran reports that destruction from missile and drone strikes has caused a massive civilian cost.
        Strait of Hormuz Conflict: A major flashpoint is the Strait of Hormuz, where 20% of the world's oil flows. Al Jazeera reports that Iran has repeatedly closed the strait in response to a U.S. naval blockade of Iranian ports. While Iran briefly declared it "completely open" on April 17, the IRGC (Revolutionary Guard) re-imposed restrictions on April 18, citing U.S. ceasefire violations.
        Diplomatic Efforts: Indirect peace talks have been facilitated by countries like Pakistan. Al Jazeera's live updates indicate that Pakistan's army chief has been in Tehran attempting to restart negotiations between Washington and Tehran. 
        Key Events & Background
        Event 	Details
        Start Date	February 28, 2026, with U.S. and Israeli airstrikes on Iranian military and government sites.
        Casualties	Iranian officials report over 3,400 "martyrs," including at least 1,701 civilians, according to reports cited by DW.
        U.S. Position	President Trump has maintained a "maximum pressure" strategy, threatening to hit power plants if a deal isn't reached, while also hinting at a desire for a "better deal" than the 2015 nuclear agreement.
        Iran's Strategy	Iran has used its regional proxies (the "Axis of Resistance") and control over the Strait of Hormuz to exert political pressure on the U.S. and its allies.
        Major Humanitarian and Economic Impact
        The war has led to significant global economic disruption. The IMF and World Bank have expressed grave concerns about "long-term economic pain" due to damaged oil and gas facilities. Within Iran, reports from the 2026 Iran war - Wikipedia entry highlight that surprise attacks and retaliatory strikes have devastated infrastructure and led to thousands of deaths and injuries on both sides. 
        Would you like more details on the current diplomatic negotiations or the military capabilities being used in this conflict?
    """
    summary_template="""Given the news {hot_news} do followings:
            1.summarize it.
            2.its impact.
    """
    prompt_template = PromptTemplate(input_variables=[hot_news],template=summary_template)
    # llm = ChatOpenAI(temperature=0,model="gpt-5")
    # llm = ChatOllama(temperature=0,model="gemma3:270m")
    llm = ChatOllama(temperature=0,model="gpt-oss:latest")
    chain = prompt_template | llm
    response = chain.invoke(input={"hot_news":hot_news})
    print(response.content)



if __name__ == "__main__":
    main()
