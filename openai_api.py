import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

base_text = "Emergency management specialists plan for and coordinate emergency response programs and activities for " \
            "natural, wartime, and technological disasters. Based on the SCENARIO (with a type of disaster, " \
            "area of impact, affected number of people and other data) we want to generate immediate TASKS for the " \
            "first 72 hours after the huge disaster (floods, forest fires, power outages etc.) on the local level (" \
            "village, small city, city etc.). Some of the TASKS might include: ensuring various agencies are in place " \
            "to set up temporary shelters if needed; coordinating the delivery of food, water, and medical supplies " \
            "to areas that have been hit by a natural disaster; maximizing disaster relief efforts by acting as the " \
            "liaison between federal, state, local, and municipal agencies; preparing status reports on the recovery " \
            "efforts, needs, and preliminary damage assessments for all emergency situations.\n\nScenario: Flooded " \
            "village in Vietnam. The population of the village is around 13500 people. There are considerable power " \
            "outages and risks of water contamination throughout the whole area.\nTask: For the rapid distribution of " \
            "the task force throughout the village, set up a group of 14 to 20 people to gather the available " \
            "resources of bottled water and a map of safe water resources (which based on your location could include " \
            "rainwater, natural springs, or rivers) with the fastest way of treating the water from those resources, " \
            "for example by using iodine tablets or boiling the water.\nTask: Based on the tropical climate zone of " \
            "Vietnam, (if available) deploy mobile stand-alone off-grid solar panels systems. Alternatively, " \
            "utilize the available energy generators for rapid power restoration in the community. Proactively ask " \
            "people in your community for currently available generators and solar panels or any other sources of " \
            "energy generation.\nTask: Gather all available food resources in the village and create a list of all " \
            "people with special dietary needs (e.g. infants, elderly, pregnant women, people with diabetes, " \
            "etc.).\nTask: Set up 4 temporary tents for medical assistance. Recruit the available med experts for " \
            "volunteering in these tents. Prepare all the available medical supplies before the arrival of the " \
            "external support.\nTask: Create a list of people who need to be evacuated from the " \
            "village.\n###\nScenario: "


def parse_openai_response(response):
    """Parse the response from OpenAI API to get the tasks. Split the response by 'Task: '"""

    def strip(text):
        return text.strip()

    tasks = response['choices'][0]['text'].split('Task: ')
    tasks = list(map(strip, tasks))

    return tasks


def create_a_request(scenario_text: str):
    """Create a request to the OpenAI API"""
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=base_text + scenario_text + "\nTask:",
        temperature=0.42,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response


def get_tasks_from_the_scenario(scenario_text):
    """Get the tasks from OpenAI API"""
    response = create_a_request(scenario_text)
    tasks = parse_openai_response(response)
    return tasks

#
#if __name__ == '__main__':
#    sample_text = "Massive destruction after the hurricane in the small town in the south of Miami. The population " \
#                    "estimation of the town is 75000 people. There are several road blockages to the bigger cities " \
#                    "and multiple gas leakages."
#    tasks = get_tasks_from_the_scenario(sample_text)
#    print(tasks)
