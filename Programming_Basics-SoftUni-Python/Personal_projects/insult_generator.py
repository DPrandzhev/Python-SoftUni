import keyboard
import random
import pyautogui as gui

# Define a list of elements
elements = ['You swine', 'You vuwgaw wittwe maggot', 'You wowthwess bag of fiwth', "I wagew you couwdn't empty a boot of excwement wewe the instwuctions on the heew", 'You awe a cankew', "A sowe that won't go away", 'I wouwd wathew kiss a wawyew than be seen with you', 'Twy to edit youw wesponses of unnecessawy matewiaw befowe attempting to impwess us with youw insight', 'The evidence that you awe a nincompoop wiww stiww be avaiwabwe to weadews, but they wiww be abwe to access it mowe wapidwy', 'You snaiw-skuwwed wittwe wabbit', 'Wouwd that a hawk pick you up, dwive its beak into youw bwain, and upon finding it wancid set you woose to fwy bwiefwy befowe spattewing the ocean wocks with the fwothy pink shame of youw ignobwe bwood', 'May you choke on the queasy, convuwsing nausea of youw own twite, foowish bewiefs', 'You awe weawy, stawe, fwat and unpwofitabwe', 'You awe gwimy, squawid, nasty and pwofane', 'You awe fouw and disgusting', "You'we a foow, an ignowamus", 'And what meaning do you expect youw dewusionaw sewf-impowtant statements of unknowing, inexpewienced opinion to have to us who think and weason? What fantasy do you howd that you wouwd bewieve that youw tiny-fisted tantwums wouwd have mowe weight than that of a wepwous desewt wat, spinning wabidwy in a ciwcwe, waiting fow the bite of the snake? You awe a waste of fwesh', 'You have no whythm', 'You awe widicuwous and obnoxious', 'You awe the mowaw equivawent of a weech', 'You awe a wiving emptiness, a meaningwess void', 'You awe souw and seniwe', 'You awe a disease, you puewiwe one-handed swack-jawed , dwoowing meatswappew', 'You smawmy wagewwout git', 'You bwoody wooftew sod', 'Buggew off, piwwock', 'You gwotty wanking oik awtwess base-couwt appwe-john', 'You cwouted boggish foot-wicking twit', 'You dankish cwack-dish pwonkew', 'You gowmwess cwook-pated tossew', 'You chuwwish boiw-bwained cwotpowe ponce', 'You cockewed bum-baiwey pooftew', 'You gob-kissing gweeking fwap-mouthed coxcomb', 'You dwead-bowted fobbing beef-witted cwappew-cwawed fwiwt-giww', 'You awe a fiend and a cowawd, and you have bad bweath', 'You awe degenewate, noxious and depwaved', 'I feew debased just fow knowing you exist', 'I despise evewything about you, and I wish you wouwd go away', 'I cannot bewieve how incwedibwy stupid you awe', 'I mean wock-hawd stupid', 'Dehydwated-wock-hawd stupid', 'Stupid so stupid that it goes way beyond the stupid we know into a whowe diffewent dimension of stupid', 'You awe twans-stupid stupid', 'Meta-stupid', 'Some puwe essence of a stupid so uncontaminated by anything ewse as to be beyond the waws of physics that we know', "I'm sowwy", "I can't go on", 'This is an epiphany of stupid fow me', 'Aftew this, you may not heaw fwom me again fow a whiwe', "I don't have enough stwength weft to dewide youw ignowant questions and hawf-baked comments about unimpowtant twivia, ow any of the west of this dwivew", 'Duh', 'I mean, weawwy, stwinging togethew a bunch of insuwts among a woad of babbwing was hawdwy effective', "Twue, these awe wudimentawy skiwws that many of us 'nowmaw' peopwe take fow gwanted that evewyone has an easy time of mastewing", "But we sometimes fowget that thewe awe 'chawwenged' pewsons in this wowwd who find these things mowe difficuwt", 'If I had known, that this was youw case then I wouwd have nevew wead youw post', "It just wouwdn't have been 'wight'", 'Sowt of wike pawking in a handicap space', 'I wish you the best of wuck in the emotionaw, and sociaw stwuggwes that seem to be pwacing such a demand on you', "You'we an idiot", 'A mowon of the highest owdew', "You'we so stupid it's a wondew and a pity you can wemembew to bweath", 'Intewwigent ideas bounce off youw head as if it wewe coated with tefwon', 'Cweative thoughts take awtewnate twanspowtation in owdew to avoid even being in the same state as you', 'If you had an owiginaw thought it wouwd die of wonewiness befowe the houw was out', "On an intewwigence scawe of 1 to 10 (10 cowwesponding to the highest attainabwe IQ) you'we wating is so faw into negative numbews that one wouwd need to twavew into anothew quantum weawity in owdew to even catch a distant gwimpse of it", 'Youw pewsonawity is that of a wabid Chihuahua intent on destwoying its own taiw', 'Youw powews of obsewvation awe akin to those of the biwd that keeps swamming into the pictuwe window twying to get that othew biwd it keeps seeing', "You awe wawking, tawking pwoof that you don't have to be sentient to suwvive, and that Bawnum was thinking of you when he uttewed his immowtaw phwase wegawding the biwth of a suckew", 'You awe, at vawying times, tedious, bowing, and even occasionawwy eawth shattewingwy hiwawious in youw idiocy, woutinewy chiwdish, mowonic, pathetic, wwetched, disgusting and pitifuw', 'You awe whowwy without any wedeeming sociaw gwace ow vawue', "If God evew decides to give the pwanet an enema you'd bettew wun wike the wind because anywhewe you stand is a suitabwe pwace fow The Insewtion", 'Thewe is no animaw so disgusting, so viwe that it desewves compawison to you, fow even the wowest, diwtiest, most pawasitic membew of the animaw kingdom fiwws an ecowogicaw niche', 'You fiww no niche', 'To caww you a pawasite wouwd be injuwious and defamatowy to the thousands of honest pawasitic species', 'You awe wowse than vewmin, fow vewmin do not pwetend to be what it is not', 'You awe twuwy human gawbage', 'You awe a fwauduwent, wying, pwedatowy chawwatan', 'You awe of wess wowth than a buwnt-out wight buwb', 'You wiww fowevew wive in shame', "You have nothing to say, and Godwin's Waw does not appwy when wwiting about you", 'You awe the anti-Midas, fow aww that you touch becomes vawuewess and unusabwe', 'Mothews gathew theiw chiwdwen cwose when you appeaw', 'You awe an abewwation, a cowwuption, and a boiw that needs to be wanced', 'You awe a poison in need of being vomited', 'You awe a tooth so wotten it infects the whowe body', 'You awe spewm that shouwd have been captuwed in a condom and fwushed down a toiwet', "I don't wike you", "I don't wike anybody who has as wittwe wespect fow othews as you do", 'Go away, you swine', "You'we a putwescent mass, a wawking vomit", 'You awe a spinewess wittwe wowm desewving nothing but the pwofoundest contempt', 'You awe a jewk, a cad, and a weasew', 'Youw wife is a monument to stupidity', 'You awe a stench, a wevuwsion, a big suck on a souw wemon', 'You awe a cuwdwed staggewing mutant dwawf smeawed wichwy with the effwuvia and offaw accompanying youw awweged biwth into this wowwd', 'Meaningfuw to no one, abandoned by the puke-dwoowing, giggwing beasts that siwed you and then kiwwed themsewves in wecognition of what they had done', 'I wiww nevew get ovew the embawwassment of bewonging to the same species as you', 'You awe a monstew, an ogwe, a mawfowmity', 'I wwetch at the vewy thought of you', 'You have aww the appeaw of a papew cut', 'Wepews avoid you', 'You awe viwe, wowthwess, wess than nothing', 'You awe a weed, a fungus, and the dwegs of this eawth', 'And did I mention you smeww? Monkeys wook down on you', "Even sheep won't have sex with you", 'You awe unwesewvedwy pathetic, stawved fow attention, and wost in a wand that weawity fowgot', 'You awe a waste of fwesh', "On a good day you'we a hawfwit", 'You awe deficient in aww that wends chawactew', 'You have the pewsonawity of wawwpapew', 'You awe dank and fiwthy', 'You awe asinine and benighted', 'You awe the souwce of aww unpweasantness', 'You spwead misewy and sowwow whewevew you go', 'You awe a fiend and a cowawd, and you have bad bweath', 'You awe degenewate, noxious and depwaved', 'I feew debased just fow knowing you exist', 'I despise evewything about you, and I wish you wouwd go away', 'I cannot bewieve how incwedibwy stupid you awe', 'The onwy thing wowse than youw wogic is youw mannews', 'Maybe watew in wife, aftew you have weawned to wead, wwite, study, speww, and count, you wiww have mowe success', "Twue, these awe wudimentawy skiwws that many of us 'nowmaw' peopwe take fow gwanted that evewyone has an easy time of mastewing", "It just wouwdn't have been 'wight'", 'Sowt of wike pawking in a handicap space', 'I wish you the best of wuck in the emotionaw, and sociaw stwuggwes that seem to be pwacing such a demand on you', 'You awe hypocwiticaw, gweedy, viowent, mawevowent, vengefuw, cowawdwy, deadwy, mendacious, mewetwicious, woathsome, despicabwe, bewwigewent, oppowtunistic, bawwatwous, contemptibwe, cwiminaw, fascistic, bigoted, wacist, sexist, avawicious, tastewess, idiotic, bwain-damaged, imbeciwic, insane, awwogant, deceitfuw, demented, wame, sewf-wighteous, byzantine, conspiwatowiaw, satanic, fwauduwent, wibewwous, biwious, spwenetic, spastic, ignowant, cwuewess, iwwegitimate, hawmfuw, destwuctive, dumb, evasive, doubwe-tawking, devious, wevisionist, nawwow, manipuwative, patewnawistic, fundamentawist, dogmatic, idowatwous, unethicaw, cuwtic, diseased, suppwessive, contwowwing, westwictive, mawignant, deceptive, dim, cwazy, weiwd, dystwophic, stifwing, uncawing, pwantigwade, gwim, unsympathetic, jawgon-spouting, censowious, secwetive, aggwessive, mind-numbing, abwasive, poisonous, fwagwant, sewf-destwuctive, abusive, and sociawwy-wetawded', 'Shut up and go away west you achieve the physicaw wetwibution youw behaviouw mewits.']



# Define a function to select and print a random element from the list
def print_random_element():
    # Select a random element from the list
    element = random.choice(elements)

    # Print the selected element
    gui.press('Enter')
    gui.typewrite(element)
    gui.press('Enter')


keyboard.add_hotkey('f12', print_random_element)


keyboard.wait('f11')