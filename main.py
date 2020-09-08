from schemdraw.elements.elements import Element
from schemdraw.elements.twoterm import reswidth, Element2Term
from schemdraw.segments import Segment, SegmentArrow, SegmentCircle
from schemdraw.adddocs import adddocs

from schemdraw.elements.oneterm import Vdd, Ground
from schemdraw.elements.lines import Dot, LineDot, Line, CurrentLabelInline

import schemdraw
import schemdraw.elements as e

from NPMos import *

#--------------------------Middle branch-------------------
dr = schemdraw.Drawing() # lw is line widwth
VDD = dr.add(Vdd(toplabel='$V_{DD}$'))
I2 = dr.add(Line('down'))
dr.labelI_inline(I2, '$2I_{bias}$', d='in')
M6 = dr.add(NMos('l', rgtlabel='M6', flip=True))
dr.add(Bias('left', open=True, l=fetw, lftlabel='$V_{cmfb}$',
    b=True, lblofst=0.3, at=(M6, 'gate')))
M1a_M1b = dr.add(Dot(at=(M6, 'source')))
I2_l = dr.add(Line('left', l=3*fetw))
dr.labelI_inline(I2_l, botlabel='$i_{bias}$', d='in', ofst=0.1)
#dr.add(Line('down'))
M1a = dr.add(NMos('l', bulk=True, rgtlabel='M1a', flip=True))

dr.add(Dot(open=True, at=(M1a, 'gate'), lftlabel='$V_{in+}$'))
I2_r = dr.add(Line('right', at=(M1a_M1b, 'end'), l=3*fetw))
dr.labelI_inline(I2_r, botlabel='$i_{bias}$', d='in', ofst=0.1)
#dr.add(Line('down'))
M1b = dr.add(NMos('r', bulk=True, lftlabel='M1b'))
dr.add(Dot(open=True, at=(M1b, 'gate'), rgtlabel='$V_{in-}$'))

#-----------------------------Left branch---------------------------
dr.add(Line('left', at=(VDD, 'end')))
dr.add(Line('left'))
dr.add(Line('left'))
I1 = dr.add(Line('down', toy=M6.drain/2))
dr.labelI_inline(I1, '$I_{bias}$', d='in', ofst=0.2)
M5a = dr.add(NMos('r', lftlabel='M5a'))
M4a = dr.add(NMos('r', lftlabel='M4a'))

dr.add(Dot(at=(M4a, 'source')))
dr.add(Bias('left', open=True, l=fetw, lftlabel='$V_{out-}$', lblofst=0.3))
M3a = dr.add(PMos('r', lftlabel='M3a', at=(M4a, 'source')))
M2a = dr.add(PMos('r', lftlabel='M2a'))
M2a_M3a = dr.add(Dot(at=(M2a, 'source')))
dr.add(Line('down', at=(M1a, 'source'), toy=M2a_M3a.start))
dr.add(Line('left', tox=(M2a_M3a.start)))
dr.add(Ground(at=(M2a, 'drain')))

Vbiasn = dr.add(LineDot('right', at=(M2a, 'gate'), tox=VDD.start))
Vbiasp = dr.add(LineDot('right', at=(M5a, 'gate')))

dr.add(Bias('right', open=True, l=fetw, rgtlabel='$V_{cascp}$',
    b=True, lblofst=0.1, at=(M4a, 'gate')))
dr.add(Bias('right', open=True, l=fetw, rgtlabel='$V_{cascn}$',
    b=True, lblofst=0.1, at=(M3a, 'gate')))
dr.add(Bias('up', open=True, l=fetw, toplabel='$V_{biasn}$',
    b=True, lblofst=0.3, at=(Vbiasn, 'end')))
dr.add(Bias('up', open=True, l=fetw, rgtlabel='$V_{biasp}$',
    b=True, lblofst=0.3, at=(Vbiasp, 'end')))

#-----------------------------Right branch---------------------------
dr.add(Line('right', at=(VDD, 'end')))
dr.add(Line('right'))
dr.add(Line('right'))
I3 = dr.add(Line('down', toy=M6.drain/2))
dr.labelI_inline(I3, '$I_{bias}$', d='in', ofst=0.2)
M5b = dr.add(NMos('l', rgtlabel='M5b', flip=True))
M4b = dr.add(NMos('l', rgtlabel='M4b', flip=True, at=(M5b, 'source')))
dr.add(Dot(at=(M4b, 'source')))
dr.add(Bias('right', open=True, l=fetw, rgtlabel='$V_{out+}$', lblofst=0.3))
M3b = dr.add(PMos('l', rgtlabel='M3b', flip=True, at=(M4b, 'source')))
M2b = dr.add(PMos('l', rgtlabel='M2b', flip=True, at=(M3b, 'drain')))
M2b_M3b = dr.add(Dot(at=(M2b, 'source')))
dr.add(Line('down', at=(M1b, 'source'), toy=M2b_M3b.start))
dr.add(Line('right', tox=(M2b_M3b.start)))
dr.add(Ground(at=(M2b, 'drain')))
dr.add(Line('left', at=(M2b, 'gate'), tox=VDD.start))
dr.add(Line('left', at=(M5b, 'gate'), tox=Vbiasp.end))

dr.add(Bias('left', open=True, l=fetw, lftlabel='$V_{cascp}$',
    b=True, lblofst=0.1, at=(M4b, 'gate')))
dr.add(Bias('left', open=True, l=fetw, lftlabel='$V_{cascn}$',
    b=True, lblofst=0.1, at=(M3b, 'gate')))


# dr.add(Dot('up', open=True))
dr.draw()
dp = schemdraw.Drawing() # lw is line widwth
dp.add(PMos())
#dp.draw()
"""
x.draw()
d.draw()
"""
