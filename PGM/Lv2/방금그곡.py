def solution(m, musicinfos):
    note = {'C#': '0', 'D#': '1', 'F#': '2', 'G#': '3', 'A#': '4', 'C': '5', 'D': '6', 'E': '7', 'F': '8', 'G': '9'}

    def music_convert(s):
        for char in note:
            s = s.replace(char, note[char])
        return s

    def time_convert(t):
        h, m = map(int, t.split(':'))
        return h*60+m

    result = ["(None)", -1]
    m = music_convert(m)
    for i, info in enumerate(musicinfos):
        t1, t2, title, music = info.split(',')
        time = time_convert(t2) - time_convert(t1)
        music = music_convert(music)
        quo, r = divmod(time, len(music))
        melody = music * quo + music[:r]

        if m in melody and time > result[1]:
            result = [title, time]

    return result[0]
import heapq