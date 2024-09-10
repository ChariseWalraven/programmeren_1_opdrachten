# Write your solution here
voornaam = input('wat is je voornaam?')
achternaam = input('wat is je achternaam?')
straatdres = input('wat is je straatadres (inclusief huisnr)?')
stad_postcode = input('wat is je stad en postcode?')


res = f"""{voornaam} {achternaam}
{straatdres}
{stad_postcode}"""

print(res)
