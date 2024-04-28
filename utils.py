import pandas as pd


def get_files_from_split(split):
    """ "
    Get filenames for real and fake samples

    Parameters
    ----------
    split : pandas.DataFrame
        DataFrame containing filenames
    """
    real_actors_videos = [
        "01__hugging_happy", "01__kitchen_pan", "01__kitchen_still", "01__outside_talking_pan_laughing",
        "01__outside_talking_still_laughing", "01__walking_outside_cafe_disgusted", "02__exit_phone_room",
        "02__meeting_serious", "02__talking_against_wall", "02__walking_and_outside_surprised",
        "02__walking_down_indoor_hall_disgust", "02__walking_down_street_outside_angry", "03__exit_phone_room",
        "03__hugging_happy", "03__outside_talking_pan_laughing", "03__outside_talking_still_laughing",
        "03__podium_speech_happy", "03__walk_down_hall_angry", "03__walking_and_outside_surprised",
        "03__walking_outside_cafe_disgusted", "04__podium_speech_happy", "04__walk_down_hall_angry",
        "04__walking_down_street_outside_angry", "05__exit_phone_room", "05__kitchen_still",
        "05__outside_talking_pan_laughing", "05__outside_talking_still_laughing", "05__podium_speech_happy",
        "05__walking_down_street_outside_angry", "06__exit_phone_room"
    ]
    real_youtube_videos = [
        "008", "033", "035", "036", "044", "046", "054", "055", "062", "066",
        "071", "096", "097", "101", "107", "109", "112", "128", "134", "147",
        "150", "153", "159", "168", "175", "183", "189", "192", "200", "206"
    ]
    fake_actors_videos = [
        "01_11__talking_against_wall__9229VVZ3",
        "01_27__outside_talking_still_laughing__ZYCZ30C0",
        "02_06__walking_down_indoor_hall_disgust__U6MDWIHG",
        "02_15__talking_against_wall__HTG660F8",
        "03_11__talking_against_wall__P08VGHTA",
        "03_18__walking_outside_cafe_disgusted__22UBC0BS",
        "03_21__exit_phone_room__YCSEBZO4",
        "04_06__kitchen_still__ZK95PQDE",
        "04_07__exit_phone_room__ITC0C48B",
        "04_13__podium_speech_happy__00T3UYOR",
        "05_16__exit_phone_room__B62WCGUN",
        "05_28__exit_phone_room__U9LRLJ6N",
        "06_04__outside_talking_still_laughing__ZK95PQDE",
        "06_04__walking_outside_cafe_disgusted__ZK95PQDE",
        "07_03__outside_talking_pan_laughing__IFSURI9X",
        "07_03__walking_outside_cafe_disgusted__F0YYEA5W",
        "07_14__talking_against_wall__P9QFO50U",
        "07_20__outside_talking_pan_laughing__KV6Q7D6C",
        "08_28__outside_talking_pan_laughing__8BC35RFU",
        "09_03__kitchen_pan__8DTEGQ54",
        "09_13__kitchen_pan__21H6XSPE",
        "09_14__talking_angry_couch__6TEK3ZX0",
        "10_22__kitchen_pan__EHARPYBT",
        "11_18__walking_outside_cafe_disgusted__R1NMCHKG",
        "12_15__talking_angry_couch__N0SRODQD",
        "12_18__outside_talking_pan_laughing__IKH1LBBY",
        "13_03__exit_phone_room__GBYWJW06",
        "14_03__exit_phone_room__KJ221YN0",
        "14_13__walk_down_hall_angry__KMQ3AW6A",
        "14_21__podium_speech_happy__IRKML4J0",
        "15_02__talking_against_wall__MZWH8ATN"
    ]
    fake_youtube_videos =  [ "033_097", "035_036", "036_035", "044_945", "055_147", "097_033", "134_192", "147_055", "159_175", "175_159" ]

    return real_actors_videos, real_youtube_videos, fake_actors_videos, fake_youtube_videos

