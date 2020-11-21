import scraper
import solver

scraper.scrape()
choice = input('Show Possible Solution(s)?\n(Y)es\t(n)o\n\n')
if choice.lower() == 'y' or choice.lower() == 'yes':
    print("\nAll Possible Solutions are:\n")
    solver.solve()
print('Done...')
print("tes")
