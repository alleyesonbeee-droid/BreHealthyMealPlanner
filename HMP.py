
# Bre Healthy Meal Planner
# Final Project 

import tkinter as tk
from tkinter import messagebox


# --------------------------------------------------------
# Create Main Application Window
# --------------------------------------------------------
root = tk.Tk()                                   # Create main window
root.title("Bre Healthy Meal Planner")           # Set title
root.geometry("1050x800")                        # Set window size


# --------------------------------------------------------
# Global Variables
# --------------------------------------------------------
selected_preferences = []   # Stores selected diet options
images = {}                 # Stores image references to prevent disappearing


# --------------------------------------------------------
# FUNCTION: show_main()
# --------------------------------------------------------
def show_main():

    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # Load and resize logo (smaller)
    images["logo"] = tk.PhotoImage(file="logo.png").subsample(4,4)

    tk.Label(root, image=images["logo"]).pack(pady=20)

    tk.Label(root,
             text="Bre Healthy Meal Planner",
             font=("Arial", 26, "bold")).pack(pady=10)

    tk.Label(root,
             text="Plan your weekly meals based on your diet preference.",
             font=("Arial", 14)).pack(pady=10)

    # Navigation Buttons
    tk.Button(root,
              text="Start Planning",
              width=20,
              command=show_preferences).pack(pady=10)

    tk.Button(root,
              text="Exit",
              width=20,
              command=root.quit).pack(pady=10)


# --------------------------------------------------------
# FUNCTION: show_preferences()
# --------------------------------------------------------
def show_preferences():

    global veg, vegan, gluten, keto, lowcarb

    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root,
             text="Select Your Dietary Preferences",
             font=("Arial", 22, "bold")).pack(pady=20)

    # Boolean variables for selections
    veg = tk.BooleanVar()
    vegan = tk.BooleanVar()
    gluten = tk.BooleanVar()
    keto = tk.BooleanVar()
    lowcarb = tk.BooleanVar()

    # Checkboxes
    tk.Checkbutton(root, text="Vegetarian", variable=veg).pack()
    tk.Checkbutton(root, text="Vegan", variable=vegan).pack()
    tk.Checkbutton(root, text="Gluten-Free", variable=gluten).pack()
    tk.Checkbutton(root, text="Keto", variable=keto).pack()
    tk.Checkbutton(root, text="Low Carb", variable=lowcarb).pack()

    # Buttons
    tk.Button(root,
              text="Next",
              command=validate_preferences).pack(pady=15)

    tk.Button(root,
              text="Back",
              command=show_main).pack()

    tk.Button(root,
              text="Exit",
              command=root.quit).pack(pady=5)


# --------------------------------------------------------
# FUNCTION: validate_preferences()
# --------------------------------------------------------
def validate_preferences():

    global selected_preferences
    selected_preferences = []

    if veg.get():
        selected_preferences.append("Vegetarian")
    if vegan.get():
        selected_preferences.append("Vegan")
    if gluten.get():
        selected_preferences.append("Gluten-Free")
    if keto.get():
        selected_preferences.append("Keto")
    if lowcarb.get():
        selected_preferences.append("Low Carb")

    if len(selected_preferences) == 0:
        messagebox.showerror("Error",
                             "Please select at least one preference.")
    else:
        show_meal_plan()


# --------------------------------------------------------
# FUNCTION: show_meal_plan()
# --------------------------------------------------------
def show_meal_plan():

    for widget in root.winfo_children():
        widget.destroy()

    if not selected_preferences:
        show_preferences()
        return

    pref = selected_preferences[0]

    tk.Label(root,
             text=f"{pref} Meal Plan",
             font=("Arial", 24, "bold")).pack(pady=20)

    meal_data = {

        "Vegetarian":
        ("vegetarian.png",
         "Breakfast:\nGreek yogurt with fruit.\n\n"
         "Lunch:\nCaprese salad.\n\n"
         "Dinner:\nVegetable stir fry with tofu.\n"),

        "Gluten-Free":
        ("glutenfree.png",
         "Breakfast:\nGluten-free oatmeal with berries.\n\n"
         "Lunch:\nGrilled chicken with sweet potatoes.\n\n"
         "Dinner:\nShrimp with quinoa and vegetables.\n"),

        "Keto":
        ("keto.png",
         "Breakfast:\nScrambled eggs with avocado.\n\n"
         "Lunch:\nGrilled chicken over greens.\n\n"
         "Dinner:\nBaked salmon with vegetables.\n"),

        "Vegan":
        ("vegan.png",
         "Breakfast:\nChia pudding with berries.\n\n"
         "Lunch:\nQuinoa bowl with chickpeas.\n\n"
         "Dinner:\nLentil curry over rice.\n"),

        "Low Carb":
        ("lowcarb.png",
         "Breakfast:\nSpinach omelet.\n\n"
         "Lunch:\nTurkey lettuce wraps.\n\n"
         "Dinner:\nGrilled steak with asparagus.\n")
    }

    img_file, text = meal_data[pref]

    section = tk.Frame(root)
    section.pack(pady=20, fill="x")

    # TEXT (Always shown)
    tk.Label(section,
             text=text,
             justify="left",
             wraplength=650,
             font=("Arial", 12)).pack(pady=10)

    # SHOW IMAGE FOR ALL EXCEPT VEGETARIAN
    if pref != "Vegetarian":
        images[pref] = tk.PhotoImage(file=img_file).subsample(5,5)

        tk.Label(section,
                 image=images[pref]).pack(pady=10)

    # BACK & EXIT BUTTONS (Now clearly visible)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=30)

    tk.Button(button_frame,
              text="Back",
              width=15,
              command=show_preferences).grid(row=0, column=0, padx=30)

    tk.Button(button_frame,
              text="Exit",
              width=15,
              command=root.quit).grid(row=0, column=1, padx=30)

# --------------------------------------------------------
# Start Program
# --------------------------------------------------------
show_main()
root.mainloop()