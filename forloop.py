def forloop(socketio):
    counter = 0
    for x in range(1,100):
        counter = counter + 1
        print(f"counting {counter}")
        socketio.emit('progress',counter)

    return "done"
