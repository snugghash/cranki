computeIntervals :: (timeLeft, sessions) -> [intervals]
computeIntervals timeLeft sessions = 
    intervals = [timeLeft*(1-1/x) | x <- 1..sessions]
