    while not game.done:
        action = rn.randint(0,2)
        state,reward,done,info = game.run(action)
        # time.sleep(0.02)