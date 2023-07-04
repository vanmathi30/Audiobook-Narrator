import pyttsx3
import PyPDF2
import sys
import time

print("")
print("")
print("")
print("....#.....#...#.###..##..##....###...##...##..#..#...##..#.....#.....###..###......#.....#####..##..###.")
print("...#.#....#...#.#..#.##.#..#...#..#.#..#.#..#.#.#....##..#....#.#....#..#.#..#....#.#......#...#..#.#..#")
print("..#...#...#...#.#..#.##.#..#...###..#..#.#..#.##.....#.#.#...#...#...###..###....#...#.....#...#..#.###.")
print(".#######..#...#.#..#.##.#..#...#..#.#..#.#..#.#.#....#..##..#######..#.#..#.#...#######....#...#..#.#.#.")
print("#.......#...#...###..##..##....###...##...##..#..#...#..##.#.......#.#..#.#..#.#.......#...#....##..#..#")

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty("voices")
speaker.setProperty("voice", voices[0].id)
def speak(sentence):
    speaker.say(sentence)
    speaker.runAndWait()

speak("hai, i am audiobook narrator.....created by Vanmathie soogoomaaran ...... I will help you to read the book.....")


try:
    book = open('narrate.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    
    speak("Now i am going to read the book.............")

    for num in range(0, pages):
        page = pdfreader.getPage(0)
        text = page.extractText()
        speaker.setProperty("rate", 150)
        speak(text)

except FileNotFoundError:

    print("\n\n\nPlease set the pdf name as 'narrate' !!!")
    speak("Please set the pdf name as..... 'narrate'")

except Exception as e:

    print(e)

time.sleep(10)
sys.exit()
