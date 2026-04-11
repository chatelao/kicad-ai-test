import os

files = [
    '/home/jules/.pyenv/versions/3.12.13/lib/python3.12/site-packages/skidl/tools/kicad9/lib.py',
    '/home/jules/.pyenv/versions/3.12.13/lib/python3.12/site-packages/skidl/tools/kicad8/lib.py',
    '/home/jules/.pyenv/versions/3.12.13/lib/python3.12/site-packages/skidl/tools/kicad7/lib.py',
    '/home/jules/.pyenv/versions/3.12.13/lib/python3.12/site-packages/skidl/tools/kicad6/lib.py'
]

for filepath in files:
    if not os.path.exists(filepath):
        continue

    kicad_version = "9"
    if "kicad8" in filepath: kicad_version = "8"
    elif "kicad7" in filepath: kicad_version = "7"
    elif "kicad6" in filepath: kicad_version = "6"

    content = f"""
import os
from collections import defaultdict, OrderedDict
from simp_sexp import Sexp

from skidl.logger import active_logger
from skidl.part import LIBRARY
from skidl.pin import pin_types
from skidl.geometry import mils_per_mm, BBox
from skidl.utilities import (
    export_to_all,
    find_and_open_file,
    get_abs_filename,
    num_to_chars,
    to_list,
    add_unique_attr,
)

lib_suffix = [".kicad_sym"]

@export_to_all
def default_lib_paths():
    return [".", os.environ.get("KICAD{kicad_version}_SYMBOL_DIR", "/usr/share/kicad/symbols")]

@export_to_all
def get_fp_lib_tbl_dir():
    return os.path.expanduser("~/.config/kicad/{kicad_version}.0")

@export_to_all
def load_sch_lib(lib, filename=None, lib_search_paths_=None, lib_section=None):
    import sys
    from skidl.part import Part
    from skidl.skidl import get_default_tool
    from skidl.tools import lib_suffixes

    dflt_tool = get_default_tool()
    suffixes = lib_suffixes[dflt_tool]
    base, suffix = os.path.splitext(filename)
    if suffix:
        suffixes = [suffix]
    for suffix in suffixes:
        f, _ = find_and_open_file(
            filename, lib_search_paths_, suffix, allow_failure=True
        )
        if f:
            break
    if not f:
        raise FileNotFoundError(
            f"Unable to open KiCad Schematic Library File {{filename}}"
        )

    lib_txt = f.read()
    try:
        lib_txt = lib_txt.decode("latin_1")
    except AttributeError:
        pass

    try:
        lib_sexp = Sexp(lib_txt)
    except:
        active_logger.raise_(
            RuntimeError,
            f"The file {{filename}} is not a KiCad Schematic Library File.",
        )

    symbols = OrderedDict(
        [
            (symbol[1], symbol)
            for symbol in lib_sexp.search("/kicad_symbol_lib/symbol", ignore_case=True)
        ]
    )

    for symbol_name, symbol in symbols.items():
        properties = {{}}
        extends = symbol.search("/symbol/extends", ignore_case=True)
        if extends:
            parent_name = extends[0][1]
            parent = symbols[parent_name]
            parent_properties = parent.search("/symbol/property", ignore_case=True)
            properties = {{p[1].lower(): p[2] for p in parent_properties}}
        current_properties = symbol.search("/symbol/property", ignore_case=True)
        properties.update({{p[1].lower(): p[2] for p in current_properties}})

        keywords = properties.get("ki_keywords", "")
        datasheet = properties.get("datasheet", "")
        description = properties.get("description", "")
        search_text = "\\n".join([filename, symbol_name, description, keywords])

        lib.add_parts(
            Part(
                part_defn=symbol,
                tool=dflt_tool,
                dest=LIBRARY,
                filename=filename,
                name=symbol_name,
                aliases=list(),
                keywords=keywords,
                datasheet=datasheet,
                description=description,
                search_text=search_text,
            )
        )

@export_to_all
def parse_lib_part(part, partial_parse):
    import sys
    from skidl.part import TEMPLATE
    from skidl.pin import Pin

    if not part.part_defn:
        return
    if partial_parse:
        return

    part_defn = part.part_defn
    from skidl.alias import Alias
    part.aliases = Alias()
    part.fplist = []
    part.draw_cmds = defaultdict(list)

    extends = part_defn.search("/symbol/extends", ignore_case=True)
    if extends:
        parent_name = extends[0][1]
        parent_part = part.lib[parent_name].copy(dest=TEMPLATE)
        parent_part_dict = vars(parent_part)
        for property_key in (
            "part_defn", "_name", "_aliases", "description", "datasheet", "keywords", "search_text",
        ):
            try:
                del parent_part_dict[property_key]
            except KeyError:
                pass
        vars(part).update(parent_part_dict)
        part.associate_pins()
        part.copy_units(parent_part)

        for item in part_defn:
            cmd = item[0].lower()
            if cmd == "del":
                part.rmv_pins(item[1])
            elif cmd == "swap":
                part.swap_pins(item[1], item[2])
            elif cmd == "renum":
                part.renumber_pin(item[1], item[2])
            elif cmd == "rename":
                part.rename_pin(item[1], item[2])
            elif cmd == "property_del":
                del part.fields[item[1]]

    def parse_pins(symbol, unit):
        pin_io_type_translation = {{
            "input": pin_types.INPUT, "output": pin_types.OUTPUT, "bidirectional": pin_types.BIDIR,
            "tri_state": pin_types.TRISTATE, "passive": pin_types.PASSIVE, "free": pin_types.FREE,
            "unspecified": pin_types.UNSPEC, "power_in": pin_types.PWRIN, "power_out": pin_types.PWROUT,
            "open_collector": pin_types.OPENCOLL, "open_emitter": pin_types.OPENEMIT, "no_connect": pin_types.NOCONNECT,
        }}
        symbol_pins = symbol.search("/symbol/pin", ignore_case=True)
        for pin in symbol_pins:
            pin_func = pin_io_type_translation[pin[1].lower()]
            pin_name = pin.search("/pin/name", ignore_case=True)
            pin_name = pin_name[0][1] if pin_name else ""
            pin_number = pin.search("/pin/number", ignore_case=True)
            pin_number = pin_number[0][1] if pin_number else None
            pin_length = pin.search("/pin/length", ignore_case=True)
            pin_length = pin_length[0][1] if pin_length else 1000
            at = pin.search("/pin/at", ignore_case=True)
            if at:
                pin_x, pin_y = at[0][1:3]
                pin_angle = at[0][3] if len(at[0]) > 3 else 0
                pin_orientation = {{0: "R", 90: "U", 180: "L", 270: "D"}}.get(pin_angle, "R")
            else:
                pin_x, pin_y, pin_angle, pin_orientation = 0, 0, 0, "R"
            alternate_names = pin.search("/pin/alternate", ignore_case=True)
            aliases = [a[1] for a in alternate_names] if alternate_names else []
            p = Pin(
                name=pin_name, num=pin_number, func=pin_func, unit=unit, x=pin_x, y=pin_y,
                length=pin_length, rotation=pin_angle, orientation=pin_orientation,
            )
            p.aliases += aliases
            part.add_pins(p)
        return bool(symbol_pins)

    def parse_draw_cmds(symbol):
        return [item for item in symbol if item[0].lower() in ("arc", "bezier", "circle", "pin", "polyline", "rectangle", "text")]

    top_has_pins = parse_pins(part_defn, unit=1)
    units = {{unit[1]: unit for unit in part_defn.search("/symbol/symbol", ignore_case=True)}}
    if top_has_pins:
        part.make_unit("uA", unit=1)
    part.draw_cmds[1].extend(parse_draw_cmds(part.part_defn))
    unit_nums = []
    for unit_name, unit_data in units.items():
        major, minor = [int(n) for n in unit_name.split("_")[-2:]]
        if major != 0 and minor > 1:
            continue
        part.draw_cmds[major].extend(parse_draw_cmds(unit_data))
        unit_has_pins = parse_pins(unit_data, unit=major)
        if major == 0 and unit_has_pins:
            unit_nums.append(major)
        elif major != 0:
            unit_nums.append(major)
    if unit_nums:
        for unit_major, unit_draw_cmds in part.draw_cmds.items():
            if unit_major != 0:
                unit_draw_cmds.extend(part.draw_cmds.get(0, []))
    part._ref = None
    part.associate_pins()
    if 0 in unit_nums:
        if len(unit_nums) == 1:
            unit_nums = [1]
        else:
            unit_nums.remove(0)
    for unit_num in unit_nums:
        unit_label = "u" + num_to_chars(unit_num)
        u = part.make_unit(unit_label, unit=unit_num)
    if len(part.unit) == 1:
        unit_label = list(part.unit.keys())[0]
        part.rmv_unit(unit_label)
        part.unit[unit_label] = part
        part.num = 1
        add_unique_attr(part, unit_label, part)
    props = {{"reference": ("", "", ""), "value": ("", "", ""), "footprint": ("", "", ""), "datasheet": ("", "", "")}}
    props.update({{prop[1].lower(): prop for prop in part_defn.search("/symbol/property", ignore_case=True)}})
    part.ref_prefix = props["reference"][2]
    part.value = props["value"][2]
    part.fplist.append(props["footprint"][2])
    part.datasheet = props["datasheet"][2]
    part.draw_cmds[1].extend([props["reference"], props["value"]])
    already_defined = vars(part).keys()
    part_dict = {{k.replace(" ", "_").replace("/", "_"): v[2] for k, v in props.items() if k not in already_defined}}
    for k, v in part_dict.items():
        setattr(part, k, v)
    part.part_defn = None
"""
    with open(filepath, 'w') as f:
        f.write(content)
