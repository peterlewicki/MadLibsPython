user1 = input("Hello there, what's your name? ")
print()
print(f"Alright, {user1.title()}, let's make a quick Mad Lib together!")
print()

Name1 = input('Give me a Name: ').title()

Noun1 = input('Give me a noun: ').lower()

Noun2 = input('Lets have another noun: ').lower()

Adjective1 = input('Now I need an adjective: ').lower()

Noun3 = input('One more noun: ').lower()

Noun4 = input('Yet another noun: ').lower()

PluralNoun = input('And lastly, a plural noun: ').lower()

print()

print(f"Cool!  Here's your story, {user1.title()}...")

print()

#below
print(f'Once upon a time, in a faraway Kingdom, was a Prince named {Name1}, who lived in a tall {Noun1} made of {Noun2}.\n'
     f'Each morning, Prince {Name1} would usually look out over the land and see the {Noun3} rise above the horizon. \n' 
     f'This morning was different though.  Rather than the {Noun3}, Prince {Name1} saw a {Adjective1} {Noun4} rising in the sky. \n'
      f' "Good Heavens", thought the Prince. "Looks like I have to wear my {PluralNoun} today." ')

print()

print(f'I hope you had a laugh, {user1.title()}, and we will do this again sometime.' )