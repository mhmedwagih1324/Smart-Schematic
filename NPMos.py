from schemdraw.elements.elements import Element
from schemdraw.elements.twoterm import reswidth, Element2Term
from schemdraw.segments import Segment, SegmentArrow, SegmentCircle
from schemdraw.adddocs import adddocs

from schemdraw.elements.oneterm import Vdd, Ground
from schemdraw.elements.lines import Dot, LineDot, Line, CurrentLabelInline

import schemdraw
import schemdraw.elements as e

fetw = reswidth*4
feth = reswidth*5
fetl = feth/2
fetgap = reswidth*1.5
fetr = reswidth*.7  # Radius of "not" bubble

@adddocs(Element)
class NMos(Element):
    ''' N-type Field Effect Transistor
        Anchors: `source`, `drain`, `gate`.

        Parameters
        ----------
        bulk : bool
            Draw bulk contact
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        bulk = kwargs.pop('bulk', False)
        self.segments.append(Segment([[0, 0], [0, -fetl]]))
        self.segments.append(SegmentArrow([0, -fetl], [fetw, -fetl], headwidth=0.2))
        self.segments.append(Segment([[fetw, -fetl/2], [fetw, -1.5*fetl-fetw]]))
        self.segments.append(Segment([[fetw, -fetl-fetw], [0, -fetl-fetw],
                                      [0, -2*fetl-fetw]]))


        self.segments.append(Segment([[fetw+fetgap, -fetl],
                                      [fetw+fetgap, -fetl-fetw]]))
        self.segments.append(Segment([[fetw+fetgap, -fetl-fetw/2],
                                      [fetw+fetgap+fetl+fetr, -fetl-fetw/2]]))

        self.anchors['source'] = [0, -2*fetl-fetw]
        self.anchors['drain'] = [0, 0]
        self.anchors['gate'] = [fetw+fetgap+fetl+fetr, -fetl-fetw/2]
        self.params['drop'] = [0, -2*fetl-fetw]
        self.params['lblloc'] = 'lft'
        if bulk:
            self.segments.append(Segment([[0, -fetl], [0, -fetl-fetw/2],
                                              [fetw, -fetl-fetw/2]]))
            self.anchors['bulk'] = [0, -fetl-fetw/2]


@adddocs(Element)
class PMos(Element):
    ''' P-type Field Effect Transistor
        Anchors: `source`, `drain`, `gate`.

        Parameters
        ----------
        bulk : bool
            Draw bulk contact
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        bulk = kwargs.pop('bulk', False)
        self.segments.append(Segment([[0, 0], [0, -fetl], [fetw, -fetl]]))
        self.segments.append(Segment([[fetw, -fetl/2], [fetw, -1.5*fetl-fetw]]))
        self.segments.append(SegmentArrow([fetw, -fetl-fetw], [0, -fetl-fetw], headwidth=0.2))
        self.segments.append(Segment([[0, -fetl-fetw], [0, -2*fetl-fetw]]))


        self.segments.append(Segment([[fetw+fetgap, -fetl],
                                      [fetw+fetgap, -fetl-fetw]]))
        self.segments.append(Segment([[fetw+fetgap, -fetl-fetw/2],
                                      [fetw+fetgap+fetl+fetr, -fetl-fetw/2]]))

        self.anchors['source'] = [0, 0]
        self.anchors['drain'] = [0, -2*fetl-fetw]
        self.anchors['gate'] = [fetw+fetgap+fetl+fetr, -fetl-fetw/2]
        self.params['drop'] = [0, -2*fetl-fetw]
        self.params['lblloc'] = 'lft'
        if bulk:
            self.segments.append(SegmentArrow([0, -fetl-fetw/2],
                                              [fetw, -fetl-fetw/2],
                                              headwidth=.2))
            self.anchors['bulk'] = [0, -fetl-fetw/2]



@adddocs(Element2Term)
class Bias(Line):
    ''' Line with a dot at the end

        Parameters
        ----------
        double : bool
            Show dot on both ends
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        radius = kwargs.get('radius', 0.125)
        fill = None if kwargs.get('open', False) else kwargs.get('fill', True)
        zorder = kwargs.get('zorder', 4)
        self.segments.append(SegmentCircle(
            [radius, 0], radius, ref='end', fill=fill, zorder=zorder))
        l = kwargs["l"] # represents length
        if kwargs.get('b', False):
            self.segments.append(Segment([[l, -radius], [l-3*radius, radius]],
                ref='end', fill=fill, zorder=zorder))
        if kwargs.get('double', False):
            self.segments.append(SegmentCircle(
                [0, 0], radius, ref='start'))
        self.anchors['center'] = [0, 0]  # Explicitly define center so reverses work
