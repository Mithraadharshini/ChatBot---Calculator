# actions.py

from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionAddition(Action):

    def name(self) -> Text:
        return "action_addition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        num1 = tracker.get_slot("number1")
        num2 = tracker.get_slot("number2")
        result = num1 + num2
        response = f"The answer is {result}."
        dispatcher.utter_message(text=response)
        return []

class ActionSubtraction(Action):

    def name(self) -> Text:
        return "action_subtraction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        num1 = tracker.get_slot("number1")
        num2 = tracker.get_slot("number2")
        result = num1 - num2
        response = f"The answer is {result}."
        dispatcher.utter_message(text=response)
