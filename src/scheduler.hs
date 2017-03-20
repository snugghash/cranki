computeIntervals :: Float -> Float -> [Float]
computeIntervals timeLeft sessions = [timeLeft*(1-1/x) | x <- [1..sessions]]
