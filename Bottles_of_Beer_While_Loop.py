beers = 99
while (beers > 0):
   print str(beers) + " bottles of beer on the wall", str(beers) + " bottles of beer, if one of those bottles happens to fall"
   beers = beers - 1
   if beers < 99:
       print str(beers) + " bottles of beer on the wall"
   if beers < 1:
       print "no more bottles of beer on the wall"
