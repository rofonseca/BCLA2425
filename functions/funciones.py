import pandas as pd

def shooting(local_path, visit_path):
    df = pd.read_csv(local_path)
    FG = df['2PA'].sum()+df['3PA'].sum()
    P3 = df['3PA'].sum()
    FGA = df['2P'].sum()+df['3P'].sum()
    offense = (FG+0.5*P3)/FGA
    df = pd.read_csv(visit_path)
    FG = df['2PA'].sum()+df['3PA'].sum()
    P3 = df['3PA'].sum()
    FGA = df['2P'].sum()+df['3P'].sum()
    defense = (FG+0.5*P3)/FGA
    return offense, defense

def turnover(local_path, visit_path):
    df = pd.read_csv(local_path)
    TOV = df['TOV'].sum()
    FTA = df['FT'].sum()
    FGA = df['2P'].sum()+df['3P'].sum()
    offense = TOV/(FGA+0.44*FTA+TOV)
    df = pd.read_csv(visit_path)
    TOV = df['TOV'].sum()
    FTA = df['FT'].sum()
    FGA = df['2P'].sum()+df['3P'].sum()
    defense = TOV/(FGA+0.44*FTA+TOV)
    return offense, defense

def rebounding(local_path, visit_path):
    df = pd.read_csv(local_path)
    df_op = pd.read_csv(visit_path)
    ORB = df['ORB'].sum()
    DRB = df['DRB'].sum()
    ORB_op = df_op['ORB'].sum()
    DRB_op = df_op['DRB'].sum()
    offense = ORB/(ORB+DRB_op)
    defense = DRB/(ORB_op+DRB)
    return offense, defense

def free_throws(local_path, visit_path):
    df = pd.read_csv(local_path)
    FT = df['FTA'].sum()
    FGA = df['FT'].sum()
    offense = FT/FGA
    df = pd.read_csv(visit_path)
    FT = df['FTA'].sum()
    FGA = df['FT'].sum()
    defense = FT/FGA
    return offense, defense

def four_factors(local_path, visit_path):
    df = pd.read_csv(local_path)
    df_op = pd.read_csv(visit_path)
    FG = df['2PA'].sum()+df['3PA'].sum()
    P3 = df['3PA'].sum()
    FGA = df['2P'].sum()+df['3P'].sum()
    TOV = df['TOV'].sum()
    FTA = df['FT'].sum()
    ORB = df['ORB'].sum()
    DRB = df['DRB'].sum()
    FT = df['FTA'].sum()

    FG_op = df_op['2PA'].sum()+df_op['3PA'].sum()
    P3_op = df_op['3PA'].sum()
    FGA_op = df_op['2P'].sum()+df_op['3P'].sum()
    TOV_op = df_op['TOV'].sum()
    FTA_op = df_op['FT'].sum()
    ORB_op = df_op['ORB'].sum()
    DRB_op = df_op['DRB'].sum()
    FT_op = df_op['FTA'].sum()

    shoot_offense = (FG + 0.5*P3)/FGA
    shoot_defense = (FG_op + 0.5*P3_op)/FGA_op
    turn_offense = TOV/(FGA+0.44*FTA+TOV)
    turn_defense = TOV_op/(FGA_op+0.44*FTA_op+TOV_op)
    rb_offense = ORB/(ORB+DRB_op)
    rb_defense = DRB/(ORB_op+DRB)
    free_offense = FT/FGA
    free_defense = FT_op/FGA_op

    return shoot_offense, shoot_defense, turn_offense, turn_defense, rb_offense, rb_defense, free_offense, free_defense

def show_four_factors(local_path, visit_path):
    [shoot_offense, shoot_defense, turn_offense, turn_defense, rb_offense, rb_defense, free_offense, free_defense] = four_factors(local_path, visit_path)

    print('shooting offensive: ', shoot_offense)
    print('shooting defensive: ', shoot_defense)
    print('turnover offensive: ', turn_offense)
    print('turnover defensive: ', turn_defense)
    print('rebounding offensive: ', rb_offense)
    print('rebounding defensive: ', rb_defense)
    print('Free throws offensive: ', free_offense)
    print('Free throws defense: ', free_defense)

def show_four_factor_tabla(array):
    data = {
    "shooting": [array[0], array[1]],
    "turnover": [array[2], array[3]],
    "rebounding": [array[4], array[5]],
    "Free throws": [array[6], array[7]]
    }
    # Crear un DataFrame de pandas con las filas 'offensive' y 'defensive'
    df = pd.DataFrame(data, index=["offensive", "defensive"])
    # Mostrar la tabla
    print(df)