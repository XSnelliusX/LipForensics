import pandas as pd


def get_files_from_dataset(dataset):
    """ "
    Get filenames for real and fake samples

    Parameters
    ----------
    split : string
        String containing the Dataset Name
    """
    if dataset == "VASA":
        # Using some Real videos from FF++ so the AUC can be calculated
        real_videos = ["01__hugging_happy", "01__kitchen_pan", "01__kitchen_still",
            "01__outside_talking_pan_laughing", "01__outside_talking_still_laughing", 
            "008", "033", "035", "036", "044", "046", "054", "055", "062", "066"
        ]
        fake_videos = [
            "10", "11", "12", "13", "15", "17", "3", "5", "7", "9", "l3", "l4", "l5", "l7", "l8"
        ]
    elif dataset == "DFDC":
        real_videos == []
        fake_videos == []
    elif dataset == "CelebDF":
        real_videos == [
            "00000", "00001", "00002", "00003", "00004", "00005",
            "00006", "00007", "00008", "00009", "00010", "00011",
            "00012", "00013", "00014", "00015", "00016", "00017",
            "00018", "00019", "00020", "00021", "00022", "00023",
            "00024", "00025", "00026", "00027", "00028", "00029"
        ]
        fake_videos == [
            "id0_id16_0000", "id0_id16_0001", "id0_id16_0002", "id0_id16_0003", "id0_id16_0004",
            "id0_id16_0005", "id0_id16_0006", "id0_id16_0007", "id0_id16_0008", "id0_id16_0009",
            "id0_id17_0000", "id0_id17_0001", "id0_id17_0002", "id0_id17_0003", "id0_id17_0005",
            "id0_id17_0006", "id0_id17_0007", "id0_id17_0009", "id0_id1_0000", "id0_id1_0001",
            "id0_id1_0002", "id0_id1_0003", "id0_id1_0005", "id0_id1_0006", "id0_id1_0007",
            "id0_id1_0009", "id0_id20_0000", "id0_id20_0001", "id0_id20_0002", "id0_id20_0003"
        ]
    elif dataset == "FakeAVCeleb":
        real_videos == []
        fake_videos == []
    else:
        real_videos = [
            "01__hugging_happy", "01__kitchen_pan", "01__kitchen_still",
            "01__outside_talking_pan_laughing", "01__outside_talking_still_laughing",
            "01__walking_outside_cafe_disgusted", "02__exit_phone_room", "02__meeting_serious",
            "02__talking_against_wall", "02__walking_and_outside_surprised",
            "02__walking_down_indoor_hall_disgust", "02__walking_down_street_outside_angry",
            "03__exit_phone_room", "03__hugging_happy", "03__outside_talking_pan_laughing",
            "03__outside_talking_still_laughing", "03__podium_speech_happy",
            "03__walk_down_hall_angry", "03__walking_and_outside_surprised",
            "03__walking_outside_cafe_disgusted", "04__podium_speech_happy",
            "04__walk_down_hall_angry", "04__walking_down_street_outside_angry",
            "05__exit_phone_room", "05__kitchen_still", "05__outside_talking_pan_laughing",
            "05__outside_talking_still_laughing", "05__podium_speech_happy",
            "05__walking_down_street_outside_angry", "06__exit_phone_room", "06__hugging_happy",
            "06__kitchen_pan", "06__outside_talking_pan_laughing",
            "06__outside_talking_still_laughing", "06__talking_angry_couch",
            "06__walking_and_outside_surprised", "06__walking_down_indoor_hall_disgust",
            "06__walking_outside_cafe_disgusted", "07__hugging_happy", "07__kitchen_pan",
            "07__outside_talking_still_laughing", "07__secret_conversation",
            "07__talking_against_wall", "07__talking_angry_couch", "07__walking_down_street_outside_angry",
            "07__walking_outside_cafe_disgusted", "08__exit_phone_room", "08__outside_talking_pan_laughing",
            "08__podium_speech_happy", "08__talking_against_wall", "08__walk_down_hall_angry",
            "09__talking_angry_couch", "09__walk_down_hall_angry", "09__walking_down_street_outside_angry",
            "10__exit_phone_room", "10__podium_speech_happy", "10__talking_against_wall",
            "10__walk_down_hall_angry", "10__walking_down_street_outside_angry", "10__walking_outside_cafe_disgusted",
            "11__exit_phone_room", "11__kitchen_pan", "11__talking_against_wall", "11__talking_angry_couch",
            "11__walk_down_hall_angry", "12__exit_phone_room", "12__kitchen_pan",
            "12__outside_talking_pan_laughing", "12__podium_speech_happy", "12__talking_angry_couch",
            "12__walking_outside_cafe_disgusted", "13__outside_talking_pan_laughing", "13__podium_speech_happy",
            "13__talking_against_wall", "13__talking_angry_couch", "13__walk_down_hall_angry",
            "13__walking_down_indoor_hall_disgust", "14__kitchen_pan", "14__kitchen_still",
            "14__outside_talking_pan_laughing", "14__walk_down_hall_angry", "14__walking_down_indoor_hall_disgust",
            "14__walking_down_street_outside_angry", "14__walking_outside_cafe_disgusted",
            "15__exit_phone_room", "15__kitchen_still", "15__talking_angry_couch",
            "15__walking_and_outside_surprised", "15__walking_outside_cafe_disgusted",
            "16__outside_talking_pan_laughing",
            "008", "033", "035", "036", "044", "046", "054", "055", "062", "066",
            "071", "096", "097", "101", "107", "109", "112", "128", "134", "147",
            "150", "153", "159", "168", "175", "183", "189", "192", "200", "206",
            "210", "221", "222", "228", "241", "251", "252", "253", "254", "257",
            "261", "263", "266", "272", "284", "288", "289", "321", "324", "337",
            "339", "356", "360", "375", "376", "381", "392", "396", "399", "420",
            "434", "435", "437", "438", "439", "441", "456", "468", "469", "470",
            "479", "481", "488", "520", "522", "529", "542", "554", "556", "565",
            "572", "585", "588", "589", "599", "607", "611", "623", "630", "633"
        ]
        fake_videos = [
            "01_11__talking_against_wall__9229VVZ3", "01_27__outside_talking_still_laughing__ZYCZ30C0",
            "02_06__walking_down_indoor_hall_disgust__U6MDWIHG", "02_15__talking_against_wall__HTG660F8",
            "03_11__talking_against_wall__P08VGHTA", "03_18__walking_outside_cafe_disgusted__22UBC0BS",
            "03_21__exit_phone_room__YCSEBZO4", "04_06__kitchen_still__ZK95PQDE",
            "04_07__exit_phone_room__ITC0C48B", "04_13__podium_speech_happy__00T3UYOR",
            "05_16__exit_phone_room__B62WCGUN", "05_28__exit_phone_room__U9LRLJ6N",
            "06_04__outside_talking_still_laughing__ZK95PQDE", "06_04__walking_outside_cafe_disgusted__ZK95PQDE",
            "07_03__outside_talking_pan_laughing__IFSURI9X", "07_03__walking_outside_cafe_disgusted__F0YYEA5W",
            "07_14__talking_against_wall__P9QFO50U", "07_20__outside_talking_pan_laughing__KV6Q7D6C",
            "08_28__outside_talking_pan_laughing__8BC35RFU", "09_03__kitchen_pan__8DTEGQ54",
            "09_13__kitchen_pan__21H6XSPE", "09_14__talking_angry_couch__6TEK3ZX0",
            "10_22__kitchen_pan__EHARPYBT", "11_18__walking_outside_cafe_disgusted__R1NMCHKG",
            "12_15__talking_angry_couch__N0SRODQD", "12_18__outside_talking_pan_laughing__IKH1LBBY",
            "13_03__exit_phone_room__GBYWJW06", "14_03__exit_phone_room__KJ221YN0",
            "14_13__walk_down_hall_angry__KMQ3AW6A", "14_21__podium_speech_happy__IRKML4J0",
            "033_097", "035_036", "036_035", "044_945", "055_147",
            "097_033", "134_192", "147_055", "159_175", "175_159",
            "183_253", "192_134", "210_241", "241_210", "252_266",
            "253_183", "263_284", "266_252", "272_396", "284_263",
            "339_392", "392_339", "396_272", "469_481", "481_469",
            "585_599", "599_585", "644_657", "648_654", "654_648"
        ]

    return real_videos, fake_videos

