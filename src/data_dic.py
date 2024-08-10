# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:06:52 2024

@author: Administrator
"""
from const import WHITE,BLACK,BLUE,RED 

ball_data = {
    0 : {
        'NAME':'WHITE_BALL',
        'COLOR':WHITE,
        'LOCATION':(390.0354,385.6364),
        'CTRL':True
    },

    1 : {
        'NAME':'BLUE',
        'COLOR':BLUE,
        'LOCATION':(977.4488, 385.6364),
        'CTRL':False
    },
    
    2 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1009.49, 367.14),
        'CTRL':False
    },
    
    3 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1009.49, 404.14),
        'CTRL':False
    },
    
    4 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1041.53, 348.64),
        'CTRL':False
    },

    5 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1041.53, 422.64),
        'CTRL':False
    },

    6 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1073.58, 330.14),
        'CTRL':False
    },

    7 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1073.58, 367.14),
        'CTRL':False
    },

    8 : {
        'NAME':'BLACK',
        'COLOR':BLACK,
        'LOCATION':(1041.53, 385.64),
        'CTRL':False
    },

    9 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1073.58, 404.14),
        'CTRL':False
    },

    10 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1073.58, 441.14),
        'CTRL':False
    },

    11 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1105.62, 311.64),
        'CTRL':False
    },

    12 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1105.62, 348.64),
        'CTRL':False
    },

    13 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1105.62, 385.64),
        'CTRL':False
    },

    14 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1105.62, 422.64),
        'CTRL':False
    },

    15 : {
        'NAME':'RED',
        'COLOR':RED,
        'LOCATION':(1105.62, 459.64),
        'CTRL':False
    }

}

arcSide_data ={
  1: {
    'COLOR': BLACK,
     'RECT': (128.8262,
     73.0531,
     18.8978,
     18.8978),
     'START_ANGLE': 3.9269908169872414,
     'STOP_ANGLE': 4.71238898038469,
     'WIDTH': 1
  },
   2: {
    'COLOR': BLACK,
     'RECT': (1269.9695,
     123.77840000000002,
     18.8978,
     18.8978),
     'START_ANGLE': 2.356194490192345,
     'STOP_ANGLE': 3.141592653589793,
     'WIDTH': 1
  },
   3: {
    'COLOR': BLACK,
     'RECT': (78.48570000000001,
     123.1392,
     18.8978,
     18.8978),
     'START_ANGLE': 0.0,
     'STOP_ANGLE': 0.7853981633974483,
     'WIDTH': 1
  },
   4: {
    'COLOR': BLACK,
     'RECT': (1269.9695,
     628.5989000000001,
     18.8978,
     18.8978),
     'START_ANGLE': 3.141592653589793,
     'STOP_ANGLE': 3.9269908169872414,
     'WIDTH': 1
  },
   5: {
    'COLOR': BLACK,
     'RECT': (1216.0982,
     676.1886000000001,
     18.8978,
     18.8978),
     'START_ANGLE': 0.7853981633974483,
     'STOP_ANGLE': 1.5707963267948966,
     'WIDTH': 1
  },
   6: {
    'COLOR': BLACK,
     'RECT': (1219.52,
     73.0531,
     18.8978,
     18.8978),
     'START_ANGLE': 4.71238898038469,
     'STOP_ANGLE': 5.497787143782138,
     'WIDTH': 1
  },
   7: {
    'COLOR': BLACK,
     'RECT': (712.8655,
     73.0531,
     18.8978,
     18.8978),
     'START_ANGLE': 3.4208453339088853,
     'STOP_ANGLE': 4.71238898038469,
     'WIDTH': 1
  },
   8: {
    'COLOR': BLACK,
     'RECT': (632.9588,
     73.0531,
     18.8978,
     18.8978),
     'START_ANGLE': 4.71238898038469,
     'STOP_ANGLE': 6.003932626860493,
     'WIDTH': 1
  },
   9: {
    'COLOR': BLACK,
     'RECT': (712.9293,
     676.1886000000001,
     18.8978,
     18.8978),
     'START_ANGLE': 1.5707963267948966,
     'STOP_ANGLE': 2.8623399732707004,
     'WIDTH': 1
  },
   10: {
    'COLOR': BLACK,
     'RECT': (632.9736,
     676.1886000000001,
     18.8978,
     18.8978),
     'START_ANGLE': 0.2792526803190927,
     'STOP_ANGLE': 1.5707963267948966,
     'WIDTH': 1
  },
   11: {
    'COLOR': BLACK,
     'RECT': (79.48570000000001,
     624.0901,
     18.8978,
     18.8978),
     'START_ANGLE': 5.497787143782138,
     'STOP_ANGLE': 6.283185307179586,
     'WIDTH': 1
  },
   12: {
    'COLOR': BLACK,
     'RECT': (127.07020000000001,
     676.1886000000001,
     18.8978,
     18.8978),
     'START_ANGLE': 1.5707963267948966,
     'STOP_ANGLE': 2.356194490192345,
     'WIDTH': 1
  },
   13: {
    'COLOR': BLACK,
     'RECT': (1253.8735000000001,
     664.9123,
     81.5368,
     81.5368),
     'START_ANGLE': 4.71238898038469,
     'STOP_ANGLE': 6.283185307179586,
     'WIDTH': 1
  },
   14: {
    'COLOR': BLACK,
     'RECT': (1253.8735000000001,
     21.5509,
     81.5368,
     81.5368),
     'START_ANGLE': 0.0,
     'STOP_ANGLE': 1.5707963267948966,
     'WIDTH': 1
  },
   15: {
    'COLOR': BLACK,
     'RECT': (30.589699999999993,
     21.5509,
     81.5368,
     81.5368),
     'START_ANGLE': 1.5707963267948966,
     'STOP_ANGLE': 3.141592653589793,
     'WIDTH': 1
  },
   16: {
    'COLOR': BLACK,
     'RECT': (30.589699999999993,
     664.9123,
     81.5368,
     81.5368),
     'START_ANGLE': 3.141592653589793,
     'STOP_ANGLE': 4.71238898038469,
     'WIDTH': 1
  }
}

lineSide_data = {
  1: {
     'COLOR': BLACK,
     'START_POINT': (710.7609,76.3125),
     'STOP_POINT': (713.2177,85.0576),
     'WIDTH': 1
  },
   2: {
     'COLOR': BLACK,
     'START_POINT': (653.9612,76.3125),
     'STOP_POINT': (651.5044,85.0576),
     'WIDTH': 1
  },
   3: {
     'COLOR': BLACK,
     'START_POINT': (713.2732,683.1117),
     'STOP_POINT': (710.8002,692.0267),
     'WIDTH': 1
  },
   4: {
     'COLOR': BLACK,
     'START_POINT': (651.5276,683.1117),
     'STOP_POINT': (654.0006,692.0267),
     'WIDTH': 1
  },
   5: {
     'COLOR': BLACK,
     'START_POINT': (1272.737,644.7291),
     'STOP_POINT': (1280.9862,652.9783),
     'WIDTH': 1
  },
   6: {
     'COLOR': BLACK,
     'START_POINT': (84.0587,115.3495),
     'STOP_POINT': (94.616,125.9067),
     'WIDTH': 1
  },
   7: {
     'COLOR': BLACK,
     'START_POINT': (1235.6503,89.1834),
     'STOP_POINT': (1246.3347,78.4989),
     'WIDTH': 1
  },
   8: {
     'COLOR': BLACK,
     'START_POINT': (120.9093,78.4989),
     'STOP_POINT': (131.5937,89.1834),
     'WIDTH': 1
  },
   9: {
     'COLOR': BLACK,
     'START_POINT': (1272.737,126.5459),
     'STOP_POINT': (1283.5036,115.7793),
     'WIDTH': 1
  },
   10: {
     'COLOR': BLACK,
     'START_POINT': (118.5354,690.2585),
     'STOP_POINT': (129.8378,678.9561),
     'WIDTH': 1
  },
   11: {
     'COLOR': BLACK,
     'START_POINT': (1232.2285,678.9561),
     'STOP_POINT': (1243.5309,690.2585),
     'WIDTH': 1
  },
   12: {
     'COLOR': BLACK,
     'START_POINT': (80.8563,652.98),
     'STOP_POINT': (94.6159,639.2204),
     'WIDTH': 1
  },
   13: {
     'COLOR': BLACK,
     'START_POINT': (97.3835,632.539),
     'STOP_POINT': (97.3835,132.5881),
     'WIDTH': 1
  },
   14: {
     'COLOR': BLACK,
     'START_POINT': (722.3782,676.1886),
     'STOP_POINT': (1225.5471,676.1886),
     'WIDTH': 1
  },
   15: {
     'COLOR': BLACK,
     'START_POINT': (138.2751,91.9509),
     'STOP_POINT': (642.4077,91.9509),
     'WIDTH': 1
  },
   16: {
     'COLOR': BLACK,
     'START_POINT': (1269.9695,638.0478),
     'STOP_POINT': (1269.9695,133.2273),
     'WIDTH': 1
  },
   17: {
     'COLOR': BLACK,
     'START_POINT': (136.5191,676.1886),
     'STOP_POINT': (642.4225,676.1886),
     'WIDTH': 1
  },
   18: {
     'COLOR': BLACK,
     'START_POINT': (722.3144,91.9509),
     'STOP_POINT': (1228.9689,91.9509),
     'WIDTH': 1
  },
   19: {
     'COLOR': WHITE,
     'START_POINT': (390.0354,91.9509),
     'STOP_POINT': (390.0354,676.1886),
     'WIDTH': 1
  },
   20: {
     'COLOR': BLACK,
     'START_POINT': (1335.4103,62.3193),
     'STOP_POINT': (1335.4103,705.6807),
     'WIDTH': 1
  },
   21: {
     'COLOR': BLACK,
     'START_POINT': (30.5897,705.6807),
     'STOP_POINT': (30.5897,62.3193),
     'WIDTH': 1
  },
   22: {
     'COLOR': BLACK,
     'START_POINT': (71.3581,21.5509),
     'STOP_POINT': (1294.6419,21.5509),
     'WIDTH': 1
  }, 
   23: {
    'COLOR': BLACK, 
    'START_POINT': (1294.6419, 746.4491), 
    'STOP_POINT': (71.3581, 746.4491), 
    'WIDTH': 1
  }
}