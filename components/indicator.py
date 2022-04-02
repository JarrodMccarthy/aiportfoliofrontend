import dash_daq as daq

def make_indicator(colour, compliant, entity):
    ind = daq.Indicator(
        label="{} Compliant : {}".format(entity, compliant),
        color=colour,
        value=True,
        width=30,
        height=30
    )
    return ind