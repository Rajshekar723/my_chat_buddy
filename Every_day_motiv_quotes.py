<<<<<<< Updated upstream
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

import time
opts = Options()
opts.headless = True
assert opts.headless

driver=Chrome(executable_path="C:\\bin\\chromedriver.exe",options=opts)

def quote():
    driver.get('https://quotesondesign.com/gonxalo-blanco/')
    driver.find_element("id", "get-another-quote-button").click()
    driver.implicitly_wait(9000000)
    quote = driver.find_element("id","quote-content").text
    driver.close()
    return quote

def main():
    motiquote = quote()
    print(motiquote)
    quit()


if __name__ == '__main__':
    main()
=======
import random

quotes = ["1. “You can get everything in life you want if you will just help enough other people get what they want.” —Zig Ziglar",
          "2. “Inspiration does exist, but it must find you working.” —Pablo Picasso",
          "3. “Don't settle for average. Bring your best to the moment. Then, whether it fails or succeeds, at least you know you gave all you had.” —Angela Basset",
          "4. “Show up, show up, show up, and after a while the muse shows up, too.” —Isabel Allend",
          "5. “Don't bunt. Aim out of the ballpark. Aim for the company of immortals.” ―David Ogilvy",
          "6. “I have stood on a mountain of no for one yes.” —Barbara Elaine Smit",
          "7. “If you believe something needs to exist, if it's something you want to use yourself, don't let anyone ever stop you from doing it.” —Tobias Lütk",
          "8. “First forget inspiration. Habit is more dependable. Habit will sustain you whether you're inspired or not. Habit will help you finish and polish your stories. Inspiration won't. Habit is persistence in practice.” ―Octavia Butle",
          "9. “The best way out is always through.” ―Robert Fros",
          "10. “The battles that count aren't the ones for gold medals. The struggles within yourself—the invisible, inevitable battles inside all of us—that's where it's at.",
          "11. “If there is no struggle, there is no progress.” —Frederick Douglas",
          "12. “Someone will declare, “I am the leader!” and expect everyone to get in line and follow him or her to the gates of heaven or hell. My experience is that it doesn’t happen that way. Others follow you based on the quality of your actions rather than the magnitude of your declarations.” ―Bill Wals",
          "13. “Courage is like a muscle. We strengthen it by use.” —Ruth Gord",
          "14. “Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegi",
          "15. “Relentlessly prune bullshit, don't wait to do things that matter, and savor the time you have. That's what you do when life is short.” —Paul Graha",
          "16. “More is lost by indecision than wrong decision.” —Marcus Tullius Cicero",
          "17. “If the highest aim of a captain were to preserve his ship, he would keep it in port forever.” —Thomas Aquinas",
          "19. “Keep a little fire burning; however small, however hidden.” ―Cormac McCarthy",
          "21. “The only way of discovering the limits of the possible is to venture a little way past them into the impossible.” ―Arthur C. Clarke",
          "23. “Courage is the most important of all the virtues because without courage, you can't practice any other virtue consistently.” ―Maya Angelou",
          "28. “Don’t worry about failure; you only have to be right once.” —Drew Houston",
          "29. “You carry the passport to your own happiness.” —Diane von Furstenberg",
          "30. “Never let success get to your head and never let failure get to your heart.” —Drake",
          "31. “The most difficult thing is the decision to act, the rest is merely tenacity.” —Amelia Earhart",
          "32. “I’d rather regret the things I’ve done than regret the things I haven’t done.” —Lucille Ball",
          "33. “I will not lose, for even in defeat, there’s a valuable lesson learned, so it evens up for me.” —Jay-Z",
          "34. “I do not try to dance better than anyone else. I only try to dance better than myself.” —Arianna Huffington",
          "35. “If you don’t risk anything, you risk even more.” —Erica Jong",
          "36. “I think it’s intoxicating when somebody is so unapologetically who they are.” —Don Cheadle",
          "37. “You can never leave footprints that last if you are always walking on tiptoe.” —Leymah Gbowee",
          "38. “If you don’t like the road you’re walking, start paving another one.” —Dolly Parton",
          "39. “If it makes you nervous, you’re doing it right.” —Childish Gambino",
          "40. “What you do makes a difference, and you have to decide what kind of difference you want to make.” —Jane Goodall",
          "41. “I choose to make the rest of my life the best of my life.” —Louise Hay",
          "42. “In order to be irreplaceable one must always be different.” —Coco Chanel",
          "43. “Anything can make me stop and look and wonder, and sometimes learn.” —Kurt Vonnegut",
          "44. “People's passion and desire for authenticity is strong.” —Constance Wu",
          "45. “A surplus of effort could overcome a deficit of confidence.” —Sonia Sotomayor",
          "46. “Doubt is a killer. You just have to know who you are and what you stand for.” —Jennifer Lopez",
          "47. “There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers",
          "48 “No one changes the world who isn’t obsessed.” —Billie Jean King",
          "49. “I learned a long time ago that there is something worse than missing the goal, and that’s not pulling the trigger.” —Mia Hamm",
          "50. “Some people want it to happen, some wish it would happen, others make it happen.” —Michael Jordan",
          "51. “It is remarkable how much long-term advantage people like us have gotten by trying to be consistently not stupid, instead of trying to be very intelligent.” —Charlie Munger",
        ]

random_element = random.choice(quotes)

print(random_element)
>>>>>>> Stashed changes
