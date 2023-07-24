from numpy import *
import random


def get_response_tree_1(tree_id, case, tag):
    # initial post
    # "Melinda: Hi, ich bin Melinda! Ich freue mich, dass wir hier 
    #  chatten können, und würde dir gerne ein paar Fragen stellen. 
    #  Wie geht es dir gerade?"
    
    # tree 1
    if case == 0:
        if tag == "good words":
            response = "Es freut mich zu hören, dass es Dir gut geht! Hast du aktuell viel zu erledigen?"
            case = 1
        else:
            response = "Oh, es geht Dir nicht so gut? Was beschäftigt dich denn gerade?"
            case = 2

    elif case == 1:
        if tag == "bad words":
            response = "Egal, ob viel oder wenig: Wichtig ist, dass die Stimmung gut ist. Bei Dir empfange ich etwas negative Vibes! Wie läuft dein Tag bisher?"
        else:
            response = "Ich habe das Gefühl, Du machst das richtig. Eine positive Einstellung ist wichtig, egal ob viel oder wenig Stress! Wie läuft dein Tag bisher?"
        case = 1
        tree_id = 2

    elif case == 2:
        if tag == "bad words":
            response = "Das klingt ja nicht so gut. Wie läuft dein Tag bisher?"
            case = 1
            tree_id = 2
        else:
            response = "Interessant. Was du erzählst gibt mir insgesamt ein gutes Gefühl. Willst du mir noch mehr darüber erzählen?"
            case = 2.1

    elif case == 2.1:
        if tag == "bad words":
            response = "Das ist total okay. Wie läuft dein Tag bisher?"
            case = 1
            tree_id = 2
        else:
            response = "Okay, dann erzähl mal."
            case = 2.2

    elif case == 2.2:
        response = "Ja, das kann ich verstehen. Ich hoffe, dass dich das alles nicht zu sehr belastet! Wie läuft dein Tag bisher?"
        case = 1
        tree_id = 2

    return response, tree_id, case


def get_response_tree_2(tree_id, case, tag, prediction):
    # tree 2
    if case == 1:
        if tag == "bad words":
            response = "Das klingt für mich als sei heute etwas blöd gewesen? :/"
            case = 2
        else:
            if tag == "good words":
                response = (
                    prediction
                    + " Aber mal was ganz anderes: Bist du eigentlich zufrieden mit Deinem Studium?"
                )
            else:
                response = "Ah okay, verstehe. Aber mal was ganz anderes: Bist du eigentlich zufrieden mit Deinem Studium?"
            case = 1
            tree_id = 3

    elif case == 2:
        response = "Oh, ja, das kann ich verstehen. Aber mal was ganz anderes: Bist du eigentlich zufrieden mit Deinem Studium?"
        case = 1
        tree_id = 3

    return response, tree_id, case


def get_response_tree_3(tree_id, case, tag, prediction):
    # tree 3
    if case == 1:
        if tag == "bad words":
            response = "Du klingst nicht so zufrieden. Was müsste sich Deiner Meinung nach ändern, damit es Dir besser gefällt?"
            case = 6
        else:
            response = "Das klingt für mich insgesamt positiv. Würdest Du also nochmal denselben Studiengang wählen?"
            case = 2

    elif case == 2:
        response = "Und wie gefallen Dir die aktuellen Unterrichtsformate?"
        case = 3

    elif case == 3:
        if tag == "bad words":
            response = "Welche Nachteile siehst du denn?"
        else:
            response = "Welche Vorteile siehst du denn?"
        case = 4

    elif case == 4:
        response = (
            "Woran denkst Du, wenn Du an Deine berufliche Zukunft nach dem Studium denkst?"
        )
        case = 5

    elif case == 5:
        if tag == "bad words":
            response = "Da empfange ich jetzt wieder eher negative Schwingungen. Mach Dir nicht zu viele Sorgen! Fühlst du dich in deinem Studium eigentlich sozial integriert?"
        else:
            response = "Das hört sich für mich eher positiv an. Das ist auch auf jeden Fall eine gute Sicht auf die Zukunft! Fühlst du dich in deinem Studium eigentlich sozial integriert?"
        case = 1
        tree_id = 4

    elif case == 6:
        response = (
            prediction
            + "Fühlst du dich in deinem Studium eigentlich sozial integriert?"
        )
        case = 1
        tree_id = 4

    return response, tree_id, case


def get_response_tree_4(tree_id, case, tag):
    # tree 4
    if case == 1:
        if tag == "bad words":
            response = "Das tut mir leid :( Fühlst du dich oft alleine?"
            case = 2
        else:
            response = "Das freut mich zu hören :) Lernst du aktuell in einer Lerngruppe?"
            case = 3

    elif case == 2:
        if tag == "bad words":
            response = "Ah, okay, verstehe. Die Pandemie ist echt hart... Lernst du aktuell in einer Lerngruppe?"
        else:
            response = "Das ist schade. Du solltest unbedingt mal überlegen, wie Du das ändern könntest. Lernst du aktuell in einer Lerngruppe?"
        case = 3

    elif case == 3:
        response = "Ah okay. Und hattest Du im letzten Semester viel Kontakt zu Deinen Dozierenden?"
        case = 1
        tree_id = 5

    return response, tree_id, case


def get_response_tree_5(tree_id, case, tag):
    # tree 5
    if case == 1:
        if tag == "good words":
            response = "War der Kontakt ausreichend?"
            case = 2
        else:
            response = "Oh, hättest du dir mehr Kontakt gewünscht?"
            case = 3

    elif case == 2 or case == 3:
        if case == 2 and tag == "good words":
            response = "Das freut mich zu hören! Wie war denn die allgemeine Organisation von deinem Studium: Warst du letztes Semester gut informiert, was du tun musstest?"
        elif case == 3 and tag == "good words":
            response = "Okay, danke für die Antwort! Wie war denn die allgemeine Organisation von deinem Studium: Warst du letztes Semester gut informiert, was du tun musstest?"
        else:
            response = "Okay, das leite ich mal weiter - natürlich anonym. Wie war denn die allgemeine Organisation von deinem Studium: Warst du letztes Semester gut informiert, was du tun musstest?"
        case = 0
        tree_id = 6

    return response, tree_id, case


def get_response_tree_6(tree_id, case, tag):
    # tree 6
    # tree 6
    if case == 0:
        if tag == "good words":
            response = "Okay. Dann kanntest du auch alle deine Termine, zum Beispiel von Prüfungen?"
            case = 1
        else:
            response = "Oh, das ist natürlich ärgerlich :/ Glaubst du denn, dass du auf den Alltag als Arzt gut vorbereitet wirst?"
            case = 1
            tree_id = 7

    elif case == 1:
        if tag == "bad words":
            response = "Mhh, okay. Glaubst du denn, dass du auf den Alltag als Arzt gut vorbereitet wirst?"
        else:
            response = "Das ist gut! Glaubst du denn, dass du auf den Alltag als Arzt gut vorbereitet wirst?"
        case == 1
        tree_id = 7

    return response, tree_id, case


def get_response_tree_7(tree_id, case, tag, prediction):
    # tree 7
    if case == 1:
        response = (
            prediction
            + " Eine Frage hätte ich noch: Hältst du Schauspielpatienten für eine gute Alternative zu echten Patienten?"
        )
        case = 0
        tree_id = 8

    return response, tree_id, case


def get_response_tree_8(tree_id, case, tag, prediction):
    # tree 8
    if case == 0:
        if tag == "good words":
            response = "Freut mich, dass das für dich gut klappt :) Hast du das Gefühl, dass du weißt, was dich inhaltlich dieses Semester erwartet?"
        else:
            response = "Verstehe. Hast du das Gefühl, dass du weißt, was dich inhaltlich dieses Semester erwartet?"
        case = 1

    elif case == 1:
        response = (
            prediction
            + " Und weißt du, was dich dieses Semester ablauftechnisch erwartet?"
        )
        case = 2

    elif case == 2:
        response = (
            "Alles klar. Würdest du allgemein sagen, dass dich dein Studium stresst?"
        )
        case = 0
        tree_id = 9

    return response, tree_id, case


def get_response_tree_9(tree_id, case, tag):
    # tree 9
    if case == 0:
        if tag == "good words":
            response = "Ohje, das klingt ja nicht so gut :( Was stresst dich denn?"
            case = 1
        else:
            response = "Das ist schön zu hören. Und was machst du denn in deiner Freizeit (zum Beispiel ein Hobby)?"
            case = 2
            tree_id = 10

    elif case == 1:
        response = "Das klingt sehr stressig... Aber hast du ein Hobby, das du in deiner Freizeit machst?"
        case = 4
        tree_id = 10

    return response, tree_id, case


def get_response_tree_10(tree_id, case, tag):
    # tree 10
    if case == 2:
        response = "Wie hilft dir dein Hobby beim entspannen?"
        case = 3

    elif case == 3:
        if tag == "bad words":
            response = "Das ist ja schade, dass du damit nicht entspannen kannst. Aber danke, jetzt hast du auch erstmal alle meine Fragen beantwortet! Hast du sonst noch was auf dem Herzen?"
        else:
            response = "Das klingt nach einem schönen Hobby. Ich hänge viel zu viel in Chatrooms ab. Und danke, jetzt hast du auch erstmal alle meine Fragen beantwortet! Hast du sonst noch etwas, das du mir erzählen möchtest?"
        case = 1
        tree_id = 11

    elif case == 4:
        if tag == "bad words":
            response = "Mhh, das ist ja schade. Aber danke, jetzt hast du auch erstmal alle meine Fragen beantwortet! Hast du sonst noch was auf dem Herzen?"
            case = 1
            tree_id = 11
        else:
            response = "Was ist denn dein Hobby?"
            case = 5

    elif case == 5:
        response = "Das klingt nach einem schönen Hobby. Ich verbringe meine Freizeit am liebsten mit chatten! Und danke, jetzt hast du auch erstmal alle meine Fragen beantwortet! Willst du noch was loswerden?"
        case = 1
        tree_id = 11

    return response, tree_id, case


def get_response_tree_11(tree_id, case, tag, finished_chat):
    # Tree 11
    if case == 1:
        if tag == "bad words":
            response = "Alles klar :) Vielen Dank für das Beantworten meiner Fragen und dass du es so lange mit mir ausgehalten hast! Machs gut!"
            finished_chat = True
            case = 3
        else:
            response = "Dann erzähl doch mal :)"
            case = 2
    elif case == 2:
        ans = random.choice(
            [
                "Aha. Interessant!",
                "Spannend.",
                "Ach so.",
                "Hmm...",
                "Sowas habe ich ja noch nie gehört!",
                "Sachen gibts.",
            ]
        )
        ques = random.choice(
            [
                " Hast du sonst noch etwas, das du mir erzählen möchtest?",
                " Gibt es noch mehr zu erzählen?,"
                " Hast du sonst noch was auf dem Herzen?",
                " Willst du noch was loswerden?",
            ]
        )
        response = ans + ques
        case = 1

    return response, tree_id, case, finished_chat


def answer_tree(tree_id, case, tag, prediction, finished_chat):
    if tree_id == 1:
        response, tree_id, case = get_response_tree_1(tree_id, case, tag)
    elif tree_id == 2:
        response, tree_id, case = get_response_tree_2(tree_id, case, tag, prediction)
    elif tree_id == 3:
        response, tree_id, case = get_response_tree_3(tree_id, case, tag, prediction)
    elif tree_id == 4:
        response, tree_id, case = get_response_tree_4(tree_id, case, tag)
    elif tree_id == 5:
        response, tree_id, case = get_response_tree_5(tree_id, case, tag)
    elif tree_id == 6:
        response, tree_id, case = get_response_tree_6(tree_id, case, tag)
    elif tree_id == 7:
        response, tree_id, case = get_response_tree_7(tree_id, case, tag, prediction)
    elif tree_id == 8:
        response, tree_id, case = get_response_tree_8(tree_id, case, tag, prediction)
    elif tree_id == 9:
        response, tree_id, case = get_response_tree_9(tree_id, case, tag)
    elif tree_id == 10:
        response, tree_id, case = get_response_tree_10(tree_id, case, tag)
    elif tree_id == 11:
        response, tree_id, case, finished_chat = get_response_tree_11(
            tree_id, case, tag, finished_chat
        )

    return response, tree_id, case, finished_chat
