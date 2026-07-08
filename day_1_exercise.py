# Python

# Part 1: Mentorship & Real-World Theory (20 Minutes)
# In the real world of Data and AI, your code will constantly talk to
# external software via APIs (Application Programming Interfaces).
# When you request data from an AI model or a marketing platform,
# it returns that data as text, numbers, or true/false flags.
#
# To handle this data in Python,
# you use Variables (think of them as labeled storage boxes in computer memory).
# Python uses Dynamic Typing, which means it instantly figures out
# what kind of data you put inside the box without you having to spell it out.
#
# The four essential building blocks you must know today are:
#
# String (str): Text data, always enclosed in quotes. e.g., "Alex" or "Enterprise"
#
# 1 - Integer (int): Whole numbers without decimals.
#       e.g., 25 or 5000 (Great for counting rows/users)
#
# 2 - Float (float): Numbers with decimals.
#       e.g., 45.50 or 0.05 (Crucial for percentages, financial rates, or weights)
#
# 3 - Boolean (bool): True or False.
#       e.g., True or False (Used as binary switches to trigger automations)


# ======================================================
# Part 2: Interactive Code Construction (20 Minutes)
# Day 1 - Variable assigment and String Interpolation(f-string)

# 1. Silumating data received from a client database
client_name = "Acme Analytics"      #String
monthly_ad_spend = 5000             #Integer
conversion_rate = 0.045             #Float(This represents 4.5%)
is_active_account = True            # Boolean

# 2. performing a quick Data Transformation
# We calculate total esimated conversions(Ad spend multiplied by conversion rate)
estimated_conversions = monthly_ad_spend * conversion_rate

# 3. Presenting the data professionally using and f-string
# The 'f' before the quote lets you drop variables directly into text using curly brackets {}
performance_summary =  f"Client: {client_name} | Spend: ${monthly_ad_spend} | Est. Conversions: {estimated_conversions}"

# 4. Printing the output in terminal
print(performance_summary)
print(f"Data type of conversion rate is: {type(conversion_rate)}")


# ======================================================
# Part 3: Your Daily Exercise Challenge (20 Minutes)
# Now, it's your turn to write code from scratch.
# I want you to simulate an AI pipeline input.
#
# The Scenario: An AI chatbot processes a customer inquiry and
# hands off three pieces of raw data to your script.
#
# 1. Create a variable named customer_email and assign it any email address string.
customer_email = "jane_doe@coldmail.co"

# 2. Create a variable named ai_confidence_score and
#       assign it a decimal value between 0 and 1 (e.g., 0.88).
ai_confidence_score = 0.75

# 3. Create a variable named requires_human_intervention and
#       assign it a Boolean (True or False).
requires_human_intervention = True

# 4. Calculate a fictional priority score by multiplying ai_confidence_score by 100.
priority_score = ai_confidence_score * 100

# 5. Use an f-string to print a clean message that looks exactly like this in the terminal:

#   SYSTEM ALERT: [Email] processed with a priority score of [Score].
#   Human Review Required: [True/False]

print(f"SYSTEM ALERT: {customer_email} processed with a priority score of {priority_score}")
print(f"Human Review Required: {requires_human_intervention}")