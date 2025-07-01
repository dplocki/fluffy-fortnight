class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = self.split_to_lines(words, maxWidth)

        result = [
            self.build_line(line, maxWidth)
            for line in lines[:-1]
        ]

        result.append(self.build_last_line(lines[-1], maxWidth))

        return result

    def split_to_lines(self, words: List[str], max_width: int) -> List[str]:
        lines = []
        words_count = len(words)
        index = 0
        current_line = []
        word_count = 0
        current_line_len = 0

        while index < words_count:
            word = words[index]
            word_len = len(word)
            if current_line_len + word_len + word_count - 1 < max_width:
                current_line.append(word)
                current_line_len += word_len
                word_count += 1
                index += 1
            else:
                current_line.append(word_count - 1)
                current_line.append(current_line_len)
                lines.append(current_line)
                current_line = []
                current_line_len = 0
                word_count = 0
       
        current_line.append(word_count - 1)
        current_line.append(current_line_len)
        lines.append(current_line)

        return lines

    def build_line(self, tokens: List, max_width: int) -> str:
        letters = tokens[-1]
        breaks_count = tokens[-2]

        if breaks_count == 0:
            return tokens[0] + ' ' * (max_width - letters)
        
        spaces, more_spaces = divmod(max_width - letters, breaks_count)

        result = ''
        for index, word in enumerate(tokens[:-3]):
            result += word
            result += ' ' * (spaces + (0 if index >= more_spaces else 1))

        result += tokens[-3]

        return result

    def build_last_line(self, tokens: List, max_width: int) -> str:
        letters = tokens[-1]
        breaks_count = tokens[-2]

        return ' '.join(tokens[:-2]) + ' ' * (max_width - letters - breaks_count)
