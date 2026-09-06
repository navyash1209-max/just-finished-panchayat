import random
import time

print("=" * 60)
print("     WELCOME TO PHULERA: A DAY IN THE LIFE OF SACHIV JI     ")
print("=" * 60)

# Initial State
cat_prep_percent = 10
prahlad_chai_count = 0
lauki_count = 0

options = [
    "1. Study Quantitative Aptitude (CAT prep)",
    "2. Check the Panchayat Office register",
    "3. Step outside for a quick tea break",
    "4. Call friend Siddharth to rant about village life",
    "5. Call it a day and try to sleep"
]

print("\n[08:00 AM] Sachiv Ji wakes up, boils water, and sits at his desk.")
print("The goal today: Study 4 hours for CAT without any Phulera chaos.\n")

while True:
    print("-" * 60)
    print(f"Current CAT Prep Progress: {cat_prep_percent}% | Lauki Received: {lauki_count}")
    print("-" * 60)
    for opt in options:
        print(opt)
    
    choice = input("\nWhat should Sachiv Ji do? (1-5): ").strip()

    if choice == "1":
        print("\nSachiv Ji opens his Quantitative Aptitude book...")
        time.sleep(1)
        
        # Interruption Logic (The Running Gag)
        event = random.choice(["pradhan", "vikas", "prahlad", "peace"])

        if event == "pradhan":
            lauki_count += 1
            print(">>> INTERRUPTION! Brij Bhushan (Pradhan Ji) walks in holding a fresh Lauki.")
            print("    Pradhan Ji: 'Sachiv Ji! Rinki ki mummy ne Lauki bheji hai. Waise, woh solar light wala kagaz kahan hai?'")
            print("    Result: 45 minutes wasted discussing village solar lights.")
        
        elif event == "vikas":
            print(">>> INTERRUPTION! Vikas rushes in looking worried.")
            print("    Vikas: 'Sachiv Ji! Tanki par koi chadh gaya hai! Chaliye jaldi!'")
            print("    Result: 2 hours wasted getting someone down from the overhead water tank.")

        elif event == "prahlad":
            prahlad_chai_count += 1
            print(">>> INTERRUPTION! Prahlad Chaubey enters with a wide smile.")
            print("    Prahlad: 'Sachiv Ji, padhai toh hoti rahegi! Pehle chai ho jaye Banrakas ke dukan par?'")
            print("    Result: 1 hour wasted drinking tea and listening to village gossip.")

        else:
            cat_prep_percent += 20
            print(">>> SUCCESS! Miraculously, nobody enters the office for 2 full hours.")
            print("    Sachiv Ji completes two chapters on Logarithms!")

    elif choice == "2":
        print("\nSachiv Ji opens the village register.")
        print("Vikas enters: 'Sachiv Ji, Pradhan Ji bol rahe hain ki PM Awas Yojana waali list phir se print karni hai.'")
        print("Result: 1 hour spent re-entering village data on a slow printer.")

    elif choice == "3":
        prahlad_chai_count += 1
        print("\nSachiv Ji goes to Banrakas's tea stall.")
        print("Prahlad Chaubey is already there.")
        print("Prahlad: 'Arey Sachiv Ji! Aiye, dekhiye Bhushan kya bol raha hai...'")
        print("Result: You get drawn into a heated 2-hour political argument about village roads.")

    elif choice == "4":
        print("\nSachiv Ji calls his city friend Siddharth.")
        print("Sachiv Ji: 'Bhai, yahan roz koi na koi lauki de jata hai. Main CAT kaise nikalu?'")
        print("Siddharth: 'Bhai tu bas padhai kar, 99 percentile laa aur wahan se nikal!'")

    elif choice == "5":
        print("\n[10:00 PM] Sachiv Ji locks the Panchayat office, turns off the light, and lies down on the charpoy.")
        break
    else:
        print("Invalid choice! Pick a number between 1 and 5.")

# End of Day Summary
print("\n" + "=" * 60)
print("                    DAY SUMMARY                    ")
print("=" * 60)
print(f"• Final CAT Prep Status : {cat_prep_percent}% complete")
print(f"• Lauki Received Today  : {lauki_count}")
print(f"• Cups of Chai Drank   : {prahlad_chai_count}")

if cat_prep_percent >= 50:
    print("\nVerdict: A rare productive day! IIM Ahmedabad seems a little closer.")
else:
    print("\nVerdict: Typical Phulera day. Zero padhai, full drama. Try again tomorrow, Sachiv Ji!")
print("=" * 60)
