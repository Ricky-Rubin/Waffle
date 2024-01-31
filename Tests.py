# wid = input('Enter the value for width: ')
# wid1 = float(wid)
# be = float(wid) * 1000
# print(be)

# M = 18.3022
# Sub = 6.32
# mul = M * Sub
# ll = round(mul)
# print(ll)

# una = m*m
# unb = m*m**2
# unc = m**2
# und = K*N/m
# ab = input('Enter a number: ')
# zk = input('Enter another number: ')
# mul = ab * zk * unb
# lum = ab / zk * unc
# print('This= ', mul)
# print('That= ',lum)

# print('Panel dimensions')
# len, wid = input('Enter panel lenght: '), input('Enter panel width: ')
# sdep = input('Enter slab depth: ')
# mod1 = float(sdep)
# vol =  float(len) * float(wid) * float(sdep)
# print('Panel volume is', vol)
# m1, m2 = input('Enter mould length: '), input('Enter mould width: ')
# m11 = float(m1)
# m22 = float(m2)
# given = input('Volume of void in one mould: ')
# dut = float(given)
# given2 = input('Enter the length of slab rib: ')
# mod2 = float(given2)
# A1 = float(len) * float(wid)
# dig = m11 + mod2
# A2 = dig * dig
# nom = A1 / A2
# print('Number of mould in one panel=', nom)
# vol2 = nom * dut
# print('Volume of void in one panel= ',vol2)
# Netv = vol - vol2
# print('Net volume of concrete in one panel= ', Netv)
#
# count = 50.5
# for values in (50.5, 50.5, 50.5, 50.5, 50.5):
#     count = count + values
# print(count, values)

# def rein(asr, dos):
#     dia = float(dos)
#     pi = math.pi
#     area = pi * ((dos/2)**2)
#     xx = asr / area
#     print(f'Provide{xx}mm bars')
#
# rein(asr=177, dos=16)

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

# dah = input('Enter a number: ')
# had = input('Enter another number: ')
# path = float(had) * float(dah)
# ba = round(path)
# print(ba)

# ts = Mm * 0.15
# tsp = round(ts, 3)
# bb = 1000.0
# hos = 75.0cmd
# voc = 20.0
# ren = 8.0
# ner = ren / 2
# dd = (hos) - (voc) - (ner)
# kr = tsp * 10 ** 6
# den = fcu1 * bb * dd
# rk = kr / den
# rrk = round(rk, 3)
# zz = la * dd
# ned = la * fyy * zz
# sa = kr / ned
# sas = round(sa)
# print('Area of Steel for the top slab= ', sas)


# len, wid = input('Enter panel length: '), input('Enter panel width: ')
# lenm = len * 1000
# widm = wid * 1000
# dat = input('Enter bar spacing: ')
# print(dat)
# tab = float(dat)
# print(tab)
# nub = float(lenm) / tab
# print('Number of bars=', nub)

# len, wid = input('Enter panel length: '), input('Enter panel width: ')
# print('Length is ', len, 'Width is ', wid)
# con = 1000
# sta = input('Enter the preferred spacing: ')
# ats = float(sta)/float(con)
# print(ats)

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


def main(panel_length, panel_width, entire_slab_depth, slab_thickness, void_mould_length, void_mould_width,
         volume_of_void_in_one_mould, bottom_length_of_rib, top_length_of_rib, dead_load_constant, live_load_constant,
         finishes_value, live_load_value, negative_moment_at_continuous_edge, positive_moment_at_mid_span, steel_strength,
         stirrup_diameter, cover_length, fcu_value, preferred_reinforcement_size,preferred_support_reinforcement_size,
         bar_spacing, shear_coefficient, shear_reinforcement_size, shear_reinforcement_strength):
    print('Design Loadings')
    factor_x = 1000

    panel_length = panel_length
    panel_width = panel_width
    entire_slab_depth = entire_slab_depth
    slab_thickness = slab_thickness

    top_slab_thickness = slab_thickness * 1000.0
    panel_volume = panel_length * panel_width * entire_slab_depth
    slab_depth_ratio = top_slab_thickness / (entire_slab_depth * 1000)

    void_mould_length = void_mould_length
    void_mould_width = void_mould_width
    volume_of_void_in_one_mould = volume_of_void_in_one_mould
    bottom_length_of_rib = bottom_length_of_rib
    top_length_of_rib = top_length_of_rib

    rib_breadth = ((bottom_length_of_rib + top_length_of_rib) / 2) * 1000.0
    #Rib_bradth is used as the breadth when calculating shear

    rib_length_centre_to_centre = void_mould_length + bottom_length_of_rib
    rib_width_centre_to_centre = void_mould_width + bottom_length_of_rib


    num_void_moulds = math.ceil(calculate_area(panel_length, panel_width) / calculate_area(rib_length_centre_to_centre, rib_width_centre_to_centre))
    void_volume = num_void_moulds * volume_of_void_in_one_mould

    net_void_volume = panel_volume - void_volume

    dead_load_constant = dead_load_constant
    live_load_constant = live_load_constant

    dead_load = 24.0 * net_void_volume * dead_load_constant
    finishes_value = finishes_value
    finishes = finishes_value * panel_length * panel_width * dead_load_constant
    live_load_value = live_load_value
    live_load = live_load_value * panel_length * panel_width * live_load_constant
    total_load = finishes + dead_load + live_load
    unit_load = total_load / calculate_area(panel_length, panel_width)

    unit_load_per_rib = unit_load * void_mould_length

    print(f'Unit load = {unit_load:.3f}KN/m per m. run')
    print(f'Unit load per rib = {unit_load_per_rib:.3f}KN/m per rib')

    print('Enter moment coefficients from Table 3.14(BS 8110-1:1997)\n')
    negative_moment_at_continuous_edge = negative_moment_at_continuous_edge
    positive_moment_at_mid_span = positive_moment_at_mid_span

    print('Designing for Span:')
    moment = unit_load_per_rib * panel_width ** 2 * positive_moment_at_mid_span
    print(f'Moment = {moment:.3f}KNm per rib')

    steel_strength = steel_strength
    stirrup_diameter = stirrup_diameter
    cover_length = cover_length
    fcu_value = fcu_value

    effective_depth = entire_slab_depth * 1000 - stirrup_diameter - cover_length
    beam_width = panel_width * 1000
    span_moment = moment * 10 ** 6
    span_denominator = fcu_value * beam_width * effective_depth ** 2
    k_value = span_moment / span_denominator

    la = 0.95
    z = la * effective_depth
    Area_of_steel_denominator = la * steel_strength * z
    Area_of_steel_for_span = span_moment / Area_of_steel_denominator

    print(f'Area of steel required = {Area_of_steel_for_span:.2f}mm^2')

    preferred_reinforcement_size = preferred_reinforcement_size
    reinforcement_area = math.pi * (preferred_reinforcement_size / 2) ** 2

    number_of_bars = math.ceil(Area_of_steel_for_span / reinforcement_area)
    if number_of_bars == 1:
        number_of_bars += 1

    total_reinforcement_area = number_of_bars * reinforcement_area

    print(f'Provide {number_of_bars} - Y{preferred_reinforcement_size}mm bars @ {total_reinforcement_area:.2f} bottom\n')

    print('Designing for Support:')
    support_moment = unit_load_per_rib * panel_width ** 2 * negative_moment_at_continuous_edge
    print(f'Moment = {support_moment:.3f}KNm')

    moment_conversion = support_moment * 10 ** 6
    moment_divisor = void_mould_length * 1000 * fcu_value * effective_depth ** 2
    support_k_value = moment_conversion / moment_divisor
    Ais = la * steel_strength * z
    support_area_of_steel = moment_conversion / Ais
    As_support = round(support_area_of_steel, 2)

    print(f'Area of steel required = {As_support:.2f}mm^2')

    preferred_support_reinforcement_size = preferred_support_reinforcement_size
    reinforcement_area = math.pi * (preferred_support_reinforcement_size / 2) ** 2

    number_of_bars = math.ceil(As_support / reinforcement_area)
    if number_of_bars == 1:
        number_of_bars += 1

    total_reinforcement_area = number_of_bars * reinforcement_area

    print(
        f'Provide {number_of_bars} - Y{preferred_support_reinforcement_size}mm bars @ {total_reinforcement_area:.2f} top\n')

    print('Designing for top slab area to provide adequate minimum reinforcement:')
    top_slab_moment = span_moment * slab_depth_ratio * 10 ** -6
    print(f'Moment = {top_slab_moment:.3f}KNm')
    #where perc is the ratio of slat thickness to entire slab depth. Multiplying the factor by the span moment to top slab moment.

    void_cover = 20.0
    reinforcement_size = 8.0
    no_of_reinforcement = reinforcement_size / 2
    top_slab_effective_depth = (slab_thickness * 1000) - void_cover - no_of_reinforcement

    denominator_for_k_value = fcu_value * (void_mould_width * 1000) * top_slab_effective_depth ** 2
    k_process = top_slab_moment / denominator_for_k_value
    final_k_value = round(k_process, 3)

    la = 0.95
    zz = la * top_slab_effective_depth
    denominator = la * steel_strength * zz
    AS_for_top_slab = top_slab_moment * 10 ** 6 / denominator
    Top_slab_area_of_steel = round(AS_for_top_slab)

    print(f'Area of Steel for the top slab = {Top_slab_area_of_steel}mm^2')

    print('Choose a satisfactory bar spacing and area from the spacing table within the 8mm row')
    bar_spacing = bar_spacing
    tab = bar_spacing / factor_x
    wall_thickness_deduction_for_bars = (230 + (2 * cover_length)) / factor_x
    no_of_bars_bottom = math.ceil(((panel_length - wall_thickness_deduction_for_bars) / tab) + 1)
    no_of_bars_top = math.ceil(((panel_width - wall_thickness_deduction_for_bars) / tab) + 1)

    print(f'Provide {no_of_bars_bottom} Y 8mm bars @ {bar_spacing}mm c/c bottom')
    print(f'Provide {no_of_bars_top} Y 8mm bars @ {bar_spacing}mm c/c top\n')

    print('Calculating Shear:')
    shear_coefficient = shear_coefficient
    shear_force = shear_coefficient * unit_load_per_rib * panel_width
    print(f'Maximum shear force in the rib = {shear_force:.3f}KN')

    v = (shear_force * 10 ** 3) / (rib_breadth * effective_depth)
    print(f'v = {v:.3f}N/mm^2')

    reinforcement_ratio = (100 * total_reinforcement_area) / (rib_breadth * effective_depth)
    print(f'{reinforcement_ratio:.3f} %')

    zap = (400 / effective_depth) ** 0.25
    paz = 0.632 * (reinforcement_ratio ** 0.333) * zap
    vc = round(paz, 3)

    if vc > v:
        print(f'Vc = {vc}N/mm^2, Shear is satisfied\n')
    else:
        print(f'Vc = {vc}N/mm^2, Shear not satisfied\n')

    print('Providing Shear reinforcement:')
    shear_reinforcement_size = shear_reinforcement_size
    shear_reinforcement_strength = shear_reinforcement_strength

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
        print(f'Panel Dimensions\n'
              f'Panel Length = {panel_length} '
              f'Panel Width = {panel_width} '
              f'Total Slab Depth = {entire_slab_depth} '
              f'Top Slab Thickness = {slab_thickness} '
              f'Top Length of Rib = {top_length_of_rib} '
              f'Bottom Length of Rib = {bottom_length_of_rib}\n'
              f'Mould Properties\n'
              f'Mould Length = {void_mould_length}'
              f'Mould Width = {void_mould_width}'
              f'Volume of Void in One Mould = {volume_of_void_in_one_mould}'
              f'Loading Conditions/n'
              f'Dead Load Constant = {dead_load_constant}'
              f'Live Load Constant = {live_load_constant}'
              f'Finishes = {finishes_value}'
              f'Live Load = {live_load}'
              f'Reinforcement Details/n'
              f'Strength of Steel = {steel_strength}'
              f'Diameter of Links = "{stirrup_diameter}'
              f'Length of Cover = {cover_length}'
              f'FCu Value = {fcu_value}'
              f'Span Reinforcement = {preferred_reinforcement_size}'
              f'Support Reinforcement = {preferred_support_reinforcement_size}')


if __name__ == "__main__":
    main(panel_length=7.2, panel_width=7.2, entire_slab_depth=0.5, slab_thickness=0.075,
         void_mould_length=0.9, void_mould_width=0.9, volume_of_void_in_one_mould=0.194,
         bottom_length_of_rib=0.130, top_length_of_rib=0.298, dead_load_constant=1.4,
         live_load_constant=1.6, negative_moment_at_continuous_edge=0.032, positive_moment_at_mid_span=0.024,
         steel_strength=410, stirrup_diameter=10, cover_length=25, fcu_value=25,
         preferred_reinforcement_size=12, preferred_support_reinforcement_size=16,
         bar_spacing=250, shear_coefficient=0.33, shear_reinforcement_size=10,
         shear_reinforcement_strength=250, finishes_value=1.2, live_load_value=5)