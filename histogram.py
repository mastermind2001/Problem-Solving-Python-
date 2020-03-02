# Date : 21-06-2018
# Histogram

# Input Format :
# 5    # For number of values in input
# 2    # First value
# 3    # Second value
# 6    # Third value
# 6    # Fourth value
# 1    # Fifth value

import statistics


class Statistics(object):
    def __init__(self, data=[]):
        self.data = data

    def getData(self):
        return self.data

    def calculate_mean(self):
        if not self.data:
            return 'Mean is : None'
        return 'Mean is : ' + str(round(statistics.mean(self.data), 4))

    def calculate_median(self):
        if not self.data:
            return 'Data is : None'
        return 'Median is : ' + str(statistics.median(self.data))

    def calculate_mode(self):
        if not self.data:
            return 'Mode is : None'

        mode_data = self.data
        mode_data.sort()
        mode_data = mode_data[::-1]
        pop_element = []
        sample_mode = ''
        sample_mode_copy = ''
        mode = []
        index = 1
        flag = True
        while flag:
            count_element = 0
            best_count = 0
            for i in mode_data:
                count_element = mode_data.count(i)
                sample_mode_copy = str(i)
                if count_element >= best_count:
                    best_count = count_element
                    sample_mode = sample_mode_copy

            if index > 1:
                for k in range(mode_data.count(int(sample_mode))):
                    mode_data.remove(int(sample_mode))
                if best_count == pop_element[0]:
                    mode.append(sample_mode)
                else:
                    flag = False

            if index == 1:
                for l in range(mode_data.count(int(sample_mode))):
                    mode_data.remove(int(sample_mode))
                mode.append(sample_mode)
                pop_element.append(best_count)
                index += 1

        mode = ', '.join(mode)

        return 'Mode is : ' + mode

    def draw_histogram(self):
        if not self.data:
            print('None')
            return ''

        hist_range = []

        for a in self.data:
            if a not in hist_range:
                hist_range.append(a)
        hist_range.sort()

        for i in range(len(hist_range)):
            print(str(hist_range[i]).rjust(6) + '  |  ' + str('*'*self.data.count(hist_range[i])))

    def __str__(self):
        if not self.data:
            return 'Data is : None'

        result = ''
        for i in self.data:
            result += str(i)

        result = ', '.join(result)
        return 'Data is : ' + result


try:
    count = int(input())
    all_data = [int(input()) for i in range(count)]
    stats = Statistics(all_data)
    print('Your added data is : \n\nData : ', all_data)
    print('\n===================================\n')
    print(stats.calculate_mean())
    print('\n===================================\n')
    print(stats.calculate_median())
    print('\n===================================\n')
    print(stats.calculate_mode())
    print('\n===================================\n')
    print('Histogram : \n')
    stats.draw_histogram()
except:
    print('Invalid input. You can enter only integer values.')
    print('\n===================================\n')
    print("""Input Format : 

5    # For number of values in input
2    # First value
3    # Second value
6    # Third value
6    # Fourth value
1    # Fifth value""")

