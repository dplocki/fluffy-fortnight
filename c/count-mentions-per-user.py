class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        user_online = {}
        result = [0] * numberOfUsers
        preparsed_events = list(map(lambda x: (x[0], int(x[1]), x[2]), events))

        for event_type, timestamp, properties in sorted(preparsed_events, key=lambda x: (x[1], x[0] == 'MESSAGE')):
            if event_type == 'MESSAGE':
                if properties == 'ALL':
                    for i, r in enumerate(result):
                        result[i] = r + 1

                elif properties == 'HERE':
                    for user_id in range(numberOfUsers):
                        if user_online.get(user_id, 0) <= timestamp:
                            result[user_id] += 1

                else:
                    for user_id in map(lambda x: int(x[2:]), properties.split(' ')):
                        result[user_id] += 1

            if event_type == 'OFFLINE':
                user_id = int(properties)
                user_online[user_id] = timestamp + 60

        return result
