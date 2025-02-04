def tournamentWinner(competitions, results):
    points = {}

    for i in range(len(competitions)):
        homeTeam = competitions[i][0]
        awayTeam = competitions[i][1]
        
        # Check for home team victory
        if results[i] == 1:
            points[homeTeam] = points.get(homeTeam, 0) + 1
        else:
            points[awayTeam] = points.get(awayTeam, 0) + 1
    return f'{max(points, key=points.get)}'
