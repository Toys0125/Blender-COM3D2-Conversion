import bpy
translateTable={
        "Arm.": {
            "L/R":True,
            "Groups":["Uppertwist_","Uppertwist1_","Bip01 * UpperArm."]
        },
        "Elbow.":{
            "L/R":True,
            "Groups":["Foretwist_","Foretwist1_","Bip01 * Forearm."]
        },
        "Spine": {
            "L/R":False,
            "Groups":["Bip01 Spine","Bip01 Spine0a"]
        },
        "Chest":{
            "L/R":False,
            "Groups":["Bip01 Spine1","Bip01 Spine1a"]
        },
        "Neck":{
            "L/R":False,
            "Groups":["Bip01 Neck"]
        },
        "Hip":{
            "L/R":False,
            "Groups":["Bip01 Pelvis"]
        },
        "Butt.":{
            "L/R":True,
            "Groups":["Hip_","Hip_*_nub."]
        },
        "Shoulder.":{
            "L/R":True,
            "Groups":["Bip01 * Clavicle.","Kata "]
        },
        "Mune_sub.":{
            "L/R":True,
            "Groups":["Mune_*_sub."]
        },
        "Toes.":{
            "L/R":True,
            "Groups":["Bip01 * Toe0.","Bip01 * Toe1.","Bip01 * Toe01.","Bip01 * Toe1.","Bip01 * Toe11.","Bip01 * Toe2.","Bip01 * Toe21."]
        },
        "Leg.":{
            "L/R":True,
            "Groups":["momoniku_","momotwist_","momotwist2_"]
        },
        "Calf.":{
            "L/R":True,
            "Groups":["Bip01 * Calf."]
        },
        "Foot.":{
            "L/R":True,
            "Groups":["Bip01 * Foot."]
        },
        "Right Wrist":{
            "L/R":False,
            "Groups":["Bip01 * Hand.R"]
        },
        "Left Wrist":{
            "L/R":False,
            "Groups":["Bip01 * Hand.L"]
        },
        "Thumb0.":{
            "L/R":True,
            "Groups":["Bip01 * Finger0."]
        }
        ,
        "Thumb1.":{
            "L/R":True,
            "Groups":["Bip01 * Finger01."]
        }
        ,
        "Thumb2.":{
            "L/R":True,
            "Groups":["Bip01 * Finger02."]
        }
        ,
        "IndexFinger0.":{
            "L/R":True,
            "Groups":["Bip01 * Finger1."]
        }
        ,
        "IndexFinger1.":{
            "L/R":True,
            "Groups":["Bip01 * Finger11."]
        }
        ,
        "IndexFinger2.":{
            "L/R":True,
            "Groups":["Bip01 * Finger12."]
        }
        ,
        "MiddleFinger0.":{
            "L/R":True,
            "Groups":["Bip01 * Finger2."]
        }
        ,
        "MiddleFinger1.":{
            "L/R":True,
            "Groups":["Bip01 * Finger21."]
        },
        "MiddleFinger2.":{
            "L/R":True,
            "Groups":["Bip01 * Finger22."]
        }
        ,
        "RingFinger0.":{
            "L/R":True,
            "Groups":["Bip01 * Finger3."]
        }
        ,
        "RingFinger1.":{
            "L/R":True,
            "Groups":["Bip01 * Finger31."]
        }
        ,
        "RingFinger2.":{
            "L/R":True,
            "Groups":["Bip01 * Finger32."]
        }
        ,
        "PinkyFinger0.":{
            "L/R":True,
            "Groups":["Bip01 * Finger4."]
        }
        ,
        "PinkyFinger1.":{
            "L/R":True,
            "Groups":["Bip01 * Finger41."]
        }
        ,
        "PinkyFinger2.":{
            "L/R":True,
            "Groups":["Bip01 * Finger42."]
        }
    }