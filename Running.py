import math
# def rein(asr, dos):
#     dia = float(dos)
#     pi = math.pi
#     area = pi * ((dos/2)**2)
#     xx = asr / area
#     xxa = math.ceil(xx)
#     print('Provide', xxa, dos,'mm bar')
#
# rein(asr=177, dos=16)

# val = int(input('Enter a number to check whether it is even or odd:'))
# if (val%2) == 0:
#     print('The entered value is even')
# else:
#     print('The entered value is odd')

# import math
# asr = input('Enter the area of steel required: ')
# di = input('Enter the preferred diameter of reinforcement: ')
# ara = float(asr)
# diam = float(di)
# pi = math.pi
# area = pi * (diam/2)**2
# nor = ara / area
# noq = math.ceil(nor)
# if (noq%2) == 0:
#     noq = noq
# else:
#     noq = noq + 1
# at = float(noq * area)
# print('Provide', noq,'Y',diam,'mm bars @', at, 'bottom')

# thi = input('Enter the slab thickness: ')
# ith = float(thi)
# vac = ith * 1000.0
# tha = mod1 * 1000.0
# perc = vac / tha
# ts = Mm * perc

import math


def get_float_input(prompt):
    return float(input(prompt))


def calculate_area(length, width):
    return length * width


def calculate_steel_area(moment, fyy, depth, width):
    la = 0.95
    z = la * depth
    return la * fyy * z


def calculate_reinforcement_area(area, bar_size):
    pi = math.pi
    return pi * (bar_size / 2) ** 2


def main():
    print('Panel dimensions')
    concrete_strength = 1000  # kN/m^2

    panel_length = get_float_input('Enter panel length: ')
    panel_width = get_float_input('Enter panel width: ')
    entire_slab_depth = get_float_input('Enter entire slab depth: ')
    slab_thickness = get_float_input('Enter the slab thickness: ')

    vacuum_area = slab_thickness * 1000.0
    total_area = panel_length * panel_width * entire_slab_depth
    perc = vacuum_area / entire_slab_depth

    void_mould_length = get_float_input('Enter mould length: ')
    void_mould_width = get_float_input('Enter mould width: ')
    volume_of_void_in_one_mould = get_float_input('Volume of void in one mould: ')
    bottom_length_of_rib = get_float_input('Enter the bottom length of rib: ')
    top_length_of_rib = get_float_input('Enter the top length of rib: ')

    rib_breadth = ((bottom_length_of_rib + top_length_of_rib) / 2) * 1000.0
    rib_area = void_mould_length * void_mould_width

    num_void_moulds = math.ceil(calculate_area(panel_length, panel_width) / calculate_area(rib_breadth, rib_breadth))
    void_volume = num_void_moulds * volume_of_void_in_one_mould

    net_void_volume = total_area - void_volume

    dead_load_constant = get_float_input('Enter dead load constant: ')
    live_load_constant = get_float_input('Enter live load constant: ')

    dead_load = 24.0 * panel_length * panel_width * dead_load_constant
    finishes_value = get_float_input('Enter the value for finishes: ')
    live_load = get_float_input('Enter the value for live load: ')
    total_load = live_load * panel_length * panel_width * live_load_constant + dead_load
    unit_load = total_load / calculate_area(panel_length, panel_width)

    unit_load_per_rib = unit_load * void_mould_length

    print(f'Unit load = {unit_load}')
    print(f'Unit load per rib = {unit_load_per_rib}')

    print('Enter moment coefficients from Table 3.14(BS 8110-1:1997)')
    negative_moment_at_continuous_edge = get_float_input('Enter negative moment at continuous edge: ')
    positive_moment_at_mid_span = get_float_input('Enter positive moment at mid-span: ')

    print('Designing for Span:')
    moment = unit_load_per_rib * panel_width ** 2 * positive_moment_at_mid_span
    print(f'Moment = {moment}')

    steel_strength = get_float_input('Enter the strength of steel: ')
    stirrup_diameter = get_float_input('Enter diameter of links: ')
    cover_length = get_float_input('Enter the length of cover: ')
    fcu_value = get_float_input('Enter value for FCu: ')

    effective_depth = entire_slab_depth * 1000 - stirrup_diameter - cover_length
    beam_width = panel_width * 1000
    Ak = moment * 10 ** 6
    Bk = fcu_value * beam_width * effective_depth ** 2
    K = Ak / Bk

    la = 0.95
    z = la * effective_depth
    As = la * steel_strength * z
    As_ratio = Ak / As

    print(f'Area of steel required = {As_ratio:.2f}')

    preferred_reinforcement_size = get_float_input('Enter the preferred reinforcement size: ')
    reinforcement_area = math.pi * (preferred_reinforcement_size / 2) ** 2

    number_of_bars = math.ceil(As_ratio / reinforcement_area)
    if number_of_bars == 1:
        number_of_bars += 1

    total_reinforcement_area = number_of_bars * reinforcement_area

    print(f'Provide {number_of_bars} - Y{preferred_reinforcement_size}mm bars @ {total_reinforcement_area:.2f} bottom')

    print('Designing for Support:')
    support_moment = unit_load_per_rib * panel_width ** 2 * negative_moment_at_continuous_edge
    print(f'Moment = {support_moment}')

    ka = support_moment * 10 ** 6
    den = void_mould_length * 1000 * fcu_value * effective_depth ** 2
    Ks = ka / den
    Ais = la * steel_strength * z
    ind = ka / Ais
    As_support = round(ind, 2)

    print(f'Area of steel required = {As_support:.2f}')

    preferred_support_reinforcement_size = get_float_input('Enter the preferred reinforcement size: ')
    reinforcement_area = math.pi * (preferred_support_reinforcement_size / 2) ** 2

    number_of_bars = math.ceil(As_support / reinforcement_area)
    if number_of_bars == 1:
        number_of_bars += 1

    total_reinforcement_area = number_of_bars * reinforcement_area

    print(
        f'Provide {number_of_bars} - Y{preferred_support_reinforcement_size}mm bars @ {total_reinforcement_area:.2f} top')

    print('Designing for top slab area to provide adequate minimum reinforcement:')
    top_slab_moment = moment * perc
    print(f'Moment = {top_slab_moment}')

    void_cover = 20.0
    reinforcement_size = 8.0
    no_of_reinforcement = reinforcement_size / 2
    void_depth = void_mould_length * 1000 - void_cover - no_of_reinforcement

    kr = top_slab_moment * 10 ** 6
    den = fcu_value * concrete_strength * void_depth
    rk = kr / den
    rrk = round(rk, 3)

    la = 0.95
    zz = la * void_depth
    ned = la * steel_strength * zz
    sa = kr / ned
    sas = round(sa)

    print(f'Area of Steel for the top slab = {sas}')

    print('Choose a satisfactory bar spacing and area from the spacing table within the 8mm row')
    bar_spacing = get_float_input('Enter bar spacing: ')
    tab = bar_spacing / concrete_strength
    no_of_bars_bottom = math.ceil(panel_length / tab)
    no_of_bars_top = math.ceil(panel_width / tab)

    print(f'Provide {no_of_bars_bottom} Y 8mm bars @ {bar_spacing}mm c/c bottom')
    print(f'Provide {no_of_bars_top} Y 8mm bars @ {bar_spacing}mm c/c top')

    print('Calculating Shear:')
    shear_coefficient = get_float_input('Enter value of shear coefficient: ')
    shear_force = shear_coefficient * unit_load_per_rib * panel_width
    print(f'Maximum shear force in the rib = {shear_force:.3f}')

    v = (shear_force * 10 ** 3) / (rib_breadth * effective_depth)
    print(f'v = {v:.3f}')

    reinforcement_ratio = (100 * total_reinforcement_area) / (rib_breadth * effective_depth)
    print(f'{reinforcement_ratio:.3f} %')

    zap = (400 / effective_depth) ** 0.25
    paz = 0.632 * (reinforcement_ratio ** 0.333) * zap
    vc = round(paz, 3)

    if vc > v:
        print(f'Vc = {vc}, Shear is satisfied')
    else:
        print(f'Vc = {vc}, Shear not satisfied')

    print('Providing Shear reinforcement:')
    shear_reinforcement_size = get_float_input('Enter shear reinforcement size: ')
    shear_reinforcement_strength = get_float_input('Enter the strength of the shear reinforcement: ')

    shear_reinforcement_area = (math.pi * (shear_reinforcement_size ** 2) / 4) * 2
    sv = (la * shear_reinforcement_area * shear_reinforcement_strength) / (rib_breadth * (v - vc))
    sp = (la * shear_reinforcement_area * shear_reinforcement_strength) / (0.4 * rib_breadth)

    spacing = math.ceil(sp)
    ad = 0.5 * vc
    bg = 0.4 + vc

    if v < ad:
        print('Provide minimum links')
    elif ad < v < bg:
        print(f'Provide R{shear_reinforcement_size}mm @ {spacing}mm c/c')


if __name__ == "__main__":
    main()



