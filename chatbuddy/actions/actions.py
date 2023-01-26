# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_motiv"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
           
        quotes = [" “You can get everything in life you want if you will just help enough other people get what they want.” —Zig Ziglar",
          " “Inspiration does exist, but it must find you working.” —Pablo Picasso",
          " “Don't settle for average. Bring your best to the moment. Then, whether it fails or succeeds, at least you know you gave all you had.” —Angela Basset",
          " “Show up, show up, show up, and after a while the muse shows up, too.” —Isabel Allend",
          " “Don't bunt. Aim out of the ballpark. Aim for the company of immortals.” ―David Ogilvy",
          " “I have stood on a mountain of no for one yes.” —Barbara Elaine Smit",
          " “If you believe something needs to exist, if it's something you want to use yourself, don't let anyone ever stop you from doing it.” —Tobias Lütk",
          " “First forget inspiration. Habit is more dependable. Habit will sustain you whether you're inspired or not. Habit will help you finish and polish your stories. Inspiration won't. Habit is persistence in practice.” ―Octavia Butle",
          " “The best way out is always through.” ―Robert Fros",
          " “The battles that count aren't the ones for gold medals. The struggles within yourself—the invisible, inevitable battles inside all of us—that's where it's at.",
          " “If there is no struggle, there is no progress.” —Frederick Douglas",
          " “Someone will declare, “I am the leader!” and expect everyone to get in line and follow him or her to the gates of heaven or hell. My experience is that it doesn’t happen that way. Others follow you based on the quality of your actions rather than the magnitude of your declarations.” ―Bill Wals",
          " “Courage is like a muscle. We strengthen it by use.” —Ruth Gord",
          " “Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegi",
          " “Relentlessly prune bullshit, don't wait to do things that matter, and savor the time you have. That's what you do when life is short.” —Paul Graha",
          " “More is lost by indecision than wrong decision.” —Marcus Tullius Cicero",
          " “If the highest aim of a captain were to preserve his ship, he would keep it in port forever.” —Thomas Aquinas",
          " “Keep a little fire burning; however small, however hidden.” ―Cormac McCarthy",
          " “The only way of discovering the limits of the possible is to venture a little way past them into the impossible.” ―Arthur C. Clarke",
          " “Courage is the most important of all the virtues because without courage, you can't practice any other virtue consistently.” ―Maya Angelou",
          " “Don’t worry about failure; you only have to be right once.” —Drew Houston",
          " “You carry the passport to your own happiness.” —Diane von Furstenberg",
          " “Never let success get to your head and never let failure get to your heart.” —Drake",
          " “The most difficult thing is the decision to act, the rest is merely tenacity.” —Amelia Earhart",
          " “I’d rather regret the things I’ve done than regret the things I haven’t done.” —Lucille Ball",
          " “I will not lose, for even in defeat, there’s a valuable lesson learned, so it evens up for me.” —Jay-Z",
          " “I do not try to dance better than anyone else. I only try to dance better than myself.” —Arianna Huffington",
          " “If you don’t risk anything, you risk even more.” —Erica Jong",
          " “I think it’s intoxicating when somebody is so unapologetically who they are.” —Don Cheadle",
          " “You can never leave footprints that last if you are always walking on tiptoe.” —Leymah Gbowee",
          " “If you don’t like the road you’re walking, start paving another one.” —Dolly Parton",
          " “If it makes you nervous, you’re doing it right.” —Childish Gambino",
          " “What you do makes a difference, and you have to decide what kind of difference you want to make.” —Jane Goodall",
          " “I choose to make the rest of my life the best of my life.” —Louise Hay",
          " “In order to be irreplaceable one must always be different.” —Coco Chanel",
          " “Anything can make me stop and look and wonder, and sometimes learn.” —Kurt Vonnegut",
          " “People's passion and desire for authenticity is strong.” —Constance Wu",
          " “A surplus of effort could overcome a deficit of confidence.” —Sonia Sotomayor",
          " “Doubt is a killer. You just have to know who you are and what you stand for.” —Jennifer Lopez",
          " “There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers",
          " “No one changes the world who isn’t obsessed.” —Billie Jean King",
          " “I learned a long time ago that there is something worse than missing the goal, and that’s not pulling the trigger.” —Mia Hamm",
          " “Some people want it to happen, some wish it would happen, others make it happen.” —Michael Jordan",
          " “It is remarkable how much long-term advantage people like us have gotten by trying to be consistently not stupid, instead of trying to be very intelligent.” —Charlie Munger",
        ]

        random_element = random.choice(quotes)
        dispatcher.utter_message(text=random_element)
        return []
