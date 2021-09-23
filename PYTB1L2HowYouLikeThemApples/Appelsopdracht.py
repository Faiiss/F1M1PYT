import math


trees               = 333             
shadedTrees         = math.ceil(222)  
sunnyTrees          = 146             

shadeOutputModifier = 80             #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 20             #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = 30             #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = 20             #hoeveel appels geven alle zonnige bomen? 
shadedOutput        = 15             #hoeveel appels geven alle schaduw bomen?
totalOutput         = 35             #hoeveel appels zijn er in totaal?

owners              = 3             #met hoeveel mensen verdelen we de appels?

eatCount            = 8            #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = 26             #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = 26             #hoeveel appels mag ik verkopen?

print(cut)