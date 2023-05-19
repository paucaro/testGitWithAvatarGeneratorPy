import py_avataaars as pa
avatar = pa.PyAvataaar(
    style=pa.AvatarStyle.CIRCLE,
    skin_color=pa.SkinColor.LIGHT,
    hair_color=pa.HairColor.AUBURN,
    top_type=pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
    nose_type=pa.NoseType.DEFAULT,
    accessories_type=pa.AccessoriesType.PRESCRIPTION_02,
)
avatar.render_png_file('avatar1.png')