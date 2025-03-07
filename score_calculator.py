def calculate_health_score(physical_params, mental_params, lifestyle_params):
    # Define weightage
    physical_weight = 0.50
    mental_weight = 0.25
    lifestyle_weight = 0.25
    
    # Calculate score for physical parameters
    physical_score = calculate_physical_score(physical_params)
    
    # Calculate score for mental parameters
    mental_score = calculate_mental_score(mental_params)
    
    # Calculate score for lifestyle parameters
    lifestyle_score = calculate_lifestyle_score(lifestyle_params)
    
    # Final health score based on the weighted sum of the three categories
    total_score = (physical_score * physical_weight) + \
                  (mental_score * mental_weight) + \
                  (lifestyle_score * lifestyle_weight)
    
    # Return the total health score
    return total_score


def calculate_physical_score(params):
    score = 0
    # Systolic Pressure
    if 100 <= params['systolic'] <= 140:
        score += 8.33
    elif 90 <= params['systolic'] < 100 or 140 < params['systolic'] <= 180:
        score += 4.17  # Moderate alert, 50% score
    else:
        score += 0  # Critical alert, 0% score
    
    # Diastolic Pressure
    if 60 <= params['diastolic'] <= 90:
        score += 8.33
    elif 50 <= params['diastolic'] < 60 or 90 < params['diastolic'] <= 120:
        score += 4.17
    else:
        score += 0
    
    # Heart Rate
    if 60 <= params['heart_rate'] <= 100:
        score += 8.33
    elif 50 <= params['heart_rate'] < 60 or 110 < params['heart_rate'] <= 140:
        score += 4.17
    else:
        score += 0
    
    # Respiratory Rate
    if 12 <= params['respiratory_rate'] <= 20:
        score += 8.33
    elif 10 <= params['respiratory_rate'] < 12 or 24 < params['respiratory_rate'] <= 30:
        score += 4.17
    else:
        score += 0
    
    # Body Temperature
    if 36 <= params['temperature'] <= 37.5:
        score += 8.33
    elif 35 <= params['temperature'] < 36 or 38 < params['temperature'] <= 39.4:
        score += 4.17
    else:
        score += 0
    
    # Oxygen Saturation
    if 95 <= params['oxygen_saturation'] <= 100:
        score += 8.33
    elif 90 <= params['oxygen_saturation'] < 95:
        score += 4.17
    else:
        score += 0
    
    return score


def calculate_mental_score(params):
    score = 0
    # Cortisol Levels
    if 5 <= params['cortisol'] <= 25:
        score += 8.33
    elif 2 <= params['cortisol'] < 5 or 25 < params['cortisol'] <= 30:
        score += 4.17
    else:
        score += 0
    
    # Serotonin Levels
    if 101 <= params['serotonin'] <= 283:
        score += 8.33
    elif 50 <= params['serotonin'] < 101 or 283 < params['serotonin'] <= 350:
        score += 4.17
    else:
        score += 0
    
    # Vitamin D Levels
    if 30 <= params['vitamin_d'] <= 100:
        score += 8.33
    elif 10 <= params['vitamin_d'] < 30 or 100 < params['vitamin_d'] <= 200:
        score += 4.17
    else:
        score += 0
    
    return score


def calculate_lifestyle_score(params):
    score = 0
    # Sleep Hours
    if 7 <= params['sleep_hours'] <= 9:
        score += 8.33
    elif 4 <= params['sleep_hours'] < 7 or 9 < params['sleep_hours'] <= 12:
        score += 4.17
    else:
        score += 0
    
    # Physical Activity (Steps)
    if 7000 <= params['steps'] <= 10000:
        score += 8.33
    elif 1000 <= params['steps'] < 3000 or 15000 < params['steps'] <= 20000:
        score += 4.17
    else:
        score += 0
    
    # Screen Time
    if 2 <= params['screen_time'] <= 4:
        score += 8.33
    elif 1 <= params['screen_time'] < 2 or 6 < params['screen_time'] <= 8:
        score += 4.17
    else:
        score += 0
    
    return score
