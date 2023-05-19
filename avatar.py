import py_avataaars as pa
avatar = pa.PyAvataaar(
    style=pa.AvatarStyle.CIRCLE,
    skin_color=pa.SkinColor.LIGHT,
    hair_color=pa.HairColor.AUBURN,
    top_type=pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
    nose_type=pa.NoseType.DEFAULT,
    accessories_type=pa.AccessoriesType.PRESCRIPTION_02,
    facial_hair_type=pa.FacialHairType.MOUSTACHE_MAGNUM,
    mouth_type=pa.MouthType.SCREAM_OPEN,
    eye_type=pa.EyesType.SQUINT,
    eyebrow_type=pa.EyebrowType.RAISED_EXCITED_NATURAL,
    clothe_type=pa.ClotheType.HOODIE,
    clothe_graphic_type=pa.ClotheGraphicType.BAT,
)
avatar.render_png_file('avatar1.png')