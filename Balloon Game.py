import cv2
import random
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as draw

# Camera setup
cap = cv2.VideoCapture(0)
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Game variables
score = 0
balloons = [] # This will store the falling balloons
missed = 0    # Keep track of balloons that fall past the screen

while True:
    ok, frame = cap.read()
    if not ok: 
        break
    
    # Flip frame like a mirror
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # 1. Randomly generate a new balloon (1 in 20 chance per frame)
    if random.randint(1, 20) == 1:
        radius = random.randint(30, 50)
        balloons.append({
            'x': random.randint(radius, w - radius),
            'y': -radius, # Start slightly above the screen
            'color': (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
            'speed': random.randint(5, 12),
            'radius': radius
        })

    # 2. Process hand tracking
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    ix, iy = -1, -1 # Default finger coordinates

    if res.multi_hand_landmarks:
        hand = res.multi_hand_landmarks[0]
        # Draw the hand skeleton (Optional, you can remove this to make it look like magic)
        draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        
        # Get Index Finger Tip coordinates (Landmark 8)
        ix = int(hand.landmark[8].x * w)
        iy = int(hand.landmark[8].y * h)
        
        # Draw a "Magic Pointer" on the index finger
        cv2.circle(frame, (ix, iy), 12, (255, 255, 255), -1)
        cv2.circle(frame, (ix, iy), 15, (0, 0, 255), 2)

    # 3. Update and draw balloons
    for b in balloons[:]: # Iterate over a copy of the list
        # Move balloon down
        b['y'] += b['speed']
        
        # Draw the balloon
        cv2.circle(frame, (b['x'], b['y']), b['radius'], b['color'], -1)
        # Draw a small string/tail for the balloon
        cv2.line(frame, (b['x'], b['y'] + b['radius']), (b['x'], b['y'] + b['radius'] + 20), (200, 200, 200), 2)

        # Check collision with index finger
        if ix != -1 and iy != -1:
            # Calculate distance between finger tip and balloon center
            dist = ((ix - b['x']) ** 2 + (iy - b['y']) ** 2) ** 0.5
            if dist < b['radius'] + 10: # If touched
                balloons.remove(b) # Pop!
                score += 10        # Increase score
                continue

        # If balloon falls off the screen
        if b['y'] > h + b['radius']:
            balloons.remove(b)
            missed += 1

    # 4. Draw Score and Missed UI
    cv2.putText(frame, f"SCORE: {score}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 4)
    cv2.putText(frame, f"MISSED: {missed}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the game window
    cv2.imshow("Magic Balloon Popper", frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()