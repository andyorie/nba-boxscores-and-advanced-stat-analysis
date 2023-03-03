# nba_adv_stat module for calculating several additional stats.
# https://bleacherreport.com/articles/1039116-understanding-the-nba-explaining-advanced-offensive-stats-and-metrics

def asst_perct(asst, mins, tot_tm_mins, tm_fg, fg_ply):
    ''' Assist Percentage (AST%): estimates the % of made shots by teammates that were assisted 
    by a player while he was on the court. 
    '''

    if mins != 0 and asst != 0:
        return (asst/ ((mins/ (tot_tm_mins/5)) * (tm_fg - fg_ply))) * 100
    else:
        return 0

def turnover_perct(turnover_ply, fga, fta):
    ''' Turnover Percentage (TOV%): Calculates the # of turnovers a player will make in 100 
    individual plays.
    '''

    if turnover_ply != 0:
        return (turnover_ply / (fga + (0.44 * fta) + turnover_ply)) * 100
    else:
        return 0

def off_rebs_pct(oreb_ply, tot_tm_mins, mins_ply, oreb_tm, oreb_opp):
    ''' Offensive Rebound Percentage (ORB%): Calculates the % of available offenside rebounds that a 
    player grabs while he's on the court.
    '''

    if oreb_ply != 0 and mins_ply != 0:
        return ((oreb_ply * (tot_tm_mins/ 5))/ (mins_ply * (oreb_tm + oreb_opp))*100)
    elif mins_ply == 0 or oreb_ply == 0:
        return 0
    else:
        return 0

def eff_fg_pct(fg_ply, fg_3m_ply, fga):
    ''' Effective FG % (eFG%): Calculates a player's shooting ability by considering 2 and 3
    pointer made.
    '''

    if fg_ply !=0 and fg_3m_ply !=0:
        return (fg_ply + (0.5* fg_3m_ply) / fga) * 100
    else:
        return 0

def true_sht_pct(pts, fga, fta):
    ''' True Shooting Percentage(TS%): Calcuates the scoring efficiency of a player.
    Stat also calledAdjusted Shooting %, Effective shooting %, Effective %, Points per shot attempted,
    Scoring Effeciency.
    '''

    if pts != 0:
        return (pts / (2 * (fga + (0.44*fta))) * 100)
    else:
        return 0

def usage_rate(fga, fta, turnover_ply, tot_tm_mins, mins, tm_fg, tm_ft, tm_to):
    ''' Usage Rate(USG%): Calculates the % of team plays a player was involved in, while he was on the
    floor, provided the play ends in either a FGA, FTA, or TO. e.g. = Kobe Bryant's USG% of 38.8 
    is the highest of his career and is leading the league 
    in the category for the second straight year. How I interpret that sentence: 
    Kobe Bryant needs to pass more. 
    '''

    if mins != 0:
        return ((((fga+(0.44*fta)+turnover_ply) * (tot_tm_mins/5)) / (mins * (tm_fg + tm_to + (0.44*tm_ft)))) * 100)
    else:
        return 0


def pts_per_poss(pts, fga, fta, turnover_ply):
    ''' PPP%: This stat in its simplest form explains how efficiently a player uses his 
    time with the ball to score.
    '''
    if pts != 0:
        return ((pts/ (fga + turnover_ply + (0.44*fta))) * 100)
    else:
        return 0


def off_rating(pp, fga, fta, turnover_ply):
    ''' Offensive Rating (ORtg): Offensive rating is just the amount of points produced 
    by a player per 100 possessions. It's another tempo-free stat. 
    Offensive rating eliminates factors like pace of play and minutes played per game.
    '''

    if pp != 0:
        return ((pp / (fga + turnover_ply + (0.44 * fta))) * 100)
    else:
        return 0


