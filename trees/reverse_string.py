def reverse_characters(message):
    message_list = list(message)

    print message_list
    # walk towards the middle, from both sides
    for front_index in xrange(len(message_list) / 2):
        print -front_index-1
        back_index = -front_index-1

        # swap the front char and back char
        message_list[front_index], message_list[back_index] = \
            message_list[back_index], message_list[front_index]

    return ''.join(message_list)

print reverse_characters("i am great")